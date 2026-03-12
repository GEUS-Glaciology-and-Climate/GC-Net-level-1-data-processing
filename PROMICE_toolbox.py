# -*- coding: utf-8 -*-

"""
tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pytz
import os
import warnings
import jaws_tools
import nead
warnings.filterwarnings("ignore", category=RuntimeWarning)
from sklearn.linear_model import LinearRegression
import xarray as xr
import re


DEFAULT_VARIABLE_THRESHOLDS = {
    r"^TA[1234]$": {"tol": 3, "factor": 2.2},
    r"^P$": {"tol": 5.0, "factor": 0.5},
    r"^RH[12]$": {"tol": 2.0, "factor": 3.5},
    r"^TS(?:10|[1-9])$": {"tol": 0.5, "factor": 1.5},
}


NO_QC_VAR = ['time','rec']


def set_flag(ds: xr.Dataset, v: str, flag: str, index_slice=None, mask=None) -> xr.Dataset:
    if v in NO_QC_VAR: return ds

    if index_slice is None:
        index_slice = {"time": slice(None, None)}

    vqc = f"{v}_qc"
    if vqc not in ds:
        ds[vqc] = xr.DataArray(
            np.full(ds[v].shape, "OK", dtype=object),
            coords=ds[v].coords,
            dims=ds[v].dims,
        )
    else:
        if ds[vqc].dtype.kind in ("U", "S"):
            ds[vqc] = ds[vqc].astype(object)

    q = ds[vqc].loc[index_slice]
    x = ds[v].loc[index_slice]
    if q.size == 0:
        return ds

    m = xr.ones_like(x, dtype=bool) if mask is None else (
        mask.loc[index_slice] if isinstance(mask, xr.DataArray) else mask
    )

    cond = m & x.notnull() & (q == "OK")

    ds[vqc].loc[index_slice] = xr.where(cond, str(flag), q)
    return ds

def _get_params(var, tol=None, factor=None):
    if tol is not None and factor is not None:
        logger.debug(f"{var}: using user tol={tol}, factor={factor}")
        return float(tol), float(factor)

    for pat, cfg in DEFAULT_VARIABLE_THRESHOLDS.items():
        if re.match(pat, var):
            vt = float(cfg["tol"]) if tol is None else float(tol)
            vf = float(cfg["factor"]) if factor is None else float(factor)
            return vt, vf

    vt = 0.1 if tol is None else float(tol)
    vf = 2.0 if factor is None else float(factor)
    return vt, vf

# avoid xarray ffill/bfill (slow) -> numpy forward/backward fill
def _ffill_idx(a):
    a = a.copy()
    m = np.isnan(a)
    idx = np.where(~m, np.arange(a.size), 0)
    np.maximum.accumulate(idx, out=idx)
    a[m] = a[idx[m]]
    return a

def _bfill_idx(a):
    a = a.copy()
    m = np.isnan(a)
    idx = np.where(~m, np.arange(a.size), a.size-1)
    idx = idx[::-1]
    np.minimum.accumulate(idx, out=idx)
    idx = idx[::-1]
    a[m] = a[idx[m]]
    return a

def unflag_if_linear_interp(ds, var, flag, tol=0.1, time="time"):
    """
    Remove flags where values follow linear interpolation within tolerance.

    Parameters
    ----------
    ds : xarray.Dataset
        Dataset containing the variable.
    var : str
        Variable name in ds to evaluate.
    flag : xarray.DataArray (bool)
        Initial flag array on the same time axis as the evaluated data.
    tol : float, optional
        Absolute tolerance for deviation from linear interpolation.
    time : str, optional
        Name of the time dimension.

    Returns
    -------
    xarray.DataArray
        Updated flag array where linearly interpolated points are unflagged.
    """
    # Align variable to flag time axis
    v = ds[var].sel({time: flag[time]}).astype("float64")
    t = v[time].values.astype("datetime64[ns]").astype("int64")

    n = v.sizes[time]
    idx = np.arange(n, dtype=np.int64)

    # Valid (non-flagged and finite) samples
    okv = ((~flag.values) & np.isfinite(v.values))
    base = np.where(okv, idx.astype("float64"), np.nan)
    pi = _ffill_idx(base)
    ni = _bfill_idx(base)
    # finding points that has two valid neigbors
    has_both = np.isfinite(pi) & np.isfinite(ni) & (pi != ni)

    pi_i = np.zeros(n, dtype=np.int64)
    ni_i = np.zeros(n, dtype=np.int64)
    pi_i[has_both] = pi[has_both].astype(np.int64)
    ni_i[has_both] = ni[has_both].astype(np.int64)

    t_prev = np.zeros(n, dtype=np.int64)
    t_next = np.zeros(n, dtype=np.int64)
    v_prev = np.zeros(n, dtype=float)
    v_next = np.zeros(n, dtype=float)

    t_prev[has_both] = t[pi_i[has_both]]
    t_next[has_both] = t[ni_i[has_both]]
    v_prev[has_both] = v.values[pi_i[has_both]]
    v_next[has_both] = v.values[ni_i[has_both]]

    # Linear interpolation weights
    denom = (t_next - t_prev).astype("float64")
    w = np.full(n, np.nan, dtype="float64")
    w[has_both] = (t[has_both] - t_prev[has_both]) / denom[has_both]

    # Interpolated estimate
    v_hat = v_prev + w * (v_next - v_prev)

    # Unflag if close to linear interpolation
    unflag = (
        flag.values
        & has_both
        & np.isfinite(v_hat)
        & (np.abs(v.values - v_hat) <= tol)
    )

    return xr.DataArray(flag.values & ~unflag,
                        coords=flag.coords, dims=flag.dims,
                        name=f"{flag.name}_final")

def rate_of_change_fwd_bwd_and_thresholds(da, var, window="7D", time="time", per="h",
                              min_periods=10, factor=None, tol=None):
    """Compute forward/backward rate-of-change flags and rolling thresholds.

    Calculates absolute rates of change between consecutive samples of a
    time series, derives rolling 95th percentile thresholds, and returns
    forward- and backward-assigned exceedance flags aligned to the full
    time axis of the input DataArray.

    Args:
        da (xr.DataArray): Input variable time series with NaNs already removed.
        var (str): Name of the variable (used for logging and metadata).
        window (str, optional): Rolling window length as a pandas offset
            string (e.g. "7D"). Defaults to "7D".
        time (str, optional): Name of the time dimension. Defaults to "time".
        per (str, optional): Time unit used to normalize rates (e.g. "h", "D").
            Defaults to "h".
        min_periods (int, optional): Minimum number of samples required in the
            rolling window. Defaults to 10.
        factor (float, optional): Multiplier applied to the rolling 95th
            percentile to form detection thresholds. If None, a
            variable-specific default is used.
        tol (float, optional): Interpolation tolerance passed through for
            metadata consistency. If None, a variable-specific default is used.

    Returns:
        Tuple[xr.Dataset, xr.DataArray, xr.DataArray]:
            - roc_ds: Dataset containing raw rates and rolling thresholds.
            - fwd_full: Boolean DataArray of forward rate exceedances aligned
              to the full time axis.
            - bwd_full: Boolean DataArray of backward rate exceedances aligned
              to the full time axis.
    """
    if (tol is None) | (factor is None):
        tol, factor = _get_params(var, tol=tol, factor=factor)

    t = da[time].values.astype("datetime64[ns]")
    v = da.values.astype("float64")

    dt_ns = (t[1:] - t[:-1]).astype("timedelta64[ns]").astype("int64")
    dv = v[1:] - v[:-1]
    denom_ns = np.timedelta64(1, per).astype("timedelta64[ns]").astype("int64")
    rate = np.abs(dv) / (dt_ns / denom_ns)

    idx_fwd = pd.to_datetime(t[1:])
    s_fwd = pd.Series(rate, index=idx_fwd)
    thr_fwd = factor * s_fwd.rolling(window=window, center=True, min_periods=min_periods).quantile(0.95)
    flag_fwd_s = s_fwd > thr_fwd

    idx_bwd = pd.to_datetime(t[:-1])
    s_bwd = pd.Series(rate, index=idx_bwd)
    thr_bwd = factor * s_bwd.rolling(window=window, center=True, min_periods=min_periods).quantile(0.95)
    flag_bwd_s = s_bwd > thr_bwd

    flag_fwd = xr.DataArray(
        flag_fwd_s.values.astype(bool),
        coords={time: da[time].values[1:]},
        dims=(time,),
        name=f"{var}_high_var_flag_fwd",
    )
    flag_bwd = xr.DataArray(
        flag_bwd_s.values.astype(bool),
        coords={time: da[time].values[:-1]},
        dims=(time,),
        name=f"{var}_high_var_flag_bwd",
    )

    tfull = da[time].values
    fwd_full = xr.DataArray(np.zeros(tfull.shape, bool), coords={time: tfull}, dims=(time,))
    bwd_full = xr.DataArray(np.zeros(tfull.shape, bool), coords={time: tfull}, dims=(time,))
    fwd_full.loc[{time: flag_fwd[time]}] = flag_fwd
    bwd_full.loc[{time: flag_bwd[time]}] = flag_bwd

    roc_ds = xr.Dataset(
        data_vars=dict(
            roc_rate=(("time_rate",), rate),
            roc_thr_fwd=(("time_fwd",), thr_fwd.values.astype("float64")),
            roc_thr_bwd=(("time_bwd",), thr_bwd.values.astype("float64")),
        ),
        coords=dict(
            time_rate=da[time].values[1:],
            time_fwd=da[time].values[1:],
            time_bwd=da[time].values[:-1],
        ),
        attrs=dict(var=var, per=per, window=window, min_periods=min_periods, factor=factor, tol=tol),
    )

    return roc_ds, fwd_full, bwd_full


def flag_high_rate_of_change(ds, var, window="7D", time="time",
                                       per="h", min_periods=10, factor=None, tol=None):
    """Flag anomalously high rates of change and refine using interpolation logic.

    Detects time steps where the rate of change exceeds a rolling percentile-
    based threshold (forward and backward differences), applies additional
    logical rules related to missing neighbors and uneven sampling, and
    finally removes flags consistent with linear interpolation.

    Args:
        ds (xr.Dataset): Dataset containing the variable.
        var (str): Name of the variable to analyze.
        window (str, optional): Rolling window length (pandas offset string).
            Defaults to "7D".
        time (str, optional): Name of the time dimension. Defaults to "time".
        per (str, optional): Time unit used to normalize rates (e.g. "h", "D").
            Defaults to "h".
        min_periods (int, optional): Minimum samples required in the rolling
            window. Defaults to 10.
        factor (float, optional): Multiplier applied to the rolling 95th
            percentile threshold. If None, a variable-specific default is used.
        tol (float, optional): Tolerance for linear interpolation unflagging.
            If None, a variable-specific default is used.

    Returns:
        Tuple[xr.DataArray, xr.DataArray, xr.DataArray, xr.DataArray]:
            - fwd_full: Forward rate-of-change flags on the full time axis.
            - bwd_full: Backward rate-of-change flags on the full time axis.
            - flag_combined: Combined logical flag before interpolation refinement.
            - flag_final: Final flag after interpolation-based unflagging.
    """
    tol, factor = _get_params(var, tol=tol, factor=factor)

    da = ds[var].where(ds[f"{var}_qc"] == "OK").dropna(dim=time)
    roc_ds, fwd_full, bwd_full = rate_of_change_fwd_bwd_and_thresholds(
        da, var, window=window, time=time, per=per, min_periods=min_periods, factor=factor, tol=tol
    )

    y = da
    prev_missing = y.shift({time: 1}).isnull()
    next_missing = y.shift({time: -1}).isnull()

    tt = da[time]
    dt_prev = tt - tt.shift({time: 1})
    dt_next = tt.shift({time: -1}) - tt
    uneven_dt = dt_prev != dt_next

    if da.sizes[time] > 0:
        prev_missing.values[0] = True
        next_missing.values[-1] = True
        uneven_dt.values[0] = True
        uneven_dt.values[-1] = True

    # Combine multiple logical criteria
    flag_combined = (
        (fwd_full & bwd_full)
        | (fwd_full & prev_missing)
        | (fwd_full & next_missing)
        | (bwd_full & prev_missing)
        | (bwd_full & next_missing)
        | (fwd_full & uneven_dt)
        | (bwd_full & uneven_dt)
    ).rename(f"{var}_high_var_flag_combined")

    # Final refinement step
    if flag_combined.any():
        flag_final = unflag_if_linear_interp(ds, var, flag_combined, tol=tol, time=time)
    else:
        flag_final = flag_combined
    logger.info(f"ROC filter on {var} (tol={tol}, factor={factor}): filtering {flag_final.sum().item()}/{len(ds.time)}")

    return fwd_full, bwd_full, flag_combined, flag_final

def rate_of_change_filter(ds):
    """Apply the rate-of-change outlier filter to all matching variables in a dataset.

    Selects variables in `ds.data_vars` whose names match any regex pattern in
    `DEFAULT_VARIABLE_THRESHOLDS`, then runs `flag_high_rate_of_change` to
    identify outliers. The filter is applied in up to two passes: after the
    first pass, flagged samples are temporarily set to NaN and the filter is
    rerun to catch additional outliers. Final flags are the logical OR of both
    passes.

    Args:
        ds (xr.Dataset): Input dataset containing time series variables.

    Returns:
        xr.Dataset: Dataset (same object) with the rate-of-change filter applied.
    """

    patterns = [re.compile(p) for p in DEFAULT_VARIABLE_THRESHOLDS]

    vars_with_thresholds = [
        v for v in ds.data_vars
        if any(p.match(v) for p in patterns)
    ]

    max_iter = 20
    thr_new_flags = 10

    for var in vars_with_thresholds:
        flag_final = xr.zeros_like(ds[var].isel(time=slice(0, 0)).reindex(time=ds.time), dtype=bool).reindex_like(ds.time, fill_value=False)
        flag_combined = flag_final.copy()

        tmp = ds.copy(deep=True)

        for _ in range(max_iter):
            _, _, fc, ff = flag_high_rate_of_change(tmp, var, window="7D")

            fc = fc.reindex_like(ds.time, fill_value=False)
            ff = ff.reindex_like(ds.time, fill_value=False)

            new = ff & ~flag_final
            nnew = int(new.sum().item()) if new.size else 0

            flag_combined = flag_combined | fc
            flag_final = flag_final | ff

            if nnew == 0 or nnew <= thr_new_flags:
                break

            tmp[var] = tmp[var].where(~new)

        ds = set_flag(ds, var, flag="ROC", mask=flag_final)

    return ds

def roc_filter_dataframe(df):
    df_in = df.copy()
    df_in.index = df_in.index.tz_convert(None)
    df_in.index.name = "time"
    df_out = rate_of_change_filter(df_in.to_xarray()).to_dataframe()
    df_out.index = df_out.index.tz_localize("UTC")
    df_out.index.name = "timestamp"
    return df_out

def field_info(fields):
    tmp =pd.read_csv('L1/L1_variable_list.csv', skipinitialspace=True)
    field_list = tmp.fields.tolist()
    units = tmp.units.tolist()
    display_description = tmp.display_description.tolist()
    database_fields = tmp.database_fields.tolist()
    database_fields_data_types = tmp.database_fields_data_types.tolist()

    field_list = (
        field_list
        + [s + "_qc" for s in field_list]
        + [s + "_adj_flag" for s in field_list]
    )
    units = units + ["-" for s in units] + ["-" for s in units]
    display_description = (
        display_description
        + [s + "_quality_flag" for s in display_description]
        + [s + "_adj_flag" for s in display_description]
    )
    database_fields = (
        database_fields
        + [s + "_quality_flag" for s in database_fields]
        + [s + "_adj_flag" for s in database_fields]
    )
    database_fields_data_types = (
        database_fields_data_types
        + ["int" for s in database_fields_data_types]
        + ["int" for s in database_fields_data_types]
    )

    ind = [field_list.index(s) for s in fields]

    return (
        [units[i] for i in ind],
        [display_description[i] for i in ind],
        [database_fields[i] for i in ind],
        [database_fields_data_types[i] for i in ind],
    )


def Msg(txt):
    f = open("out/Report.md", "a")
    print(txt)
    f.write(txt + "\n")


def flag_data(df, site, var_list=["all"]):
    """
    Replace data within a specified variable, between specified dates by NaN.
    Reads from file "metadata/flags/<site>.csv".

    INTPUTS:
        df: PROMICE data with time index
        site: string of PROMICE site
        var_list: list of the variables for which data removal should be
            conducted (default: all)
        plot: whether data removal should be plotted

    OUTPUTS:
        promice_data: Dataframe containing PROMICE data for the desired settings [DataFrame]
    """

    df_out = df.copy()
    if not os.path.isfile("metadata/flags/" + site + ".csv"):
        Msg("===============")
        Msg("No erroneous data listed for " + site)
        Msg("===============")
        return df

    flag_data = pd.read_csv("metadata/flags/" + site + ".csv",
                            comment="#",
                            skipinitialspace=True)

    flag_data.t0 = pd.to_datetime(flag_data.t0, format='mixed', utc=True)
    flag_data.t1 = pd.to_datetime(flag_data.t1, format='mixed', utc= True)

    flag_data.loc[flag_data.t0.isnull(), "t0"] = df_out.index[0]
    flag_data.loc[flag_data.t1.isnull(), "t1"] = df_out.index[-1]

    if var_list[0] == "all":
        var_list = np.unique(flag_data.variable)

    Msg("Flagging data:")
    Msg("|start time|end time|variable|")
    Msg("|-|-|-|")
    for ind in flag_data.index:
        var = flag_data.loc[ind,'variable']
        t0 = flag_data.loc[ind,'t0']
        t1 = flag_data.loc[ind,'t1']
        flag = flag_data.loc[ind,'flag']

        if (var not in df_out.columns) & ('*' not in var) & ('$' not in var) & (' ' not in var):
            Msg("Warning: " + var + " not found")
            continue

        if ('*' in var) |('$' in var):
            var_list = df_out.filter(regex=(var)).columns
        else:
            var_list = var.split(' ')

        for var in var_list:
            if '_qc' in var: continue
            Msg("|" + str(t0) + "|" + str(t1) + "|" + var + "|")

            if var in df_out.columns.values:
                if var + "_qc" in df_out.columns:
                    df_out.loc[t0:t1, var + "_qc"] = flag
                else:
                    df_out[var + "_qc"] = "OK"
                    df_out.loc[t0:t1, var + "_qc"] = flag

    return df_out

def plot_flagged_data(df1, df2, site, tag="", var_list=[]):
    Msg(" ")
    df = df1.copy()
    df_out = df2.copy()
    adj_path = f"metadata/adjustments/{site}.csv"

    if not os.path.isfile(adj_path):
        Msg("===============")
        Msg(f"No data to fix at {site}")
        Msg("===============")
        return []

    # ---- Load adjustments ----
    adj_info = pd.read_csv(adj_path, comment="#", skipinitialspace=True)
    adj_info["t0"] = pd.to_datetime(adj_info["t0"], format="mixed", utc=True)
    adj_info["t1"] = pd.to_datetime(adj_info["t1"], format="mixed", utc=True)

    adj_info.loc[adj_info.t0.isnull(), "t0"] = df_out.index[0]
    adj_info.loc[adj_info.t1.isnull(), "t1"] = df_out.index[-1]

    # Wildcard "*" expands to all variables
    if "*" in adj_info.variable.values:
        all_vars = df_out.columns
        template = adj_info[adj_info.variable == "*"].copy()
        adj_info = adj_info[adj_info.variable != "*"]
        for var in all_vars:
            t = template.copy()
            t["variable"] = var
            adj_info = pd.concat([adj_info, t], ignore_index=True)

    adj_info.set_index(["variable", "t0"], drop=False, inplace=True)

    # Default: plot all variables from df
    if not var_list:
        var_list = df.columns
    if isinstance(var_list, str):
        var_list = [var_list]

    flag_colors = {
        "OK": "green",
        "CHECKME": "orange",
        "NAN": "violet",
        "CONFIRMED": "tab:brown",
        "OOL": "red",
        "OOP": "magenta",
        "IWS": "cyan",
        "FROZEN": "blue",
        "FROZEN_WS": "lightblue",
        "ROC": "goldenrod",
        "LIN": "lime",
    }


    excluded_substrings = ["_qc", "_min", "_max", "_std", "_adj_flag"]

    for var in var_list:
        if (df[var].isnull().all() or
            any(s in var for s in excluded_substrings)):
            continue

        qc_var = var + "_qc"
        if qc_var not in df.columns: df[qc_var] = "OK"

        flags_uni = np.unique(df[qc_var].astype(str).fillna("OK"))
        if len(flags_uni) <= 1 and df[var].isnull().all(): continue

        fig, ax = plt.subplots(figsize=(10, 7))
        plt.subplots_adjust(top=0.85, bottom=0.08, left=0.1, right=0.98)

        ax.scatter(df_out.index, df_out[var], s=8, color="gray", label="raw")

        # flagged points
        for flag in flags_uni:
            mask = df[qc_var] == flag
            color = flag_colors.get(flag, None)
            ax.scatter(df.index[mask], df[var][mask], s=12, color=color, label=flag)

        if var in adj_info.index.get_level_values(0).unique():
            for t in adj_info.loc[var].t0.values:
                ax.axvline(t, linestyle="--", color="red")
            ax.axvline(np.nan, linestyle="--", color="red", label="Adjustment times")

        # robust x-limits
        try:
            ax.set_xlim(df_out.index.min(), df_out.index.max())
        except:
            pass

        vals = df.loc[df[qc_var] == "OK", var].astype(float)
        vals = vals.replace([np.inf, -np.inf], np.nan).dropna()

        if len(vals) > 0:
            vmin, vmax = vals.min(), vals.max()
            if np.isfinite(vmin) and np.isfinite(vmax) and vmax > vmin:
                pad = 0.05 * (vmax - vmin)
                ax.set_ylim(vmin - pad, vmax + pad)

        ax.set_xlabel("Year")
        ax.set_ylabel(var)
        ax.legend(loc="upper center", ncols=5,
          bbox_to_anchor=(0.5, 1.15), title = site, )
        ax.grid()
        fname = f"figures/L1_data_treatment/{site.replace(' ', '')}_{var}.jpeg"
        fig.savefig(fname, dpi=120)

        Msg(f"![Adjusted and flagged data at {site}]({fname})")
        # plt.close(fig)

    Msg(" ")


def flag_linear_interp_runs(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    var_list = df.columns
    VAR_SKIP = ["HW1", "HW2", "V"]
    for var in var_list:
        if var in VAR_SKIP: continue

        if "TS" in var:
            N=10
        else:
            N=3
        qc = f"{var}_qc"
        if qc not in df.columns:
            df[qc] = "OK"

        v = df[var].astype(float)
        dv = v.diff()

        is_const = (np.abs(dv - dv.shift())<0.01001) & dv.notna() & (np.abs(dv)>=0.01)

        rid = is_const.ne(is_const.shift(fill_value=False)).cumsum()
        f = (is_const & (is_const.groupby(rid).transform("sum") >= N)).to_numpy(bool)

        f = np.r_[f[1:], False]                          # shift -1
        f = f | np.r_[False, f[:-1]] | np.r_[f[1:], False]  # expand by 1
        f = f & np.r_[False, f[:-1]] & np.r_[f[1:], False]  # shrink by 1

        flag = f

        nflag = int(np.sum(flag))
        if nflag > 0:
            Msg(f"{var}: {nflag} samples flagged")

        df.loc[flag, qc] = "LIN"

    return df

def remove_flagged_data(df):
    df = df.copy()
    qc_cols = [c for c in df.columns if c.endswith("_qc")]

    for qc in qc_cols:
        s = df[qc].astype(object).fillna("OK")
        if s.nunique(dropna=False) > 1:
            msk = s.isin(["OK", ""])
            base = qc[:-3]
            if base in df.columns:
                df.loc[~msk, base] = np.nan
        df = df.drop(columns=[qc])

    return df


import pytz


def adjust_data(df_in, site, var_list=[], skip_var=[], skip_time_shifts=False):
    df_out = df_in.copy(deep=True)
    if not os.path.isfile("metadata/adjustments/" + site + ".csv"):
        Msg("No data to fix at " + site)
        return df_out

    adj_info = pd.read_csv(
        "metadata/adjustments/" + site + ".csv",
        comment="#", skipinitialspace=True
    )

    adj_info.t0 = pd.to_datetime(adj_info.t0, format='mixed', utc=True)
    adj_info.t1 = pd.to_datetime(adj_info.t1, format='mixed', utc= True)
    adj_info.loc[adj_info.t0.isnull(), "t0"] = df_out.index[0]
    adj_info.loc[adj_info.t1.isnull(), "t1"] = df_out.index[-1]

    # if "*" is given as variable then we append this adjustement for all variables
    for ind in adj_info.loc[adj_info.variable == "*", :].index:
        line_template = adj_info.loc[[ind], :].copy()
        for var in df_out.columns:
            line_template.variable = var
            line_template.index = [adj_info.index.max() + 1]
            adj_info = pd.concat((adj_info, line_template))
        adj_info = adj_info.drop(labels=ind, axis=0)

    adj_info = adj_info.sort_values(by=["variable", "t0"])
    # putting sonic correction first
    adj_info = pd.concat((adj_info.loc[adj_info.adjust_function.str.startswith('sonic_correction'),:],
                          adj_info.loc[~adj_info.adjust_function.str.startswith('sonic_correction'),:]))
    # putting sensor swap first
    adj_info = pd.concat((adj_info.loc[adj_info.adjust_function.str.startswith('swap'),:],
                          adj_info.loc[~adj_info.adjust_function.str.startswith('swap'),:]))

    msk = adj_info["adjust_function"].eq("time_shift")
    adj_info = pd.concat([adj_info.loc[msk].sort_values("t0", ascending=False),
                          adj_info.loc[~msk]], axis=0)
    if skip_time_shifts:
        adj_info = adj_info.loc[adj_info.adjust_function != "time_shift", :]
    adj_info.set_index(["variable", "t0"], drop=False, inplace=True)


    adj_info_save = adj_info.copy()
    for adj_info in [adj_info_save.loc[adj_info_save.adjust_function == "time_shift", :],
                     adj_info_save.loc[adj_info_save.adjust_function != "time_shift", :]]:
        if len(adj_info) == 0 :
            continue
        if len(var_list) > 0:
            adj_info = adj_info.loc[np.isin(adj_info.variable, var_list), :]

        if len(skip_var) > 0:
            adj_info = adj_info.loc[~np.isin(adj_info.variable, skip_var), :]
        var_list = np.unique(adj_info.variable)

        Msg("\n|start time|end time|variable|operation|value|number of removed samples|")
        Msg("|-|-|-|-|-|-|")
        for var in var_list:
            for t0, t1, func, val in zip(
                adj_info.loc[var].t0,
                adj_info.loc[var].t1,
                adj_info.loc[var].adjust_function,
                adj_info.loc[var].adjust_value,
            ):
                if (pd.to_datetime(t0) > df_in.index[-1]) | (pd.to_datetime(t1) < df_in.index[0]):
                    continue

                # counting nan values before filtering
                if "_qc" not in var:
                    nan_count_1 = np.sum(np.isnan(df_out.loc[t0:t1, var].values))

                if t1 < t0:
                    Msg("Dates in wrong order")

                if func == "add":
                    df_out.loc[t0:t1, var] = df_out.loc[t0:t1, var].values + val
                    # flagging adjusted values
                    if var + "_adj_flag" not in df_out.columns:
                        df_out[var + "_adj_flag"] = 0
                    msk = df_out.loc[t0:t1, var].notnull()
                    ind = df_out.loc[t0:t1, var].loc[msk].index
                    df_out.loc[ind, var + "_adj_flag"] = 1

                if func == "multiply":
                    df_out.loc[t0:t1, var] = df_out.loc[t0:t1, var].values * val
                    if "DW" in var:
                        df_out.loc[t0:t1, var] = df_out.loc[t0:t1, var] % 360
                    # flagging adjusted values
                    if var + "_adj_flag" not in df_out.columns:
                        df_out[var + "_adj_flag"] = 0
                    msk = df_out.loc[t0:t1, var].notnull()
                    ind = df_out.loc[t0:t1, var].loc[msk].index
                    df_out.loc[ind, var + "_adj_flag"] = 1

                if func == "min_filter":
                    tmp = df_out.loc[t0:t1, var].to_numpy(copy=True)
                    tmp[tmp < val] = np.nan
                    df_out.loc[t0:t1, var] = tmp
                if func == "max_filter":
                    tmp = df_out.loc[t0:t1, var].to_numpy(copy=True)
                    tmp[tmp > val] = np.nan
                    df_out.loc[t0:t1, var] = tmp
                if func == "upper_perc_filter":
                    tmp = df_out.loc[t0:t1, var].copy()
                    df_w = df_out.loc[t0:t1, var].resample("14D").quantile(1 - val / 100)
                    df_w = df_out.loc[t0:t1, var].resample("14D").var()
                    for m_start, m_end in zip(df_w.index[:-2], df_w.index[1:]):
                        msk = (tmp.index >= m_start) & (tmp.index < m_end)
                        values_month = tmp.loc[msk].values
                        values_month[values_month < df_w.loc[m_start]] = np.nan
                        tmp.loc[msk] = values_month

                    df_out.loc[t0:t1, var] = tmp.values

                if func == "biweekly_upper_range_filter":
                    tmp = df_out.loc[t0:t1, var].copy()
                    df_max = df_out.loc[t0:t1, var].resample("14D").max()
                    for m_start, m_end in zip(df_max.index[:-2], df_max.index[1:]):
                        msk = (tmp.index >= m_start) & (tmp.index < m_end)
                        lim = df_max.loc[m_start] - val
                        values_month = tmp.loc[msk].to_numpy(copy=True)
                        values_month[values_month < lim] = np.nan
                        tmp.loc[msk] = values_month
                    # remaining samples following outside of the last 2 weeks window
                    msk = tmp.index >= m_end
                    lim = df_max.loc[m_start] - val
                    values_month = tmp.loc[msk].to_numpy(copy=True)
                    values_month[values_month < lim] = np.nan
                    tmp.loc[msk] = values_month
                    # updating original pandas
                    df_out.loc[t0:t1, var] = tmp.values

                if func == "hampel_filter":
                    tmp = df_out.loc[t0:t1, var]
                    tmp = hampel(tmp, k=7 * 24, t0=val)
                    df_out.loc[t0:t1, var] = tmp.values

                if func == "grad_filter":
                    tmp = df_out.loc[t0:t1, var].copy()
                    msk = df_out.loc[t0:t1, var].copy().diff()
                    tmp[np.roll(msk.abs() > val, -1)] = np.nan
                    df_out.loc[t0:t1, var] = tmp

                if "swap_with_" in func:
                    var2 = func[10:]
                    val_var = df_out.loc[t0:t1, var].values.copy()
                    val_var2 = df_out.loc[t0:t1, var2].values.copy()
                    df_out.loc[t0:t1, var2] = val_var
                    df_out.loc[t0:t1, var] = val_var2

                if func == "rotate":
                    df_out.loc[t0:t1, var] = (df_out.loc[t0:t1, var].values + val) % 360

                if func == "air_temp_sonic_correction":
                    # finding the available air temp measurements
                    if "TA" + var[-1] in df_out.columns:
                        tmp = df_out.loc[t0:t1, "TA" + var[-1]]
                    else:
                        tmp = df_out.loc[t0:t1, "TA1"]
                    TA_var =  ["TA" + str(i) for i in range(1, 5) if "TA" + str(i) in df_out.columns]
                    tmp2 = df_out.loc[t0:t1, TA_var].mean(axis=1)
                    tmp.loc[tmp.isnull()] = tmp2.loc[tmp.isnull()]
                    tmp = tmp.interpolate(method="nearest", fill_value="extrapolate")

                    df_out.loc[t0:t1, var] = df_out.loc[t0:t1, var].values * np.sqrt(
                        (tmp.values + 273.15) / 273.15
                    )

                if func == "air_temp_sonic_anticorrection":
                    # finding the available air temp measurements
                    if "TA" + var[-1] in df_out.columns:
                        tmp = df_out.loc[t0:t1, "TA" + var[-1]]
                    else:
                        tmp = df_out.loc[t0:t1, "TA1"]
                    TA_var =  ["TA" + str(i) for i in range(1, 5) if "TA" + str(i) in df_out.columns]
                    tmp2 = df_out.loc[t0:t1, TA_var].mean(axis=1)
                    tmp.loc[tmp.isnull()] = tmp2.loc[tmp.isnull()]
                    tmp = tmp.interpolate(method="nearest", fill_value="extrapolate")
                    # plt.figure()
                    # df_out.loc[t0:t1, var].plot(ax=plt.gca(), label='original')
                    # (df_out.loc[t0:t1, var] * np.sqrt((tmp + 273.15) / 273.15)).plot(ax=plt.gca(), label='corrected')
                    df_out.loc[t0:t1, var] = df_out.loc[t0:t1, var].values / np.sqrt(
                        (tmp.values + 273.15) / 273.15
                    )
                    # df_out.loc[t0:t1, var].plot(ax=plt.gca(), label='anticorrected')
                    # plt.gca().legend()

                if func == "ice_to_water":
                    tmp = df_out.loc[t0:t1, "TA" + var[-1]]
                    tmp2 = df_out.loc[t0:t1, "TA" + str(int(var[-1]) % 2 + 1)]
                    tmp.loc[tmp.isnull()] = tmp2.loc[tmp.isnull()].values
                    tmp = tmp.interpolate(method="nearest", fill_value="extrapolate")
                    df_out.loc[t0:t1, var] = RH_ice2water(
                        df_out.loc[t0:t1, var].values, tmp.values
                    )

                if func == "water_to_ice":
                    tmp = df_out.loc[t0:t1, "TA" + var[-1]]
                    tmp2 = df_out.loc[t0:t1, "TA" + str(int(var[-1]) % 2 + 1)]
                    tmp.loc[tmp.isnull()] = tmp2.loc[tmp.isnull()].values
                    tmp = tmp.interpolate(method="nearest", fill_value="extrapolate")
                    df_out.loc[t0:t1, var] = RH_water2ice(
                        df_out.loc[t0:t1, var].values, tmp.values
                    )

                if func == "time_shift":
                    t0 = pd.to_datetime(t0)
                    t1 = pd.to_datetime(t1)

                    if t1 + pd.Timedelta(hours=val) > df_out.index[-1]:
                        # case where the files needs to be extended to receive the shifted data
                        nb_new_rows = (
                            t1 + pd.Timedelta(hours=val) - df_out.index[-1]
                        ).total_seconds() / 3600
                        df_new_rows = df_out.iloc[-int(nb_new_rows) :, :].copy()
                        df_new_rows.loc[:, :] = np.NaN
                        df_new_rows.index = df_new_rows.index + (
                            t1 + pd.Timedelta(hours=val) - df_out.index[-1]
                        )
                        df_out = pd.concat((df_out, df_new_rows))

                    df_out.loc[
                        t0 + pd.Timedelta(hours=val) : t1 + pd.Timedelta(hours=val), var
                    ] = df_out.loc[t0:t1, var].values

                    if val > 0:
                        if val < 10000:
                            # errasing data that existed during the time shift
                            col = df_out[var]
                            if pd.api.types.is_numeric_dtype(col):
                                df_out[var] = col.astype("float64")
                                df_out.loc[t0:(t0 + pd.Timedelta(hours=val)), var] = np.nan
                            else:
                                df_out[var] = col.astype(object)
                                df_out.loc[t0:(t0 + pd.Timedelta(hours=val)), var] = None
                        else:
                            # case of Crawford Point where only the shifted data should be errased
                            col = df_out[var]
                            if pd.api.types.is_numeric_dtype(col):
                                df_out[var] = col.astype("float64")
                                df_out.loc[t0:t1, var] = np.nan
                            else:
                                df_out[var] = col.astype(object)
                                df_out.loc[t0:t1, var] = None
                    else:
                        df_out.loc[t1 + pd.Timedelta(hours=val) : t1, var] = np.nan

                if (
                    ("_qc" not in var) & ("_min" not in var) & ("_max" not in var)
                    & ("_std" not in var)  & ("_adj_flag" not in var) & ("_min" not in var)
                ):
                    nan_count_2 = np.sum(np.isnan(df_out.loc[t0:t1, var].values))
                    Msg("|" + str(t0) + "|" + str(t1)  + "|" + var +"|" + func
                        + "|" + str(val) + "|" + str(nan_count_2 - nan_count_1) + "|"
                    )
    return df_out


def correct_net_rad(df_in, site):
    df_v5 = df_in.copy()
    df_v5['NR_cor'] = np.nan
    VW = df_v5[[v for v in ['VW1','VW2'] if v in df_v5.columns]].mean(axis=1)
    C_pos = 1 + (0.066*0.2*VW)/(0.066+(0.2*VW))
    C_neg = (0.00174*VW)+0.99755
    C_pos.loc[C_pos.isnull()] = 1.045
    C_neg.loc[C_neg.isnull()] = 1
    if site in ['Summit','Swiss Camp']:
        # At Summit and Swiss Camp:
        # The NR Lite2 is sensitive to wind. A correction theoretically can be
        # made by multiplying the calculated irradiances with a factor
        # ( 1 + x • v**(3/4) ), where v is the windspeed in m/s, x is determined
        # empirically to be approximately 0.01
        df_v5.loc['2000-06-01':, 'NR_cor'] = df_v5.loc['2000-06-01':, 'NR'] * \
            ( 1 + 0.01 * VW.loc['2000-06-01':]**(3/4) )
        tmp = df_v5.loc[:'2000-06-01', 'NR']
        tmp.loc[tmp>0] = C_pos * tmp.loc[tmp>0]
        tmp.loc[tmp<0] = C_neg * tmp.loc[tmp<0]
        df_v5.loc[:'2000-06-01', 'NR_cor'] = tmp
    else:
        df_v5.loc[df_v5.NR>0, 'NR_cor'] = C_pos * df_v5.loc[df_v5.NR>0, 'NR']
        df_v5.loc[df_v5.NR<0, 'NR_cor'] = C_neg * df_v5.loc[df_v5.NR<0, 'NR']
    return df_v5


def fill_gap_HW(df1, df2, var_target="HW1", var_sec="HW2", note=''):
    # Filling the gaps in HW1 with HW2
    if var_target+'_org' not in df1.columns:
        df1[var_target+'_org'] = ''
    # Gap-filling HW using other sensor if available
    prev_no_nan = df1[var_target].notnull().shift(1, fill_value=False)
    is_nan = df1[var_target].isnull()
    list_start_gaps = df1.index[(prev_no_nan & is_nan)]

    prev_nan = df1[var_target].isnull().shift(1, fill_value=False)
    no_nan = df1[var_target].notnull()
    list_end_gaps = df1.index[(prev_nan & no_nan)]

    list_start_gaps = list_start_gaps[list_start_gaps < df2.index[-1]]
    list_start_gaps = list_start_gaps[list_start_gaps > df2.index[0]]
    list_end_gaps = list_end_gaps[list_end_gaps < df2.index[-1]]
    list_end_gaps = list_end_gaps[list_end_gaps > df2.index[0]]

    if list_end_gaps[-1] < list_start_gaps[-1]:
        list_end_gaps = np.append(list_end_gaps, min(df1.index[-1],df2.index[-1]))
    if list_end_gaps[0] < list_start_gaps[0]:
        list_start_gaps = np.append(max(df1.index[0],df2.index[0]), list_start_gaps)


    for start, end in zip(list_start_gaps, list_end_gaps):
        # we look at the month preceeding the gap
        # calculate the mean difference between the two heights during that time
        mean_diff = (
            df1.loc[(start - pd.Timedelta(days=30)) : start, var_target]
            - df2.loc[(start - pd.Timedelta(days=30)) : start, var_sec]
        ).mean()
        if np.isnan(mean_diff):
            mean_diff = df1.loc[:, var_target].mean() - df2.loc[:, var_sec].mean()

        # and use that difference to adjust the secondary height to the height
        # that is to be gap-filled
        df1.loc[start:end, var_target] = (
            df2.loc[start:end, var_sec].values + mean_diff
        )
        df1.loc[start:end, var_target+'_org'] = var_sec + note

    return df1[var_target].values


def augment_data(df_in, latitude, longitude, elevation, site):
    # Interpolate small gaps in available variables
    # and add variables to the dataset:
    # Surface height HS
    # Sensible and Latent Heat Fluxes SHF & LHF
    # Solar azimuth and zenith angles
    # albedo

    # for debug:
    # df_in = df_v5.copy()
    df = df_in.copy()

    # Interpolation over gaps smaller than two days
    for var in ['HW1','HW2']:
        if var not in df.columns:
            Msg(var+' '+ 'not in dataframe')
            continue

        if df[var].isnull().all():
            Msg('No valid data for '+var)
            continue

        # Creating surface height field
        ind1 = df[var].first_valid_index()
        var_HS = "HS"+var[-1]
        df[var_HS] = df.loc[ind1, var] - df[var]


        if site in ['SMS1', 'SMS2', 'SMS3', 'SMS4', 'SMS5', 'SMS-PET', 'Summit',
                    'NASA-SE','Tunu-N', 'EastGRIP', 'LAR1', 'JAR2', 'JAR1',
                    'Petermann ELA', 'NGRIP']:
            thresh = 0.7
            if site == 'Tunu-N':
                thresh=0.173
            if site == 'JAR1':
                thresh=0.8

            # plt.close('all')
            fig, ax = plt.subplots(1,1)
            df[var].bfill().plot(ax=ax,marker='.', linestyle='None', label=var+' backfilled')
            df[var].plot(ax=ax,marker='.', linestyle='None', label=var)

            diff = df[var].bfill().diff()
            diff.plot(ax=ax,marker='o', linestyle='None', label='all shifts')
            if (diff.abs()>thresh).any():
                diff.loc[diff.abs()>thresh].plot(ax=ax, marker='o',
                                                 linestyle='None',
                                                 label='selected shifts')
            diff.loc[diff.abs()<thresh] = 0
            if 'SMS' in site:
                diff.loc[diff>0] = 0

            # average daily accumulation
            if site == 'Tunu-N':
                avg_accum = 0.000784
            elif site == 'JAR1':
                avg_accum = -.0043
            elif site == 'NASA-SE':
                avg_accum = 0.003
            else:
                avg_accum = -df[var].resample('D').mean().diff().mean()

            large_diff_times = pd.to_datetime(diff.loc[diff.abs() > thresh].index.values, utc=True)

            for i, t in enumerate(large_diff_times):
                t_prev = large_diff_times[i-1] if i > 0 else pd.Timestamp.min.tz_localize("UTC")
                t_next = large_diff_times[i+1] if i < len(large_diff_times)-1 else pd.Timestamp.max.tz_localize("UTC")

                one_week_before_gap = slice(max(t - pd.Timedelta(days=7), t_prev), t)
                one_week_after_gap  = slice(t, min(t + pd.Timedelta(days=7), t_next))
                no_values_before_or_after = df.loc[one_week_after_gap, var].isnull().all() | df.loc[one_week_before_gap, var].isnull().all()
                if no_values_before_or_after:
                    last_good_index = df.loc[:t, var].last_valid_index()
                    next_good_index = df.loc[t:, var].first_valid_index()
                    diff.loc[t] = df.loc[next_good_index, var] - df.loc[last_good_index, var] + avg_accum * (next_good_index-last_good_index).total_seconds()/3600/24
                    if (site =='JAR1'):
                        if (t.year == 2018):
                            diff.loc[t] = 0
                        if ((t.year==2012) & (t.month==7)):
                            diff.loc[t] = 0
                else:
                    diff.loc[t] = df.loc[one_week_after_gap, var].median() - df.loc[one_week_before_gap, var].median()
                if  (diff.loc[t]!=0):
                    if t == diff.loc[diff.abs()>thresh].index.values[0]:
                        ax.axvline(t, linestyle='--', label='shift applied')
                    else:
                        ax.axvline(t, linestyle='--', label='_nolegend_')
            df[var_HS] = df[var_HS] + diff.cumsum()
            df[var_HS].plot(label=var_HS)
            plt.legend()
            fig.savefig("figures/L1_data_treatment/" + site + "_"+var_HS+"_adjust_auto.png")
            # x = df[var_HS].index.values.astype(float)/10**9/3600/24
            # y = df[var_HS].values
        else:
            # we then adjust and filter all surface height (could be replaced by an automated adjustment)
            df_save=df.copy()
            df = adjust_data(df, site, var_list=[var_HS], skip_time_shifts=True)
            plot_flagged_data(df, df_save, site, var_list=var_HS)



        # HW1 gapfilled with HW2 and inversely
        var_sec = var[:-1]+str(int(var[-1])%2 +1)
        if var_sec in df.columns:
            if df[var].notnull().any():
                df[var+'_org'] = var
                # df[var] = fill_gap_HW(df, df, var, var_sec)
                df.loc[df[var]<0, var] = np.nan

        # At swiss camp, using HW from tower to fill the gaps
        if site == 'Swiss Camp 10m':
            if var == 'HW1':
                df_swc = nead.read("L1/hourly/SwissCamp.csv").to_dataframe().reset_index(drop=True)
                df_swc['timestamp'] = pd.to_datetime(df_swc.timestamp)
                df_swc = df_swc.set_index("timestamp").replace(-999, np.nan)

            df[var] = fill_gap_HW(df, df_swc, var, "HW1", note= ' aws')
            df[var] = fill_gap_HW(df, df_swc, var, "HW2", note= ' aws')
            df.loc[df[var]<0, var] = np.nan

    # HS summary:
    if 'HS2' in df.columns:
        df[['HS1','HS2']].plot()
        tmp = df[ ["HS1", "HS2"]].copy()
        tmp.HS2 = tmp.HS2- (tmp.HS2-tmp.HS1).mean()
        df['HS_combined'] = tmp[["HS1", "HS2"]].mean(axis=1)

    # plotting gap-filling process
    fig,ax = plt.subplots(2,1, figsize=(15,8))
    if 'HW1_org' in df.columns:
        df.HW2.plot(ax=ax[0], marker='.',color='gray')
        for src in df.HW1_org.unique():
            df.HW1.loc[df.HW1_org == src].plot(ax=ax[0], label=src, marker="o", linestyle="None")
        df = df.drop(columns=['HW1_org'])
        ax[0].set_ylabel('HW1')
    if 'HW2_org' in df.columns:
        df.HW1.plot(ax=ax[1], marker='.',color='gray')
        for src in df.HW2_org.unique():
            df.HW2.loc[df.HW2_org == src].plot(ax=ax[1], label=src, marker="o", linestyle="None")
        df = df.drop(columns=['HW2_org'])
        ax[0].set_ylabel('HW1')
    ax[0].legend()
    ax[1].legend()
    fig.savefig("figures/L1_data_treatment/" + site + "_gap_filling_HW.png")

    if 'TA3' in df.columns:
        # calculating SHF and LHF
        df["SHF"], df["LHF"] = jaws_tools.gradient_fluxes(df.copy())

        # interpolating variables at standard heights
        df["TA2m"] = extrapolate_variable_standard_height(df,
                                                          var=["TA1", "TA2"],
                                                          target_height=2,
                                                          max_diff=5)
        df["RH2m"] = extrapolate_variable_standard_height(df,
                                                          var=["RH1", "RH2"],
                                                          target_height=2,
                                                          max_diff=10)
        df["VW10m"] = extrapolate_variable_standard_height(df,
                                                           var=["VW1", "VW2"],
                                                           target_height=10,
                                                           max_diff=10)

        df.loc[df['TA2m']>20, 'TA2m'] = np.nan
        df.loc[df['TA2m']<-80, 'TA2m'] = np.nan
        df.loc[df['RH2m']>120, 'RH2m'] = np.nan
        df.loc[df['RH2m']<20, 'RH2m'] = np.nan
        df.loc[df['VW10m']>40, 'VW10m'] = np.nan
        df.loc[df['VW10m']<0, 'VW10m'] = 0

    # Solar zenith and azimuth angles
    df["SZA"], df["SAA"] = sza_saa(df, longitude, latitude)

    # Albedo
    if 'OSWR' in df.columns:
        df['Alb'] = calcAlbedo(df.OSWR, df.ISWR, df.SZA)

    # Humidity with regard to ice and specific humidity
    T1 = df.TA1.copy()
    if 'TA3' in df.columns:
        T1.loc[T1.isnull()] = df.loc[T1.isnull(), 'TA3']
        T1.loc[T1.isnull()] = df.loc[T1.isnull(), 'TA2']
        T1.loc[T1.isnull()] = df.loc[T1.isnull(), 'TA4']
    df['RH1_wrt_ice_or_water'] = correctHumidity(df.RH1, T1)
    if 'P' in df.columns:
        df['Q1'] = calcHumid(T1, df.P, df.RH1_wrt_ice_or_water)  *1000
        df.loc[df['Q1']>40, 'Q1'] = np.nan

    if 'RH2' in df.columns:
        T2 = df.TA2.copy()
        T2.loc[T2.isnull()] = df.loc[T2.isnull(), 'TA4']
        T2.loc[T2.isnull()] = df.loc[T2.isnull(), 'TA1']
        T2.loc[T2.isnull()] = df.loc[T2.isnull(), 'TA3']

        df['RH2_wrt_ice_or_water'] = correctHumidity(df.RH2, T2)

        df['Q2'] = calcHumid(T2, df.P, df.RH2_wrt_ice_or_water)  *1000
        df.loc[df['Q2']>40, 'Q2'] = np.nan

    # %% adding latitude and longitude fields
    # initialization
    df['latitude'] = latitude
    df['longitude'] = longitude
    df['elevation'] = elevation

    # filling lat lon if available
    p = f"metadata/interpolated positions/{site}_position_interpolated.csv"
    def extrapolate(df, y_col):
        df_ = df[[y_col]].dropna()
        return LinearRegression().fit(
            df_.index.values.astype(float).reshape(-1,1), df_[y_col]).predict(
            df.index.values.astype(float).reshape(-1,1))

    df_pos = None
    if os.path.isfile(p):
        Msg(f'Using {p} for variable latitude and longitude')
        df_pos = pd.read_csv(p, index_col=0, parse_dates=[0]).sort_index()
        df_pos.index = pd.to_datetime(df_pos.index, utc=True)

        # keep only anchor points (interpolate needs non-NaN anchors)
        df_pos = df_pos[["lon", "lat"]].dropna(how="any")
        if len(df_pos) < 2:
            raise ValueError("Need at least two non-NaN lon/lat points to interpolate/extrapolate.")

        offset = pd.DateOffset(months=7)
        df_pos = df_pos.shift(freq=-offset).resample("YS").first().shift(freq=offset).sort_index()

        full_index = pd.to_datetime(df_pos.index.union(df.index), utc=True).drop_duplicates().sort_values()
        x = df_pos.reindex(full_index).interpolate(method="time")
        t0, t1 = df_pos.index.min(), df_pos.index.max()
        x = x.loc[(x.index >= t0) & (x.index <= t1)]

        df_pos_resampled = x.reindex(df.index)

        df_pos_resampled['lat'] = extrapolate(df_pos_resampled, 'lat')
        df_pos_resampled['lon'] = extrapolate(df_pos_resampled, 'lon')

        df["latitude"] = df_pos_resampled["lat"]
        df["longitude"] = df_pos_resampled["lon"]

    df_elev = None
    if site in ['JAR1','Swiss Camp 10m', 'Swiss Camp', 'JAR2','JAR3']:
        p='metadata/interpolated positions/GC-Net_elevation_tie_points.csv'
        Msg(f'Using {p} for variable elevation')
        df_elev = pd.read_csv(p)
        site_tmp = 'Swiss Camp' if site=='Swiss Camp 10m' else site
        df_elev = df_elev.loc[df_elev["site"].eq(site_tmp)].drop(columns="site")
        df_elev["time"] = pd.to_datetime(df_elev["year"].astype(int).astype(str) + "-01-01", utc=True) + pd.to_timedelta((df_elev["year"] % 1) * 365, unit="D")
        df_elev = df_elev.set_index('time')

        full_index = pd.to_datetime(df_elev.index.union(df.index), utc=True).drop_duplicates().sort_values()
        x = df_elev.reindex(full_index).interpolate(method="time")
        t0, t1 = df_elev.index.min(), df_elev.index.max()
        x = x.loc[(x.index >= t0) & (x.index <= t1)]

        df_elev_resampled = x.reindex(df.index)
        df["elevation"] = df_elev_resampled["altitude"]

    fig, ax = plt.subplots(3,1,sharex=True)
    df[['latitude']].plot(ax=ax[0])
    df[['longitude']].plot(ax=ax[1])
    if df_pos is not None:
        df_pos.lat.plot(ax=ax[0], marker='o',ls='None', label='anchor points')
        df_pos.lon.plot(ax=ax[1], marker='o',ls='None', label='anchor points')
    df[['elevation']].plot(ax=ax[2])
    if df_elev is not None:
        df_elev.altitude.plot(ax=ax[2], marker='o',ls='None', label='anchor points')
    fig.suptitle(site)
    fig.savefig("figures/positions/" + site + "_positions.png", dpi=120)

    return df

from scipy.interpolate import interp1d

def interpolate_temperature(dates, depth_cor, temp, depth=10,
                            min_diff_to_depth=2, kind="quadratic", title="",
                            plot=True, surface_height=[]):
    depth_cor = depth_cor.astype(float)
    df_interp = pd.DataFrame()
    df_interp["date"] = dates
    df_interp["temperatureObserved"] = np.nan

    # preprocessing temperatures for small gaps
    tmp = pd.DataFrame(temp)
    tmp["time"] = dates
    tmp = tmp.set_index("time")
    tmp = tmp.resample("h").mean()
    # tmp = tmp.interpolate(limit=24*7)
    temp = tmp.loc[dates].values
    for i in (range(len(dates))):
        x = depth_cor[i, :].astype(float)
        y = temp[i, :].astype(float)
        ind_no_nan = ~np.isnan(x + y)
        x = x[ind_no_nan]
        y = y[ind_no_nan]
        x, indices = np.unique(x, return_index=True)
        y = y[indices]
        if len(x) < 2 or np.min(np.abs(x - depth)) > min_diff_to_depth:
            continue
        f = interp1d(x, y, kind, fill_value="extrapolate")
        df_interp.iloc[i, 1] = np.min(f(depth), 0)

    if df_interp.iloc[:5, 1].std() > 0.1:
        df_interp.iloc[:5, 1] = np.nan
    # df_interp['temperatureObserved']  = df_interp['temperatureObserved'].interpolate(limit=24*7).values
    if plot:
        import matplotlib.dates as mdates

        myFmt = mdates.DateFormatter("%Y-%m")

        for i in range(len(depth_cor[0, :]) - 1, 0, -1):
            if all(np.isnan(depth_cor[:, i])):
                continue
            else:
                break
        if len(surface_height) == 0:
            surface_height = (
                depth_cor[:, i] - depth_cor[:, i][np.isfinite(depth_cor[:, i])][0]
            )

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(17, 6))
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.99, top=0.8)
        ax1.plot(dates, surface_height, color="black", linewidth=3)
        for i in range(np.shape(depth_cor)[1]):
            ax1.plot(dates, -depth_cor[:, i] + surface_height)

        ax1.plot(dates, surface_height - 10, color="red", linewidth=5)
        ax1.set_ylim(
            np.nanmin(surface_height) * 1.1 - 10, np.nanmax(surface_height) * 1.1
        )
        ax1.set_xlim(min(dates), max(dates))
        ax1.set_ylabel("Height (m)")
        ax1.xaxis.set_major_formatter(myFmt)
        ax1.tick_params(axis="x", rotation=45)

        for i in range(np.shape(depth_cor)[1]):
            ax2.plot(dates, temp[:, i])
        ax2.plot(
            dates,
            df_interp["temperatureObserved"],
            marker="o",
            markersize=5,
            color="red",
            linestyle=None,
        )
        ax2.set_ylabel("Firn temperature (degC)")
        ax2.set_ylim(np.nanmin(temp) * 1.2, min(1, 0.8 * np.nanmax(temp)))
        ax2.xaxis.set_major_formatter(myFmt)
        ax2.tick_params(axis="x", rotation=45)
        ax2.axes.grid()
        ax2.set_xlim(min(dates), max(dates))

        fig.suptitle(title)  # or plt.suptitle('Main title')
        im = plt.imread("figures/legend_1.png")  # insert local path of the image.
        newax = fig.add_axes([0.15, 0.8, 0.2, 0.2], anchor="NW", zorder=0)
        newax.imshow(im)
        newax.axes.xaxis.set_visible(False)
        newax.axes.yaxis.set_visible(False)
        fig.savefig("figures/string processing/interp_" + title + ".png", dpi=300)
    return df_interp


def calcAlbedo(usr, dsr, ZenithAngle_deg):
    '''Calculate surface albedo based on upwelling and downwelling shorwave
    flux, the angle between the sun and sensor, and the sun zenith'''
    albedo = usr / dsr

    # NaN bad data
    OKalbedos = (ZenithAngle_deg < 70) & (albedo < 1) & (albedo > 0) & (usr >100) & (dsr>100)
    albedo[~OKalbedos] = np.nan

    # Interpolate all. Note "use_coordinate=False" is used here to force
    # comparison against the GDL code when that is run with *only* a TX file.
    # Should eventually set to default (True) and interpolate based on time,
    # not index.
    # albedo = albedo.interpolate_na(dim='time', use_coordinate=False)
    # albedo = albedo.ffill(dim='time').bfill(dim='time')                        #TODO remove this line and one above?
    return albedo


def therm_depth(df_in, site,min_diff_to_depth=1.5,kind="linear"):
    df_v6 = df_in.copy()

    # downloading metadata from online google sheet
    try:
        url = (
            "https://docs.google.com/spreadsheets/d/172LNxgYevqwO892zrc98UDMAVTQmJ0XZB5kmMLme4GM/gviz/tq?tqx=out:csv&sheet="
            + site.replace(" ", "%20")
        )
        pd.read_csv(url).to_csv("metadata/maintenance summary/" + site + ".csv")
    except:
        Msg("Cannot download maintenance summary. Using local file.")
        pass

    maintenance_string = pd.read_csv("metadata/maintenance summary/" + site + ".csv")

    col_depth_installation = ['NewDepth1 (m)', 'NewDepth2 (m)', 'NewDepth3 (m)',
                          'NewDepth4 (m)', 'NewDepth5 (m)', 'NewDepth6 (m)',
                          'NewDepth7 (m)', 'NewDepth8 (m)', 'NewDepth9 (m)',
                          'NewDepth10 (m)']
    if maintenance_string.shape[0] == 0:
        Msg('No installtion depth reported, using default')
        maintenance_string['date'] = [df_v6.index[0]]
        maintenance_string[col_depth_installation] = [np.arange(1,11)]
    maintenance_string.date = pd.to_datetime(maintenance_string.date,
                                             format='mixed', utc=True)
    maintenance_string = maintenance_string.set_index('date')
    maintenance_string = maintenance_string[col_depth_installation]
    msk = maintenance_string[col_depth_installation].notnull().all(axis=1)
    maintenance_string = maintenance_string.loc[msk, :]

    temp_cols_name = [v for v in df_v6.columns if 'TS' in v]
    num_therm = len(temp_cols_name)
    depth_cols_name = ['DTS'+str(i) for i in range(1,num_therm+1)]

    df_v6[depth_cols_name] = np.nan

    ini_depth = np.arange(1,11)

    # filtering the surface height
    surface_height = df_v6["HS_combined"].copy()
    ind_filter = surface_height.rolling(window=14, center=True).var() > 0.1
    if any(ind_filter):
        surface_height[ind_filter] = np.nan
    df_v6["HS_combined"] = surface_height.values
    start = df_v6["HS_combined"].first_valid_index()
    end = df_v6["HS_combined"].last_valid_index()
    df_v6["HS_combined"] = df_v6["HS_combined"].interpolate().values
    df_v6.loc[slice(None,start), "HS_combined"] = np.nan
    df_v6.loc[slice(end,None), "HS_combined"] = np.nan
    # first initialization of the depths
    for i, col in enumerate(depth_cols_name):
        df_v6[col] = (
            ini_depth[i]
            + df_v6["HS_combined"].values
            - df_v6["HS_combined"][
                df_v6["HS_combined"].first_valid_index()
            ]
        )

    # reseting depth at maintenance
    for date in maintenance_string.index:
        if date > df_v6["HS_combined"].last_valid_index():
            continue
        new_depth = maintenance_string.loc[
                                        date,
                                        col_depth_installation
                                    ].values

        for i, col in enumerate(depth_cols_name):
            tmp = df_v6[col].copy()
            tmp.loc[date:] = (
                new_depth[i]
                + df_v6["HS_combined"][date:].values
                - df_v6["HS_combined"][date:][
                    df_v6["HS_combined"][
                        date:
                    ].first_valid_index()
                ]
            )
            df_v6[col] = tmp.values

    # % Filtering thermistor data
    for i in range(len(temp_cols_name)):
        tmp = df_v6[temp_cols_name[i]].copy()

        # variance filter
        ind_filter = (
            df_v6[temp_cols_name[i]]
            .interpolate(limit=14)
            .rolling(window=7)
            .var()
            > 0.5
        )
        month = (
            df_v6[temp_cols_name[i]].interpolate(limit=14).index.month.values
        )
        ind_filter.loc[np.isin(month, [5, 6, 7])] = False
        if any(ind_filter):
            tmp.loc[ind_filter] = np.nan

        # before and after maintenance_string adaptation filter
        if len(maintenance_string.index) > 0:
            for date in maintenance_string.index:
                ind_adapt = np.abs(
                    tmp.interpolate(limit=14).index.values
                    - pd.to_datetime(date).to_datetime64()
                ) < np.timedelta64(7, "D")
                if any(ind_adapt):
                    tmp.loc[ind_adapt] = np.nan

        # surfaced thermistor
        ind_pos = df_v6[depth_cols_name[i]] < 0.1
        if any(ind_pos):
            tmp.loc[ind_pos] = np.nan
        # copying the filtered values to the original table
        df_v6[temp_cols_name[i]] = tmp.values

    # interpolating 10 m firn/ice temp
    df_v6['TS_10m'] = interpolate_temperature(
        df_v6.index.values,
        df_v6[depth_cols_name].values.astype(float),
        df_v6[temp_cols_name].values.astype(float),
        kind=kind,
        title=site,
        plot=False,
        min_diff_to_depth=min_diff_to_depth,
    ).set_index('date').values

    # filtering
    ind_pos = df_v6["TS_10m"] > 0.1
    ind_low = df_v6["TS_10m"] < -70
    df_v6.loc[ind_pos, "TS_10m"] = np.nan
    df_v6.loc[ind_low, "TS_10m"] = np.nan

    #  Plotting
    fig, ax = plt.subplots(1, 2, figsize=(15, 6),sharex=True)
    plt.subplots_adjust(left=0.05, right=0.95, wspace=0.15, top=0.95)

    df_v6["HS_combined"].plot(
        ax=ax[0], color="black", label="surface", linewidth=3
    )
    (df_v6["HS_combined"] - 10).plot(
        ax=ax[0],  color="red", linestyle="-", linewidth=4,
        label="10 m depth",
    )

    for date in maintenance_string.index:
        index = df_v6["HS_combined"].index
        date2 = index[index.get_indexer([date], method="nearest")[0]]
        if np.abs(date - date2) <= pd.Timedelta("7 days"):
            ax[0].axvline(np.datetime64(date), color='r')
    depth_cols_name.reverse()
    for i, col in enumerate(depth_cols_name):
        (-df_v6[col] + df_v6["HS_combined"]).plot(
            ax=ax[0],
            label="_nolegend_",
        )
    depth_cols_name.reverse()

    ax[0].set_ylim(
        df_v6["HS_combined"].min() - 11,
        df_v6["HS_combined"].max() + 1,
    )

    for i in reversed(range(len(temp_cols_name))):
        df_in[temp_cols_name[i]].interpolate(limit=14).plot(
            ax=ax[1], label="_nolegend_"
        )

        tmp = df_in[temp_cols_name[i]].copy()
        # variance filter
        ind_filter = (
            df_in[temp_cols_name[i]]
            .interpolate(limit=14)
            .rolling(window=7)
            .var()
            > 0.5
        )
        month = (
            df_in[temp_cols_name[i]]
            .interpolate(limit=14)
            .index.month.values
        )
        ind_filter.loc[np.isin(month, [5, 6, 7])] = False
        if any(ind_filter):
            tmp.loc[ind_filter].plot(
                ax=ax[1], marker=".", linestyle="none",
                color="lightgray", alpha=0.5,  label="_nolegend_",
            )

        # before and after maintenance_string adaptation filter
        for date in maintenance_string.index:
            ind_adapt = np.abs(
                tmp.interpolate(limit=14).index.values
                - pd.to_datetime(date).to_datetime64()
            ) < np.timedelta64(7, "D")
            if any(ind_adapt):
                tmp.loc[ind_adapt].plot(
                    ax=ax[1], marker="o", linestyle="none",
                    color="lightgray", alpha=0.5,  label="_nolegend_",
                )

        # surfaced thermistor
        ind_pos = df_v6[depth_cols_name[i]] < 0.1
        if any(ind_pos):
            tmp.loc[ind_pos].plot(
                ax=ax[1], marker=".", alpha=0.5, linestyle="none", color="lightgray",
                label="_nolegend_",
            )
    if len(df_v6["TS_10m"]) == 0:
        Msg("No 10m temp for "+site)
    else:
        df_v6["TS_10m"].resample("D").mean().plot(ax=ax[1],
                                                               color="red",
                                                               linewidth=5,
                                                               label="10 m temperature")
    ax[1].plot(
        np.nan, np.nan,  marker="o", linestyle="none", color="lightgray",
        label="filtered",
    )
    ax[1].plot(
        np.nan, np.nan, marker="o", linestyle="none",
        color="purple", label="maintenance",
    )
    ax[1].plot(
        np.nan, np.nan, marker="o", linestyle="none", color="pink", label="var filter"
    )
    ax[1].legend(loc='upper center')
    ax[0].legend(loc='upper right')
    ax[0].set_ylabel("Height (m)")
    ax[1].set_ylabel("Subsurface temperature ($^o$C)")
    fig.suptitle(site)
    fig.savefig("figures/string_processing/" + site + ".png", dpi=90)
    return df_v6


def calcHumid(T_h, p_h, RH_cor_h, T_0=273.15, T_100=373.15,
              es_0=6.1071, es_100=1013.246, eps=0.622):
    '''Calculate specific humidity'''
    # Saturation vapour pressure above 0 C (hPa)
    es_wtr = 10**(-7.90298 * (T_100 / (T_h + T_0) - 1) + 5.02808 * np.log10(T_100 / (T_h + T_0))
                  - 1.3816E-7 * (10**(11.344 * (1 - (T_h + T_0) / T_100)) - 1)
                  + 8.1328E-3 * (10**(-3.49149 * (T_100 / (T_h + T_0) -1)) - 1) + np.log10(es_100))

    # Saturation vapour pressure below 0 C (hPa)
    es_ice = 10**(-9.09718 * (T_0 / (T_h + T_0) - 1) - 3.56654
                  * np.log10(T_0 / (T_h + T_0)) + 0.876793
                  * (1 - (T_h + T_0) / T_0)
                  + np.log10(es_0))

    # Specific humidity at saturation (incorrect below melting point)
    q_sat = eps * es_wtr / (p_h - (1 - eps) * es_wtr)

    # Replace saturation specific humidity values below melting point
    freezing = T_h < 0
    q_sat[freezing] = eps * es_ice[freezing] / (p_h[freezing] - (1 - eps) * es_ice[freezing])

    # Convert to kg/kg
    return RH_cor_h * q_sat / 100


def correctHumidity(rh, T, T_0=273.15, T_100=373.15, ews=1013.246, ei0=6.1071):
    '''Correct relative humidity using Groff & Gratch method
    Parameters
    ----------
    rh : xarray.DataArray
        Relative humidity
    T : xarray.DataArray
        Air temperature
    T_0 : int
        Steam point temperature
    T_100 : int
        Steam point temperature in K
    ews : int
        Saturation pressure (normal atmosphere) at steam point temperature
    ei0 : int
        DESCRIPTION

    Returns
    -------
    xarray.DataArray
        Corrected relative humidity
    '''
    # Convert to hPa (Groff & Gratch)
    e_s_wtr = 10**(-7.90298 * (T_100 / (T + T_0) - 1)
                   + 5.02808 * np.log10(T_100 / (T + T_0))
                   - 1.3816E-7 * (10**(11.344 * (1 - (T + T_0) / T_100)) - 1)
                   + 8.1328E-3 * (10**(-3.49149 * (T_100/(T + T_0) - 1)) -1)
                   + np.log10(ews))
    e_s_ice = 10**(-9.09718 * (T_0 / (T + T_0) - 1)
                   - 3.56654 * np.log10(T_0 / (T + T_0))
                   + 0.876793 * (1 - (T + T_0) / T_0)
                   + np.log10(ei0))

    # Define freezing point. Why > -100?
    freezing = (T < 0) & (T > -100).values

    # Set to Groff & Gratch values when freezing, otherwise just rh
    rh_cor = rh.where(~freezing, other = rh*(e_s_wtr / e_s_ice))
    return rh_cor


def sza_saa(df, longitude, latitude):
        # calculatin SZA and SAA with same script as for PROMICE stations
    doy = df.index.dayofyear.values
    hour = df.index.hour.values
    minute = df.index.minute.values
    lon = np.abs(longitude)
    deg2rad = np.pi / 180
    rad2deg = 1 / deg2rad

    d0_rad = 2 * np.pi * (doy + (hour + minute / 60) / 24 - 1) / 365

    Declination_rad = np.arcsin(
        0.006918
        - 0.399912 * np.cos(d0_rad)
        + 0.070257 * np.sin(d0_rad)
        - 0.006758 * np.cos(2 * d0_rad)
        + 0.000907 * np.sin(2 * d0_rad)
        - 0.002697 * np.cos(3 * d0_rad)
        + 0.00148 * np.sin(3 * d0_rad)
    )

    HourAngle_rad = 2 * np.pi * (((hour + minute / 60) / 24 - 0.5) - lon / 360)
    # ; - 15.*timezone/360.) ; NB: Make sure time is in UTC and longitude is positive when west! Hour angle should be 0 at noon.

    # This is 180 deg at noon (NH), as opposed to HourAngle.
    DirectionSun_deg = HourAngle_rad * 180 / np.pi - 180

    DirectionSun_deg[DirectionSun_deg < 0] += 360
    DirectionSun_deg[DirectionSun_deg < 0] += 360

    ZenithAngle_rad = np.arccos(
        np.cos(latitude * deg2rad) * np.cos(Declination_rad) * np.cos(HourAngle_rad)
        + np.sin(latitude * deg2rad) * np.sin(Declination_rad)
    )

    ZenithAngle_deg = ZenithAngle_rad * rad2deg
    return ZenithAngle_deg, DirectionSun_deg


def extrapolate_variable_standard_height(df, var=["TA1", "TA2"], log=False,
                     target_height=2, max_diff=5):
    ht_low = df["HW1"].copy()  # height of lower level
    ht_high = df["HW2"].copy()  # height of upper level
    if log:
        ht_low = np.log(ht_low)
        ht_high = np.log(ht_high)
        target_height = np.log(target_height)
    var_low = df[var[0]].copy()
    var_high = df[var[1]].copy()

    # making sure the level 1 is the lowest and 2 the highest
    ind = ht_high < ht_low
    ht_low.loc[ind] = df["HW2"].values[ind]
    ht_high.loc[ind] = df["HW1"].values[ind]
    var_low.loc[ind] = df[var[1]].values[ind]
    var_high.loc[ind] = df[var[0]].values[ind]

    msk = (
        (var_low+var_high+ht_low+ht_high).notnull()
        & ((var_low - var_high) != 0)
        & ((ht_low - ht_high) != 0)
    )
    if log:
        # if we assume a logarithmic profile, then we can only use timestamps
        # where wind speed is lower at the lower level than at the upper level
        msk = msk & (var_low <= var_high)
    extrapolated_var = ht_low * np.nan

    extrapolated_var.loc[msk] = var_low.loc[msk] + (
        ((var_high.loc[msk] - var_low.loc[msk]) / (ht_high.loc[msk] - ht_low.loc[msk]))
        * (target_height - ht_low.loc[msk])
    )

    extrapolated_var.loc[extrapolated_var<0] = np.nan
    extrapolated_var.loc[extrapolated_var>35] = np.nan
    # filter on difference between the extrapolated value and the original measurement
    diff_1 = (extrapolated_var - var_low).abs()
    diff_2 = (extrapolated_var - var_high).abs()
    extrapolated_var.loc[(diff_1 > max_diff) | (diff_2 > max_diff)] = np.nan

    if log & (target_height == np.log(10)):
        # if we deal with wind extrapolation, we fill the gaps in extrapolated
        # 10 m wind speed by a theoretical extrapolation to 10 m using a log
        # profile and a roughness length of 0.01 m
        Z0 = 0.01          # Surface Roughness (m)
        # theoretical U10m from lower level
        U10m_theoretical = pd.DataFrame()
        U10m_theoretical['from_low'] = var_low * np.log(10/Z0)/np.log(np.exp(ht_low)/Z0)
        # theoretical U10m from upper level
        U10m_theoretical['from_high'] = var_high * np.log(10/Z0)/np.log(np.exp(ht_high)/Z0)
        U10m_theoretical.loc[U10m_theoretical.from_low<0, 'from_low'] = np.nan
        U10m_theoretical.loc[U10m_theoretical.from_low>35, 'from_low'] = np.nan
        U10m_theoretical.loc[U10m_theoretical.from_high<0, 'from_high'] = np.nan
        U10m_theoretical.loc[U10m_theoretical.from_high>35, 'from_high'] = np.nan

        extrapolated_var.loc[extrapolated_var.isnull()] = \
            U10m_theoretical.from_high.combine_first(U10m_theoretical.from_low).loc[extrapolated_var.isnull()]
    return extrapolated_var


def filter_zero_gradient(df_out):
    # Filter frozen values
    # default settings:
    thresh = 0.000001
    length_frozen = 6
    not_in_dark_season = False
    var_list = [
        "VW1", "VW2", "DW1", "DW2", "TA1", "TA1", "TA2",
        "TA3", "TA4", "P", "ISWR", "OSWR",
    ]
    for var in var_list:
        if var not in df_out.columns:
            continue
        if var in ["HW1", "HW2"]:
            length_frozen = 5 * 24
        if var in ["ISWR", "OSWR"]:
            thresh = 1
            length_frozen = 24
            not_in_dark_season = True

        ind = np.abs(df_out[var].diff().values) < thresh

        if not_in_dark_season:
            dark_month = df_out["ISWR"].groupby(df_out.index.month).mean() < 5
            ind_winter = np.isin(df_out.index.month, dark_month[dark_month].index)
            ind[ind_winter] = False

        if np.any(ind):
            no_wind_count = 0
            for i, val in enumerate(ind):
                if val:
                    no_wind_count = no_wind_count + 1
                else:
                    if no_wind_count > 0:
                        if no_wind_count <= length_frozen:
                            # gap less than length_frozen hours putting down the flag
                            ind[np.arange(i - no_wind_count, i + 1)] = False
                            no_wind_count = 0
                        else:
                            # too long period without wind, leaving flags up
                            no_wind_count = 0
            # ind = binary_dilation(ind)

            if var + "_qc" in df_out.columns:
                df_out.loc[ind, var + "_qc"] = "FROZEN"
            else:
                df_out[var + "_qc"] = "OK"
                df_out.loc[ind, var + "_qc"] = "FROZEN"
    return df_out


def filter_data(df, site, lat, lon, plot=True):
    """
    Applies standard filter on data.

    INTPUTS:
        df: PROMICE data with time index
        site: string of PROMICE site
        var_list: list of the variables for which data removal should be
            conducted (default: all)
        plot: whether data removal should be plotted

    OUTPUTS:
        promice_data: Dataframe containing PROMICE data for the desired settings [DataFrame]
    """
    df_out = df.copy()

    # flagging frozen values
    df_out = filter_zero_gradient(df_out)

    # Limits filter:
    df_lim = pd.read_csv("metadata/limits.csv",comment="#",  skipinitialspace=True)
    df_lim.columns = ["site", "var_lim", "var_min", "var_max"]
    for site_lim, var, var_min, var_max in zip(
        df_lim.site, df_lim.var_lim, df_lim.var_min, df_lim.var_max
    ):
        if site_lim == "*" or site_lim == site:
            if ('*' in var) |('$' in var):
                var_list = df_out.filter(regex=(var)).columns
                var_list = [v for v in var_list if "qc" not in v]
            else:
                var_list = [var]
            for var in var_list:
                if var in df_out.columns.values:
                    ind = np.logical_or(df_out[var] > var_max, df_out[var] < var_min)
                    if var + "_qc" in df_out.columns:
                        df_out.loc[ind, var + "_qc"] = "OOL"
                    else:
                        df_out[var + "_qc"] = "OK"
                        df_out.loc[ind, var + "_qc"] = "OOL"

    # Isolated measurements filter
    msk1 = df_out.HW1.isnull().shift(2, fill_value=False)
    msk2 = df_out.HW1.isnull().shift(1, fill_value=False)
    msk3 = df_out.HW1.isnull().shift(-1, fill_value=False)
    msk4 = df_out.HW1.isnull().shift(-2, fill_value=False)
    msk = (msk2 & msk3) | (msk1 & msk3) | (msk2 & msk4)
    df_out.loc[msk, "HW1"] = np.nan
    if 'HW2' in df_out.columns:
        msk1 = df_out.HW2.isnull().shift(2, fill_value=False)
        msk2 = df_out.HW2.isnull().shift(1, fill_value=False)
        msk3 = df_out.HW2.isnull().shift(-1, fill_value=False)
        msk4 = df_out.HW2.isnull().shift(-2, fill_value=False)
        msk = (msk2 & msk3) | (msk1 & msk3) | (msk2 & msk4)
        df_out.loc[msk, "HW2"] = np.nan

    # Filtering DW for low or NaN values of VW
    msk = df_out.VW1.isnull() | df_out.VW1 < 0.5
    df_out.loc[msk, "DW1_qc"] = "IWS"
    if 'VW2' in df_out.columns:
        msk = df_out.VW2.isnull() | df_out.VW2 < 0.5
        df_out.loc[msk, "DW2_qc"] = "IWS"

    # filtering radiation
    if 'ISWR' in df.columns:
        ZenithAngle_deg, _ = sza_saa(df_out, lon, lat)
        ZenithAngle_rad = np.deg2rad(ZenithAngle_deg)

        # Setting to zero when sun below the horizon.
        bad = ZenithAngle_deg > 95
        df_out.loc[bad & df['ISWR'].notnull(), 'ISWR'] = 0
        df_out.loc[bad & df_out['OSWR'].notnull(), 'OSWR'] = 0

        # Calculate angle between sun and sensor
        # AngleDif_deg = calcAngleDiff(ZenithAngle_rad, HourAngle_rad,
        #                              phi_sensor_rad, theta_sensor_rad)

        # Filtering OSWR and ISWR for sun on lower dome
        # in theory, this is not a problem in cloudy conditions, but the cloud cover
        # index is too uncertain at this point to be used
        # sunonlowerdome = (AngleDif_deg >= 90) & (ZenithAngle_deg <= 90)
        # mask = ~sunonlowerdome | AngleDif_deg.isnull()                             # relaxing the filter for cases where sensor tilt is unknown
        # df_out['ISWR'] = df_out['ISWR'].where(mask)
        # df_out['OSWR'] = df_out['OSWR'].where(mask)

        # Filter ISWR values that are greater than top of the atmosphere irradiance
        # Case where no tilt is available. If it is, then the same filter is used
        # after tilt correction.
        isr_toa = calcTOA(ZenithAngle_deg, ZenithAngle_rad)                        # Calculate TOA shortwave radiation
        TOA_crit_nopass = (df_out['ISWR'] > (1.2 * isr_toa + 20))

        # plt.figure()
        # ax=plt.gca()
        # ax.plot(df_out.index,  (1.1 * isr_toa + 20), c='k', alpha=0.6)
        # ax.plot(df_out.index, df_out.ISWR.values)
        # ax.plot(df_out.index[TOA_crit_nopass], df_out.ISWR.values[TOA_crit_nopass], marker='.', ls='None')

        df_out.loc[TOA_crit_nopass, "ISWR_qc"] = "OOL"
        df_out.loc[TOA_crit_nopass, "OSWR_qc"] = "OOL"

        df_threshold = pd.read_csv('metadata/thresholds.csv')

        mask = detect_outliers(df_out, df_threshold.loc[(df_threshold.stid==site)])

        for var in mask.columns:
            if var in df_out.columns:
                var_qc= var+"_qc"
                if var_qc not in df_out.columns: df_out[var_qc]= 'OK'
                df_out.loc[mask[var], var_qc] = "OOP"

    return df_out


def detect_outliers(data_set: pd.DataFrame, thresholds: pd.DataFrame) -> pd.DataFrame:
    masks = []

    idx_month = data_set.index.tz_localize(None).month
    month_masks = {m: (idx_month == m)
                   for m in thresholds["month"].dropna().unique()}

    for var, cfg in thresholds.groupby("variable_pattern"):
        series = data_set[var].astype(float)
        mask = np.zeros(len(series), dtype=bool)

        for _, row in cfg.iterrows():
            if pd.isna(row.month):      # global threshold
                thr_mask = (series < row.lo) | (series > row.hi)
            else:                       # monthly threshold
                thr_mask = ((series < row.lo) | (series > row.hi)) & month_masks[int(row.month)]

            mask |= thr_mask

        masks.append(pd.Series(mask, index=data_set.index, name=var))

    return pd.concat(masks, axis=1)



def get_season_index_mask(data_set: pd.DataFrame, season: str) -> np.ndarray:
    season_month_map = {
        "winter": {12, 1, 2},
        "spring": {3, 4, 5},
        "summer": {6, 7, 8},
        "fall": {9, 10, 11},
    }
    season_months = season_month_map.get(
        season, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    )
    return data_set.index.month.isin(season_months)[:, None]


def calcTOA(ZenithAngle_deg, ZenithAngle_rad):
    '''Calculate incoming shortwave radiation at the top of the atmosphere,
    accounting for sunset periods

    Parameters
    ----------
    ZenithAngle_deg : float
        Zenith angle in degrees
    ZenithAngle_rad : float
        Zenith angle in radians

    Returns
    -------
    isr_toa : float
        Incoming shortwave radiation at the top of the atmosphere
    '''
    sundown = ZenithAngle_deg >= 90

    # Incoming shortware radiation at the top of the atmosphere
    isr_toa = 1372 * np.cos(ZenithAngle_rad)
    isr_toa[sundown] = 0
    return isr_toa

def hampel(vals_orig, k=7, t0=3):
    """
    vals: pandas series of values from which to remove outliers
    k: size of window (including the sample; 7 is equal to 3 on either side of value)
    """
    # Make copy so original not edited
    vals = vals_orig.copy()
    # Hampel Filter
    L = 1.4826
    rolling_median = vals.rolling(k).median()
    difference = np.abs(rolling_median - vals)
    median_abs_deviation = difference.rolling(k).median()
    threshold = t0 * L * median_abs_deviation
    outlier_idx = difference > threshold
    vals[outlier_idx] = np.nan
    return vals


def RH_water2ice(RH, T):
    # switch ONLY SUBFREEZING timesteps to with-regards-to-ice
    Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
    Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
    Rv = 461.5  # H2O Vapor Gaz constant (J/kg/K)
    ind = T < 0
    # ind = T == T
    TCoeff = 1 / 273.15 - 1 / (T + 273.15)
    Es_Water = 6.112 * np.exp(Lv / Rv * TCoeff)
    Es_Ice = 6.112 * np.exp(Ls / Rv * TCoeff)
    RH_out = RH.copy()
    RH_out[ind] = RH[ind] * Es_Water[ind] / Es_Ice[ind]
    return RH_out


def RH_ice2water(RH, T):
    # switch ALL timestep to with-regards-to-water
    RH = np.array(RH)
    Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
    Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
    Rv = 461.5  # H2O Vapor Gaz constant (J/kg/K)
    ind = T < 0
    TCoeff = 1 / 273.15 - 1 / (T + 273.15)
    Es_Water = 6.112 * np.exp(Lv / Rv * TCoeff)
    Es_Ice = 6.112 * np.exp(Ls / Rv * TCoeff)
    RH_out = RH.copy()

    # T_100 = 373.15
    # T_0 = 273.15
    # T = T +T_0
    # # GOFF-GRATCH 1945 equation
    #    # saturation vapour pressure above 0 C (hPa)
    # Es_Water = 10**(  -7.90298*(T_100/T - 1) + 5.02808 * np.log(T_100/T)
    #     - 1.3816E-7 * (10**(11.344*(1-T/T_100))-1)
    #     + 8.1328E-3*(10**(-3.49149*(T_100/T-1)) -1.) + np.log(1013.246) )
    # # saturation vapour pressure below 0 C (hPa)
    # Es_Ice = 10**(  -9.09718 * (T_0 / T - 1.) - 3.56654 * np.log(T_0 / T) +
    #              0.876793 * (1. - T / T_0) + np.log(6.1071)  )

    RH_out[ind] = RH[ind] / Es_Water[ind] * Es_Ice[ind]

    return RH_out


def RH_ice2water2(RH, T):
    # switch ALL timestep to with-regards-to-water
    RH = np.array(RH)
    # Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
    # Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
    # Rv = 461.5     # H2O Vapor Gaz constant (J/kg/K)
    ind = T == T  # T < 0
    # TCoeff = 1/273.15 - 1/(T+273.15)
    # Es_Water = 6.112*np.exp(Lv/Rv*TCoeff)
    # Es_Ice = 6.112*np.exp(Ls/Rv*TCoeff)
    RH_out = RH.copy()

    T_100 = 373.15
    T_0 = 273.15
    T = T + T_0
    # GOFF-GRATCH 1945 equation
    # saturation vapour pressure above 0 C (hPa)
    Es_Water = 10 ** (
        -7.90298 * (T_100 / T - 1)
        + 5.02808 * np.log10(T_100 / T)
        - 1.3816e-7 * (10 ** (11.344 * (1 - T / T_100)) - 1)
        + 8.1328e-3 * (10 ** (-3.49149 * (T_100 / T - 1)) - 1.0)
        + np.log10(1013.246)
    )
    # saturation vapour pressure below 0 C (hPa)
    Es_Ice = 10 ** (
        -9.09718 * (T_0 / T - 1.0)
        - 3.56654 * np.log10(T_0 / T)
        + 0.876793 * (1.0 - T / T_0)
        + np.log10(6.1071)
    )

    RH_out[ind] = RH[ind] / Es_Water[ind] * Es_Ice[ind]

    return RH_out


# def RH_ice2water3(RH, T):
#     # switch ALL timestep to with-regards-to-water
#     RH = np.array(RH)
#     # Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
#     # Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
#     # Rv = 461.5     # H2O Vapor Gaz constant (J/kg/K)
#     ind = T < 0
#     # TCoeff = 1/273.15 - 1/(T+273.15)
#     # Es_Water = 6.112*np.exp(Lv/Rv*TCoeff)
#     # Es_Ice = 6.112*np.exp(Ls/Rv*TCoeff)
#     RH_out = RH.copy()

#     T_100 = 373.15
#     T_0 = 273.15
#     T = T +T_0
#    # saturation vapour pressure above 0 C (hPa)
#     Es_Water = 10**(  10.79574*(1 - T_100/T) + 5.028 * np.log10(T / T_100)
#                     + 1.50475E-4 * (1 - 10**(-8.2969 * (T/T_100 - 1)))
#                     + 0.42873E-3*(10**(4.76955*(1 - T_100/T)) -1.) +  0.78614 + 2.0 )

#     Es_Ice = 10**( -9.09685 * (T_0 / T - 1.) - 3.56654 * np.log10(T_0 / T) +
#                   0.87682 * (1. - T / T_0) + 0.78614   )
#     RH_out[ind] = RH[ind] / Es_Water[ind]*Es_Ice[ind]

#     return RH_out


def RH2SpecHum(RH, T, pres):
    # Note: RH[T<0] needs to be with regards to ice

    Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
    Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
    Rv = 461.5  # H2O Vapor Gaz constant (J/kg/K)
    es = 0.622

    TCoeff = 1 / 273.15 - 1 / (T + 273.15)
    Es_Water = 6.112 * np.exp(Lv / Rv * TCoeff)
    Es_Ice = 6.112 * np.exp(Ls / Rv * TCoeff)

    es_all = Es_Water.copy()
    es_all[T < 0] = Es_Ice[T < 0]

    # specific humidity at saturation
    q_sat = es * es_all / (pres - (1 - es) * es_all)

    # specific humidity
    q = RH * q_sat / 100
    return q


def SpecHum2RH(q, T, pres):
    # Note: RH[T<0] will be with regards to ice

    Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
    Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
    Rv = 461.5  # H2O Vapor Gaz constant (J/kg/K)
    es = 0.622

    TCoeff = 1 / 273.15 - 1 / (T + 273.15)
    Es_Water = 6.112 * np.exp(Lv / Rv * TCoeff)
    Es_Ice = 6.112 * np.exp(Ls / Rv * TCoeff)

    es_all = Es_Water
    es_all[T < 0] = Es_Ice

    # specific humidity at saturation
    q_sat = es * es_all / (pres - (1 - es) * es_all)

    # relative humidity
    RH = q / q_sat * 100
    return RH


def limited_mean(array_like):
    if pd.isnull(array_like).sum()>6:
        return np.nan
    else:
        return array_like.mean()


def limited_max(array_like):
    if pd.isnull(array_like).sum()>6:
        return np.nan
    else:
        return array_like.max()


def limited_min(array_like):
    if pd.isnull(array_like).sum()>6:
        return np.nan
    else:
        return array_like.min()


def daily_average(df_in):
    df_v6 = df_in.copy()

    # caluclating directional wind speed
    for i in ['1','2']:
        if ('VW'+i  not in df_v6.columns) |('DW'+i not in df_v6.columns):
            continue
        df_v6['VW'+i+'_x'] = df_v6['VW'+i] * np.sin(df_v6['DW'+i] * np.pi/180)
        df_v6['VW'+i+'_y'] = df_v6['VW'+i]  * np.cos(df_v6['DW'+i] * np.pi/180)


    df_v7 = df_v6.resample('D').apply(limited_mean)
    max_vars = [var for var in df_v6.keys() if 'max' in var]
    if len(max_vars)>0: df_v7[max_vars] = df_v6[max_vars].resample('D').apply(limited_max)
    min_vars = [var for var in df_v6.keys() if 'min' in var]
    if len(min_vars)>0: df_v7[min_vars] = df_v6[min_vars].resample('D').apply(limited_min)
    flag_vars = [var for var in df_v6.keys() if 'adj_flag' in var]
    if len(flag_vars)>0: df_v7[flag_vars] = df_v6[flag_vars].resample('D').apply(limited_max)

    # calculating daily wind direction from daily mean directional wind speed
    for i in ['1','2']:
        if ('VW'+i+'_x' not in df_v6.columns )|('VW'+i+'_x' not in df_v6.columns):
            continue
        df_v7['DW'+i] = np.arctan2(df_v6['VW'+i+'_x'], df_v6['VW'+i+'_y'] ) * 180 / np.pi
        df_v7['DW'+i] = (df_v7['DW'+i] + 360) % 360
        df_v7 = df_v7.drop(columns='VW'+i+'_x')
        df_v7 = df_v7.drop(columns='VW'+i+'_y')

    df_v7.attrs['averaging'] = 'daily'
    return df_v7
# %%
import sys
from datetime import datetime
import pandas as pd
from pypromice.pipeline.aws import AWS
from pathlib import Path
from os import path
import logging
from pypromice.core.qc.github_data_issues import adjustTime, flagNAN, adjustData
logger = logging.getLogger("ComputeThreshold")
import argparse
import nead

logging.basicConfig(
    format="%(asctime)s; %(levelname)s; %(name)s; %(message)s",
    level=logging.INFO,
    stream=sys.stdout,
)



# %%
def compute_all_thresholds():
    # %%
    thresholds_output_path=Path(__file__).parent.joinpath("metadata/thresholds.csv")
    station_thresholds_root=Path(__file__).parent.joinpath("metadata/station_thresholds")

    logger.info("Computing all thresholds for stations available in the L0 repository")
    logger.info(f"station_thresholds_root: {station_thresholds_root}")
    logger.info(f"thresholds_output_path:  {thresholds_output_path}")


    station_thresholds_root.mkdir(parents=True, exist_ok=True)
    output_paths = []
    site_list = pd.read_csv("L1/GC-Net_location.csv", header=0, skipinitialspace=(True))
    # site_list = site_list.loc[site_list.Name == 'Swiss Camp 10m']

    for stid in site_list.Name:
        logger.info(f"Processing {stid}")
        output_path = station_thresholds_root.joinpath(f"{stid}.csv")
        threshold = find_thresholds(stid)
        threshold.to_csv(
            path_or_buf=output_path, index=False, float_format="{:.2f}".format
        )
        output_paths.append(output_path)

    logger.info("Merge threshold files")
    pd.concat(pd.read_csv(p) for p in output_paths).to_csv(
        thresholds_output_path, index=False, float_format="{:.2f}".format
    )

# %%
def find_thresholds(stid: str) -> pd.DataFrame:

    var_list = ["P","VW1","VW2","RH1","RH2","TA1","TA2","TA3","TA4"]
    stid_logger = logger.getChild(stid)
    stid_logger.info("Read AWS data and get L1")
    filename = "L1/hourly/" + stid.replace(" ", "") + ".csv"

    ds = nead.read(filename)
    df_aws = ds.to_dataframe().reset_index(drop=True)
    df_aws.timestamp = pd.to_datetime(df_aws.timestamp, utc=False)
    df_aws = df_aws.set_index("timestamp")

    stid_logger.info("Determine thresholds")

    df = df_aws[[v for v in var_list if v in df_aws.columns]].copy()
    df["month"] = df.index.month

    threshold_rows = []

    # ---- GLOBAL THRESHOLDS (P, VW1, VW2, RH1, RH2) ----
    for var in ["P","VW1","VW2","RH1","RH2"]:
        if var in df.columns:
            lo, hi = df[var].quantile([0.005, 0.995]) + [-12, 12]
            threshold_rows.append(dict(
                stid=stid, variable_pattern=var,
                lo=lo, hi=hi
            ))

    # ---- MONTHLY TEMPERATURE THRESHOLDS ----
    for var in ["TA1","TA2","TA3","TA4"]:
        if var not in df.columns:
            continue

        for month, sdf in df[[var,"month"]].groupby("month"):
            lo, hi = sdf[var].quantile([0.005, 0.995]) + [-9, 9]

            threshold_rows.append(dict(
                stid=stid,
                variable_pattern=var,
                month=int(month),
                lo=lo, hi=hi
            ))

    threshold = pd.DataFrame(threshold_rows)
    stid_logger.info(threshold)

    # ---- PLOTTING ----
    import matplotlib.pyplot as plt
    from pathlib import Path

    out = Path("figures/thresholds")
    out.mkdir(parents=True, exist_ok=True)

    for var in ["P","VW1","VW2","TA1","TA2","TA3","TA4"]:
        if var not in df.columns:
            continue

        plt.close("all")
        fig, ax = plt.subplots(figsize=(12,4))

        # monthly min/max gray band
        m = df[var].resample("M")
        lo_band = m.min()
        hi_band = m.max()
        ax.fill_between(lo_band.index, lo_band, hi_band,
                        color="lightgray", alpha=0.6, step="mid")

        # global thresholds
        g = threshold[
            (threshold.stid==stid) &
            (threshold.variable_pattern==var) &
            (threshold.month.isna())
        ]
        if len(g):
            lo, hi = g.iloc[0][["lo","hi"]]
            ax.axhline(lo, color="black", linestyle="--")
            ax.axhline(hi, color="black", linestyle="--")

        # monthly temperature thresholds
        s = threshold[
            (threshold.stid==stid) &
            (threshold.variable_pattern==var) &
            (threshold.month.notna())
        ]

        if len(s):
            lo = lo_band.index.map(
                lambda t: s.loc[s.month == t.month, "lo"].iloc[0]
            )
            hi = lo_band.index.map(
                lambda t: s.loc[s.month == t.month, "hi"].iloc[0]
            )

            ax.step(lo_band.index, lo, where="post", color="blue", linestyle="--")
            ax.step(lo_band.index, hi, where="post", color="blue", linestyle="--")

        ax.set_title(f"{stid} — {var}")
        fig.autofmt_xdate()
        fig.savefig(out / f"{stid}_{var}.png", dpi=120)
        Msg(f"![]({out}/{stid}_{var}.png)")

    return threshold

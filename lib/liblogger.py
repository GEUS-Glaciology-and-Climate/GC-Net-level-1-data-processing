# -*- coding: utf-8 -*-
"""Logger-first helpers for the L0 -> L0M step.

  * reading any raw logger file (CR1000 or the historical, headerless CR10X format, including Swiss Camp 10 m's
    year-embedded CR10X format) through its own <file>.toml configuration file (read_configured_files): logger type, column
    names, and the calibration to apply as soon as the file is read. tools/generate_logger_configs.py writes these
    configuration files; a file with none is simply skipped.
  * keeping track of which file every value came from, and plotting it
  * comparing the logger data with the C-level files

Nothing here filters data. L0M stacks the logger files; whatever looks wrong is handled at L1
(metadata/flags, metadata/adjustments, PROMICE_toolbox.py).
"""
import os
import collections
import numpy as np
import pandas as pd
from lib import libgcnet as gc
from lib import write_nead
INI = "L0/L0_ini/"
REVIEW = "metadata/logger_first/"   # curated findings and choices (see README.md there)
WORK = "out/logger_first_review/"   # working files that can be regenerated



def _savefig(fig, fname, tries=10, **kwargs):
    """fig.savefig that survives a brief lock of the target file: a sync client, an antivirus scan or an image preview can
    make the overwrite fail with OSError 22 for a few seconds, which used to abort a whole L1 run."""
    import time
    for k in range(tries):
        try:
            fig.savefig(fname, **kwargs)
            return
        except OSError:
            if k == tries - 1:
                raise
            time.sleep(1.5)

def update_table(path, df, site):
    """write df to path, replacing only the rows of `site` (one consolidated table for all stations)"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if len(df) == 0 and not os.path.isfile(path):
        return
    if "site" not in df.columns:
        df = df.assign(site=site)
    if os.path.isfile(path) and os.path.getsize(path) > 5:
        old = pd.read_csv(path)
        df = pd.concat([old[old.site != site], df], ignore_index=True)
    df.to_csv(path, index=False)


def _ini_csv(name):
    return pd.read_csv(INI + name, skipinitialspace=True)


# ---------------------------------------------------------------------------------------------
# parsing (shared with tools/cr10x_decode.py so that registry row numbers always match)
# ---------------------------------------------------------------------------------------------
def parse_lines(path):
    """numeric rows of a comma- or whitespace-delimited text file, in file order"""
    txt = open(path, "rb").read().decode("latin-1")
    rows = []
    for line in txt.splitlines():
        s = line.strip()
        if not s:
            continue
        parts = s.split(",") if "," in s else s.split()
        while parts and parts[-1].strip() == "":
            parts.pop()
        try:
            rows.append([float(x) for x in parts])
        except ValueError:
            continue
    return rows


def split_groups(rows):
    """rows grouped by (output array id = first column, number of columns), in file order"""
    g = collections.defaultdict(list)
    for r in rows:
        g[(int(r[0]) if r[0] == int(r[0]) else -1, len(r))].append(r)
    return g


def time_pattern(a):
    """(number of time columns, has a year column, row mask): array id, [year,] day of year, hhmm.
    A pattern is accepted when >=90% of the rows fit it; the other rows are dropped."""
    if a.shape[1] < 6:
        return None
    m4 = (a[:, 1] >= 1990) & (a[:, 1] <= 2030) & (a[:, 2] >= 1) & (a[:, 2] <= 366) & (a[:, 3] >= 0) & (a[:, 3] <= 2400)
    if m4.mean() >= 0.9:
        return 4, True, m4
    m3 = (a[:, 1] >= 1) & (a[:, 1] <= 366) & (a[:, 2] >= 0) & (a[:, 2] <= 2400)
    if m3.mean() >= 0.9:
        return 3, False, m3
    return None


def group_array(path, array, ncols):
    """rows of one output array of a file, time-pattern-masked -> (values array, n_time, has_year)"""
    g = split_groups(parse_lines(path))
    a = np.array(g[(array, ncols)])
    tp = time_pattern(a)
    return a[tp[2]], tp[0], tp[1]


def run_dates(doy, hhmm, y0):
    """timestamps of a run that starts in year y0 (the year increments at day-of-year rollovers)"""
    yr = np.full(len(doy), y0, dtype=int)
    for r in np.where((doy[:-1] > 300) & (doy[1:] < 60))[0] + 1:
        yr[r:] += 1
    minutes = (hhmm // 100) * 60 + (hhmm % 100)
    ts = pd.to_datetime(pd.Series(yr), format="%Y") + pd.to_timedelta(doy - 1, unit="D") + pd.to_timedelta(minutes, unit="min")
    return pd.DatetimeIndex(ts.values, tz="UTC")


def name_maximum_columns(vals, var_list):
    """The CR10X programs store, next to the hourly averages, the hourly MAXIMUM of a wind speed
    (instruction 'Maximize' on the anemometer input; a gust). The layouts leave that column unnamed ('_').
    An unnamed column is named VW1_max / VW2_max when it tracks that wind speed (r >= 0.95), is not below it in
    >= 98% of the records and averages 1.0-2.0 times it. Only names are given; nothing is removed."""
    vals = np.asarray(vals, dtype=float)
    out = list(var_list)
    for i, name in enumerate(out):
        if name != "_":
            continue
        for w in ("VW2", "VW1"):
            if w not in out or w + "_max" in out:
                continue
            x, y = vals[:, i], vals[:, out.index(w)]
            m = np.isfinite(x) & np.isfinite(y) & (x != -6999) & (y != -6999) & (y > 0.5)
            if m.sum() < 200:
                continue
            if np.corrcoef(x[m], y[m])[0, 1] >= 0.95 and np.mean(x[m] >= y[m] - 0.01) >= 0.98 and 1.0 <= np.mean(x[m]) / np.mean(y[m]) <= 2.0:
                out[i] = w + "_max"
                break
    return out


def hourly_frame(vals, ts, var_list):
    """hourly UTC frame with one column per named variable ('_' columns are dropped).
    Sub-hourly data are averaged over the hour ending at the label; hourly data are rounded
    to the nearest hour (the loggers stamp e.g. 13:59)."""
    var_list = name_maximum_columns(vals, var_list)
    df = pd.DataFrame(vals, index=ts, columns=var_list)
    df = df.loc[:, [c for c in df.columns if c != "_"]].replace(-6999, np.nan)
    df = df[~df.index.duplicated(keep="first")].sort_index()
    step = float(np.median(np.diff(df.index.values).astype("timedelta64[m]").astype(float))) if len(df) > 5 else 60.0
    if step < 50:
        agg = {c: ("max" if c.endswith("_max") else "mean") for c in df.columns}
        df = df.resample("h", closed="right", label="right").agg(agg).dropna(how="all")
    else:
        df.index = df.index.round("h")
        df = df[~df.index.duplicated(keep="first")]
    return df, step


# ---------------------------------------------------------------------------------------------
# reading a station from the per-file .toml configs (tools/generate_logger_configs.py writes these from the
# older CR10X_layouts.csv / CR10X_calibration*.csv / CR10X_file_registry.csv / station header.ini sources)
# ---------------------------------------------------------------------------------------------
def _apply_calibration(df, calibration):
    """physical units from a raw dataframe, per column, using a {var: {scale|scale_pos/scale_neg, add}} mapping
    (a .toml [calibration] table, already parsed). Columns without an entry are left as the logger reports them."""
    for var, c in calibration.items():
        if var not in df.columns:
            continue
        x = df[var] + c.get("add", 0)
        if "scale_pos" in c:
            df[var] = np.where(x > 0, x * c["scale_pos"], np.where(x < 0, x * c["scale_neg"], x))
        elif "scale" in c:
            df[var] = x * c["scale"]
    return df


def iter_cr10x_segments(path, cfg):
    """every (array, run) of a CR10X file via its .toml, before hourly averaging or calibration: yields dicts with
    array_index, run_index (positions into cfg['array'][i] / cfg['array'][i]['run'][j], for a caller that wants to
    edit that run's entry, e.g. a calibration or dating audit tool updating the .toml in place), array_id, ncols,
    column_header, row_from, row_to, year (resolved, whether the run stated it or it came from the rollover
    default), has_year, n_t (number of leading time columns) and seg (the run's raw rows, time columns included).
    This is the shared core other functions and tools/*.py build on, so they all see exactly the same runs and the
    same year for each - raw_cr10x_runs (hourly, uncalibrated) and _read_cr10x_configured (hourly, calibrated) below
    just call hourly_frame()/calibrate on top of it."""
    for ai, arr in enumerate(cfg.get("array", [])):
        a, n_t, has_year = group_array(path, int(arr["id"]), int(arr["ncols"]))
        runs = arr.get("run") or [{"row_from": 0, "row_to": len(a) - 1}]
        # the default year at any row without an explicit start_year: the first run's start_year, +1 at every real
        # DOY rollover from there, scanned over the file's WHOLE raw row sequence (including the rows between
        # registered runs) -- this must match tools/generate_logger_configs.py's own naive-year computation exactly,
        # since that is what decided whether a run's start_year could be omitted in the first place.
        # anchored at the first run's own row_from, not at row 0 of the whole array: the same array id can carry an
        # earlier run under a DIFFERENT layout (a logger reprogram, a separate [[array]] block of its own), whose
        # dating is irrelevant here (matches tools/generate_logger_configs.py exactly)
        default_year = None
        if not has_year:
            doy = a[:, 1]
            row_from0 = int(runs[0]["row_from"])
            default_year = np.zeros(len(doy), dtype=int)
            default_year[row_from0:] = int(runs[0]["start_year"])
            for k in np.where((doy[:-1] > 300) & (doy[1:] < 60))[0] + 1:
                if k >= row_from0:
                    default_year[k:] += 1
        for ri, r in enumerate(runs):
            seg = a[int(r["row_from"]): int(r["row_to"]) + 1]
            if has_year:
                year = int(seg[0, 1])
            elif "start_year" in r:
                year = int(r["start_year"])
            else:
                year = int(default_year[int(r["row_from"])])
            yield dict(array_index=ai, run_index=ri, array_id=int(arr["id"]), ncols=int(arr["ncols"]),
                       column_header=list(arr["column_header"]), row_from=int(r["row_from"]), row_to=int(r["row_to"]),
                       year=year, has_year=has_year, n_t=n_t, seg=seg)


def raw_cr10x_runs(path, cfg):
    """one CR10X file via its .toml, WITHOUT calibration applied: a list of (priority_key, array_index, run_index,
    hourly dataframe) items, one per (array, run) -- matching the granularity the old registry-driven reader merged
    at (a single file can hold runs spanning different years, with other files' runs interleaved between them by
    date, so the cross-file/cross-run priority order has to work at the run level, not the file level)."""
    items = []
    for s in iter_cr10x_segments(path, cfg):
        if s["has_year"]:
            # embedded-year format (Swiss Camp 10 m): already one row per hour, no sub-hourly averaging needed;
            # rows are kept exactly as logged, including literal duplicate timestamps, matching the old
            # read_swisscamp10m_cr10x + stack_sources convention of never deduplicating this station's CR10X data
            ts = (pd.to_datetime(pd.Series(s["seg"][:, 1].astype(int)), format="%Y") + pd.to_timedelta(s["seg"][:, 2] - 1, unit="D")
                  + pd.to_timedelta((s["seg"][:, 3] // 100) * 60 + s["seg"][:, 3] % 100, unit="min"))
            ts = pd.DatetimeIndex(ts.values, tz="UTC")
            df = pd.DataFrame(s["seg"][:, s["n_t"]:], index=ts, columns=s["column_header"])
            df = df.loc[:, [c for c in df.columns if c != "_"]].replace(-6999, np.nan)
        else:
            ts = run_dates(s["seg"][:, 1], s["seg"][:, 2], s["year"])
            df, _ = hourly_frame(s["seg"][:, s["n_t"]:], ts, s["column_header"])
            df = df[~df.index.duplicated(keep="first")]
        items.append((s["year"], s["array_index"], s["run_index"], df))
    return items


def _read_cr10x_configured(path, cfg):
    """one CR10X file via its .toml: a list of (priority_key, calibrated dataframe) items, one per (array, run)."""
    cal = cfg.get("calibration", {})
    return [(y, _apply_calibration(df, cal)) for y, ai, ri, df in raw_cr10x_runs(path, cfg)]


def _read_cr1000_configured(path, cfg):
    """one CR1000 file via its .toml: calibrated dataframe indexed by UTC timestamp"""
    df = gc.read_cr1000_tables(os.path.dirname(path) + os.sep, os.path.basename(path))
    df = df.set_index("timestamp")
    df.index = pd.to_datetime(df.index, utc=True)
    df = df[~df.index.duplicated(keep="first")]   # a file can carry a few literal duplicate rows internally
    return _apply_calibration(df, cfg.get("calibration", {}))


def list_configs(directory):
    """(filename, parsed .toml dict) for every raw file in `directory` that has a matching <file>.toml configuration file
    (tools/generate_logger_configs.py writes these). A file without one is skipped - this is the one place that
    decides what counts as "configured"; read_configured_files and the diagnostic tools in tools/ both use it, so a
    file is either seen by all of them or by none."""
    import tomllib
    out = []
    for f in sorted(os.listdir(directory)):
        if os.path.isdir(os.path.join(directory, f)):
            continue
        cfg_path = os.path.join(directory, f + ".toml")
        if f.endswith(".toml") or not os.path.isfile(cfg_path):
            continue
        with open(cfg_path, "rb") as fh:
            out.append((f, tomllib.load(fh)))
    return out


def _apply_ignore_rows(df, cfg):
    """Drop the rows of the periods listed in the configuration file's [[ignore_rows]] tables (start and end included, UTC when no zone is given),
    for a file whose records are known to be wrong, e.g. dated before the installation of the station. Give a `reason` in the table:

        [[ignore_rows]]
        start = "1900-01-01 00:00:00"
        end = "1997-04-19 23:00:00"
        reason = "before the installation of the station (1997-04-20)"
    """
    for w in cfg.get("ignore_rows", []):
        t0, t1 = pd.Timestamp(w["start"]), pd.Timestamp(w["end"])
        t0 = t0.tz_localize("UTC") if t0.tzinfo is None else t0.tz_convert("UTC")
        t1 = t1.tz_localize("UTC") if t1.tzinfo is None else t1.tz_convert("UTC")
        df = df.loc[~((df.index >= t0) & (df.index <= t1))]
    return df


def _apply_calibration_periods(df, cfg):
    """Multiply columns by a factor inside a period, from the configuration file's [[calibration_period]] tables (applied after the
    [calibration.<var>] scale, UTC when no zone is given; the variable's _max/_min/_std columns follow it). For a factor that is a
    property of a sensor and not of a logger channel: when the sensors were exchanged between two channels from a date on (the
    `swap_with_OSWR` adjustments of Crawford Point 1 and Swiss Camp), the sensor factor moves with them:

        [[calibration_period]]
        variable = "ISWR"
        start = "2012-01-01 00:00:00"
        end = "2100-01-01 00:00:00"
        multiply = 0.934
        reason = "the OSWR sensor (x0.934) is wired to the ISWR channel from 2012"
    """
    for w in cfg.get("calibration_period", []):
        t0, t1 = pd.Timestamp(w["start"]), pd.Timestamp(w["end"])
        t0 = t0.tz_localize("UTC") if t0.tzinfo is None else t0.tz_convert("UTC")
        t1 = t1.tz_localize("UTC") if t1.tzinfo is None else t1.tz_convert("UTC")
        m = (df.index >= t0) & (df.index <= t1)
        for c in [w["variable"]] + [w["variable"] + s for s in ("_max", "_min", "_std", "_stdev")]:
            if c in df.columns:
                df.loc[m, c] = df.loc[m, c] * float(w["multiply"])
    return df


def _utc(t):
    t = pd.Timestamp(t)
    return t.tz_localize("UTC") if t.tzinfo is None else t.tz_convert("UTC")


def _swap_in_period(df, var_a, var_b, t0, t1):
    """exchange the values of two columns (and of their _max/_min/_std/_stdev columns) from t0 to t1, both included"""
    m = (df.index >= t0) & (df.index <= t1)
    if not m.any():
        return df
    for s in ("", "_max", "_min", "_std", "_stdev"):
        a, b = var_a + s, var_b + s
        if a not in df.columns and b not in df.columns:
            continue
        for c in (a, b):
            if c not in df.columns:
                df[c] = np.nan
        va, vb = df.loc[m, a].to_numpy().copy(), df.loc[m, b].to_numpy().copy()
        df.loc[m, a], df.loc[m, b] = vb, va
    return df


def _apply_swap_columns(df, cfg):
    """Exchange the values of two columns inside a period, from the configuration file's [[swap_columns]] tables (UTC when no zone is given). For
    two sensors that are read on each other's logger channel from a date on (the label HW1 is the upper sonic ranger, the field
    notes call it 2): the decoding gives every sensor its own name, so the L0M, the L1 and the comparisons with the C-level see the
    same sensors under the same names. The C-level files have the same table in metadata/c_level_swaps.csv.

        [[swap_columns]]
        variables = ["HW1", "HW2"]
        start = "2006-07-20 22:00:00"
        end = "2100-01-01 00:00:00"
        reason = "the sonic rangers are read on each other's channel (HW1 is the upper one)"
    """
    for w in cfg.get("swap_columns", []):
        a, b = w["variables"]
        df = _swap_in_period(df, a, b, _utc(w["start"]), _utc(w["end"]))
    return df


def apply_c_level_swaps(dfj, dfc, site, path="metadata/c_level_swaps.csv"):
    """Exchange the values of two columns of the C-level frames in the periods of metadata/c_level_swaps.csv (site, var_a, var_b, t0,
    t1, reason; empty t1 = to the end of the record). The same exchange as the [[swap_columns]] of the logger configuration files, for the
    C-level files that carry the heights where no logger file does. Returns (dfj, dfc)."""
    if not os.path.isfile(path):
        return dfj, dfc
    tab = pd.read_csv(path, comment="#", skipinitialspace=True)
    for r in tab.loc[tab.site == site, :].itertuples():
        for d in (dfj, dfc):
            if d is None or len(d) == 0:
                continue
            t0 = _utc(r.t0) if isinstance(r.t0, str) and r.t0.strip() else d.index.min()
            t1 = _utc(r.t1) if isinstance(r.t1, str) and r.t1.strip() else d.index.max()
            _swap_in_period(d, r.var_a, r.var_b, t0, t1)
    return dfj, dfc


def read_configured_files(directory, priority="latest_first", dedup=True):
    """Every raw file in `directory` that has a matching <file>.toml configuration file, read, calibrated, and combined into
    one (data, provenance) pair; (None, None) if none are configured yet.
    `priority`: 'latest_first' processes CR10X-style overlapping cumulative downloads with the most recent one
    winning where they overlap (matching the old read_station_cr10x); 'earliest_first' keeps the first file's value
    on overlap (matching the old read_cr1000_files's drop_duplicates(keep='first')).
    `dedup=False` stacks every file's rows instead (kept even where two files share a timestamp): matches Swiss
    Camp 10 m's old read_swisscamp10m_cr10x + stack_sources, which never deduplicated its CR10X files."""
    items = []   # (priority_key, file_label, dataframe); for CR10X one entry per (array, run), matching the
                 # granularity the old registry-driven reader combined at (see _read_cr10x_configured)
    for f, cfg in list_configs(directory):
        path = os.path.join(directory, f)
        if cfg["logger_type"] == "CR1000":
            df = _apply_swap_columns(_apply_calibration_periods(_apply_ignore_rows(_read_cr1000_configured(path, cfg), cfg), cfg), cfg)
            items.append((f, f, df))    # yearly files sort well enough by name; ties keep directory listing order
        else:
            for y, df in _read_cr10x_configured(path, cfg):
                items.append((y, f, _apply_swap_columns(_apply_calibration_periods(_apply_ignore_rows(df, cfg), cfg), cfg)))
    if not items:
        return None, None
    if dedup:
        # a file (or a run of it) can repeat a timestamp internally, e.g. after a logger reboot: the first row is kept
        items = [(k, lab, df.loc[~df.index.duplicated(keep="first")] if df.index.has_duplicates else df) for k, lab, df in items]
    items.sort(key=lambda x: x[0], reverse=(priority == "latest_first"))
    if not dedup:
        combined = pd.concat([df for _, _, df in items])
        prov = pd.concat([tag(df, label) for _, label, df in items])
        return combined.sort_index(), prov.reindex(index=combined.index, columns=combined.columns).sort_index()
    try:
        return _merge_first_wins(items)
    except (ValueError, TypeError):
        # a frame that cannot be handled as plain numbers (text column, repeated column name): the slow generic merge
        combined, prov = pd.DataFrame(), pd.DataFrame()
        for _, label, df in items:
            p = tag(df, label)
            if len(combined) == 0:
                combined, prov = df, p
            else:
                combined = combined.combine_first(df)
                prov = prov.combine_first(p)
        return combined.sort_index(), prov.reindex(index=combined.index, columns=combined.columns).sort_index()


def _merge_first_wins(items):
    """The frames of `items` ((key, label, frame), highest priority first, each with a unique index) merged value by value:
    where several have a value, the first one wins. Same result as chaining DataFrame.combine_first over the frames (and the
    same for the provenance), but it fills one array and one small integer code array (which frame the value came from)
    instead of building a new string-labelled frame for every file: combine_first on object frames took 35 of the 45 s
    needed to read the 11 Summit CR1000 files, and its temporary copies made the process grow to more than 1 GB."""
    idx, one_row = items[0][2].index, items[0][2].iloc[:1]
    for _, _, df in items[1:]:
        idx = idx.union(df.index)
        one_row = one_row.combine_first(df.iloc[:1])    # only to get the column order that chaining combine_first gives
    cols = one_row.columns
    if not idx.is_monotonic_increasing:
        idx = idx.sort_values()
    out = np.full((len(idx), len(cols)), np.nan)
    code = np.full(out.shape, -1, dtype=np.int16)
    for k, (_, _, df) in enumerate(items):
        r = idx.get_indexer(df.index)[:, None]
        c = cols.get_indexer(df.columns)[None, :]
        if (r < 0).any() or (c < 0).any():
            raise ValueError("index or columns not found")
        v = df.to_numpy(dtype=float)
        cur = out[r, c]
        take = np.isnan(cur) & ~np.isnan(v)
        out[r, c] = np.where(take, v, cur)
        code[r, c] = np.where(take, k, code[r, c])
    labels = np.array([lab for _, lab, _ in items] + [np.nan], dtype=object)   # code -1 -> the last element: NaN
    combined = pd.DataFrame(out, index=idx, columns=cols)
    # integer columns (e.g. the record number) stay integers where the result has no gap, as with combine_first
    for j, c in enumerate(cols):
        dts = [df[c].dtype for _, _, df in items if c in df.columns]
        if dts and all(pd.api.types.is_integer_dtype(d) for d in dts) and not np.isnan(out[:, j]).any():
            combined[c] = combined[c].astype(dts[0])
    prov = pd.DataFrame(labels[code], index=idx, columns=cols, dtype=object)
    return combined, prov


# read_station_cr10x (the CR10X_file_registry.csv / CR10X_layouts.csv / CR10X_calibration*.csv - driven reader) was
# removed 2026-09: superseded by read_configured_files, which reads the same information from each raw file's own
# .toml configuration file instead (tools/generate_logger_configs.py wrote those configuration files from these CSVs, verified
# byte-identical against this function network-wide, before it and the CSVs were retired). A handful of tools built
# during that migration (tools/cr10x_calibration_by_file.py, tools/logger_timing_check.py, tools/verify_run_dating.py,
# tools/build_logger_first_report.py) still read those CSVs for their own analysis and need them regenerated
# (tools/cr10x_decode.py decode <station> && registry <station>) before they can run again.


# read_swisscamp10m_cr10x (CR10X_all_station.ini - driven reader for Swiss Camp 10 m's year-embedded CR10X files) was
# removed 2026-09: superseded by read_configured_files(dir, dedup=False), which reads the same station-wide
# calibration from each file's own .toml configuration file (tools/generate_logger_configs.py's sc10m_configs wrote those from
# CR10X_all_station.ini) and, via iter_cr10x_segments's has_year branch, keeps every row with no deduplication -
# matching this station's historical convention of never dropping a row, even a literal duplicate timestamp.
# Verified against this function network-wide (dedup=False, same row count, same values) before removal, except for
# one found-and-kept improvement: this function's pd.to_datetime(..., format="%Y%j%H") silently truncated the
# minutes of the raw "hour" (HHMM) column, collapsing a burst of 10-minute readings on 2002-05-12/13 onto their
# enclosing hour; the new reader resolves their true HH:MM timestamps instead.


# ---------------------------------------------------------------------------------------------
# putting the logger sources together; every source is (data, label) or (data, provenance frame), None sources are skipped
# ---------------------------------------------------------------------------------------------
def _with_provenance(parts):
    out = []
    for data, lab in parts:
        if data is None or len(data) == 0:
            continue
        data = data.copy()
        data.index = pd.to_datetime(data.index, utc=True)
        out.append((data, tag(data, lab) if isinstance(lab, str) else lab))
    return out


def stack_sources(parts):
    """the sources one after the other, every row kept (no de-duplication). Returns (data, provenance) or (None, None)"""
    parts = _with_provenance(parts)
    if len(parts) == 0:
        return None, None
    return pd.concat([d for d, _ in parts]), pd.concat([p for _, p in parts])


def combine_sources(parts):
    """the first source has priority; each following source only fills the hours/variables the earlier ones lack.
    Returns (data, provenance) or (None, None)"""
    parts = _with_provenance(parts)
    if len(parts) == 0:
        return None, None
    data, prov = parts[0]
    for d, p in parts[1:]:
        data, prov = data.combine_first(d), prov.combine_first(p)
    return data, prov


# ---------------------------------------------------------------------------------------------
# origin (provenance) of the values
# ---------------------------------------------------------------------------------------------
def tag(df, label):
    """frame of the same shape as df holding `label` where df has a value and NaN elsewhere"""
    arr = np.full(df.shape, np.nan, dtype=object)
    arr[df.notna().to_numpy()] = label
    return pd.DataFrame(arr, index=df.index, columns=df.columns, dtype=object)


def c_level_provenance(dfc, dfc_jeb, cols):
    """which C-level file a value comes from: Jason's file first, the per-station file for its gaps"""
    p = tag(dfc.reindex(columns=cols), "C-level (station file)")
    if dfc_jeb is not None:
        p = tag(dfc_jeb.reindex(columns=cols), "C-level (Jason file)").combine_first(p)
    return p


PLOT_GROUPS = {
    "air_temperature_humidity": ["TA1", "TA2", "TA3", "TA4"],
    "pressure_humdity": ["P", "RH1", "RH2"],
    "wind_pressure_battery": ["VW1", "VW2", "DW1", "DW2"],
    "radiation": ["ISWR", "OSWR", "NR"],
    "snow_height": ["HW1", "HW2", "HS1","HS2"],
    "snow_temperature": ["TS1", "TS2", "TS3", "TS4", "TS5", "TS6", "TS7", "TS8", "TS9", "TS10"],
    "extra_variables": None,      # every other column of L0M (gusts, maxima, standard deviations ...)
}


def _ylim(*series):
    """P05 - A/10 ... P95 + A/10, with A = P95 - P05, over all the plotted values"""
    arrs = [np.asarray(x, dtype=float) for x in series if x is not None and len(x)]
    v = np.concatenate([a[np.isfinite(a)] for a in arrs]) if arrs else np.array([])
    if len(v) < 5:
        return None
    p05, p95 = np.percentile(v, [5, 95])
    A = p95 - p05 if p95 > p05 else max(abs(p95), 1.0)
    return p05 - A / 10, p95 + A / 10


def plot_sources(site, values, prov, clevel, out_png, variables=None):
    """Origin plots, several figures per site (out_png is used as the base name: <base>_<group>.png).
    One panel per variable: daily means coloured by the file they come from, the C-level data
    as a wide transparent grey line underneath (visible where the two differ). The y axis runs from
    P05 - A/10 to P95 + A/10 (A = P95 - P05) so that glitches do not squash the panel.
    Uses matplotlib's Figure directly, so it does not touch pyplot's backend or open windows."""
    import matplotlib
    from matplotlib.figure import Figure
    from matplotlib.lines import Line2D
    listed = {v for g in PLOT_GROUPS.values() if g for v in g}
    groups = {}
    for name, cols in PLOT_GROUPS.items():
        if cols is None:
            cols = [c for c in values.columns if c not in listed and c not in ("timestamp", "ID", "year", "DoY")]
        groups[name] = [v for v in cols if v in values.columns and values[v].notna().any()]
    all_labels = sorted({l for v in values.columns for l in prov[v].dropna().unique()}) if len(prov.columns) else []
    cmap = matplotlib.colormaps["tab20"]
    colors = {l: ("#d62728" if l == "CR1000" else "#444444" if l.startswith("C-level (Jason") else "#9a9a9a" if l.startswith("C-level")
                  else cmap(i % 20)) for i, l in enumerate(all_labels)}
    base = out_png[:-4] if out_png.endswith(".png") else out_png
    os.makedirs(os.path.dirname(base) or ".", exist_ok=True)
    for name, vs in groups.items():
        if len(vs) == 0:
            continue
        labels = sorted({l for v in vs for l in prov[v].dropna().unique()})
        fig = Figure(figsize=(15, 1.9 * len(vs) + 1.8))
        axes = np.atleast_1d(fig.subplots(len(vs), 1, sharex=True))
        for ax, v in zip(axes, vs):
            c = None
            if clevel is not None and v in clevel.columns:
                c = clevel[v].dropna().resample("D").mean()
                ax.plot(c.index, c.values, color="0.55", lw=3.5, alpha=0.35, solid_capstyle="round", zorder=1)
            val, src = values[v], prov[v]
            daily = []
            for l in labels:
                m = (src == l) & val.notna()
                if not m.any():
                    continue
                d = val[m].groupby(val[m].index.floor("D")).mean()
                daily.append(d.values)
                ax.plot(d.index, d.values, ".", ms=1.6, color=colors[l], zorder=2, rasterized=True)
            lim = _ylim(*daily, None if c is None else c.values)
            if lim is not None:
                ax.set_ylim(*lim)
            ax.set_ylabel(v, fontsize=9)
            ax.tick_params(labelsize=8)
            ax.grid(alpha=0.25)
        handles = [Line2D([0], [0], marker="o", ls="", color=colors[l], label=l, ms=5) for l in labels]
        if clevel is not None:
            handles.append(Line2D([0], [0], color="0.55", lw=3.5, alpha=0.4, label="C-level (all sources)"))
        ncol = min(5, len(handles))
        nrow = -(-len(handles) // ncol)
        fig.suptitle(f"{site} - {name.replace('_', ' ')}: origin of each value (coloured, daily means)" + (" vs the C-level files (grey)" if clevel is not None else ""),
                     fontsize=11)
        fig.tight_layout(rect=[0, 0.02 + 0.022 * nrow, 1, 0.965])
        fig.legend(handles=handles, loc="lower center", ncol=ncol, fontsize=7, frameon=False)
        _savefig(fig, f"{base}_{name}.png", dpi=110)


def source_windows(prov):
    """runs of consecutive hours with the same source, per variable: variable, source_class, source, start, end, hours.
    source: the file the value came from; source_class: 'CR1000', 'CR10X' (any historical logger file), 'transmission'
    (telemetry received after the last logger record, same generation as CR1000) or 'C-level'.
    Provenance information for L1 (CR10X values are the raw logger values, C-level values went through the legacy C-level
    processing); no judgement is made."""
    rows = []
    prov = prov.loc[~prov.index.duplicated(keep="first")]
    for v in prov.columns:
        lab = prov[v].dropna().astype(str)
        for label, g in lab.groupby(lab):
            cls = ("C-level" if label.startswith("C-level") else "CR1000" if label == "CR1000"
                   else "transmission" if label.startswith("transmission") else "CR10X")
            idx = g.index
            grp = (idx.to_series().diff() != pd.Timedelta(hours=1)).cumsum()
            for _, gg in idx.to_series().groupby(grp.values):
                rows.append(dict(variable=v, source_class=cls, source=label, start=gg.index.min(), end=gg.index.max(), hours=len(gg)))
    return pd.DataFrame(rows, columns=["variable", "source_class", "source", "start", "end", "hours"])


def prov_from_windows(windows, index, columns):
    """inverse of source_windows: frame of source labels (index x columns) rebuilt from the configuration file table"""
    p = pd.DataFrame(np.nan, index=index, columns=columns, dtype=object)
    for r in windows.itertuples():
        if r.variable in p.columns:
            p.loc[pd.Timestamp(r.start):pd.Timestamp(r.end), r.variable] = getattr(r, "source", r.source_class)
    return p


# ---------------------------------------------------------------------------------------------
# logger versus C-level
# ---------------------------------------------------------------------------------------------
TOL = {"ISWR": 0.5, "OSWR": 0.5, "NR": 0.5, "P": 0.15, "VW1": 0.06, "VW2": 0.06, "DW1": 0.6,
       "DW2": 0.6, "HW1": 0.02, "HW2": 0.02, "TA3": 0.03, "TA4": 0.03}
DEFAULT_TOL = 0.011


def compare_logger_to_clevel(site, logger, clevel, min_run_hours=24):
    """Compare hourly logger data with hourly C-level data.

    Returns (summary, windows):
      summary: per variable, hours with both / logger only / C-level only, share of equal values
               (within TOL) and the median logger-minus-C-level difference;
      windows: runs of >= min_run_hours where the logger has data but the C-level file has none,
               inside the period the C-level file covers for that variable. A gap in the C-level
               file can mean the original processors removed a malfunction, or that data was
               overlooked -- these are candidates for review and for an L1 flag, never removed
               automatically.
    """
    logger = logger[~logger.index.duplicated(keep="first")]
    clevel = clevel[~clevel.index.duplicated(keep="first")]
    summary, windows = [], []
    for v in [c for c in logger.columns if c in clevel.columns and c not in ("ID", "year", "DoY")]:
        c_valid = clevel[v].dropna()
        if len(c_valid) == 0 or logger[v].notna().sum() == 0:
            continue
        idx = logger.index.union(clevel.index)
        idx = idx[(idx >= c_valid.index.min()) & (idx <= c_valid.index.max())]
        a = logger[v].reindex(idx)
        b = clevel[v].reindex(idx)
        both = a.notna() & b.notna()
        only_l = a.notna() & b.isna()
        only_c = a.isna() & b.notna()
        diff = (a - b)[both]
        summary.append(dict(
            site=site, variable=v, hours_both=int(both.sum()), hours_logger_only=int(only_l.sum()),
            hours_clevel_only=int(only_c.sum()),
            pct_equal=round(float((diff.abs() <= TOL.get(v, DEFAULT_TOL)).mean() * 100), 1) if both.any() else np.nan,
            median_logger_minus_clevel=round(float(diff.median()), 3) if both.any() else np.nan,
            first_overlap=idx[both.values].min() if both.any() else pd.NaT,
            last_overlap=idx[both.values].max() if both.any() else pd.NaT))
        grp = (only_l != only_l.shift()).cumsum()
        for _, g in only_l[only_l].groupby(grp[only_l]):
            if len(g) < min_run_hours:
                continue
            vals = a.loc[g.index]
            windows.append(dict(
                site=site, variable=v, start=g.index.min(), end=g.index.max(), hours=len(g),
                logger_median=round(float(vals.median()), 3), logger_min=round(float(vals.min()), 3),
                logger_max=round(float(vals.max()), 3),
                logger_share_exactly_zero=round(float((vals == 0).mean()), 3)))
    return pd.DataFrame(summary), pd.DataFrame(windows)


# ---------------------------------------------------------------------------------------------
# what did the C-level processing do to each variable? (per logger file and year)
# ---------------------------------------------------------------------------------------------
def _es(T):
    Lv, Ls, Rv = 2.5001e6, 2.8337e6, 461.5
    k = 1 / 273.15 - 1 / (T + 273.15)
    return 6.112 * np.exp(Lv / Rv * k), 6.112 * np.exp(Ls / Rv * k)


def yearly_diagnostics(site, logger, clevel, prov=None, min_hours=100):
    """Logger versus C-level, one row per (variable, logger file, year) with enough hours in common.
    It answers, for the values the two sources share:
      radiation (ISWR, OSWR, NR>0, NR<0): median C-level/logger ratio and the through-origin slope
                       -> was the C-level file calibrated with the same factor as the logger data in L0M?
                          ratio ~1: same calibration; ratio far from 1: different calibration or raw counts
      P:               median C-level minus logger (hPa)
      RH1, RH2:        median |C-logger| and |C-ice(logger)| at T < -2 degC, and a verdict (same / with respect
                       to ice / other): the C-level files hold RH wrt ice in some periods and wrt water in others
      HW1, HW2:        median |C - logger| for the same sensor and the other sensor, each with and without the
                       sonic air-temperature factor sqrt((T+273.15)/273.15) -> was the C-level distance
                       temperature-corrected, were the two sensors swapped or gap-filled with each other
      HW1, HW2, ...:   share of the logger HW hours that equal one of the TS1-TS10 columns exactly
                       (a temperature string column stored under an HW name)
    Nothing is changed by this; the tables feed the L1 metadata (adjustments and flags).
    """
    logger = logger[~logger.index.duplicated(keep="first")]
    clevel = clevel[~clevel.index.duplicated(keep="first")]
    # one time resolution for all the indexes: when the logger, C-level and provenance frames differ in it (ns / us), every
    # .loc[...] below converts a 100 000-element index again (about 170 of the 215 s this function took for Summit)
    logger = logger.set_axis(logger.index.as_unit("ns"))
    clevel = clevel.set_axis(clevel.index.as_unit("ns"))
    if prov is not None:
        prov = prov.copy()
        prov.index = pd.to_datetime(prov.index, utc=True).floor("h").as_unit("ns")
        prov = prov.loc[~prov.index.duplicated(keep="first")]
    idx = logger.index.intersection(clevel.index)
    L, C = logger.loc[idx], clevel.loc[idx]
    P = prov.reindex(idx) if prov is not None else None
    rows = []

    def label(v):
        if P is None or v not in P.columns:
            return pd.Series("logger", index=idx)
        return P[v].fillna("unknown").astype(str)

    def emit(v, kind, mask_fn, kw):
        lab = label(v)
        yr = pd.Series(idx.year, index=idx)
        for (lb, y), g in pd.DataFrame({"lab": lab, "yr": yr}).groupby(["lab", "yr"]):
            m = mask_fn(g.index)
            if m.sum() >= min_hours:
                rows.append(dict(site=site, variable=v, file=lb, year=int(y), test=kind, hours=int(m.sum()), **kw(g.index[m.values])))

    for v in ("ISWR", "OSWR"):
        if v in L.columns and v in C.columns:
            emit(v, "radiation", lambda ix, v=v: (L.loc[ix, v].abs() > 20) & C.loc[ix, v].notna() & L.loc[ix, v].notna(),
                 lambda ix, v=v: dict(ratio_c_over_logger=round(float((C.loc[ix, v] / L.loc[ix, v]).median()), 4),
                                      slope=round(float((C.loc[ix, v] * L.loc[ix, v]).sum() / (L.loc[ix, v] ** 2).sum()), 4),
                                      r=round(float(np.corrcoef(C.loc[ix, v], L.loc[ix, v])[0, 1]), 4)))
    if "NR" in L.columns and "NR" in C.columns:
        for nm, sel in (("NR>0", lambda x: x > 20), ("NR<0", lambda x: x < -20)):
            emit("NR", nm, lambda ix, sel=sel: sel(L.loc[ix, "NR"]) & C.loc[ix, "NR"].notna(),
                 lambda ix: dict(ratio_c_over_logger=round(float((C.loc[ix, "NR"] / L.loc[ix, "NR"]).median()), 4),
                                 slope=round(float((C.loc[ix, "NR"] * L.loc[ix, "NR"]).sum() / (L.loc[ix, "NR"] ** 2).sum()), 4),
                                 r=round(float(np.corrcoef(C.loc[ix, "NR"], L.loc[ix, "NR"])[0, 1]), 4)))
    if "P" in L.columns and "P" in C.columns:
        emit("P", "pressure", lambda ix: L.loc[ix, "P"].notna() & C.loc[ix, "P"].notna(),
             lambda ix: dict(median_c_minus_logger=round(float((C.loc[ix, "P"] - L.loc[ix, "P"]).median()), 3)))
    Tcols = [c for c in ("TA1", "TA2", "TA3", "TA4") if c in L.columns]
    for k in ("1", "2"):
        v = "RH" + k
        if v not in L.columns or v not in C.columns:
            continue
        T = L["TA" + k] if "TA" + k in L.columns else (L[Tcols].mean(axis=1) if Tcols else None)
        if T is None:
            continue
        ew, ei = _es(T)
        ice = (L[v] * ew / ei).clip(upper=100)

        def rh(ix, v=v, T=T, ice=ice):
            d_same = (C.loc[ix, v] - L.loc[ix, v]).abs().median()
            d_ice = (C.loc[ix, v] - ice.loc[ix]).abs().median()
            verdict = "same (wrt water)" if (d_same < 4 and d_same <= d_ice) else "wrt ice" if (d_ice < 4 and d_ice < d_same) else "other"
            return dict(median_abs_diff_same=round(float(d_same), 2), median_abs_diff_ice=round(float(d_ice), 2), verdict=verdict)
        emit(v, "RH ice/water", lambda ix, v=v, T=T: (T.loc[ix] < -2) & (L.loc[ix, v] > 5) & L.loc[ix, v].notna() & C.loc[ix, v].notna(), rh)
    for k in ("1", "2"):
        v, o = "HW" + k, "HW" + ("2" if k == "1" else "1")
        if v not in L.columns or v not in C.columns:
            continue
        T = L["TA" + k] if "TA" + k in L.columns else (L[Tcols].mean(axis=1) if Tcols else None)
        if T is None:
            continue
        f = np.sqrt((T + 273.15) / 273.15)

        def hw(ix, v=v, o=o, f=f):
            # the spread of C - candidate around its median (a constant offset between the two series is ignored)
            c = C.loc[ix, v]
            cands = {"same_raw": L.loc[ix, v], "same_sonic": L.loc[ix, v] * f.loc[ix]}
            if o in L.columns:
                cands["other_raw"] = L.loc[ix, o]
                cands["other_sonic"] = L.loc[ix, o] * f.loc[ix]
            out = {}
            for name, x in cands.items():
                m = x.notna() & c.notna()
                if m.sum() < 50:
                    continue
                sgn = 1.0 if np.corrcoef(x[m], c[m])[0, 1] >= 0 else -1.0
                res = c[m] - sgn * x[m]
                out[name] = float((res - res.median()).abs().median())
                if name in ("same_raw", "other_raw"):
                    out["r_" + name[:-4]] = float(np.corrcoef(x[m], c[m])[0, 1])
            spread = {k: vv for k, vv in out.items() if not k.startswith("r_")}
            best = min(spread, key=spread.get) if spread else None
            out = {kk: round(vv, 3) for kk, vv in out.items()}
            out["best"] = best
            if best is not None:
                x = cands[best]
                m = x.notna() & c.notna()
                out["offset_c_minus_best"] = round(float((c[m] - x[m]).median()), 3)
            return out
        emit(v, "HW correction/swap", lambda ix, v=v: L.loc[ix, v].notna() & C.loc[ix, v].notna(), hw)
    # HW columns that hold a temperature-string column: whole logger record, no C-level needed
    ts = [c for c in logger.columns if c.startswith("TS")]
    pl = prov.reindex(logger.index) if prov is not None else None
    for v in ("HW1", "HW2"):
        if v not in logger.columns or not ts:
            continue
        lab = pl[v].fillna("unknown").astype(str) if pl is not None and v in pl.columns else pd.Series("logger", index=logger.index)
        for (lb, y), g in pd.DataFrame({"lab": lab, "yr": logger.index.year}, index=logger.index).groupby(["lab", "yr"]):
            x = logger.loc[g.index]
            if x[v].notna().sum() < min_hours:
                continue
            best, share = None, 0.0
            for t in ts:
                m = x[v].notna() & x[t].notna()
                if m.sum() < 50:
                    continue
                e = float(((x[v] - x[t]).abs()[m] < 0.005).mean())
                if e > share:
                    best, share = t, e
            rows.append(dict(site=site, variable=v, file=lb, year=int(y), test="HW equals TS column", hours=int(x[v].notna().sum()),
                             best_ts_column=best, share_equal=round(share, 3)))
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------------------------
# transmissions (L0 data received by satellite; the envidat API that served them is gone, nothing is downloaded any more)
# ---------------------------------------------------------------------------------------------
TRANSMISSION_ALIASES = {"EastGRIP": ["E-GRIP", "EastGRIP"], "Petermann Glacier": ["Petermann Gl", "Petermann Glacier"]}


def _read_transmission_file(path):
    """NEAD transmission file -> DataFrame indexed by UTC time, or None if the file is empty, missing or not a data file
    (some copies are an envidat 'Page not found' HTML answer)"""
    import nead
    if not os.path.isfile(path) or os.path.getsize(path) < 100:
        return None
    with open(path, encoding="utf-8", errors="replace") as fh:
        if fh.read(200).lstrip().startswith("<"):
            return None
    try:
        d = nead.read(path).to_dataframe()
        d["timestamp"] = pd.to_datetime(d["timestamp"], utc=True)
    except Exception:
        return None
    if len(d) == 0:
        return None
    d = d.set_index("timestamp").sort_index()
    d.columns = d.columns.str.replace("NSWR", "NR")
    return d.loc[~d.index.duplicated(keep="first")]


def read_transmissions(site, station_dir, backup_dir, after=None):
    """Transmitted data of a station, only the records after `after` (the last logger record): L0 data that stand in for
    the logger files when these are not available. The copy in the station folder is used if it is valid, else the backup
    made on 2023-01-11 (L0/backup_transmissions_20230111); the one that adds more records wins. Returns (frame, label) or (None, None).
    The backup is the compiled record of the former pipeline (1995-2022; its early part equals the C-level data, RH wrt ice
    included), which is why nothing before the last logger record is taken from it."""
    names = TRANSMISSION_ALIASES.get(site, [site])
    cands = [(station_dir + n + ".csv", "transmission (station folder)") for n in names] + \
            [(backup_dir + n + ".csv", "transmission (backup 2023-01-11)") for n in names]
    best = None
    for path, label in cands:
        d = _read_transmission_file(path)
        if d is None:
            continue
        if after is not None:
            d = d.loc[d.index > pd.to_datetime(after, utc=True)]
        if len(d) and (best is None or len(d) > len(best[0])):      # the copy that adds the most records wins (ties: station folder)
            best = (d, label)
    if best is None:
        return None, None
    d, label = best
    return (d, label) if len(d) else (None, None)


# ---------------------------------------------------------------------------------------------
# editing a raw file's .toml in place (an audit tool updating the calibration it found, or dating it re-derived)
# ---------------------------------------------------------------------------------------------
def update_toml_calibration(toml_path, var, scale=None, scale_pos=None, scale_neg=None, add=0.0, source=None):
    """Replace (or add) the [calibration.<var>] block of a .toml file with the given factors; everything else in
    the file (other calibration blocks, [[array]] blocks, comments, formatting) is left untouched. Give either
    `scale` (same factor either sign) or `scale_pos`/`scale_neg` (sign-dependent, e.g. NR)."""
    raw = open(toml_path, encoding="utf-8", newline="").read()
    eol = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.replace("\r\n", "\n").split("\n")
    header = f"[calibration.{var}]"
    block = [header]
    if scale is not None:
        block.append(f"scale = {_toml_num(scale)}")
    else:
        block.append(f"scale_pos = {_toml_num(scale_pos)}")
        block.append(f"scale_neg = {_toml_num(scale_neg)}")
    block.append(f"add = {_toml_num(add)}")
    if source:
        block.append('source = "' + str(source).replace('"', "'") + '"')
    block.append("")
    start = next((i for i, l in enumerate(lines) if l.strip() == header), None)
    if start is None:
        new_lines = lines + ([""] if lines and lines[-1].strip() else []) + block
    else:
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("[")), len(lines))
        while end > start + 1 and lines[end - 1].strip() == "":
            end -= 1
        new_lines = lines[:start] + block[:-1] + lines[end:]
    text = eol.join(new_lines)
    if not text.endswith(eol):
        text += eol
    for attempt in range(20):
        try:
            with open(toml_path, "w", encoding="utf-8", newline="") as f:
                f.write(text)
            return
        except OSError:
            import time
            time.sleep(1.5)
    raise OSError("could not write " + toml_path)


def _toml_num(x):
    return str(int(x)) if float(x) == int(x) else repr(float(x))


# ---------------------------------------------------------------------------------------------
# C-level files (legacy L1 data): read and used at L1 to fill the gaps of the logger-only L0M
# ---------------------------------------------------------------------------------------------
def _installation_date(l0dir, table="L1/GC-Net_location.csv"):
    """`Date of installation` (UTC) of the station of an L0 folder name such as '10-Saddle', from the location table; None if unknown"""
    try:
        loc = pd.read_csv(table, skipinitialspace=True).set_index("Name")
        return pd.to_datetime(loc.loc[str(l0dir)[3:], "Date of installation"], utc=True)
    except Exception:
        return None


_C_FILES_CACHE = {}


def _read_c_files(l0dir, path="./L0/"):
    """The two raw C-level files of a station as read (no derived columns): (Jason file or None, per-station file or None).
    Reading them takes 10 to 15 s per station and L1 asks for them three times in a row (read_c_level, c_level_heights, and the
    L0 origin plots), so the last station read is kept and handed out as copies (callers edit them); asking for another station
    drops it, so at most one station's C-level files are in memory."""
    key = (str(l0dir), path)
    if key not in _C_FILES_CACHE:
        _C_FILES_CACHE.clear()
        _C_FILES_CACHE[key] = _read_c_files_from_disk(l0dir, path)
    dfj, dfc = tuple(None if d is None else d.copy() for d in _C_FILES_CACHE[key])
    return apply_c_level_swaps(dfj, dfc, str(l0dir)[3:])      # sensors read on each other's channel: metadata/c_level_swaps.csv


def clear_c_files_cache():
    """free the C-level files kept by _read_c_files (called at the end of a station's processing)"""
    _C_FILES_CACHE.clear()


def _read_c_files_from_disk(l0dir, path="./L0/"):
    num = str(l0dir)[:2]
    f_st = path + l0dir + "/C file/" + num + "c.dat"
    f_je = path + "C level Jason/" + num + "c.dat"
    dfc = dfj = None
    if os.path.isfile(f_st):
        hdr = write_nead.get_config_list_str(INI + "c_file_header.ini", "fields")
        dfc = gc.read_c_file(f_st, hdr)
        dfc.index = pd.to_datetime(dfc.index, utc=True)
    if os.path.isfile(f_je):
        hdr = write_nead.get_config_list_str(path + "C level Jason/c_file_header_jeb.ini", "fields")
        dfj = gc.read_c_file(f_je, hdr)
        dfj.index = pd.to_datetime(dfj.index, utc=True)
        if dfc is not None:
            ts = [v for v in dfj.columns if "TS" in v]
            dfj[ts] = dfc.reindex(dfj.index)[ts]     # the Jason file has no snow temperatures: taken from the station file
    inst = _installation_date(l0dir)
    if inst is not None:                     # rows dated before the installation of the station are not data
        dfc = dfc.loc[dfc.index >= inst] if dfc is not None else None
        dfj = dfj.loc[dfj.index >= inst] if dfj is not None else None
    return dfj, dfc


def read_c_level(l0dir, path="./L0/"):
    """The C-level data of a station on its whole time axis: Jason's file up to its last record, the per-station file after it
    (a value that looks wrong is handled by the L1 filters and flags, not here).
    Snow height: where a file has HS but no HW, HW is derived as in the C-level convention (Jason file: -HS; station file:
    max(HS) - HS). Statistics columns (_max, _min, _stdev) are not read (mislabelled, see libgcnet.read_c_file).
    NB: the heights (HW1, HW2, HS1, HS2) are NOT taken from this merged frame by the gap-fill, see c_level_heights.
    Returns (data, provenance) or (None, None) when the station has no C-level file."""
    dfj, dfc = _read_c_files(l0dir, path)
    if dfc is None and dfj is None:
        return None, None
    for d, sign in ((dfj, "jason"), (dfc, "station")):
        if d is None or "HS1" not in d.columns or "HW1" not in d.columns:
            continue
        msk = d.HS1.notnull() & d.HW1.isnull()
        if sign == "jason":
            d.loc[msk, "HW1"] = -d.loc[msk, "HS1"]
            d.loc[msk, "HW2"] = -d.loc[msk, "HS2"]
        else:
            d.loc[msk, "HW1"] = d.loc[msk, "HS1"].max() - d.loc[msk, "HS1"]
            d.loc[msk, "HW2"] = d.loc[msk, "HS2"].max() - d.loc[msk, "HS2"]
    # only measured variables: the C-level files also hold derived or unidentified columns (U2m, U10m, Alb, Z, QC1-4, 'unkown')
    keep = ["ISWR", "OSWR", "NR", "TA1", "TA2", "TA3", "TA4", "TA5", "RH1", "RH2", "VW1", "VW2", "DW1", "DW2", "P", "HS1", "HS2", "HW1", "HW2",
            "V"] + ["TS" + str(i) for i in range(1, 11)]
    cols = [c for c in keep if any(d is not None and c in d.columns for d in (dfj, dfc))]
    if dfj is not None and dfc is not None:
        # Jason's file up to its last record, the per-station file after it: as the earlier pipeline did. The two files are on
        # different calibration scales and datums (Swiss Camp 1997: ISWR 406 in Jason's file, 804 in the station file), so they
        # are never mixed value by value.
        j, c = dfj.reindex(columns=cols), dfc.reindex(columns=cols)
        j = j.loc[~j.index.duplicated(keep="first")]
        c = c.loc[~c.index.duplicated(keep="first")]
        c = c.loc[c.index > j.index.max()]
        data = pd.concat([j, c]).sort_index()
        prov = pd.concat([tag(j, "C-level (Jason file)"), tag(c, "C-level (station file)")]).sort_index()
        return data, prov
    d = dfj if dfj is not None else dfc
    data = d.reindex(columns=cols)
    data = data.loc[~data.index.duplicated(keep="first")].sort_index()
    prov = tag(data, "C-level (Jason file)" if dfj is not None else "C-level (station file)")
    return data, prov


HEIGHT_VARS = ("HW1", "HW2", "HS1", "HS2")


def c_level_heights(l0dir, first_cr1000=None, path="./L0/"):
    """HW1/HW2/HS1/HS2 from the C-level files the way the earlier pipeline built them, so that the adjustments written for them
    keep their meaning (HS is anchored on the first valid HW, and Jason's and the station file's heights are on different datums):
      - a station with CR1000 data: Jason's file up to its last record (or the first CR1000 hour), the per-station file from there
        until the first CR1000 hour; nothing after it. The two files are spliced in time, never mixed value by value.
      - a station without CR1000 data: the per-station file alone (Jason's file is not used).
    Where a file has HS but no HW, HW is derived: Jason file -HS; station file max(HS) - HS, the max taken over the part used.
    Returns (frame with the height columns, provenance frame) or (None, None) without a per-station file."""
    dfj, dfc = _read_c_files(l0dir, path)
    if dfc is None:
        return None, None
    cols = [c for c in HEIGHT_VARS if c in dfc.columns or (dfj is not None and c in dfj.columns)]
    dfc = dfc.loc[~dfc.index.duplicated(keep="first")].sort_index()
    if dfj is not None:
        dfj = dfj.loc[~dfj.index.duplicated(keep="first")].sort_index()

    def derive(d, how):
        d = d.reindex(columns=[c for c in HEIGHT_VARS if c in d.columns]).copy()
        for n in ("1", "2"):
            if "HS" + n in d.columns and "HW" + n in d.columns:
                msk = d["HS" + n].notnull() & d["HW" + n].isnull()
                if how == "jason":
                    d.loc[msk, "HW" + n] = -d.loc[msk, "HS" + n]
                else:
                    d.loc[msk, "HW" + n] = d.loc[msk, "HS" + n].max() - d.loc[msk, "HS" + n]
        return d

    one_hour = pd.Timedelta(hours=1)
    if first_cr1000 is None:                                # no logger: the station file alone, whole record
        parts = [(derive(dfc, "station"), "C-level (station file)")]
    elif dfj is not None:
        end_j = min(pd.Timestamp(first_cr1000), dfj.index.max())
        parts = [(derive(dfj.loc[: end_j - one_hour], "jason"), "C-level (Jason file)"),
                 (derive(dfc.loc[end_j: pd.Timestamp(first_cr1000) - one_hour], "station"), "C-level (station file)")]
    else:
        parts = [(derive(dfc.loc[: pd.Timestamp(first_cr1000) - one_hour], "station"), "C-level (station file)")]
    data = pd.concat([d for d, _ in parts]).sort_index()
    prov = pd.concat([pd.DataFrame(np.where(d.notna(), lab, None), index=d.index, columns=d.columns, dtype=object)
                      for d, lab in parts]).sort_index()
    return data.reindex(columns=cols), prov.reindex(columns=cols)


def apply_c_level_corrections(c_all, site, path="metadata/c_level_corrections.csv"):
    """Multiply the values of the C-level files by the factors of metadata/c_level_corrections.csv (site, variable, period).
    For corrections of the C-level values only: the calibration of the logger files is in their configuration files."""
    if c_all is None or not os.path.isfile(path):
        return c_all
    tab = pd.read_csv(path, comment="#", skipinitialspace=True)
    for r in tab.loc[tab.site == site, :].itertuples():
        if r.variable not in c_all.columns or pd.isna(r.multiply):
            continue
        t0 = pd.to_datetime(r.t0, utc=True) if isinstance(r.t0, str) and r.t0.strip() else c_all.index.min()
        t1 = pd.to_datetime(r.t1, utc=True) if isinstance(r.t1, str) and r.t1.strip() else c_all.index.max()
        m = (c_all.index >= t0) & (c_all.index <= t1)
        c_all.loc[m, r.variable] = c_all.loc[m, r.variable] * r.multiply
    return c_all


def gapfill_from_c_level(df, l0dir, path="./L0/", logger_prov=None, first_cr1000=None):
    """Fill the hours/variables the logger-only L0M lacks with the C-level data. The logger value is never replaced.
    Returns (filled frame on the union time axis, bool mask of the C-level-filled values, provenance labels, C-level data).
    All variables are filled from the merged C-level frame value by value, except the heights (HW1, HW2, HS1, HS2) which come from
    c_level_heights: only before `first_cr1000` (first CR1000 hour of the station; None if it has no CR1000 data)."""
    c_all, c_prov = read_c_level(l0dir, path)
    c_all = apply_c_level_corrections(c_all, str(l0dir)[3:])
    if c_all is None:
        return df, pd.DataFrame(False, index=df.index, columns=df.columns), None, None
    idx = df.index.union(c_all.index)
    out = df.reindex(idx)
    cols = [c for c in c_all.columns if c not in ("timestamp",)]
    for c in cols:
        if c not in out.columns:
            out[c] = np.nan
    mask = pd.DataFrame(False, index=idx, columns=out.columns)
    prov = pd.DataFrame(np.nan, index=idx, columns=out.columns, dtype=object)
    have = out.notna()
    prov = prov.mask(have, "logger (L0M)")
    if logger_prov is not None:      # the logger file every value comes from (L0M/provenance configuration file)
        lp = logger_prov.reindex(index=idx, columns=out.columns)
        prov = prov.mask(have & lp.notna(), lp)
    h_all, h_prov = c_level_heights(l0dir, first_cr1000, path)
    for c in cols:
        if c in HEIGHT_VARS:
            if h_all is None or c not in h_all.columns:
                continue
            src, src_prov = h_all[c], h_prov[c]
        else:
            src, src_prov = c_all[c], c_prov[c]
        take = out[c].isna() & src.reindex(idx).notna()
        out.loc[take, c] = src.reindex(idx)[take]
        mask.loc[take, c] = True
        prov.loc[take, c] = src_prov.reindex(idx)[take]
    return out, mask, prov, c_all


def record_comparison(site, logger_hourly, c_all, source_windows_table=None):
    """logger versus C-level tables (metadata/logger_first/, working file out/logger_first_review/c_level_gaps.csv)"""
    prov = None
    if source_windows_table is not None and len(source_windows_table):
        prov = prov_from_windows(source_windows_table, logger_hourly.index, list(logger_hourly.columns))
    summ, win = compare_logger_to_clevel(site, logger_hourly, c_all)
    update_table(REVIEW + "logger_vs_clevel_agreement.csv", summ, site)
    update_table(WORK + "c_level_gaps.csv", win, site)
    update_table(REVIEW + "c_level_treatment_by_year.csv", yearly_diagnostics(site, logger_hourly, c_all, prov), site)


def record_fill_summary(site, filled_mask, provenance):
    """hours per variable and source in the filled L1 input (metadata/logger_first/l1_fill_summary.csv)"""
    rows = []
    for c in provenance.columns:
        vc = provenance[c].dropna().astype(str).value_counts()
        for lab, n in vc.items():
            rows.append(dict(site=site, variable=c, source=lab, hours=int(n)))
    update_table(REVIEW + "l1_fill_summary.csv", pd.DataFrame(rows, columns=["site", "variable", "source", "hours"]), site)

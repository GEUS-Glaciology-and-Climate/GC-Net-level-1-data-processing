# -*- coding: utf-8 -*-
"""Compare the current L1 files with the last release kept in "old releases/", station by station.

    python tools/compare_with_release.py                      # every station, newest folder of "old releases/" vs L1/
    python tools/compare_with_release.py Summit NGRIP         # selected stations (file names of L1/hourly/<name>.csv)
    python tools/compare_with_release.py --old "old releases/V11" --new L1 --out figures/release_2026/comparison

The hourly files of the two versions are aligned on their timestamps and, for every variable, every hour is classed as
    unchanged   valid in both, |new - old| <= tolerance
    modified    valid in both, |new - old| >  tolerance
    gained      valid only in the new version
    lost        valid only in the old version
(valid = not empty). The tolerances (TOL below, in the unit of the variable) are set above the rounding of the files, so
"modified" means a real change of the value. The series figures show daily means of the hourly values, with at least
MIN_VALID_HOURS_PER_DAY valid hours (the rule of the release), computed the same way for both versions.

Written into --out (default figures/release_2026/comparison, next to the figures of the release note):
    report.md              station-by-station report with the tables and the figures
    station_summary.csv    one row per station (record, valid hours, hours gained / lost / modified)
    variable_summary.csv   one row per station and variable, for every variable the two versions share
    <station>_temperature.png, <station>_humidity_pressure.png, <station>_radiation.png, <station>_snow_temperature.png
                           one figure per group of variables (GROUPS below), made only where a variable of the group is
                           affected by a large amount (LARGE below). One row per variable of the group: a wide time series
                           (previous release in orange under this version in blue) and a square new-vs-old scatter to its right
    network_coverage.png, network_valid_hours.png, network_modified.png   the whole network at a glance

Standalone (pandas, numpy, matplotlib): it does not import lib/, so it runs with `python -I`. The L1 folders are only read.
"""
import argparse
import os
import re
import time
import numpy as np
import pandas as pd
from matplotlib import rc_context
from matplotlib.colors import LinearSegmentedColormap, Normalize, PowerNorm
from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator

# ---- what is compared -----------------------------------------------------------------------------------------------
# the measured variables (plus albedo and the combined surface height) are the ones counted in the station totals and the
# network figures; every other variable the two versions share (derived fluxes, humidity wrt ice or water...) is in the csv
CORE = ["ISWR", "OSWR", "NR", "Alb", "TA1", "TA2", "TA3", "TA4", "RH1", "RH2", "VW1", "VW2", "DW1", "DW2", "P", "HW1", "HW2",
        "HS_combined"]
# One figure per group and station, made when at least one variable of the group is critical (below) and showing every
# variable of the group that has data in either version: file name suffix -> (title, variables)
GROUPS = {"temperature": ("air temperature", ["TA1", "TA2", "TA3", "TA4"]),
          "humidity_pressure": ("humidity and pressure", ["RH1", "RH2", "P"]),
          "radiation": ("radiation and albedo", ["ISWR", "OSWR", "NR", "Alb"]),
          "snow_temperature": ("snow temperature", [f"TS{i}" for i in range(1, 11)])}
# a variable is critical when its hours gained + lost + differing by more than LARGE (hourly values, much larger than the
# tolerances below) are at least MIN_CRITICAL_HOURS and MIN_CRITICAL_SHARE of the hours valid in either version
LARGE = [(r"^(ISWR|OSWR|NR)$", 20.0), (r"^(TA\d|TS\d+)$", 1.0), (r"^RH\d$", 5.0), (r"^VW\d$", 1.0), (r"^DW\d$", 20.0),
         (r"^P$", 2.0), (r"^(HW\d|HS_combined)$", 0.2), (r"^Alb$", 0.05)]
MIN_CRITICAL_HOURS = 2000
MIN_CRITICAL_SHARE = 0.10
MIN_VALID_HOURS_PER_DAY = 18
SKIP = re.compile(r"_adj_flag$|^(latitude|longitude|elevation|SZA|SAA)$")   # flags and geometry: not measurements
TOL = [(r"^(ISWR|OSWR|NR|NR_cor|SHF|LHF)$", 1.0, "radiation and fluxes (W/m^2)"),
       (r"^(TA\d|TS\d+|DTS\d+|TS_10m|TA2m)$", 0.1, "temperatures and depths (degC, m)"),
       (r"^(RH\d|RH2m|RH\d_wrt_ice_or_water)$", 0.5, "relative humidity (%)"), (r"^(VW\d|VW10m|V)$", 0.1, "wind speed, voltage"),
       (r"^DW\d$", 1.0, "wind direction (degrees)"), (r"^P$", 0.1, "pressure (hPa)"),
       (r"^(HW\d|HS\d|HS_combined)$", 0.02, "heights (m)"), (r"^Alb$", 0.01, "albedo"), (r"^Q\d$", 0.05, "specific humidity (g/kg)")]
TOL_DEFAULT = 0.01
ROOT =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repository, whatever the working directory

# ---- colours: the reference palette of the dataviz skill (light surface) --------------------------------------------
SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
OLD_C, NEW_C = "#eb6834", "#2a78d6"                     # previous release (orange, large pale dots) / this version (blue)
SEQ = LinearSegmentedColormap.from_list("seq_blue", ["#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"])
DIV = LinearSegmentedColormap.from_list("div_loss_gain", ["#e34948", "#f0efec", "#2a78d6"])   # red = lost, blue = gained
RC = {"font.family": "sans-serif", "font.sans-serif": ["Segoe UI", "DejaVu Sans"], "font.size": 8, "axes.edgecolor": AXIS,
      "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2, "text.color": INK, "axes.facecolor": SURFACE,
      "figure.facecolor": SURFACE, "axes.spines.top": False, "axes.spines.right": False, "xtick.labelsize": 7.5,
      "ytick.labelsize": 7.5}


def tolerance(var):
    for pat, tol, _ in TOL:
        if re.match(pat, var):
            return tol
    return TOL_DEFAULT


def large_threshold(var):
    for pat, lg in LARGE:
        if re.match(pat, var):
            return lg
    return None


def angle_diff(var, d):
    """new - old; for a wind direction the shortest way round (359 -> 1 degrees is +2, not -358)"""
    return (d + 180) % 360 - 180 if var.startswith("DW") else d


# ---- reading ----------------------------------------------------------------------------------------------------------
def header_info(path):
    """fields, units, station_id and station_name from the NEAD header of an L1 file"""
    info = {"fields": [], "units": [], "station_id": 999, "station_name": os.path.basename(path)}
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.startswith("#"):
                break
            key, _, val = line[1:].partition("=")
            key, val = key.strip(), val.strip()
            if key == "fields":
                info["fields"] = [x.strip() for x in val.split(",")]
            elif key == "units":
                info["units"] = [x.strip() for x in val.split(",")]
            elif key == "station_id" and val.isdigit():
                info["station_id"] = int(val)
            elif key == "station_name":
                info["station_name"] = val
    return info


def read_l1(path, wanted):
    """the `wanted` columns (those the file has) as float32, indexed by unique UTC timestamps"""
    fields = header_info(path)["fields"]
    cols = ["timestamp"] + [c for c in wanted if c in fields and c != "timestamp"]
    df = pd.read_csv(path, comment="#", header=None, names=fields, usecols=cols, low_memory=False,
                     dtype={c: "float32" for c in cols[1:]})
    df.index = pd.DatetimeIndex(pd.to_datetime(df.pop("timestamp"), utc=True))
    return df[~df.index.duplicated(keep="first")].sort_index()


def shown(path):
    """a path relative to the repository when it is inside it"""
    try:
        return os.path.relpath(path, ROOT).replace("\\", "/")
    except ValueError:
        return path


def latest_release(folder):
    names = [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
    if not names:
        raise SystemExit(f"no release folder in {folder}")
    return os.path.join(folder, max(names, key=lambda s: [int(t) if t.isdigit() else 0 for t in re.split(r"(\d+)", s)]))


# ---- comparison -------------------------------------------------------------------------------------------------------
def daily_means(df):
    """daily means of the hourly values, only for the days with at least MIN_VALID_HOURS_PER_DAY valid hours (albedo only
    exists in the sunlit hours: one is enough)"""
    r = df.resample("D")
    need = pd.Series({c: 1 if c == "Alb" else MIN_VALID_HOURS_PER_DAY for c in df.columns})
    return r.mean().where(r.count() >= need)


def compare_station(name, old_path, new_path):
    """per-variable statistics and the station totals of one station"""
    oi, ni = header_info(old_path), header_info(new_path)
    shared = [c for c in ni["fields"][1:] if c in oi["fields"] and not SKIP.search(c)]
    units = dict(zip(ni["fields"], ni["units"]))
    old, new = read_l1(old_path, shared), read_l1(new_path, shared)
    idx = old.index.union(new.index)
    o, n = old.reindex(idx), new.reindex(idx)
    rows = []
    any_old = np.zeros(len(idx), bool)
    any_new = np.zeros(len(idx), bool)
    for v in shared:
        oa, na = o[v].to_numpy(), n[v].to_numpy()
        ov, nv = ~np.isnan(oa), ~np.isnan(na)
        both, gained, lost = ov & nv, nv & ~ov, ov & ~nv
        tol, lg = tolerance(v), large_threshold(v)
        with np.errstate(invalid="ignore"):
            d = angle_diff(v, na - oa)
            mod = both & (np.abs(d) > tol)
            big = both & (np.abs(d) > lg) if lg is not None else np.zeros(len(idx), bool)
        dm = d[mod]
        rows.append(dict(
            station=name, variable=v, unit=units.get(v, ""), tolerance=tol, old_valid=int(ov.sum()), new_valid=int(nv.sum()),
            gained=int(gained.sum()), lost=int(lost.sum()), common=int(both.sum()), modified=int(mod.sum()),
            large=lg if lg is not None else np.nan, large_diff=int(big.sum()),
            max_abs_diff=float(np.abs(d[both]).max()) if both.any() else np.nan,
            shift_median=float(np.median(dm)) if len(dm) else np.nan,
            shift_p05=float(np.percentile(dm, 5)) if len(dm) else np.nan,
            shift_p95=float(np.percentile(dm, 95)) if len(dm) else np.nan,
            first_old=idx[ov][0] if ov.any() else pd.NaT, last_old=idx[ov][-1] if ov.any() else pd.NaT,
            first_new=idx[nv][0] if nv.any() else pd.NaT, last_new=idx[nv][-1] if nv.any() else pd.NaT))
        if v in CORE:
            any_old |= ov
            any_new |= nv
    var = pd.DataFrame(rows)
    core = var[var.variable.isin(CORE)]
    tot = {k: int(core[k].sum()) for k in ("old_valid", "new_valid", "gained", "lost", "common", "modified")}
    union = tot["old_valid"] + tot["gained"]

    def span(m):
        return (idx[m][0], idx[m][-1]) if m.any() else (pd.NaT, pd.NaT)

    st = dict(station=name, station_id=ni["station_id"], rows_old=len(old), rows_new=len(new),
              rows_common=len(old.index.intersection(new.index)),
              first_old=span(any_old)[0], last_old=span(any_old)[1], first_new=span(any_new)[0], last_new=span(any_new)[1],
              core_valid_old=tot["old_valid"], core_valid_new=tot["new_valid"],
              core_change_pct=100 * (tot["new_valid"] / tot["old_valid"] - 1) if tot["old_valid"] else np.nan,
              gained=tot["gained"], lost=tot["lost"], common=tot["common"], modified=tot["modified"],
              modified_pct_of_common=100 * tot["modified"] / tot["common"] if tot["common"] else np.nan,
              affected_pct=100 * (tot["gained"] + tot["lost"] + tot["modified"]) / union if union else np.nan,
              columns_added=[c for c in ni["fields"][1:] if c not in oi["fields"]],
              columns_removed=[c for c in oi["fields"][1:] if c not in ni["fields"]])
    members = [v for _, vs in GROUPS.values() for v in vs if v in shared]
    return dict(vars=var, station=st, daily=(daily_means(old[members]), daily_means(new[members])))


# ---- figures ----------------------------------------------------------------------------------------------------------
def save_fig(fig, path):
    for attempt in range(15):   # writes in this folder sometimes fail with Errno 22 (sync / scan lock)
        try:
            fig.savefig(path, dpi=110, facecolor=SURFACE)
            return
        except OSError:
            time.sleep(1.5)
    raise OSError(f"could not write {path}")


def write_text(path, text):
    for attempt in range(15):
        try:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
            return
        except OSError:
            time.sleep(1.5)
    raise OSError(f"could not write {path}")


def style_axes(ax):
    ax.tick_params(length=2.5, width=0.6, pad=2)
    for s in ("left", "bottom"):
        ax.spines[s].set_linewidth(0.6)


def pick_group(var, members):
    """the variables of a group to draw: all those with data in either version, if at least one of them is critical (hours
    gained + lost + differing by more than LARGE are at least MIN_CRITICAL_HOURS and MIN_CRITICAL_SHARE of its hours);
    empty otherwise"""
    v = var[var.variable.isin(members)].set_index("variable")
    v = v[(v.old_valid + v.new_valid) > 0]
    crit = v.gained + v.lost + v.large_diff
    if not len(v) or not ((crit >= MIN_CRITICAL_HOURS) & (crit >= MIN_CRITICAL_SHARE * (v.old_valid + v.gained))).any():
        return []
    return [m for m in members if m in v.index]


def trim_daily(df, variables):
    """{variable: daily means from its first to its last valid day, the missing days staying as gaps}"""
    out = {}
    for v in variables:
        s = df[v]
        out[v] = s.loc[s.first_valid_index():s.last_valid_index()] if s.notna().any() else s.iloc[:0]
    return out


def frac_year(idx):
    return idx.year + (idx.dayofyear - 1) / 365.25


def clip_limits(*arrays):
    """y limits P05 - A/10 to P95 + A/10 (A = P95 - P05), as in the L0 origin plots, so that glitches do not squash a panel"""
    v = np.concatenate([x[np.isfinite(x)] for x in arrays])
    if len(v) < 2:
        return None
    lo, hi = np.percentile(v, [5, 95])
    return None if hi == lo else (lo - (hi - lo) / 10, hi + (hi - lo) / 10)


def series_figure(name, title, var, series, old_daily, new_daily, path):
    """one group of variables, one row each, laid out like the L0 origin plots: a wide time series of the daily means (the
    previous release as large pale orange dots under this version in blue) and, to its right in the same row, a square
    scatter of the new daily value against the old one on the days both exist"""
    series = [v for v in series if len(old_daily[v]) or len(new_daily[v])]
    if not series:
        return False
    n = len(series)
    H = (2.25 if n <= 4 else 1.7) * n + 1.5
    ends = [(s[v].index[0], s[v].index[-1]) for s in (old_daily, new_daily) for v in series if len(s[v])]
    x0, x1 = min(a for a, _ in ends), max(b for _, b in ends)
    with rc_context(RC):
        fig = Figure(figsize=(15, H))
        gs = GridSpec(n, 2, figure=fig, width_ratios=[6.5, 1], wspace=0.1, hspace=0.5, left=0.05, right=0.955,
                      top=1 - 1.0 / H, bottom=0.5 / H)
        first = None
        for i, v in enumerate(series):
            a = fig.add_subplot(gs[i, 0], sharex=first)
            first = a if first is None else first
            r = var[var.variable == v].iloc[0]
            so, sn = old_daily[v], new_daily[v]
            a.plot(so.index, so.to_numpy(), ".", ms=5, color=OLD_C, alpha=0.45, zorder=1, rasterized=True)
            a.plot(sn.index, sn.to_numpy(), ".", ms=1.8, color=NEW_C, zorder=2, rasterized=True)
            lim = clip_limits(so.to_numpy(float), sn.to_numpy(float))
            if lim is not None:
                a.set_ylim(*lim)
            a.set_ylabel(f"{v} ({r.unit})", fontsize=8.5)
            unit = "" if r.unit in ("", "-") else f" {r.unit}"
            a.set_title(f"{r.gained:,} h gained, {r.lost:,} h lost, {r.large_diff:,} h differing by more than {r.large:g}{unit} "
                        f"(hourly values)", loc="left", fontsize=8.5, color=INK2)
            a.grid(color=GRID, lw=0.6)
            a.set_axisbelow(True)
            style_axes(a)
            a.set_xlim(x0, x1)
            if i < n - 1:
                a.tick_params(labelbottom=False)
            sc = fig.add_subplot(gs[i, 1])
            sc.set_box_aspect(1)
            sc.yaxis.tick_right()
            sc.yaxis.set_label_position("right")
            both = pd.DataFrame({"o": so, "n": sn}).dropna()
            if len(both):
                o, nw = both.o.to_numpy(float), both.n.to_numpy(float)
                lo, hi = np.percentile(np.r_[o, nw], [0.5, 99.5])
                pad = (hi - lo) * 0.06 or 1.0
                lo, hi = lo - pad, hi + pad
                sc.plot([lo, hi], [lo, hi], color=AXIS, lw=0.9, zorder=1)
                sc.plot(o, nw, ".", ms=2.4, color=NEW_C, alpha=0.4, zorder=2, rasterized=True)
                sc.set_xlim(lo, hi)
                sc.set_ylim(lo, hi)
                big = np.mean(np.abs(angle_diff(v, nw - o)) > r.large)
                sc.text(0.04, 0.96, f"{len(both):,} days in both\n{big:.0%} differ by > {r.large:g}", transform=sc.transAxes,
                        va="top", fontsize=7.5, color=INK2)
            else:
                sc.text(0.5, 0.5, "no day in both", ha="center", va="center", color=INK2, transform=sc.transAxes)
            sc.set_xlabel("previous release", fontsize=8)
            sc.set_ylabel("this version", fontsize=8)
            sc.grid(color=GRID, lw=0.6)
            sc.set_axisbelow(True)
            style_axes(sc)
        fig.text(0.012, 1 - 0.2 / H, f"{name}: {title}, previous release vs this version", fontsize=13, weight="bold", va="top")
        fig.text(0.012, 1 - 0.55 / H, f"daily means; right: the days that exist in both versions. Drawn because a variable of "
                 f"the group has at least {MIN_CRITICAL_HOURS} h ({MIN_CRITICAL_SHARE:.0%} of its hours) gained, lost or "
                 f"differing by a large amount", fontsize=8.5, color=INK2, va="top")
        fig.legend([Line2D([], [], marker=".", ls="", ms=11, color=OLD_C, alpha=0.5), Line2D([], [], marker=".", ls="", ms=7, color=NEW_C)],
                   ["previous release", "this version"], loc="upper right", ncol=2, frameon=False, fontsize=8,
                   bbox_to_anchor=(0.955, 1 - 0.1 / H))
        save_fig(fig, path)
    return True


def matrix_figure(M, title, cmap, norm, ticks, ticklabels, annotate_min, path, special=None):
    """station x variable matrix with the value written in the cells that matter; `special` = text that replaces a value"""
    with rc_context(RC):
        fig = Figure(figsize=(0.55 * len(M.columns) + 2.6, 0.27 * len(M) + 1.5))
        ax = fig.add_axes([0.13, 0.04, 0.80, 1 - 1.15 / fig.get_figheight() - 0.04])
        cax = fig.add_axes([0.945, 0.04, 0.012, 0.25])
        cm = cmap.copy()
        cm.set_bad(SURFACE)
        pm = ax.pcolormesh(np.arange(len(M.columns) + 1), np.arange(len(M) + 1), np.ma.masked_invalid(M.to_numpy(float)),
                           cmap=cm, norm=norm, edgecolors=SURFACE, linewidth=0.5)
        ax.set_ylim(len(M), 0)
        ax.xaxis.tick_top()
        ax.set_xticks(np.arange(len(M.columns)) + 0.5, M.columns, rotation=45, ha="left")
        ax.set_yticks(np.arange(len(M)) + 0.5, M.index)
        ax.tick_params(length=0, labelsize=7.5)
        for s in ax.spines.values():
            s.set_visible(False)
        for i, st in enumerate(M.index):
            for j, v in enumerate(M.columns):
                val = M.iloc[i, j]
                txt = special.iloc[i, j] if special is not None and isinstance(special.iloc[i, j], str) else None
                if txt is None and (np.isnan(val) or abs(val) < annotate_min):
                    continue
                r, g, b, _ = cm(norm(val))
                lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
                ax.text(j + 0.5, i + 0.5, txt or f"{val:.0f}", ha="center", va="center", fontsize=6.5,
                        color="white" if lum < 0.45 else INK)
        cb = fig.colorbar(pm, cax=cax)
        cb.set_ticks(ticks)
        cb.set_ticklabels(ticklabels)
        cb.outline.set_visible(False)
        cb.ax.tick_params(length=0, labelsize=7)
        fig.text(0.012, 1 - 0.2 / fig.get_figheight(), title, fontsize=10.5, weight="bold", va="top")
        save_fig(fig, path)


def network_figures(stations, vars_all, out):
    order = [s for s in stations]
    v = vars_all[vars_all.variable.isin(CORE)]

    def wide(col):
        return v.pivot(index="station", columns="variable", values=col).reindex(index=order, columns=CORE)

    old, new, mod, com = wide("old_valid"), wide("new_valid"), wide("modified"), wide("common")
    with np.errstate(invalid="ignore", divide="ignore"):
        change = 100 * (new / old - 1)
        both_empty = (old == 0) & (new == 0)
        change = change.mask(both_empty)
        special = change.map(lambda x: "new" if x == np.inf else None)
        change = change.replace(np.inf, 50)
        shared = 100 * mod / com
    matrix_figure(change, "Valid hours, this version vs the previous release (% of the previous hours; "
                  "'new' = variable did not exist)", DIV, Normalize(-50, 50), [-50, 0, 50], ["-50 %", "0", "+50 %"], 1,
                  os.path.join(out, "network_valid_hours.png"), special=special)
    matrix_figure(shared, "Share of the hours valid in both versions whose value changed by more than the tolerance (%)", SEQ,
                  PowerNorm(0.5, 0, 100), [0, 1, 10, 50, 100], ["0", "1 %", "10 %", "50 %", "100 %"], 1,
                  os.path.join(out, "network_modified.png"))


def coverage_figure(st, path):
    st = st.sort_values("first_new")
    with rc_context(RC):
        fig = Figure(figsize=(9, 0.34 * len(st) + 1.4))
        ax = fig.add_axes([0.15, 0.05, 0.70, 1 - 1.3 / fig.get_figheight() - 0.05])
        for i, (_, r) in enumerate(st.iterrows()):
            for dy, a, b, c, lw in ((-0.17, r.first_old, r.last_old, OLD_C, 5), (0.17, r.first_new, r.last_new, NEW_C, 5)):
                if pd.notna(a):
                    ax.plot([frac_year(a), frac_year(b)], [i + dy + 0.5] * 2, color=c, lw=lw, solid_capstyle="round")
            ax.text(1.01, i + 0.5, f"{r.core_change_pct:+.1f} %" if pd.notna(r.core_change_pct) else "new",
                    transform=ax.get_yaxis_transform(), fontsize=7.5, color=INK2, va="center")
        ax.set_ylim(len(st), 0)
        ax.set_yticks(np.arange(len(st)) + 0.5, st.station)
        ax.grid(axis="x", color=GRID, lw=0.6)
        ax.set_axisbelow(True)
        ax.xaxis.set_major_locator(MultipleLocator(5))
        ax.tick_params(length=0)
        for s in ax.spines.values():
            s.set_visible(False)
        fig.text(0.012, 1 - 0.2 / fig.get_figheight(), "Span of the record (first to last valid core variable)", fontsize=10.5,
                 weight="bold", va="top")
        fig.text(0.86, 1 - 1.05 / fig.get_figheight(), "valid hours", fontsize=7.5, color=INK2)
        fig.legend([Line2D([], [], color=OLD_C, lw=5), Line2D([], [], color=NEW_C, lw=5)], ["previous release", "this version"],
                   loc="upper left", ncol=2, frameon=False, fontsize=8, bbox_to_anchor=(0.012, 1 - 0.45 / fig.get_figheight()))
        save_fig(fig, path)


# ---- report -----------------------------------------------------------------------------------------------------------
def pct(x, signed=True):
    return "new" if np.isinf(x) else "-" if pd.isna(x) else f"{x:+.1f} %" if signed else f"{x:.1f} %"


def report(old_dir, new_dir, hourly_new, stations, st_all, var_all, figures, missing, out):
    mt = [os.path.getmtime(p) for p in hourly_new]
    stamp = lambda t: time.strftime("%Y-%m-%d %H:%M", time.localtime(t))
    cols_added = sorted({c for s in st_all.itertuples() for c in s.columns_added})
    cols_removed = sorted({c for s in st_all.itertuples() for c in s.columns_removed})
    tot = {k: int(st_all[k].sum()) for k in ("core_valid_old", "core_valid_new", "gained", "lost", "common", "modified")}
    L = [f"# L1 compared with the previous release ({os.path.basename(old_dir)})", "",
         f"Generated by `tools/compare_with_release.py` from `{new_dir}/hourly` (files written {stamp(min(mt))} to {stamp(max(mt))}) "
         f"and `{old_dir}/hourly`. {len(stations)} stations.".replace("\\", "/"), "",
         "Every hour of every variable is *unchanged*, *modified* (valid in both, differing by more than the tolerance), "
         "*gained* (valid only now) or *lost* (valid only before). \"Core variables\" are the 18 columns counted in the tables: "
         + ", ".join(CORE) + ". The tolerances are " + "; ".join(f"{label} {t:g}" for _, t, label in TOL)
         + f"; any other variable {TOL_DEFAULT:g}.", "",
         f"**Network**: {tot['core_valid_old']:,} -> {tot['core_valid_new']:,} valid core-variable hours "
         f"({pct(100 * (tot['core_valid_new'] / tot['core_valid_old'] - 1))}), {tot['gained']:,} gained, {tot['lost']:,} lost, "
         f"{tot['modified']:,} modified ({100 * tot['modified'] / tot['common']:.2f} % of the {tot['common']:,} shared hours).", ""]
    if cols_added or cols_removed:
        L += [f"Columns only in the new files: {', '.join(cols_added) or 'none'}. Columns only in the old files: "
              f"{', '.join(cols_removed) or 'none'}.", ""]
    if missing:
        L += ["Not compared (file in one release only): " + ", ".join(missing) + ".", ""]
    L += ["![coverage](network_coverage.png)", "", "![valid hours](network_valid_hours.png)", "",
          "![modified](network_modified.png)", "", "## Stations", "",
          "| station | record before | record now | core hours before | now | change | gained | lost | modified | % of hours affected |",
          "|---|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for s in st_all.itertuples():
        L.append(f"| [{s.station}](#{s.station.lower()}) | {str(s.first_old)[:10]} to {str(s.last_old)[:10]} | "
                 f"{str(s.first_new)[:10]} to {str(s.last_new)[:10]} | {s.core_valid_old:,} | {s.core_valid_new:,} | "
                 f"{pct(s.core_change_pct)} | {s.gained:,} | {s.lost:,} | {s.modified:,} | {s.affected_pct:.1f} |")
    for s in st_all.itertuples():
        v = var_all[var_all.station == s.station]
        v = v.assign(affected=v.gained + v.lost + v.modified)
        v = v[v.affected > 0].sort_values("affected", ascending=False)
        L += ["", f"## {s.station}", "",
              f"Record {str(s.first_old)[:10]} to {str(s.last_old)[:10]} before, {str(s.first_new)[:10]} to "
              f"{str(s.last_new)[:10]} now. Core variables: {s.core_valid_old:,} -> {s.core_valid_new:,} valid hours "
              f"({pct(s.core_change_pct)}); {s.affected_pct:.1f} % of the hours that exist in either version are gained, lost or "
              f"modified." + ("" if s.rows_common == s.rows_new == s.rows_old else
                              f" Hourly rows: {s.rows_old:,} before, {s.rows_new:,} now, {s.rows_common:,} in both.")]
        if s.columns_added or s.columns_removed:
            L.append(f"Columns added: {', '.join(s.columns_added) or 'none'}; removed: {', '.join(s.columns_removed) or 'none'}.")
        for key, (title, _) in GROUPS.items():
            if f"{s.station}_{key}" in figures:
                L += ["", f"![{s.station} {title}]({s.station}_{key}.png)"]
        core, other = v[v.variable.isin(CORE)], v[~v.variable.isin(CORE)]
        if len(core):
            L += ["", "| variable | unit | valid h before | now | change | gained | lost | modified | % of shared | "
                  "shift of modified: median [5 %, 95 %] |", "|---|---|---:|---:|---:|---:|---:|---:|---:|---|"]
            for r in core.head(12).itertuples():
                ch = 100 * (r.new_valid / r.old_valid - 1) if r.old_valid else (np.inf if r.new_valid else np.nan)
                sh = (f"{r.shift_median:+.3g} [{r.shift_p05:+.3g}, {r.shift_p95:+.3g}]" if pd.notna(r.shift_median) else "-")
                L.append(f"| {r.variable} | {r.unit} | {r.old_valid:,} | {r.new_valid:,} | {pct(ch)} | {r.gained:,} | {r.lost:,} | "
                         f"{r.modified:,} | {100 * r.modified / r.common if r.common else 0:.1f} | {sh} |")
        else:
            L += ["", "No core variable differs."]
        if len(other):
            L += ["", f"{len(other)} other variables differ (derived, thermistors, humidity wrt ice or water...), most affected: "
                  + ", ".join(other.variable.head(6)) + "; see `variable_summary.csv`."]
    write_text(os.path.join(out, "report.md"), "\n".join(L) + "\n")


# ---- main -------------------------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("stations", nargs="*", help="station names (default: all the stations both releases have)")
    ap.add_argument("--old", default=None, help='previous release folder (default: newest folder of <repo>/"old releases/")')
    ap.add_argument("--new", default=os.path.join(ROOT, "L1"), help="folder with hourly/ and daily/ of the new version (default <repo>/L1)")
    ap.add_argument("--out", default=os.path.join(ROOT, "figures", "release_2026", "comparison"))
    a = ap.parse_args()
    old_dir = a.old or latest_release(os.path.join(ROOT, "old releases"))
    os.makedirs(a.out, exist_ok=True)
    stem = lambda d: {f[:-4] for f in os.listdir(os.path.join(d, "hourly")) if f.endswith(".csv")}
    both, missing = sorted(stem(old_dir) & stem(a.new)), sorted(stem(old_dir) ^ stem(a.new))
    stations = [s for s in both if not a.stations or s in a.stations]
    unknown = [s for s in a.stations if s not in both]
    if unknown:
        raise SystemExit(f"not in both releases: {unknown}; available: {both}")
    print(f"comparing {shown(a.new)} with {shown(old_dir)}: {len(stations)} station(s) -> {shown(a.out)}")
    results, figures = {}, set()
    for i, s in enumerate(stations, 1):
        t = time.time()
        results[s] = compare_station(s, os.path.join(old_dir, "hourly", s + ".csv"), os.path.join(a.new, "hourly", s + ".csv"))
        r = results[s]
        made = []
        for key, (title, members) in GROUPS.items():
            series = pick_group(r["vars"], members)
            if series and series_figure(s, title, r["vars"], series, trim_daily(r["daily"][0], series),
                                        trim_daily(r["daily"][1], series), os.path.join(a.out, f"{s}_{key}.png")):
                figures.add(f"{s}_{key}")
                made.append(key)
        print(f"[{i}/{len(stations)}] {s}: {r['station']['core_change_pct']:+.1f} % valid core hours, "
              f"{r['station']['modified']:,} modified, figures: {', '.join(made) or 'none'}, {time.time() - t:.0f} s")
    st_all = pd.DataFrame([results[s]["station"] for s in stations]).sort_values(["station_id", "station"])
    st_all = st_all.reset_index(drop=True)
    var_all = pd.concat([results[s]["vars"] for s in st_all.station], ignore_index=True)
    st_all.drop(columns=["columns_added", "columns_removed"]).to_csv(os.path.join(a.out, "station_summary.csv"), index=False)
    var_all.to_csv(os.path.join(a.out, "variable_summary.csv"), index=False)
    network_figures(list(st_all.station), var_all, a.out)
    coverage_figure(st_all, os.path.join(a.out, "network_coverage.png"))
    report(shown(old_dir), shown(a.new), [os.path.join(a.new, "hourly", s + ".csv") for s in stations], list(st_all.station), st_all, var_all,
           figures, missing, a.out)
    print("done:", os.path.join(a.out, "report.md"))


if __name__ == "__main__":
    main()

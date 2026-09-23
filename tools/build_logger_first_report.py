# -*- coding: utf-8 -*-
"""Builds the logger-first report (markdown, figures, tables) from the curated tables in metadata/logger_first/.

Usage (repository root):
  python tools/build_logger_first_report.py <L0M dir> <origin plot dir> [out dir]
    <L0M dir>          holds provenance/<station>_source_windows.csv (from the L0 script)
    <origin plot dir>  holds <station>_<group>.png (figures/L0_sources of the same run)
The PDF is made afterwards with pandoc (see the memory note on pandoc/MiKTeX).
"""
import os
import sys
import glob
import shutil
import warnings
warnings.simplefilter("ignore")
import numpy as np
import pandas as pd
from matplotlib.figure import Figure

M = "metadata/logger_first/"
L0M = sys.argv[1] if len(sys.argv) > 1 else "L0M"
PLOTS = sys.argv[2] if len(sys.argv) > 2 else "figures/L0_sources"
OUT = sys.argv[3] if len(sys.argv) > 3 else "out/logger_first_2026-09-24"
os.makedirs(OUT + "/figures", exist_ok=True)
md = []


def p(*a):
    md.append("\n".join(a) if len(a) > 1 else a[0])


def table(df, floatfmt=None):
    if len(df) == 0:
        return "(no rows)"
    df = df.copy()
    cols = [str(c) for c in df.columns]
    lines = ["| " + " | ".join(cols) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for _, r in df.iterrows():
        cells = []
        for v in r.values:
            if isinstance(v, float):
                cells.append("" if np.isnan(v) else (f"{v:.{floatfmt}f}" if floatfmt is not None else f"{v:g}"))
            else:
                cells.append(str(v))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def save(fig, name):
    fig.savefig(f"{OUT}/figures/{name}.png", dpi=110)
    return f"figures/{name}.png"


def stn_order(names):
    return sorted(set(names), key=lambda s: (str(s)[:2], s))


# --------------------------------------------------------------------------------------------- data
reg = pd.read_csv("L0/L0_ini/CR10X_file_registry.csv", skipinitialspace=True)
reg = reg[reg.use == 1]
ver = pd.read_csv(M + "cr10x_decode_verification.csv")
cal = pd.read_csv(M + "calibration_by_file.csv")
tim = pd.read_csv(M + "timing_check.csv")
tsc = pd.read_csv(M + "timestamp_iswr_check.csv")
gap = pd.read_csv(M + "c_level_gap_assessment.csv")
agr = pd.read_csv(M + "logger_vs_clevel_agreement.csv") if os.path.isfile(M + "logger_vs_clevel_agreement.csv") else pd.DataFrame()
trt = pd.read_csv(M + "c_level_treatment_by_year.csv") if os.path.isfile(M + "c_level_treatment_by_year.csv") else pd.DataFrame()
prog = pd.read_csv("metadata/logger_programs/programs.csv")
meas = pd.read_csv("metadata/logger_programs/measurements.csv")

# --------------------------------------------------------------------------------------------- text
p("# Logger-first L0/L0M: use the logger files before the C-level files",
  "",
  "Baptiste Vandecrux's repository `GC-Net-level-1-data-processing`, branch `2026-update`. 2026-09-24.",
  "",
  "## 1. What was done and why",
  "",
  "L0M used to be built from the CR1000 files plus the C-level files, and the historical CR10X logger files that sit in "
  "`L0/<station>/CR10X logger files/` were never read (except at Swiss Camp 10m). The C-level files are legacy L1 data, i.e. processed "
  "products: they contain conversions and corrections (RH with respect to ice in some periods, temperature-corrected snow "
  "height, per-sensor radiation factors), gap-filling between sensors, and removals of malfunctioning data that are not documented. "
  "The change is:",
  "",
  "1. **L0M = logger files only.** CR1000, CR10X (decoded with a registry in `L0/L0_ini/`: no header, no year column, several "
  "interleaved output arrays), the older loggers, and the transmissions (L0 data; used only after the last logger record, from the "
  "station folder or from `L0/backup_transmissions_20230111`; nothing is downloaded any more) are stacked. No C-level data, no "
  "filtering, no convention conversion. Radiation is calibrated with the documented (per-file) factors, like the CR1000 header factors.",
  "2. **C-level files fill the gaps at L1** (Jason's file first, then the per-station file; only where the logger has no value), "
  "until the missing logger data are found. The filled values are tracked, illustrated (`figures/L1_gapfill`) and are the only ones "
  "that receive the legacy C-level conversions (RH wrt ice -> water). "
  "For every variable the hours in both sources, logger only and C-level only are listed (L1 run). "
  "Windows where the logger has data and the C-level file none (a possible removal of a malfunction) are assessed and, when the "
  "data are demonstrably wrong, flagged at L1 (`metadata/flags`).",
  "3. **Provenance.** Every L0M value is traced to its file; `L0M/provenance/<station>_source_windows.csv` records it for L1 and the "
  "origin plots (`figures/L0_sources`) show it; the L1 gap-fill plots (`figures/L1_gapfill`) add the C-level sources.",
  "4. **Logger programs reviewed** (`metadata/logger_programs/`): variables stored, output arrays, sensors, multipliers and offsets.",
  "5. **L1 becomes source aware**: `ice_to_water` acts only on C-level-filled hours, the legacy `air_temp_sonic_correction` rows only on hours "
  "that do not come from a CR10X file, and the sonic correction plus the installation offset (`add_cr10x`) are applied to CR10X-sourced snow heights.",
  "",
  "Evidence tables and all choices are kept in `metadata/logger_first/` (see its README).", "")

# --- inventory
p("## 2. CR10X logger files: decoding", "")
n_files = len(glob.glob("L0/*/CR10X logger files/*"))
p(f"The station folders contain {n_files} files in `CR10X logger files`. {len(reg)} runs (file, output array, row range) were dated and "
  f"named and are registered; {reg.layout.nunique()} distinct column layouts occur. Dating: the start year of every run is the year "
  "whose detrended daily temperature best matches the C-level file. Columns are matched to C-level variables by exact copy or linear "
  f"relation; {int((~ver.kept.astype(bool)).sum())} of {len(ver)} column names failed the final verification against C-level and were dropped.", "")
r = reg.groupby("site").agg(files=("file", "nunique"), runs=("file", "size"), first_year=("start_year", "min"), last_year=("start_year", "max")).reset_index()
p(table(r), "")
v = ver.groupby("status").size().rename("columns").reset_index()
p("Column identification by method:", "", table(v), "")

# --- logger programs
p("## 3. Logger programs", "")
p(f"{len(prog)} programs were parsed (`.CSI` EDLOG sources with comments, `.DLD` downloads); {len(meas)} measurement instructions are listed with "
  "sensor, multiplier and offset. Findings that matter for the data:", "",
  "- All GC-Net CR10X programs use the CS105 barometer constants (multiplier 0.184, range 600-1060 hPa) and write P minus 400 "
  "(hence the +400 in the calibration). CS106 (multiplier 0.240) appears only in the Larsen C program.",
  "- The standard 28-value hourly array contains ISWR, OSWR, NR, TS1-10, TA1-4, RH1, RH2, VW1, VW2, DW1, DW2, P, HW1, HW2, one unnamed column and V. "
  "The unnamed column is the hourly maximum of the VW2 anemometer input (`Maximize` in the programs): it is never below VW2 and correlates 0.99 with it. "
  "It is stored as `VW2_max` (or `VW1_max`).",
  "- Radiation inputs are raw millivolts in the programs (multiplier 1); the conversion to W/m2 comes from a calibration, which is why it has to be documented "
  "per file (section 4).", "")

# --- calibration
p("## 4. Radiation calibration: what the C-level files applied", "")
p("For every logger file the raw radiation values were compared with the C-level file (best timing shift of -2..+2 h). The through-origin slope is the factor "
  "the C-level processing applied; it is compared with the factor documented in the station header. Classes: `documented` (within 3%), `differs` "
  "(another plausible sensitivity), `physical_units` (the logger file itself is already in W/m2), `c_level_uncalibrated`, `poor_overlap`.", "")
tab = cal.groupby(["var", "cls"]).size().unstack(fill_value=0).reset_index()
p(table(tab), "")
c = cal[cal.cls.isin(["documented", "differs", "physical_units"]) & cal["var"].isin(["ISWR", "OSWR"])].copy()
fig = Figure(figsize=(11, 4.6))
axs = fig.subplots(1, 2, sharey=True)
for ax, var in zip(axs, ["ISWR", "OSWR"]):
    d = c[c["var"] == var]
    sites = stn_order(d.site)
    for i, s in enumerate(sites):
        y = d[d.site == s].k_median_ratio.values
        ax.plot(np.full(len(y), i) + np.random.default_rng(i).normal(0, .06, len(y)), y, ".", ms=5)
    ax.set_xticks(range(len(sites)))
    ax.set_xticklabels(sites, rotation=90, fontsize=7)
    ax.axhline(200, color="k", lw=.6, ls="--")
    ax.set_title(f"{var}: factor in the C-level file", fontsize=10)
    ax.set_yscale("log")
    ax.grid(alpha=.3)
fig.axes[0].set_ylabel("factor (W/m2 per raw unit), log scale; dashed = 200")
fig.tight_layout()
p(f"![Radiation factors implied by the C-level files]({save(fig, 'fig_radiation_factors')})", "")
p("Findings:", "",
  "- ISWR: the C-level factor equals the documented 200 for most files. Several stations (GITS, JAR2, CP2, NGRIP, NASA-U, South Dome, Swiss Camp) "
  "have factors of roughly 60-83 in the CR10X era, i.e. **the CR1000-era header factors must not be applied to their CR10X files**.",
  "- OSWR: the C-level factor is a constant 186.8 where the header says 200 (Saddle, Crawford Point 1, DYE-2, JAR1, NASA-SE, Tunu-N, NEEM, Petermann Glacier). "
  "With 200 the median albedo of these stations is about 0.90, with 186.8 about 0.84, which is realistic for dry snow: the C-level factor is the individually "
  "calibrated one and is reused (a plausibility argument, not a reference measurement).",
  "- The Summit 2004 file `1minute calibrated` is already in W/m2 (factor ~1): applying the station factor would be wrong.",
  "- Deviation from the letter of 'raw values in L0M': radiation and net radiation (sign-dependent factors) are calibrated at L0 with a documented factor, because raw "
  "mV and W/m2 cannot share one column safely. The alternative (raw in L0M, calibration in `metadata/adjustments`) is possible but needs one adjustment row per file.", "")
tab = (cal[cal["var"].isin(["ISWR", "OSWR", "NR>0", "NR<0"]) & cal.cls.isin(["documented", "differs", "physical_units"])]
       .groupby(["site", "var"]).agg(files=("file", "count"), k_documented=("k_documented", "median"), k_c_level=("k_median_ratio", "median"),
                                    classes=("cls", lambda x: "/".join(sorted(set(x))))).reset_index())
p("Per station (median over files):", "", table(tab, 2), "")

# --- what C-level did to RH / HW
p("## 5. What the C-level files did to RH and snow height", "")
if len(trt):
    rh = trt[trt.test == "RH ice/water"].copy()
    hw = trt[trt.test == "HW correction/swap"].copy()
    if len(rh):
        rh["code"] = rh.verdict.map({"same (wrt water)": 0, "wrt ice": 1, "other": 2})
        piv = rh.groupby(["site", "year"]).code.agg(lambda x: x.mode().iloc[0]).unstack()
        fig = Figure(figsize=(12, 0.32 * len(piv) + 1.5))
        ax = fig.subplots()
        im = ax.imshow(piv.values, aspect="auto", cmap="viridis", vmin=0, vmax=2, interpolation="nearest")
        ax.set_yticks(range(len(piv)))
        ax.set_yticklabels(piv.index, fontsize=8)
        ax.set_xticks(range(0, len(piv.columns), 2))
        ax.set_xticklabels(piv.columns[::2], rotation=90, fontsize=8)
        cb = fig.colorbar(im, ax=ax, ticks=[0, 1, 2])
        cb.ax.set_yticklabels(["same as logger (wrt water)", "wrt ice", "other"])
        ax.set_title("RH in the C-level file compared with the raw logger RH, per station and year (T < -2 C hours)")
        fig.tight_layout()
        p("**RH.** Logger RH (raw sensor output, with respect to water) versus C-level RH: the C-level file is with respect to ice (clipped at 100%) in some "
          "years and identical to the logger in others. Logger RH is therefore the consistent source; the legacy `ice_to_water` rows now skip CR10X-sourced hours.", "",
          f"![RH treatment in the C-level files]({save(fig, 'fig_rh_treatment')})", "")
        p(table(rh.groupby(["site", "verdict"]).size().unstack(fill_value=0).reset_index()), "")
        if os.path.isfile(M + "rh_convention_by_year.csv"):
            rc = pd.read_csv(M + "rh_convention_by_year.csv")
            p("The C-level RH also stays with respect to ice after the end of the existing `ice_to_water` windows (e.g. DYE-2 through 2019 in the overlap with the CR1000). "
              "`ice_to_water` now acts only on C-level-sourced hours (never on logger values), and `tools/rh_ice_windows.py` adds rows for the years where the C-level "
              f"RH is wrt ice and no row covers it ({int((rc.action == 'add ice_to_water').sum())} station-sensor-years, merged into rows in `metadata/adjustments`). "
              f"{int(rc.action.str.startswith('existing').sum())} station-sensor-years are covered by an old row although the C-level RH is already wrt water (only concerns "
              "C-level gap-fills; listed in `metadata/logger_first/rh_convention_by_year.csv`).", "",
              "Raw logger RH is also better than the C-level RH converted back: the C-level value is clipped at 100% wrt ice, so converting it back to water gives values 9-10 points "
              "too low in cold conditions (Saddle, T < -30 C: raw logger 75%, previous L1 66%).", "")
    if len(hw):
        hw["code"] = hw.best.map(lambda b: 0 if b == "same_sonic" else 1 if b == "same_raw" else 2 if str(b).startswith("other") else np.nan)
        piv = hw.groupby(["site", "year"]).code.agg(lambda x: x.mode().iloc[0]).unstack()
        fig = Figure(figsize=(12, 0.32 * len(piv) + 1.5))
        ax = fig.subplots()
        im = ax.imshow(piv.values, aspect="auto", cmap="viridis", vmin=0, vmax=2, interpolation="nearest")
        ax.set_yticks(range(len(piv)))
        ax.set_yticklabels(piv.index, fontsize=8)
        ax.set_xticks(range(0, len(piv.columns), 2))
        ax.set_xticklabels(piv.columns[::2], rotation=90, fontsize=8)
        cb = fig.colorbar(im, ax=ax, ticks=[0, 1, 2])
        cb.ax.set_yticklabels(["C-level = logger x sonic factor", "C-level = raw logger", "matches the OTHER sensor"])
        ax.set_title("Snow height (HW) in the C-level file compared with the raw logger HW, per station and year")
        fig.tight_layout()
        p("**Snow height (HW).** The spread of `C-level minus candidate` around its median identifies whether the C-level distance is the raw logger distance, "
          "the logger distance times sqrt((T+273.15)/273.15) (sonic-ranger air-temperature correction), or the reading of the other sensor (swap or gap-fill). "
          "The logger HW is the uncorrected distance, so L1 applies the correction to CR10X-sourced hours.", "",
          f"![HW treatment in the C-level files]({save(fig, 'fig_hw_treatment')})", "")
        p(table(hw.groupby(["site", "best"]).size().unstack(fill_value=0).reset_index()), "")
    if os.path.isfile(M + "hw_offsets_by_year.csv"):
        ho = pd.read_csv(M + "hw_offsets_by_year.csv")
        sw = pd.read_csv(M + "hw_swap_candidates.csv")
        p("**Snow-height offsets.** Where the C-level HW is the same sensor's reading, it differs from the (sonic-corrected) logger distance by a constant: the installation "
          "height constant that the C-level processing added (Saddle: HW1 +0.52 m, HW2 -0.32 m in 2002-2013). The raw logger values do not have it; `tools/hw_offsets.py` "
          "derives the offsets per station, sensor and year, merges equal consecutive years, fills a year between two years with the same offset, and writes them as "
          "`add_cr10x` rows to `metadata/adjustments/<site>.csv` (applied only to CR10X-sourced hours, after the sonic correction). With them the new L1 HW reproduces the "
          "previous L1 exactly in the resolved years (Saddle: median difference 0.000 m, MAD 0.00 m).", "",
          table(ho.groupby("reason").size().rename("station-sensor-years").reset_index()), "",
          f"**Swap candidates.** In {len(sw)} file-years the C-level HW1 (HW2) reproduces the logger's OTHER sensor column within 0.02 m (after sonic factor and a constant): "
          "the C-level file swapped or gap-filled the two sensors, or the logger columns are named the other way round in that file. This is NOT decided automatically "
          "(which sensor is physically HW1 needs field knowledge); the list is `metadata/logger_first/hw_swap_candidates.csv`:", "",
          table(sw.groupby("site").agg(file_years=("year", "size"), first_year=("year", "min"), last_year=("year", "max")).reset_index()), "",
          "Consequence: in those years the new L1 HW (raw logger, no offset) differs from the previous L1 (C-level based) by the offset or by the swap, and `HS_combined` "
          "inherits a constant shift (Summit -4 m, NASA-E -1.9 m relative to the previous L1, because the series is anchored on its first values). Both need a decision per station.", "")
    ts = trt[trt.test == "HW equals TS column"]
    hit = ts[ts.share_equal > 0.05]
    p("**HW columns holding a temperature-string column.** Share of HW hours identical (within 0.005) to a TS column:", "",
      table(hit[["site", "variable", "file", "year", "hours", "best_ts_column", "share_equal"]]) if len(hit) else "No file/year has more than 5% of an HW column equal to a TS column.", "")
else:
    p("(`c_level_treatment_by_year.csv` is produced by the L0 script; not available in this build of the report.)", "")

# --- timing
p("## 6. Timestamps", "")
t = tim[tim.n_compared >= 200]
odd = t[t.best_shift_h != 0]
p(f"Logger hours were compared with the C-level file at shifts of -2..+2 h for the variables the C-level processing copied verbatim (TA, TS, DW, V). "
  f"{int((t.best_shift_h == 0).sum())} of {len(t)} station-years agree at 0 h. The exceptions:", "",
  table(odd[["station", "year", "-2", "-1", "0", "1", "2", "n_compared", "best_shift_h"]], 2), "",
  "An ISWR-versus-CARRA-ssrd scan (with the calibrated -2 h bias of that method) gives:", "", table(tsc), "",
  "NASA-E 2006-07 and NEEM 2007: the logger stamps are 2 h off while the C-level file agrees with CARRA at 0 h. The other cases are ambiguous (logger and C-level offset "
  "by different amounts) and no `time_shift` was added; the sign convention of `adjust_data` must be confirmed first.", "")

# --- origin
p("## 7. Where the values come from", "")
fs = pd.read_csv(M + "l1_fill_summary.csv") if os.path.isfile(M + "l1_fill_summary.csv") else None
if fs is not None:
    fs["cls"] = np.where(fs.source.str.startswith("C-level (Jason"), "C-level (Jason)", np.where(fs.source.str.startswith("C-level"), "C-level (station)",
                np.where(fs.source.str.startswith("transmission"), "transmission", np.where(fs.source == "CR1000", "CR1000", "CR10X / older loggers"))))
    main_v = ["TA1", "TA2", "RH1", "VW1", "P", "ISWR", "OSWR", "NR", "HW1", "TS1"]
    o = fs[fs.variable.isin(main_v)].pivot_table(index="site", columns="cls", values="hours", aggfunc="sum", fill_value=0)
    order = [c for c in ["CR1000", "CR10X / older loggers", "transmission", "C-level (Jason)", "C-level (station)"] if c in o.columns]
    sh = o[order].div(o[order].sum(axis=1), axis=0) * 100
    fig = Figure(figsize=(11, 5.5))
    ax = fig.subplots()
    left = np.zeros(len(sh))
    for c_, col in zip(order, ["#d62728", "#1f77b4", "#2ca02c", "#444444", "#9a9a9a"]):
        ax.barh(range(len(sh)), sh[c_], left=left, color=col, label=c_)
        left += sh[c_].values
    ax.set_yticks(range(len(sh)))
    ax.set_yticklabels(sh.index, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("share of the values (%), ten main variables")
    ax.legend(ncol=3, loc="lower center", bbox_to_anchor=(0.5, 1.0), fontsize=8)
    fig.tight_layout()
    p("Share of the values entering L1 (ten main variables) by source. The logger files (L0M) come first; the C-level files only fill what is missing.", "",
      f"![Source of the values at L1]({save(fig, 'fig_origin_share')})", "")
    p(table(sh.round(0).reset_index()), "")
rows = []
for f in ([] if fs is not None else sorted(glob.glob(f"{L0M}/provenance/*_source_windows.csv"))):
    d = pd.read_csv(f)
    d = d[d.variable.isin(["TA1", "TA2", "RH1", "VW1", "P", "ISWR", "OSWR", "NR", "HW1", "TS1"])]
    g = d.groupby("source_class").hours.sum()
    rows.append(dict(station=os.path.basename(f).replace("_source_windows.csv", ""), **g.to_dict()))
if rows:
    o = pd.DataFrame(rows).fillna(0).set_index("station")
    for c_ in ("CR1000", "CR10X", "C-level"):
        if c_ not in o:
            o[c_] = 0
    o = o[["CR1000", "CR10X", "C-level"]]
    sh = o.div(o.sum(axis=1), axis=0) * 100
    fig = Figure(figsize=(11, 5))
    ax = fig.subplots()
    left = np.zeros(len(sh))
    for c_, col in zip(sh.columns, ["#d62728", "#1f77b4", "#7f7f7f"]):
        ax.barh(range(len(sh)), sh[c_], left=left, color=col, label=c_)
        left += sh[c_].values
    ax.set_yticks(range(len(sh)))
    ax.set_yticklabels(sh.index, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("share of the values (%), ten main variables")
    ax.legend(ncol=3, loc="lower center", bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout()
    p("Share of the L0M values (ten main variables) by source class. C-level values remain only where no logger value exists.", "",
      f"![Source of the L0M values]({save(fig, 'fig_origin_share')})", "")
    p(table(sh.round(0).reset_index()), "")
p("Per-station origin plots (coloured by file, daily means, C-level in grey) are in `figures/L0_sources/<station>_<group>.png`. Examples:", "")
for stn, grp in (("10-Saddle", "radiation"), ("10-Saddle", "air_temperature_humidity"), ("17-JAR2", "wind_pressure_battery"), ("21-Petermann Glacier", "radiation")):
    src = f"{PLOTS}/{stn}_{grp}.png"
    if os.path.isfile(src):
        shutil.copy(src, f"{OUT}/figures/origin_{stn[:2]}_{grp}.png")
        p(f"![{stn} {grp}](figures/origin_{stn[:2]}_{grp}.png)", "")

# --- gaps
p("## 8. Data the logger has and the C-level file lacks", "")
p("A gap in the C-level file where the logger has data can mean that the C-level producers removed a malfunction, or that data were overlooked. Every window of >= 24 h was "
  "assessed with: physical range, stuck (flat) values, whether the L1 frozen-value filter already removes it, and CARRA (wind, air temperature, pressure, incoming shortwave). "
  "CARRA assimilates most of these variables, so it is used only to recognise clearly wrong values. Verdicts:", "")
g1 = gap.groupby("verdict").hours.agg(["count", "sum"]).reset_index().rename(columns={"count": "windows", "sum": "hours"})
p(table(g1), "")
g2 = gap.groupby(["site", "verdict"]).hours.sum().unstack(fill_value=0)
fig = Figure(figsize=(11, 5))
ax = fig.subplots()
left = np.zeros(len(g2))
for c_ in g2.columns:
    ax.barh(range(len(g2)), g2[c_] / 1000, left=left, label=c_)
    left += g2[c_].values / 1000
ax.set_yticks(range(len(g2)))
ax.set_yticklabels(g2.index, fontsize=8)
ax.invert_yaxis()
ax.set_xlabel("thousand hours")
ax.legend()
fig.tight_layout()
p(f"![Logger-only windows by verdict]({save(fig, 'fig_gaps_verdict')})", "")
sup = gap[gap.verdict == "supported"]
g3 = sup.groupby("variable").agg(windows=("hours", "size"), hours=("hours", "sum")).reset_index().sort_values("hours", ascending=False)
p(f"{len(sup)} windows ({int(sup.hours.sum())} h) were judged faulty and written as NAN rows to `metadata/flags/<site>.csv` "
  "(comment: 'logger-first review 2026-09'). By variable:", "", table(g3.head(25)), "")
p("Reasons of the flagged windows (main criterion):", "",
  table(sup.assign(criterion=sup.reason.str.replace(r"[-0-9.,]+", "#", regex=True).str.replace(r"\s+", " ", regex=True).str[:60])
        .groupby("criterion").hours.agg(["count", "sum"]).sort_values("sum", ascending=False).head(12).reset_index()), "",
  "The HW1/HW2 flags rest on the flat-value criterion alone and are the weakest; a snow surface can be stable, but hundreds of hours of exactly identical values "
  "point to a stuck sensor. They are listed in `metadata/logger_first/c_level_gap_assessment.csv` for review.", "")

# --- L1 check
p("## 9. L1 check (scratch run)", "")
if os.path.isfile(OUT + "/l1_comparison.csv"):
    lc = pd.read_csv(OUT + "/l1_comparison.csv")
    p("The L1 script was run in a scratch copy for Saddle, Summit and NASA-E on the new L0M (new flags, source-aware HW and RH handling, HW offsets) and compared with the "
      "previous L1 hourly files of the repository (built from the C-level-based L0M). Median differences of 0 mean the two agree where both have values; `new_only` are hours "
      "the logger-first data add.", "", table(lc), "",
      "Reading: radiation, air temperature, pressure and wind agree (median 0) and gain hours from the CR10X files. RH differs at Saddle (raw logger vs C-level converted back, see section 5). "
      "HW agrees in the years with a resolved offset; the swap-candidate years and `HS_combined` differ (section 5).", "")
p("**C-level statistics columns.** The `_max`, `_min` and `_stdev` columns of the C-level files are not read any more: their labels are wrong (a `VW1_max` ranging from -81 to 34 is a temperature; "
  "only 50-70% of the 'maxima' are >= the mean), so filling L0M from them (590,000 hours of `VW1_max` alone) would put wrong values into these columns. L1 drops these columns anyway.", "")
p("**Petermann Glacier 2002** (the case of an uncalibrated C-level file): the C-level ISWR in mid-2002 is about 300 W/m2 where the logger reaches 800 (see the radiation origin plot). The logger-to-C-level "
  "comparison for `2004_PET.DAT` has r = 0.80 and is classified `poor_overlap`, so the C-level factor is NOT copied; the station-level factor (186.5, from the 2006 file where the C-level is calibrated, "
  "r = 0.97) is used. Its accuracy (a few percent) rests on that one file.", "")

# --- open
p("## 10. Open points", "",
  "- HW swap candidates (`hw_swap_candidates.csv`) and the resulting HS_combined shifts: which sensor is HW1 needs your decision per station; HW columns holding TS data are listed in section 5.",
  "- Timestamp offsets (section 6): confirm the sign convention, then add `time_shift` rows for NASA-E 2006-07 and NEEM 2007.",
  "- The Jason C-file is ignored at stations without a CR1000 folder that have no CR10X registry (KULU, Larsen C).",
  "- Swiss Camp 10m has no C-file; its CR10X data are read as before.",
  "- Raw radiation in L0M (calibration in L1) was not done; see the deviation note in section 4.", "")

open(OUT + "/report.md", "w", encoding="utf-8").write("\n\n".join(md) + "\n")
print("wrote", OUT + "/report.md")

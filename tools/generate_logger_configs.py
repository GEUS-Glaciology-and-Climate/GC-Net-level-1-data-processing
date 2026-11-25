# -*- coding: utf-8 -*-
"""Generates the per-raw-file .toml configs (logger type, column header, calibration, and for CR10X the runs)
from the existing sources: CR10X_layouts.csv / CR10X_calibration.csv / CR10X_calibration_by_file.csv /
CR10X_file_registry.csv for CR10X, and each station's <site>_header.ini for CR1000.

Nothing is hand-authored: this is a faithful re-expression of what is already validated in those sources. One
.toml is written next to each raw file (CR1000: one per yearly Table046/048/050 file, identical content per
station; CR10X: one per registered file, possibly with several [[array]] blocks - a file can interleave several
output tables, e.g. met + snow temperature - each with its own runs).

Schema (see metadata/logger_first/README.md for the worked example):
  logger_type = "CR10X" | "CR1000" | "CR7"
  [[array]]                      # CR10X only; a CR1000/embedded-year file has exactly one implicit array
    id, ncols, column_header
    [[array.run]]                # omitted (whole file = one run) for an embedded-year file
      row_from, row_to
      start_year                 # OPTIONAL from the 2nd run on (see below)

start_year default: a day-of-year rollover (day wraps from ~365 back to ~1) always means the next calendar year --
that is hardcoded in the reader, not stored. The first run of an array always states start_year (the anchor); a
later run only repeats it when the true year does NOT simply follow from counting rollovers since that anchor
(checked empirically 2026-09: 55 of 97 multi-run cases in the current registry follow the rollover default and
need no override; 42 do not -- a stuck logger clock or an overlapping/restarted cumulative download can leave the
year unchanged or even going backwards across a run boundary, e.g. NASA-E 2011_nasae1.dat stays at 2005 across a
discontinuity where rollover-counting alone would predict 2008). This generator writes start_year on a run only
when it differs from that default, so the common case is implicit.

Usage (repository root): python tools/generate_logger_configs.py <station numbers...> [--write]
Without --write, prints what would be generated (a dry run) rather than creating any file.
"""
import os
import sys
import glob
import warnings
warnings.simplefilter("ignore")
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import liblogger as ll
from lib import write_nead
INI = "L0/L0_ini/"


def _toml_str_list(xs):
    return "[" + ", ".join('"' + x.replace('"', '\\"') + '"' for x in xs) + "]"


def _fmt_num(x):
    if float(x) == int(x):
        return str(int(x))
    return repr(float(x))


def write_toml(path, lines, dry_run):
    import time
    text = "\n".join(lines) + "\n"
    if dry_run:
        print(f"--- {path} ---\n{text}")
        return
    for attempt in range(20):
        try:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
            return
        except OSError:
            time.sleep(1.5)
    raise OSError("could not write " + path)


# ---------------------------------------------------------------------------------------------- CR10X
def cr10x_configs(site, stn_dir, dry_run):
    reg = pd.read_csv(INI + "CR10X_file_registry.csv", skipinitialspace=True)
    reg = reg[(reg.site == site) & (reg.use == 1)]
    if len(reg) == 0:
        return 0
    layouts = pd.read_csv(INI + "CR10X_layouts.csv", skipinitialspace=True).set_index("layout")
    cal = pd.read_csv(INI + "CR10X_calibration.csv", skipinitialspace=True)
    cal = cal[cal.site == site].set_index("var")
    cal_file = pd.DataFrame(columns=["site", "file", "var", "scale_pos", "scale_neg", "add", "source"])
    if os.path.isfile(INI + "CR10X_calibration_by_file.csv"):
        cf = pd.read_csv(INI + "CR10X_calibration_by_file.csv", skipinitialspace=True)
        cal_file = cf[cf.site == site]

    n = 0
    for fname, g in reg.groupby("file"):
        lines = ['logger_type = "CR10X"', ""]
        # group by (array id, ncols, layout): the SAME array id can carry a DIFFERENT column layout across runs of
        # one file (the logger program was changed), so a layout change must start a new [[array]] block, not be
        # silently folded into the first run's column names.
        # Groups are emitted in the ORIGINAL registry row order (not sorted by array id): when the same variable is
        # genuinely present in two different arrays of one file (a redundant/duplicate reading), array order decides
        # which one wins on a tie, and that has to match the already-validated CR10X_file_registry.csv row order,
        # not an arbitrary new one. Each group's OWN runs are still ordered by row_from.
        for (array_id, ncols, layout), arr in g.groupby(["array", "ncols", "layout"], sort=False):
            arr = arr.sort_values("row_from")
            row0 = arr.iloc[0]
            var_list = layouts.loc[row0["layout"], "var_list"].split(",")
            lines.append("[[array]]")
            lines.append(f"id = {int(array_id)}")
            lines.append(f"ncols = {int(ncols)}")
            lines.append(f"column_header = {_toml_str_list(var_list)}")
            # the default year at each row: this layout-subgroup's own first run's start_year, +1 at every real DOY
            # rollover from that run's row_from onward (hardcoded in the reader); a later run of the SAME layout
            # only needs an explicit start_year when it deviates from that. Anchored at row_from, not at row 0 of
            # the whole array: the same array id can carry an earlier run under a DIFFERENT layout (a logger
            # reprogram), and that earlier run's dating is irrelevant to this one.
            naive = None
            try:
                path = f"L0/{stn_dir}/CR10X logger files/{fname}"
                a, n_t, has_year = ll.group_array(path, int(array_id), int(ncols))
                if not has_year:
                    doy = a[:, 1]
                    row_from0 = int(row0["row_from"])
                    naive = np.zeros(len(doy), dtype=int)
                    naive[row_from0:] = int(row0["start_year"])
                    for k in np.where((doy[:-1] > 300) & (doy[1:] < 60))[0] + 1:
                        if k >= row_from0:
                            naive[k:] += 1
            except Exception:
                pass
            for i, (_, r) in enumerate(arr.iterrows()):
                lines.append("[[array.run]]")
                lines.append(f"row_from = {int(r['row_from'])}")
                lines.append(f"row_to = {int(r['row_to'])}")
                rf = int(r["row_from"])
                default_year = int(naive[rf]) if (naive is not None and rf < len(naive)) else None
                if i == 0 or default_year != int(r["start_year"]):
                    lines.append(f"start_year = {int(r['start_year'])}")
                if isinstance(r.get("note"), str) and r["note"]:
                    lines.append('note = "' + r["note"].replace('"', "'") + '"')
            lines.append("")
        # calibration: the per-file override table takes priority over the station-level one, variable by variable
        cvars = sorted({*cal.index, *cal_file.loc[cal_file.file == fname, "var"]})
        for var in cvars:
            over = cal_file[(cal_file.file == fname) & (cal_file["var"] == var)]
            if len(over):
                row = over.iloc[0]
            elif var in cal.index:
                row = cal.loc[var]
            else:
                continue
            lines.append(f"[calibration.{var}]")
            if "scale_pos" in row.index and pd.notna(row.get("scale_pos")):
                lines.append(f"scale_pos = {_fmt_num(row['scale_pos'])}")
                lines.append(f"scale_neg = {_fmt_num(row['scale_neg'])}")
            elif "scale" in row.index and pd.notna(row.get("scale")):
                lines.append(f"scale = {_fmt_num(row['scale'])}")
            lines.append(f"add = {_fmt_num(row.get('add', 0))}")
            src = row.get("source")
            if isinstance(src, str) and src:
                lines.append('source = "' + src.replace('"', "'") + '"')
            lines.append("")
        path = f"L0/{stn_dir}/CR10X logger files/{fname}.toml"
        write_toml(path, lines, dry_run)
        n += 1
    return n


# ---------------------------------------------------------------------------------------------- Swiss Camp 10 m
def sc10m_configs(site, stn_dir, dry_run):
    """Swiss Camp 10 m's CR10X files: a year-embedded format (array id, year, day_of_year, hour, ...) described by
    L0/L0_ini/CR10X_all_station.ini, historically read by liblogger.read_swisscamp10m_cr10x. Every file shares the
    same logger id, column layout and (one flat, station-wide, non-per-file) calibration."""
    d = f"L0/{stn_dir}/CR10X logger files/"
    if site != "Swiss Camp 10m" or not os.path.isdir(d):
        return 0
    info = pd.read_csv(INI + "CR10X_all_station.ini", skipinitialspace=True)
    info = info.loc[info.site == site]
    if len(info) == 0:
        return 0
    row = info.iloc[0]
    var_list = [v.strip() for v in row["var_list"].split(",")]
    time_cols, data_cols = var_list[1:4], var_list[4:]
    assert time_cols == ["year", "day_of_year", "hour"], time_cols
    ncols = 1 + len(time_cols) + len(data_cols)
    # the numeric array id (constant across files, verified 2026-09) is the first raw column's own value, not a name
    sample_file = sorted(f for f in os.listdir(d) if not f.startswith("."))[0]
    with open(d + sample_file) as fh:
        array_id = int(float(fh.readline().split(",")[0]))

    lines = ['logger_type = "CR10X"', "", "[[array]]", f"id = {array_id}",
             f"ncols = {ncols}", f"column_header = {_toml_str_list(data_cols)}", ""]
    for var, val, sign in (("ISWR", row["calib_ISWR"], None), ("OSWR", row["calib_OSWR"], None)):
        lines += [f"[calibration.{var}]", f"scale = {_fmt_num(val)}", "add = 0", ""]
    lines += ["[calibration.NR]", f"scale_pos = {_fmt_num(row['calib_NR_pos'])}", f"scale_neg = {_fmt_num(row['calib_NR_neg'])}", "add = 0", ""]

    n = 0
    for f in sorted(os.listdir(d)):
        if f.endswith(".toml") or f.startswith(".") or os.path.isdir(d + f):
            continue
        write_toml(d + f + ".toml", lines, dry_run)
        n += 1
    return n


# ---------------------------------------------------------------------------------------------- CR1000
def cr1000_configs(site, stn_dir, dry_run):
    d = f"L0/{stn_dir}/CR1000 logger files/"
    if not os.path.isdir(d):
        return 0
    cfg = INI + stn_dir + "_header.ini"
    fields = write_nead.get_config_list_str(cfg, "fields")
    add_value = write_nead.get_config_list(cfg, "add_value")
    scale = write_nead.get_config_list(cfg, "scale_factor")
    try:
        scale_neg = write_nead.get_config_list(cfg, "scale_factor_neg")
    except Exception:
        scale_neg = scale
    lines = ['logger_type = "CR1000"', "", f"column_header = {_toml_str_list(fields)}", ""]
    for i, var in enumerate(fields):
        if var == "timestamp":
            continue
        a, sp, sn = float(add_value[i]), float(scale[i]), float(scale_neg[i])
        if a == 0 and sp == 1 and sn == 1:
            continue   # already physical: no calibration table needed for this column
        lines.append(f"[calibration.{var}]")
        if sp != sn:
            lines.append(f"scale_pos = {_fmt_num(sp)}")
            lines.append(f"scale_neg = {_fmt_num(sn)}")
        else:
            lines.append(f"scale = {_fmt_num(sp)}")
        lines.append(f"add = {_fmt_num(a)}")
        lines.append("")
    n = 0
    for f in sorted(os.listdir(d)):
        if f.endswith(".toml") or f.startswith(".") or os.path.isdir(d + f):
            continue
        if "Table046" not in f:
            # an ARGOS station's Table048/Table050 sibling of the same year: libgcnet.read_cr1000_tables joins it
            # onto its Table046 file automatically (same rule as the old read_cr1000_files' file selection); giving
            # it its own config would read it a second time, standalone and incomplete
            continue
        write_toml(d + f + ".toml", lines, dry_run)
        n += 1
    return n


def main(nums, dry_run):
    for stn_dir in sorted(x for x in os.listdir("L0") if x[:2].isdigit() and (not nums or x[:2] in nums)):
        site = stn_dir[3:]
        n1 = sc10m_configs(site, stn_dir, dry_run) if site == "Swiss Camp 10m" else cr10x_configs(site, stn_dir, dry_run)
        n2 = cr1000_configs(site, stn_dir, dry_run)
        if n1 or n2:
            print(f"{stn_dir}: {n1} CR10X configs, {n2} CR1000 configs" + (" (dry run)" if dry_run else ""))


if __name__ == "__main__":
    args = sys.argv[1:]
    main([a for a in args if not a.startswith("--")], "--write" not in args)

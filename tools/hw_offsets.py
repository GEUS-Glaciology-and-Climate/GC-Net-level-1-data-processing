# -*- coding: utf-8 -*-
"""Constant offsets between the C-level snow height (HW1, HW2) and the raw CR10X logger distance.

liblogger.yearly_diagnostics (metadata/logger_first/c_level_treatment_by_year.csv) finds, per logger file and year, which of
  logger x sonic factor / raw logger / the other sensor
reproduces the C-level HW and what constant separates them (C-level = candidate + offset). Where the fit is tight
(spread <= 0.02 m; the same sensor, with or without the sonic factor) the offset is the installation height constant that the
C-level processing added to the sonic-ranger distance. The raw logger values do not have it, so it is written as L1
adjustments (function add_cr10x: applied only to hours that come from a CR10X file, after the sonic correction):

  t0,t1,HW1,add_cr10x,<offset>,logger-first: C-level HW offset ...

Years where the C-level HW1/HW2 matches the OTHER sensor, or has no tight fit, get no row unless the offset is the same in the
years before and after (then it is filled); they are listed in the table, for review.
Consecutive years with the same offset (+-0.02 m) are merged. Rows of an earlier run are replaced (append-only text edit).

Usage (repository root): python tools/hw_offsets.py [--write]
Output: metadata/logger_first/hw_offsets_by_year.csv (all years, with the reason a year has no row) and
        metadata/logger_first/hw_swap_candidates.csv (file-years where the C-level HW is the other sensor's reading)
"""
import os
import sys
import warnings
warnings.simplefilter("ignore")
import numpy as np
import pandas as pd

M = "metadata/logger_first/"
TAG = "logger-first: C-level HW offset"
SPREAD_MAX = 0.02

def write_bytes(path, data, tries=10):
    """the folder is synced/scanned by other programs; a write can fail briefly with 'Invalid argument'"""
    import time
    for k in range(tries):
        try:
            with open(path, "wb") as f:
                f.write(data)
            return
        except OSError:
            time.sleep(1.5)
    raise OSError("could not write " + path)



def main(write):
    t = pd.read_csv(M + "c_level_treatment_by_year.csv")
    t = t[t.test == "HW correction/swap"].copy()
    t["spread_best"] = t[["same_raw", "same_sonic", "other_raw", "other_sonic"]].min(axis=1)
    rows = []
    for (site, var, year), g in t[t.file != "CR1000"].groupby(["site", "variable", "year"]):
        g = g[g.best.isin(["same_sonic", "same_raw"]) & (g.spread_best <= SPREAD_MAX)]
        allg = t[(t.site == site) & (t.variable == var) & (t.year == year) & (t.file != "CR1000")]
        if len(g) == 0:
            why = "C-level matches the other sensor" if allg.best.astype(str).str.startswith("other").any() else "no tight fit"
            rows.append(dict(site=site, variable=var, year=int(year), offset=np.nan, hours=int(allg.hours.sum()), reason=why))
            continue
        if g.offset_c_minus_best.max() - g.offset_c_minus_best.min() > 0.05:
            rows.append(dict(site=site, variable=var, year=int(year), offset=np.nan, hours=int(allg.hours.sum()),
                             reason="the offset changes within the year (sensor reinstalled?)"))
            continue
        off = float(np.average(g.offset_c_minus_best, weights=g.hours))
        rows.append(dict(site=site, variable=var, year=int(year), offset=round(off, 3), hours=int(g.hours.sum()),
                         reason="same sensor, " + ("sonic-corrected" if (g.best == "same_sonic").any() else "raw")))
    # C-level HW1 (HW2) reproduces the logger's OTHER sensor column within 0.02 m: the C-level file swapped or gap-filled the
    # sensors, or the logger columns are named the other way round in that file. Not decided here: listed for review.
    sw = t[t.best.astype(str).str.startswith("other") & (t.spread_best <= SPREAD_MAX)]
    sw[["site", "variable", "file", "year", "hours", "best", "offset_c_minus_best", "same_raw", "same_sonic", "other_raw", "other_sonic"]]         .to_csv(M + "hw_swap_candidates.csv", index=False)
    print(len(sw), "file-years where the C-level HW matches the other sensor (metadata/logger_first/hw_swap_candidates.csv)")
    d = pd.DataFrame(rows).sort_values(["site", "variable", "year"]).reset_index(drop=True)
    # a year without an offset between two years with the same offset (+-0.02 m, at most 3 years apart) is the same installation
    for (site, var), g in d.groupby(["site", "variable"]):
        known = g[g.offset.notna()]
        for i in g.index[g.offset.isna()]:
            before = known[known.year < d.at[i, "year"]].tail(1)
            after = known[known.year > d.at[i, "year"]].head(1)
            if len(before) and len(after) and abs(before.offset.iloc[0] - after.offset.iloc[0]) <= 0.02                     and after.year.iloc[0] - before.year.iloc[0] <= 4:
                d.at[i, "offset"] = round((before.offset.iloc[0] + after.offset.iloc[0]) / 2, 3)
                d.at[i, "reason"] = "filled: the same offset before and after (" + d.at[i, "reason"] + ")"
    d.to_csv(M + "hw_offsets_by_year.csv", index=False)
    print(d.groupby("reason").size())
    out = []
    for (site, var), g in d[d.offset.notna()].groupby(["site", "variable"]):
        cur = None
        for r in g.itertuples():
            if cur is not None and abs(r.offset - cur["off"]) <= 0.02 and r.year <= cur["y1"] + 1:
                cur["y1"] = r.year
                cur["w"].append((r.offset, r.hours))
            else:
                if cur is not None:
                    out.append(cur)
                cur = dict(site=site, var=var, y0=r.year, y1=r.year, off=r.offset, w=[(r.offset, r.hours)])
        if cur is not None:
            out.append(cur)
    for c in out:
        c["off"] = round(float(np.average([o for o, _ in c["w"]], weights=[h for _, h in c["w"]])), 3)
    print(len(out), "adjustment rows for", len({c["site"] for c in out}), "sites")
    if not write:
        return
    for site in sorted({c["site"] for c in out}):
        path = f"metadata/adjustments/{site}.csv"
        raw = open(path, "rb").read().decode("utf-8") if os.path.isfile(path) else "t0,t1,variable,adjust_function,adjust_value,comment\n"
        eol = "\r\n" if "\r\n" in raw else "\n"
        keep = [l for l in raw.splitlines() if TAG not in l]
        while keep and keep[-1].strip() == "":
            keep.pop()
        lines = [f"{c['y0']}-01-01T00:00:00+00:00,{c['y1']}-12-31T23:00:00+00:00,{c['var']},add_cr10x,{c['off']},{TAG} ({c['y0']}-{c['y1']}; C-level = raw logger x sonic + offset)"
                 for c in out if c["site"] == site]
        write_bytes(path, (eol.join(keep + lines) + eol).encode("utf-8"))
        print("  wrote", path, len(lines), "rows")


if __name__ == "__main__":
    main("--write" in sys.argv)

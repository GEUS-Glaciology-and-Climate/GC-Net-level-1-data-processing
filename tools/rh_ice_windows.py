# -*- coding: utf-8 -*-
"""In which years is the C-level RH with respect to ice, and does an `ice_to_water` adjustment cover those years?

From metadata/logger_first/c_level_treatment_by_year.csv (test "RH ice/water": per logger file and year, is the C-level RH
the same as the raw logger RH (wrt water) or the logger RH converted to ice and clipped at 100%?) this tool builds
metadata/logger_first/rh_convention_by_year.csv: per site, RH sensor and year the convention of the C-level file, whether an
existing `ice_to_water` row of metadata/adjustments/<site>.csv covers the year, and what is missing.

With --write, `ice_to_water` rows are appended to metadata/adjustments/<site>.csv for the years where the C-level RH is wrt ice
and no row covers them. At L1 `ice_to_water` acts only on hours that come from a C-level file (PROMICE_toolbox._clevel_only),
so logger values are never converted; the rows exist for the C-level gap-fills. Years where an existing row converts C-level RH
that is already wrt water ("same") are listed in the table (not changed): they only concern hours filled from the C-level file.

Usage (repository root): python tools/rh_ice_windows.py [--write]
"""
import os
import sys
import warnings
warnings.simplefilter("ignore")
import numpy as np
import pandas as pd

M = "metadata/logger_first/"
TAG = "logger-first: C-level RH is wrt ice"

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



def covered_years(site, var):
    path = f"metadata/adjustments/{site}.csv"
    if not os.path.isfile(path):
        return set()
    a = pd.read_csv(path, comment="#", skipinitialspace=True)
    a = a[(a.variable == var) & (a.adjust_function == "ice_to_water")]
    yrs = set()
    for r in a.itertuples():
        t0 = pd.to_datetime(r.t0, utc=True, errors="coerce")
        t1 = pd.to_datetime(r.t1, utc=True, errors="coerce")
        y0 = 1990 if pd.isna(t0) else t0.year
        y1 = 2030 if pd.isna(t1) else t1.year
        yrs |= set(range(y0, y1 + 1))
    return yrs


def main(write):
    t = pd.read_csv(M + "c_level_treatment_by_year.csv")
    t = t[t.test == "RH ice/water"]
    rows = []
    for (site, var, year), g in t.groupby(["site", "variable", "year"]):
        w = g.groupby("verdict").hours.sum()
        verdict = w.idxmax()
        rows.append(dict(site=site, variable=var, year=int(year), c_level_convention=verdict, hours=int(w.sum()),
                         covered_by_ice_to_water=int(year) in covered_years(site, var)))
    d = pd.DataFrame(rows)
    d["action"] = ""
    d.loc[(d.c_level_convention == "wrt ice") & ~d.covered_by_ice_to_water, "action"] = "add ice_to_water"
    d.loc[(d.c_level_convention == "same (wrt water)") & d.covered_by_ice_to_water, "action"] = "existing row converts C-level RH that is already wrt water (check)"
    d.to_csv(M + "rh_convention_by_year.csv", index=False)
    print(d.groupby(["c_level_convention", "covered_by_ice_to_water"]).size())
    add = d[d.action == "add ice_to_water"]
    out = []
    for (site, var), g in add.groupby(["site", "variable"]):
        y0 = prev = None
        for y in sorted(g.year):
            if y0 is None:
                y0 = prev = y
            elif y == prev + 1:
                prev = y
            else:
                out.append((site, var, y0, prev))
                y0 = prev = y
        out.append((site, var, y0, prev))
    print(len(out), "rows to add")
    if not write:
        return
    for site in sorted({o[0] for o in out}):
        path = f"metadata/adjustments/{site}.csv"
        raw = open(path, "rb").read().decode("utf-8")
        eol = "\r\n" if "\r\n" in raw else "\n"
        keep = [l for l in raw.splitlines() if TAG not in l]
        while keep and keep[-1].strip() == "":
            keep.pop()
        lines = [f"{y0}-01-01T00:00:00+00:00,{y1}-12-31T23:00:00+00:00,{var},ice_to_water,0,{TAG} in {y0}-{y1} (only C-level-sourced hours are converted)"
                 for s_, var, y0, y1 in out if s_ == site]
        write_bytes(path, (eol.join(keep + lines) + eol).encode("utf-8"))
        print("  wrote", path, len(lines), "rows")


if __name__ == "__main__":
    main("--write" in sys.argv)

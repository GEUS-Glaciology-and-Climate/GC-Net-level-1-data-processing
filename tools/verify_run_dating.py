# -*- coding: utf-8 -*-
"""Re-checks the start year of every registered CR10X run (the whole pre-CR1000 era) against the C-level
file, using the same detrended-daily-temperature correlation as the decoder (cr10x_decode.date_run), and
flags any run where the registered year is not the best-supported one.

Why this is needed: CR10X_file_registry.csv was built by an earlier run of `cr10x_decode.py decode` +
`registry`, and has not been regenerated since later fixes to the decoder. It can go stale in a way the
column-verification pass (`cr10x_decode.py verify`) cannot catch: a wrong start year still produces
plausible-looking, well-correlated columns for the years that DO overlap the C-level record, so `verify`
keeps the run. Found this way in Petermann Glacier's `2006_PET_Camp.dat` (registered 2001, later corrected to
2002 by hand: r=undefined / no C-level overlap at 2001 vs r=0.9999 (n=2636 h) at 2002).

For every run this reports the registered year's correlation score side by side with the best year found (and
its score); a mismatch with a much higher best-year score is a likely dating bug. Nothing is changed
automatically here (only the report is written); apply a correction to L0/L0_ini/CR10X_file_registry.csv
by hand, the way the Petermann Glacier row was fixed, after checking the run's own C-level overlap window
supports the change.

Usage (repository root): python tools/verify_run_dating.py [station numbers...]
Output: metadata/logger_first/dating_reverification.csv
"""
import os
import sys
import warnings
warnings.simplefilter("ignore")
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import liblogger as ll
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cr10x_decode import load_clevel, clevel_anom, date_run, temp_columns, YEARS

M = "metadata/logger_first/"


def score_at_year(vals, doy, hhmm, anom, y0):
    """the same correlation date_run() computes, but pinned to one candidate year (registered_start_year)"""
    cols = temp_columns(np.where(vals == -6999, np.nan, vals))
    if not cols:
        return np.nan
    ts = ll.run_dates(doy, hhmm, y0)
    if ts.min() > anom.index.max() or ts.max() < anom.index.min():
        return np.nan
    dm = pd.DataFrame(vals[:, cols], index=ts).replace(-6999, np.nan).resample("D").mean()
    dm = dm - dm.rolling(15, center=True, min_periods=5).mean()
    j = dm.join(anom, how="inner")
    if len(j) < 20:
        return np.nan
    best = np.nan
    for c in range(len(cols)):
        for r in anom.columns:
            m = j[c].notna() & j[r].notna()
            if m.sum() >= 20 and j.loc[m, c].std() > 0:
                s = float(np.corrcoef(j.loc[m, c], j.loc[m, r])[0, 1])
                if np.isnan(best) or s > best:
                    best = s
    return best


def main(nums):
    reg = pd.read_csv("L0/L0_ini/CR10X_file_registry.csv", skipinitialspace=True)
    reg = reg[reg.use == 1]
    rows = []
    for stn in sorted(d for d in os.listdir("L0") if d[:2].isdigit() and (not nums or d[:2] in nums)):
        r0 = reg[reg.site == stn[3:]]
        if len(r0) == 0 or not os.path.isfile(f"L0/{stn}/C file/{stn[:2]}c.dat"):
            continue
        print("re-checking", stn, "-", len(r0), "runs", flush=True)
        cl = load_clevel(stn)
        anom = clevel_anom(cl)
        cache = {}
        for _, r in r0.iterrows():
            path = f"L0/{stn}/CR10X logger files/{r['file']}"
            key = (r["file"], int(r["array"]), int(r["ncols"]))
            if key not in cache:
                try:
                    cache[key] = ll.group_array(path, int(r["array"]), int(r["ncols"]))
                except Exception as e:
                    cache[key] = e
            a = cache[key]
            if isinstance(a, Exception):
                rows.append(dict(site=stn[3:], file=r["file"], array=r["array"], row_from=r["row_from"], row_to=r["row_to"],
                                 registered_year=r["start_year"], status=f"read failed: {a!r}"))
                continue
            a, n_t, has_year = a
            if has_year:
                continue   # dated from the file's own year column, not by correlation
            seg = a[int(r["row_from"]): int(r["row_to"]) + 1]
            vals = seg[:, n_t:]
            reg_year = int(r["start_year"])
            reg_score = score_at_year(vals, seg[:, 1], seg[:, 2], anom, reg_year)
            best_year, best_score = date_run(vals, seg[:, 1], seg[:, 2], anom, reg_year)
            mismatch = best_year != reg_year and best_score > (0 if np.isnan(reg_score) else reg_score) + 0.15
            rows.append(dict(site=stn[3:], file=r["file"], array=int(r["array"]), row_from=int(r["row_from"]), row_to=int(r["row_to"]),
                             hours=int(r["row_to"]) - int(r["row_from"]) + 1, registered_year=reg_year,
                             registered_year_score=round(reg_score, 4) if reg_score == reg_score else np.nan,
                             best_year=best_year, best_year_score=round(best_score, 4) if best_score == best_score else np.nan,
                             mismatch=mismatch, status="checked"))
    d = pd.DataFrame(rows)
    os.makedirs(M, exist_ok=True)
    out = M + "dating_reverification.csv"
    if nums and os.path.isfile(out):
        old = pd.read_csv(out)
        d = pd.concat([old[~old.site.isin(d.site.unique())], d], ignore_index=True)
    d.to_csv(out, index=False)
    bad = d[d.mismatch == True] if "mismatch" in d.columns else pd.DataFrame()
    print(f"\n{len(d)} runs checked, {len(bad)} flagged as likely mis-dated")
    if len(bad):
        print(bad[["site", "file", "row_from", "row_to", "hours", "registered_year", "registered_year_score", "best_year", "best_year_score"]]
              .to_string(index=False))


if __name__ == "__main__":
    main(sys.argv[1:])

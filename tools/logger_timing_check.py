# -*- coding: utf-8 -*-
"""How well do the logger hours line up with the C-level hours?

For every registered CR10X run, the variables that the C-level processing copied verbatim
(air temperatures, subsurface temperatures, wind direction, battery voltage) are compared with the
C-level file at shifts of -2 ... +2 hours. The share of hours that are identical (within 0.011) is
computed per year, per shift. A clean series peaks at 0 h; a peak at +1 h means the C-level file
carries the logger record one hour later than the logger stamped it (or the reverse for -1 h).
The logger stamps are not changed anywhere: an hour offset is a candidate for an L1 time_shift and
needs an independent check (CARRA ssrd against ISWR, see the network review report).

Usage (repository root): python tools/logger_timing_check.py 10 11 ...   (station numbers; default all)
Output: metadata/logger_first/timing_check.csv
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
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cr10x_decode import load_clevel, EXACT_REFS

SHIFTS = (-2, -1, 0, 1, 2)


def main(nums):
    reg = pd.read_csv("L0/L0_ini/CR10X_file_registry.csv", skipinitialspace=True)
    layouts = pd.read_csv("L0/L0_ini/CR10X_layouts.csv", skipinitialspace=True).set_index("layout")
    rows = []
    stations = sorted(d for d in os.listdir("L0") if d[:2].isdigit() and (not nums or d[:2] in nums))
    for stn in stations:
        r0 = reg[reg.site == stn[3:]]
        if len(r0) == 0 or not os.path.isfile(f"L0/{stn}/C file/{stn[:2]}c.dat"):
            continue
        cl = load_clevel(stn)
        print("timing check", stn, flush=True)
        for _, r in r0.iterrows():
            path = f"L0/{stn}/CR10X logger files/{r['file']}"
            a, n_t, has_year = ll.group_array(path, int(r["array"]), int(r["ncols"]))
            seg = a[int(r["row_from"]): int(r["row_to"]) + 1]
            var_list = layouts.loc[r["layout"], "var_list"].split(",")
            if has_year:
                ts = pd.DatetimeIndex((pd.to_datetime(pd.Series(seg[:, 1].astype(int)), format="%Y") + pd.to_timedelta(seg[:, 2] - 1, unit="D")
                                       + pd.to_timedelta((seg[:, 3] // 100) * 60 + seg[:, 3] % 100, unit="min")).values, tz="UTC")
            else:
                ts = ll.run_dates(seg[:, 1], seg[:, 2], int(r["start_year"]))
            df, step = ll.hourly_frame(seg[:, n_t:], ts, var_list)
            use = [c for c in df.columns if c in EXACT_REFS and c in cl.columns]
            for sh in SHIFTS:
                d = df[use].set_axis(df.index + pd.Timedelta(hours=sh))
                j = d.join(cl[use].add_suffix("_C"), how="inner")
                for v in use:
                    m = j[v].notna() & j[v + "_C"].notna()
                    if m.sum() == 0:
                        continue
                    eq = ((j.loc[m, v] - j.loc[m, v + "_C"]).abs() < (0.03 if v in ("TA3", "TA4") else 0.011))
                    g = eq.groupby(eq.index.year).agg(["sum", "size"])
                    for y, (s, n) in g.iterrows():
                        rows.append(dict(station=stn, file=r["file"], year=int(y), shift_h=sh, variable=v, equal=int(s), n=int(n)))
    d = pd.DataFrame(rows)
    if len(d) == 0:
        return
    g = d.groupby(["station", "year", "shift_h"])[["equal", "n"]].sum().reset_index()
    g["share_equal"] = g.equal / g.n
    piv = g.pivot_table(index=["station", "year"], columns="shift_h", values="share_equal").reset_index()
    piv["n_compared"] = g.groupby(["station", "year"]).n.max().values
    piv["best_shift_h"] = piv[list(SHIFTS)].idxmax(axis=1)
    piv["best_share"] = piv[list(SHIFTS)].max(axis=1)
    piv["share_at_0h"] = piv[0]
    os.makedirs("metadata/logger_first", exist_ok=True)
    prev = "metadata/logger_first/timing_check.csv"
    if os.path.isfile(prev) and nums:
        old = pd.read_csv(prev)
        piv.columns = [str(c) for c in piv.columns]
        old = old[~old.station.isin(piv.station.unique())]
        piv = pd.concat([old, piv], ignore_index=True)
    piv.columns = [str(c) for c in piv.columns]
    piv.round(3).to_csv(prev, index=False)
    print(piv.shape)


if __name__ == "__main__":
    main(sys.argv[1:])

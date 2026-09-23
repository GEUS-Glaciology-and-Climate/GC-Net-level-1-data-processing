# -*- coding: utf-8 -*-
"""Was the C-level radiation calibrated like the documentation says? One row per logger file (registry run) and variable.

For every registered CR10X run the raw radiation columns (ISWR, OSWR, NR) are compared with the C-level file at the
timing shift (-2..+2 h) where they correlate best. The through-origin slope is the factor the C-level processing
applied to the raw logger value. It is compared with the documented station factor (the scale_factor lines of
L0/L0_ini/<station>_header.ini, positive and negative NR factors separately):

  documented          the C-level factor is within 3% of the documented one: same calibration
  differs             a plausible sensitivity that is not the documented one (a different radiometer or an
                      updated calibration was used in the C-level file)
  c_level_uncalibrated  the implied factor is ~1 (or far below any radiometer sensitivity): the C-level file holds
                      raw logger units for that period, so it must not be used as a reference for the calibration
  physical_units      C-level / logger ~ 1: the logger file itself is already in W/m2 (factor ~1, not the station factor)
  poor_overlap        r < 0.9 or too few hours: no conclusion

Output: metadata/logger_first/calibration_by_file.csv, and with --write the factors to use per file in
L0/L0_ini/CR10X_calibration_by_file.csv (read by liblogger.read_station_cr10x, overriding the station-level
CR10X_calibration.csv for that file and variable):
  documented  -> the documented factor;   differs -> the factor the C-level processing applied (its median ratio to the
  raw value when that is stable, else the implied slope). A file where the C-level factor cannot be established
  (c_level_uncalibrated, poor_overlap) gets no row and keeps the station-level factor. NR needs both signs.
Why reuse a C-level factor that differs from the documented one: at Saddle, CP1, DYE-2, ... the C-level OSWR factor is
186.8 where the header says 200; with 200 the median albedo is ~0.90, with 186.8 ~0.84 (dry snow), so the C-level factor
is the individually calibrated one.

Usage (repository root): python tools/cr10x_calibration_by_file.py [station numbers...] [--write]
"""
import os
import sys
import warnings
warnings.simplefilter("ignore")
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import liblogger as ll
from lib import write_nead
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cr10x_decode import load_clevel

SHIFTS = (-2, -1, 0, 1, 2)
PLAUSIBLE = {"ISWR": (40, 450), "OSWR": (40, 450), "NR>0": (3, 150), "NR<0": (3, 150)}


def documented(stn):
    """documented factors from the station header: {ISWR, OSWR, NR>0, NR<0} (NaN when absent)"""
    cfg = f"L0/L0_ini/{stn}_header.ini"
    out = dict.fromkeys(PLAUSIBLE, np.nan)
    if not os.path.isfile(cfg):
        return out
    try:
        fields = write_nead.get_config_list_str(cfg, "fields")
        pos = write_nead.get_config_list_str(cfg, "scale_factor")
        try:
            neg = write_nead.get_config_list_str(cfg, "scale_factor_neg")
        except Exception:
            neg = pos
        for v, k in (("ISWR", "ISWR"), ("OSWR", "OSWR")):
            if k in fields:
                out[v] = float(pos[fields.index(k)])
        if "NR" in fields:
            out["NR>0"] = float(pos[fields.index("NR")])
            out["NR<0"] = float(neg[fields.index("NR")])
    except Exception:
        pass
    return out


def raw_run(stn, r, layouts):
    path = f"L0/{stn}/CR10X logger files/{r['file']}"
    a, n_t, has_year = ll.group_array(path, int(r["array"]), int(r["ncols"]))
    seg = a[int(r["row_from"]): int(r["row_to"]) + 1]
    var_list = layouts.loc[r["layout"], "var_list"].split(",")
    if has_year:
        ts = pd.DatetimeIndex((pd.to_datetime(pd.Series(seg[:, 1].astype(int)), format="%Y") + pd.to_timedelta(seg[:, 2] - 1, unit="D")
                               + pd.to_timedelta((seg[:, 3] // 100) * 60 + seg[:, 3] % 100, unit="min")).values, tz="UTC")
    else:
        ts = ll.run_dates(seg[:, 1], seg[:, 2], int(r["start_year"]))
    return ll.hourly_frame(seg[:, n_t:], ts, var_list)[0]


def main(nums, write=False):
    reg = pd.read_csv("L0/L0_ini/CR10X_file_registry.csv", skipinitialspace=True)
    reg = reg[reg.use == 1]
    layouts = pd.read_csv("L0/L0_ini/CR10X_layouts.csv", skipinitialspace=True).set_index("layout")
    rows = []
    for stn in sorted(d for d in os.listdir("L0") if d[:2].isdigit() and (not nums or d[:2] in nums)):
        r0 = reg[reg.site == stn[3:]]
        if len(r0) == 0 or not os.path.isfile(f"L0/{stn}/C file/{stn[:2]}c.dat"):
            continue
        print("calibration by file", stn, flush=True)
        cl = load_clevel(stn)
        doc = documented(stn)
        for _, r in r0.iterrows():
            try:
                raw = raw_run(stn, r, layouts)
            except Exception as e:
                print("   skipped", r["file"], repr(e))
                continue
            for var, name, sel in (("ISWR", "ISWR", lambda x: x > 0), ("OSWR", "OSWR", lambda x: x > 0),
                                   ("NR", "NR>0", lambda x: x > 0), ("NR", "NR<0", lambda x: x < 0)):
                if var not in raw.columns or var not in cl.columns:
                    continue
                best = None
                for sh in SHIFTS:
                    x = raw[var].copy()
                    x.index = x.index + pd.Timedelta(hours=sh)
                    j = pd.concat([x, cl[var]], axis=1, keys=["raw", "c"]).dropna()
                    thr = 20 if var != "NR" else 15
                    j = j[sel(j.raw) & (j.c.abs() > thr) & (np.sign(j.c) == np.sign(j.raw))]
                    if len(j) < 100:
                        continue
                    rr = float(np.corrcoef(j.raw, j.c)[0, 1])
                    if best is None or rr > best[0]:
                        best = (rr, sh, len(j), float((j.raw * j.c).sum() / (j.raw ** 2).sum()), float((j.c / j.raw).median()),
                                j.index.min().year, j.index.max().year)
                if best is None:
                    rows.append(dict(site=stn[3:], file=r["file"], var=name, cls="poor_overlap"))
                    continue
                rr, sh, n, k, kmed, y0, y1 = best
                kd = doc[name]
                lo, hi = PLAUSIBLE[name]
                if rr < 0.9:
                    cls = "poor_overlap"
                elif 0.7 < k < 1.3 and name in ("ISWR", "OSWR"):
                    cls = "physical_units"        # the logger file already holds W/m2 (e.g. a file named '... calibrated')
                elif abs(k) < 3 and name in ("ISWR", "OSWR"):
                    cls = "c_level_uncalibrated"
                elif not np.isnan(kd) and abs(k / kd - 1) < 0.03:
                    cls = "documented"
                elif lo <= abs(k) <= hi:
                    cls = "differs"
                else:
                    cls = "c_level_uncalibrated"
                rows.append(dict(site=stn[3:], file=r["file"], var=name, first_year=y0, last_year=y1, hours=n, shift_h=sh, r=round(rr, 3),
                                 k_implied=round(k, 3), k_median_ratio=round(kmed, 3), k_documented=kd,
                                 ratio_implied_to_documented=round(k / kd, 3) if kd == kd and kd else np.nan, cls=cls))
    d = pd.DataFrame(rows)
    os.makedirs("metadata/logger_first", exist_ok=True)
    out = "metadata/logger_first/calibration_by_file.csv"
    if nums and os.path.isfile(out):
        old = pd.read_csv(out)
        d = pd.concat([old[~old.site.isin(d.site.unique())], d], ignore_index=True)
    d.to_csv(out, index=False)
    print(d.groupby(["var", "cls"]).size().unstack(fill_value=0))
    if write:
        write_by_file(d)


def write_by_file(d):
    rows = []
    usable = d[d.cls.isin(["documented", "differs", "physical_units"])]
    usable = usable.sort_values("hours", ascending=False).drop_duplicates(["site", "file", "var"])
    for (site, f), g in usable.groupby(["site", "file"]):
        g = g.set_index("var")

        def k(v):
            r = g.loc[v]
            if r.cls == "documented":
                return float(r.k_documented)
            if r.cls == "physical_units":
                return 1.0 if abs(r.k_implied - 1) < 0.03 else float(r.k_implied)
            return float(r.k_median_ratio) if abs(r.k_implied / r.k_median_ratio - 1) < 0.03 else float(r.k_implied)

        def src(v):
            r = g.loc[v]
            return f"{r.cls}: C-level factor over {int(r.hours)} h in {int(r.first_year)}-{int(r.last_year)} (documented {r.k_documented})"
        for v in ("ISWR", "OSWR"):
            if v in g.index:
                rows.append(dict(site=site, file=f, var=v, scale_pos=round(k(v), 3), scale_neg=round(k(v), 3), add=0.0, source=src(v)))
        if "NR>0" in g.index and "NR<0" in g.index:
            rows.append(dict(site=site, file=f, var="NR", scale_pos=round(k("NR>0"), 3), scale_neg=round(k("NR<0"), 3), add=0.0,
                             source=src("NR>0") + " / " + src("NR<0")))
    out = pd.DataFrame(rows, columns=["site", "file", "var", "scale_pos", "scale_neg", "add", "source"])
    out.to_csv("L0/L0_ini/CR10X_calibration_by_file.csv", index=False)
    print("wrote L0/L0_ini/CR10X_calibration_by_file.csv:", len(out), "rows")


if __name__ == "__main__":
    main([a for a in sys.argv[1:] if not a.startswith("--")], "--write" in sys.argv)

# -*- coding: utf-8 -*-
"""Decode the headerless CR10X logger files of the GC-Net stations and write the registry that
liblogger.py / the L0 script read.

The CR10X files carry no header and no year, and several output arrays are interleaved in one file.
For every (file, output array id, number of columns) this tool
  1. splits the rows into chronological runs (a stuck logger clock or concatenated downloads give
     several runs; short fragments are dropped),
  2. dates every run by trying the possible start years and keeping the one whose detrended daily
     temperatures correlate best with the C-level file,
  3. matches every raw column to a C-level variable: an exact copy (>90% of the hours within 0.011)
     or a linear relation (r>0.9), one-to-one (Hungarian assignment),
  4. records how the logger hours line up with the C-level hours (0, +1 or -1 h).
Then `registry` turns the decode tables into
  L0/L0_ini/CR10X_layouts.csv        layout -> variable names of the columns after the time columns
  L0/L0_ini/CR10X_file_registry.csv  file / array / rows / start year, one line per dated run

Usage (from the repository root):
  python tools/cr10x_decode.py decode 10 11 ...     # station numbers, writes out/logger_first_review/decode/NN.csv
  python tools/cr10x_decode.py registry 10 11 ...   # rebuild the registry from those stations' decode cache only
                                                     # (keeps every other station's existing rows); no numbers ->
                                                     # rebuild from every ??.csv currently cached (whole network)
Raw L0 files are only read, never written.
"""
import os
import re
import sys
import glob
import hashlib
import warnings
warnings.simplefilter("ignore")
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import libgcnet as gc
from lib import liblogger as ll
from lib import write_nead
OUT = "out/logger_first_review/decode/"
YEARS = range(1990, 2016)
EXACT_REFS = ["TA1", "TA2", "TA3", "TA4", "TA5"] + [f"TS{i}" for i in range(1, 11)] + ["DW1", "DW2", "V"]
LIN_REFS = ["ISWR", "OSWR", "NR", "VW1", "VW2", "P", "HW1", "HW2", "RH1", "RH2"]
ALL_REFS = EXACT_REFS + LIN_REFS
DERIVED = re.compile(r"clean|cal(?!c)|graf|all_cab|hour_cab|debug|_cor|1minute|work|date|profile|_dd|readme", re.I)

# standard layouts of the GC-Net programs, used only to name RH and boom-height columns that the
# C-level file cannot verify (its RH is corrected and its HW derived from snow height)
T31 = ["ISWR", "OSWR", "NR"] + [f"TS{i}" for i in range(1, 11)] + ["TA1", "TA2", "TA3", "TA4", "RH1", "RH2", "VW1", "VW2",
                                                                    "DW1", "DW2", "P", "HW1", "HW2", "_", "V"]
T17_MET = ["ISWR", "OSWR", "NR", "TA1", "TA2", "RH1", "RH2", "VW1", "VW2", "DW1", "DW2", "P", "HW1", "HW2"]
T17_MET_1VANE = ["ISWR", "OSWR", "NR", "TA1", "TA2", "RH1", "RH2", "VW1", "VW2", "DW1", "P", "HW1", "HW2", "V"]
PLAUSIBLE = {"RH1": (20, 105), "RH2": (20, 105), "HW1": (0.2, 9.5), "HW2": (0.2, 9.5)}


def load_clevel(stn_dir):
    hdr = write_nead.get_config_list_str("L0/L0_ini/c_file_header.ini", "fields")
    d = gc.read_c_file(f"L0/{stn_dir}/C file/{stn_dir[:2]}c.dat", hdr)
    d.index = pd.to_datetime(d.index, utc=True)
    return d[~d.index.duplicated(keep="first")].sort_index()


def clevel_anom(cl):
    refs = [r for r in ["TA1", "TA2", "TA3", "TA4"] if r in cl.columns]
    dm = cl[refs].resample("D").mean()
    return dm - dm.rolling(15, center=True, min_periods=5).mean()


def make_runs(doy, hhmm, min_rows=100):
    t = doy + (hhmm // 100) / 24.0
    d = np.diff(t)
    rollover = (doy[:-1] > 300) & (doy[1:] < 60) & (d < -250)
    cuts = np.r_[0, np.where((d < -0.5) & ~rollover)[0] + 1, len(doy)]
    return [(int(i), int(j) - 1) for i, j in zip(cuts[:-1], cuts[1:]) if j - i >= min_rows]


def temp_columns(vals, k=6):
    out = []
    for c in range(vals.shape[1]):
        x = vals[:, c]
        x = x[~np.isnan(x)]
        if len(x) >= 100 and -65 < np.median(x) < 22 and x.min() > -85 and x.max() < 45 and x.std() > 1.5:
            out.append((x.std(), c))
    return [c for _, c in sorted(out, reverse=True)[:k]]


def date_run(vals, doy, hhmm, anom, fallback):
    """start year of a run: best detrended-daily-temperature correlation with C-level"""
    cols = temp_columns(np.where(vals == -6999, np.nan, vals))
    best = (-1.0, None)
    if not cols:
        return fallback, -1.0
    for y0 in YEARS:
        ts = ll.run_dates(doy, hhmm, y0)
        if ts.min() > anom.index.max() or ts.max() < anom.index.min():
            continue
        dm = pd.DataFrame(vals[:, cols], index=ts).replace(-6999, np.nan).resample("D").mean()
        dm = dm - dm.rolling(15, center=True, min_periods=5).mean()
        j = dm.join(anom, how="inner")
        if len(j) < 20:
            continue
        for c in range(len(cols)):
            for r in anom.columns:
                m = j[c].notna() & j[r].notna()
                if m.sum() >= 20 and j.loc[m, c].std() > 0:
                    s = float(np.corrcoef(j.loc[m, c], j.loc[m, r])[0, 1])
                    if s > best[0]:
                        best = (s, y0)
    return (best[1], best[0]) if best[1] is not None else (fallback, -1.0)


def exact_score(df, cl, sample=12000):
    refs = [c for c in EXACT_REFS if c in cl.columns]
    j = df.join(cl[refs].add_suffix("_C"), how="inner")
    if len(j) < 100:
        return -1
    if len(j) > sample:
        j = j.iloc[:: len(j) // sample]
    cnt = 0
    for c in df.columns:
        best = 0
        for r in refs:
            m = j[c].notna() & j[r + "_C"].notna()
            if m.sum() >= 100:
                best = max(best, ((j.loc[m, c] - j.loc[m, r + "_C"]).abs() < 0.011).mean())
        cnt += best > 0.9
    return cnt


def match_columns(df, cl, sample=12000):
    from scipy.optimize import linear_sum_assignment
    refs = [r for r in ALL_REFS if r in cl.columns]
    j = df.join(cl[refs].add_suffix("_C"), how="inner")
    if len(j) > sample:
        j = j.iloc[:: len(j) // sample]
    cols = list(df.columns)
    S = np.zeros((len(cols), len(refs)))
    st = {}
    for a, c in enumerate(cols):
        for b, r in enumerate(refs):
            m = j[c].notna() & j[r + "_C"].notna()
            if m.sum() < 150:
                continue
            x, y = j.loc[m, c], j.loc[m, r + "_C"]
            if x.std() == 0 or y.std() == 0:
                continue
            eq = float(((x - y).abs() < 0.011).mean())
            rr = float(np.corrcoef(x, y)[0, 1])
            sl, ic = np.polyfit(x, y, 1)
            st[(a, b)] = (eq, rr, float(sl), float(ic), int(m.sum()))
            if eq > 0.9 and abs(rr) > 0.95:
                S[a, b] = 1 + eq
            elif rr > 0.8:
                S[a, b] = rr
    out = {c: None for c in cols}
    for a, b in zip(*linear_sum_assignment(-S)):
        if S[a, b] > 0:
            out[cols[a]] = (refs[b],) + st[(a, b)]
    return out


def accept(m):
    """accepted variable name of a match or '_'"""
    if m is None:
        return "_"
    var, eq, rr, sl, ic, n = m
    if eq > 0.9:
        return var
    if var in EXACT_REFS:      # these are copied verbatim by the C-level processing (x1.00076 for TA3/TA4)
        return var if (rr > 0.995 and abs(sl - 1) < 0.01) else "_"
    return var if rr >= 0.9 else "_"


def complete(var_list, medians):
    """name the RH and boom-height columns of the standard layouts when the values look right.
    The C-level RH is corrected and its HW derived from snow height, so they cannot be matched directly.
    28-value layout: ... TA1-4, RH1, RH2, VW1, VW2, DW1, DW2, P, HW1, HW2, x, V
    14-value ARGOS meteorology array, two wind vanes:  ISWR, OSWR, NR, TA1, TA2, RH1, RH2, VW1, VW2, DW1, DW2, P, HW1, HW2
    14-value ARGOS meteorology array, one wind vane:   ISWR, OSWR, NR, TA1, TA2, RH1, RH2, VW1, VW2, DW1, P, HW1, HW2, V"""
    n = len(var_list)
    out = list(var_list)
    if n == 28:
        tmpl = T31
    elif n == 14 and var_list[:2] == ["ISWR", "OSWR"]:
        if "P" in var_list:
            tmpl = T17_MET if var_list.index("P") == 11 else (T17_MET_1VANE if var_list.index("P") == 10 else None)
        else:
            tmpl = None
    else:
        tmpl = None
    if tmpl is None:
        return out
    for k, name in enumerate(tmpl):
        if name in PLAUSIBLE and out[k] == "_" and name not in out:
            m = medians[k]
            lo, hi = PLAUSIBLE[name]
            if m is not None and lo < m < hi:
                out[k] = name
    # HW1 before HW2, as in the programs
    if "HW1" in out and "HW2" in out and out.index("HW2") < out.index("HW1"):
        i, j = out.index("HW1"), out.index("HW2")
        out[i], out[j] = "HW2", "HW1"
    return out


def decode(stn_dir):
    cl = load_clevel(stn_dir)
    anom = clevel_anom(cl)
    site = stn_dir[3:]
    fields = write_nead.get_config_list_str(f"L0/L0_ini/{stn_dir}_header.ini", "fields")
    d = f"L0/{stn_dir}/CR10X logger files/"
    rows = []
    for f in sorted(os.listdir(d)):
        fp = d + f
        if os.path.isdir(fp) or f.lower().endswith((".dld", ".for", ".txt", ".emf", ".csi", ".doc", ".toml")):
            continue
        py = int(f[:4]) if re.match(r"^\d{4}_", f) else 2000
        derived = bool(DERIVED.search(f))
        groups = ll.split_groups(ll.parse_lines(fp))
        for (aid, n), items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            if len(items) < 100 or n < 6:
                continue
            a = np.array(items)
            tp = ll.time_pattern(a)
            if tp is None:
                rows.append(dict(station=stn_dir, file=f, array=aid, ncols=n, rows=len(a), status="no time columns"))
                continue
            a = a[tp[2]]
            n_t, has_year = tp[0], tp[1]
            runs = [(0, len(a) - 1)] if has_year else make_runs(a[:, 1], a[:, 2])
            for (i0, i1) in runs:
                seg = a[i0:i1 + 1]
                vals = seg[:, n_t:]
                if has_year:
                    ts = pd.DatetimeIndex((pd.to_datetime(pd.Series(seg[:, 1].astype(int)), format="%Y")
                                           + pd.to_timedelta(seg[:, 2] - 1, unit="D")
                                           + pd.to_timedelta((seg[:, 3] // 100) * 60 + seg[:, 3] % 100, unit="min")).values, tz="UTC")
                    y0, sc = int(seg[0, 1]), 1.0
                else:
                    y0, sc = date_run(vals, seg[:, 1], seg[:, 2], anom, py - 1)
                    if sc < 0:
                        nroll = int(np.sum((seg[:, 1][:-1] > 300) & (seg[:, 1][1:] < 60)))
                        y0 = py - nroll
                    ts = ll.run_dates(seg[:, 1], seg[:, 2], y0)
                df, step = ll.hourly_frame(vals, ts, [f"c{i}" for i in range(vals.shape[1])])
                # hour offset between logger and C-level (used only for matching)
                best = (exact_score(df, cl), 0, df)
                for sh in (1, -1):
                    s2 = df.set_axis(df.index + pd.Timedelta(hours=sh))
                    e2 = exact_score(s2, cl)
                    if e2 > best[0] + 1:
                        best = (e2, sh, s2)
                ex, shift, dfm = best
                mm = match_columns(dfm, cl) if ex >= 0 else {c: None for c in df.columns}
                var_list = [accept(mm[c]) if accept(mm[c]) in fields else "_" for c in df.columns]
                stats = {c: mm[c] for c in df.columns if mm.get(c)}
                rows.append(dict(
                    station=stn_dir, site=site, file=f, array=aid, ncols=n, n_time=n_t, row_from=i0, row_to=i1,
                    start_year=y0, date_score=round(sc, 3), hourly_rows=len(df), step_min=step,
                    start=df.index.min(), end=df.index.max(), exact_cols=ex, shift_h=shift,
                    derived_name=derived, var_list=",".join(var_list),
                    col_medians=",".join("" if np.isnan(df[c].median()) else f"{df[c].median():.4g}" for c in df.columns),
                    n_named=sum(v != "_" for v in var_list),
                    implied_factors=";".join(f"{c}:{v[0]}:{v[3]:.4g}" for c, v in stats.items() if v[0] in ("ISWR", "OSWR", "NR", "P", "VW1", "VW2")),
                    status="ok"))
        os.makedirs(OUT, exist_ok=True)
        pd.DataFrame(rows).to_csv(OUT + f"{stn_dir[:2]}.csv", index=False)
    return pd.DataFrame(rows)


def registry(stations=None):
    """(Re)builds L0/L0_ini/CR10X_layouts.csv and CR10X_file_registry.csv from the decode() output cached in
    out/logger_first_review/decode/??.csv. With `stations` (station-dir prefixes like '14'), only those stations'
    rows are replaced; every other station's existing registry rows (and any layout not touched here) are kept as
    they are -- decoding one station must never wipe out the other ~20 stations' registered runs, whose decode
    cache may not even be present any more. Without `stations`, every ??.csv currently cached is used, matching
    the previous whole-network behaviour (only safe when the cache holds a fresh decode of every station)."""
    files = sorted(glob.glob(OUT + "??.csv"))
    if stations:
        files = [f for f in files if os.path.basename(f)[:2] in stations]
    d = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    ok = d[d.status == "ok"].copy()
    ok["decoded"] = ok.var_list.str.split(",")
    ok["medians"] = ok.col_medians.map(lambda s: [None if x == "" else float(x) for x in str(s).split(",")])
    ok["completed"] = [complete(v, m) for v, m in zip(ok.decoded, ok.medians)]
    # consensus: a column that is unnamed in one run but named identically in the other runs of the same
    # output array at the same station (same number of columns) gets that name; conflicts are left alone
    fin = []
    for _, r in ok.iterrows():
        fin.append(list(r.completed))
    ok["final"] = fin
    for (stn, arr, nc), g in ok.groupby(["station", "array", "ncols"]):
        names = [set(x[k] for x in g.completed if x[k] != "_") for k in range(nc - int(g.n_time.iloc[0]))]
        for idx in g.index:
            cur = ok.at[idx, "final"]
            for k, s in enumerate(names):
                if cur[k] == "_" and len(s) == 1 and not (set(s) & set(cur)):
                    cur[k] = next(iter(s))
            ok.at[idx, "final"] = cur
    ok["var_list_final"] = ok.final.map(",".join)
    ok["n_named_final"] = ok.final.map(lambda x: sum(v != "_" for v in x))
    ok["use"] = ((ok.n_named_final >= 5) & (~ok.derived_name) & ((ok.date_score >= 0.75) | (ok.date_score < 0))).astype(int)
    lay = {}
    for vl in ok.loc[ok.use == 1, "var_list_final"].unique():
        n = len(vl.split(","))
        lay[vl] = f"L{n}_{hashlib.md5(vl.encode()).hexdigest()[:5]}"
    layouts = pd.DataFrame([dict(layout=v, n_columns=len(k.split(",")), var_list=k) for k, v in lay.items()])
    reg = ok[ok.use == 1].copy()
    reg["layout"] = reg.var_list_final.map(lay)
    reg["note"] = np.where(reg.date_score < 0, "dated from the file name only (outside the C-level period)",
                           np.where(reg.date_score < 0.9, "dating score below 0.9", ""))
    reg = reg[["site", "file", "array", "ncols", "layout", "row_from", "row_to", "start_year", "use", "note"]]

    lay_path, reg_path = "L0/L0_ini/CR10X_layouts.csv", "L0/L0_ini/CR10X_file_registry.csv"
    if stations and os.path.isfile(reg_path):
        old_reg = pd.read_csv(reg_path, skipinitialspace=True)
        touched_sites = set(reg.site.unique())
        reg = pd.concat([old_reg[~old_reg.site.isin(touched_sites)], reg], ignore_index=True)
    if stations and os.path.isfile(lay_path):
        old_lay = pd.read_csv(lay_path, skipinitialspace=True)
        # layout ids are a content hash of var_list, so re-deriving one for an untouched station reproduces the
        # same id; only genuinely new layouts (ids not already present) need to be added
        layouts = pd.concat([old_lay, layouts[~layouts.layout.isin(old_lay.layout)]], ignore_index=True)

    layouts.to_csv(lay_path, index=False)
    reg.to_csv(reg_path, index=False)
    print(len(layouts), "layouts,", len(reg), "registry rows written;", int((ok.use == 0).sum()), "runs not used")
    ok.drop(columns=["decoded", "medians", "completed", "final"]).to_csv(OUT + "all_runs.csv.txt", index=False)




# ---------------------------------------------------------------------------------------------
# verification of the registry: every named column against C-level, names that do not hold are dropped
# ---------------------------------------------------------------------------------------------
def verify():
    reg = pd.read_csv("L0/L0_ini/CR10X_file_registry.csv", skipinitialspace=True)
    layouts = pd.read_csv("L0/L0_ini/CR10X_layouts.csv", skipinitialspace=True).set_index("layout")
    cl_cache, rows, newvl = {}, [], {}
    for k, r in reg.iterrows():
        stn = [d for d in os.listdir("L0") if d[3:] == r["site"] and d[:2].isdigit()][0]
        if stn not in cl_cache:
            cl_cache[stn] = load_clevel(stn)
        cl = cl_cache[stn]
        path = f"L0/{stn}/CR10X logger files/{r['file']}"
        a, n_t, has_year = ll.group_array(path, int(r["array"]), int(r["ncols"]))
        seg = a[int(r["row_from"]): int(r["row_to"]) + 1]
        vl = layouts.loc[r["layout"], "var_list"].split(",")
        if has_year:
            ts = pd.DatetimeIndex((pd.to_datetime(pd.Series(seg[:, 1].astype(int)), format="%Y") + pd.to_timedelta(seg[:, 2] - 1, unit="D")
                                   + pd.to_timedelta((seg[:, 3] // 100) * 60 + seg[:, 3] % 100, unit="min")).values, tz="UTC")
        else:
            ts = ll.run_dates(seg[:, 1], seg[:, 2], int(r["start_year"]))
        df, step = ll.hourly_frame(seg[:, n_t:], ts, vl)
        keep = list(vl)
        for v in [c for c in vl if c != "_"]:
            i = vl.index(v)
            st = dict(site=r["site"], file=r["file"], array=r["array"], row_from=r["row_from"], variable=v, n=0, r=np.nan,
                      exact=np.nan, slope=np.nan, slope_pos=np.nan, slope_neg=np.nan, median_diff=np.nan, kept=True,
                      status="no C-level overlap")
            if v in cl.columns:
                j = df[[v]].join(cl[[v]].add_suffix("_C"), how="inner").dropna()
                if len(j) > 12000:
                    j = j.iloc[:: len(j) // 12000]
                if len(j) >= 150 and j[v].std() > 0 and j[v + "_C"].std() > 0:
                    x, y = j[v], j[v + "_C"]
                    st["n"] = len(j)
                    st["r"] = float(np.corrcoef(x, y)[0, 1])
                    st["exact"] = float(((x - y).abs() < 0.011).mean())
                    st["slope"] = float(np.polyfit(x, y, 1)[0])
                    st["median_diff"] = float((y - x).median())
                    for lab, mk in (("slope_pos", x > 0), ("slope_neg", x < 0)):
                        if mk.sum() > 100 and x[mk].std() > 0:
                            st[lab] = float(np.polyfit(x[mk], y[mk], 1)[0])
                    if v in EXACT_REFS:
                        ok = st["exact"] > 0.5 or (st["r"] > 0.98 and abs(st["slope"] - 1) < 0.02)
                    elif v in ("RH1", "RH2"):
                        ok = st["r"] >= 0.15
                    elif v in ("HW1", "HW2"):
                        ok = st["r"] >= 0.4
                    else:
                        ok = st["r"] >= 0.85
                    st["kept"] = bool(ok)
                    st["status"] = "exact copy" if st["exact"] > 0.9 else ("linear" if st["r"] >= 0.9 else ("weak" if st["r"] >= 0.7 else "does not match"))
                    if not ok:
                        keep[i] = "_"
            rows.append(st)
        newvl[k] = ",".join(keep)
    reg["var_list_verified"] = pd.Series(newvl)
    reg["n_named"] = reg.var_list_verified.map(lambda s: sum(x != "_" for x in s.split(",")))
    reg.loc[reg.n_named < 5, "use"] = 0
    lay = {}
    for vl in reg.loc[reg.use == 1, "var_list_verified"].unique():
        lay[vl] = f"L{len(vl.split(','))}_{hashlib.md5(vl.encode()).hexdigest()[:5]}"
    layouts_new = pd.DataFrame([dict(layout=v, n_columns=len(k.split(",")), var_list=k) for k, v in lay.items()])
    reg["layout"] = reg.var_list_verified.map(lay).fillna(reg.layout)
    reg = reg[reg.use == 1][["site", "file", "array", "ncols", "layout", "row_from", "row_to", "start_year", "use", "note"]]
    for c in ("array", "ncols", "row_from", "row_to", "start_year", "use"):
        reg[c] = reg[c].astype(int)
    layouts_new.to_csv("L0/L0_ini/CR10X_layouts.csv", index=False)
    reg.to_csv("L0/L0_ini/CR10X_file_registry.csv", index=False)
    v = pd.DataFrame(rows)
    v.round(4).to_csv("metadata/logger_first/cr10x_decode_verification.csv", index=False)
    print(len(layouts_new), "layouts,", len(reg), "runs used; names dropped by verification:", int((~v.kept).sum()), "of", len(v))
    print(v.groupby("variable").agg(n=("kept", "size"), dropped=("kept", lambda s: int((~s).sum()))).T.to_string())


def calibration():
    """L0/L0_ini/CR10X_calibration.csv: how the raw CR10X columns become physical units.

    Radiation, NR and TA3/TA4: the documented factor of the station's CR1000-era header when the station's
    CR10X-era ISWR agrees with the header ISWR factor within 10% (the same radiometer family); otherwise the
    factor implied by the C-level file. Pressure: the additive constant implied by C-level (the programs write
    P - 400). Every other variable is used as the logger reports it (factor 1).
    The comparison between the documented and the implied factors, e.g. C-level OSWR being ~0.93 x the header
    value everywhere, is written to cr10x_calibration_check.csv: it is a finding for L1 to decide on, not
    something applied here."""
    v = pd.read_csv("metadata/logger_first/cr10x_decode_verification.csv")
    v = v[v.kept & (v.n >= 500) & (v.r >= 0.95)]
    rows, chk = [], []
    for site in sorted(v.site.unique()):
        stn = [d for d in os.listdir("L0") if d[3:] == site and d[:2].isdigit()][0]
        hdr = f"L0/L0_ini/{stn}_header.ini"
        fl = write_nead.get_config_list_str(hdr, "fields")
        sc = dict(zip(fl, write_nead.get_config_list(hdr, "scale_factor")))
        try:
            sn = dict(zip(fl, write_nead.get_config_list(hdr, "scale_factor_neg")))
        except Exception:
            sn = {}
        g = v[v.site == site]
        gi = g[g.variable == "ISWR"]
        h_iswr = sc.get("ISWR")
        same_family = bool(h_iswr and h_iswr >= 10 and len(gi) and abs(gi.slope_pos.median() / h_iswr - 1) < 0.10)
        for var in ("ISWR", "OSWR", "NR", "TA3", "TA4", "P"):
            gg = g[g.variable == var]
            if len(gg) == 0:
                continue
            ip, ineg = float(gg.slope_pos.median()), float(gg.slope_neg.median())
            hp = sc.get(var) if var != "P" else None
            hn = sn.get(var, hp) if var != "P" else None
            chk.append(dict(site=site, var=var, documented=hp, documented_neg=hn, implied_pos=ip, implied_neg=ineg,
                            ratio_pos=(ip / hp if hp else np.nan), ratio_neg=(ineg / hn if hn else np.nan), runs=len(gg),
                            spread_pos=float(gg.slope_pos.std()), same_radiometer_family=same_family))
            if var == "P":
                rows.append(dict(site=site, var=var, scale_pos=1, scale_neg=1, add=float(np.round(gg.median_diff.median())),
                                 source=f"implied by C-level ({len(gg)} runs); the programs write P minus 400"))
            elif var in ("TA3", "TA4"):
                use = hp if (same_family and hp) else (round(ip, 5) if abs(ip - 1) < 0.005 else 1.0)
                rows.append(dict(site=site, var=var, scale_pos=use, scale_neg=use, add=0,
                                 source="CR1000 header" if (same_family and hp) else "implied by C-level"))
            elif same_family and hp:
                rows.append(dict(site=site, var=var, scale_pos=hp, scale_neg=hn, add=0,
                                 source=f"CR1000 header (CR10X-era ISWR implied {gi.slope_pos.median():.1f} agrees with header {h_iswr:g})"))
            else:
                negv = ineg if (var == "NR" and not np.isnan(ineg)) else ip
                rows.append(dict(site=site, var=var, scale_pos=round(ip, 2), scale_neg=round(negv, 2), add=0,
                                 source=f"implied by C-level ({len(gg)} runs); the CR1000-era header ({h_iswr}) is not the same radiometer"
                                        if (h_iswr and h_iswr >= 10) else f"implied by C-level ({len(gg)} runs); no station calibration in the repository"))
    pd.DataFrame(rows).to_csv("L0/L0_ini/CR10X_calibration.csv", index=False)
    print(len(rows), "calibration rows for", len({r["site"] for r in rows}), "sites")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "decode":
        for num in sys.argv[2:]:
            stn = [x for x in sorted(os.listdir("L0")) if x.startswith(num.zfill(2) + "-")][0]
            print("decoding", stn, flush=True)
            decode(stn)
    elif cmd == "registry":
        # station numbers restrict the rebuild to those stations, keeping every other station's existing rows
        registry(set(n.zfill(2) for n in sys.argv[2:]) or None)
    elif cmd == "verify":
        verify()
    elif cmd == "calibration":
        calibration()

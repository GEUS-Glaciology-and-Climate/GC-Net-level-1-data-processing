# -*- coding: utf-8 -*-
"""Assess the periods where the logger files have data but the C-level file has none.

Such a gap can mean the people who produced the C-level file removed a malfunction, or that the
data were simply overlooked. For every gap window listed by the L0 script
(out/logger_first_review/c_level_gaps.csv, written by the L0 script) this tool collects evidence from the L0M
data and from CARRA, decides whether the removal is supported, and only then proposes an L1 flag:

  evidence                                       supports the removal when
  ---------------------------------------------- ----------------------------------------------------
  physical range (RANGE below)                   >= 20% of the hours are outside it
  the L1 frozen-value filter (filter_zero_gradient) already removes >= 80% of the window -> no flag needed
  flat runs (same value for >= 6 h; 24 h for radiation, HW, TS, V)   >= 60% of the hours are in such runs
  wind speed against CARRA 10 m wind             median logger wind < 0.3 m/s while CARRA median > 2.5 m/s
  air temperature against CARRA t2m              r < 0.5 and |bias| > 6 degC (window >= 72 h)
  pressure against CARRA sp                      |bias| > 12 hPa, or r < 0.4 (window >= 120 h)
  incoming shortwave against CARRA ssrd          r < 0.4 (window >= 120 h)

CARRA assimilates air temperature, pressure and wind observations, so it is used here only to
recognise clearly wrong values, not as an independent measurement of the truth.
Windows without such evidence are kept and listed as 'not supported' (the C-level gap looks like an
oversight) or 'unclear'. Flags are written to metadata/flags/<site>.csv (NAN flags, as elsewhere).

Usage (repository root):
  python tools/logger_vs_clevel_review.py assess <L0M dir> <station dir names...>
  python tools/logger_vs_clevel_review.py flags  [--write]
"""
import os
import sys
import glob
import warnings
warnings.simplefilter("ignore")
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CARRA_DIR = r"C:\Users\bav\OneDrive - GEUS\Data\CARRA\CARRA_at_AWS"
OUT = "metadata/logger_first/"
GAPS = "out/logger_first_review/c_level_gaps.csv"
ASSESSMENT = OUT + "c_level_gap_assessment.csv"
RANGE = {"TA1": (-80, 25), "TA2": (-80, 25), "TA3": (-80, 25), "TA4": (-80, 25), "TA5": (-80, 25), "RH1": (-2, 106), "RH2": (-2, 106),
         "VW1": (0, 60), "VW2": (0, 60), "DW1": (0, 360), "DW2": (0, 360), "P": (450, 1100), "ISWR": (-30, 1400),
         "OSWR": (-30, 1400), "NR": (-400, 1000), "HW1": (0, 15), "HW2": (0, 15), "V": (8, 16)}
CARRA_VAR = {"TA1": "t2m", "TA2": "t2m", "TA3": "t2m", "TA4": "t2m", "VW1": "si10", "VW2": "si10", "P": "sp", "ISWR": "ssrd"}
L1_FROZEN = ["VW1", "VW2", "DW1", "DW2", "TA1", "TA2", "TA3", "TA4", "P", "ISWR", "OSWR", "NR", "RH1", "RH2"]

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



def load_l0m(path):
    hdr = None
    with open(path, encoding="utf-8") as fh:
        for l in fh:
            if l.startswith("# fields"):
                hdr = [c.strip() for c in l.split("=", 1)[1].strip().split(",")]
                break
    d = pd.read_csv(path, comment="#", header=None, names=hdr, na_values=[""])
    d = d[d.timestamp.astype(str).str.match(r"^\d{4}-")].copy()
    d["timestamp"] = pd.to_datetime(d.timestamp, utc=True)
    d = d.set_index("timestamp").astype(float)
    return d[~d.index.duplicated(keep="first")].sort_index()


def load_carra(site):
    import xarray as xr
    for name in (site, site.replace(" ", "")):
        f = os.path.join(CARRA_DIR, name + ".nc")
        if os.path.isfile(f):
            ds = xr.open_dataset(f)
            df = ds[["t2m", "sp", "si10", "ssrd"]].to_dataframe()[["t2m", "sp", "si10", "ssrd"]]
            df.index = pd.to_datetime(df.index).tz_localize("UTC")
            ds.close()
            return df.resample("h").interpolate(limit=3)
    return None


def flat_share(x, min_len):
    """share of the non-NaN hours that belong to runs of >= min_len identical values"""
    v = x.dropna()
    if len(v) < 6:
        return np.nan
    same = np.r_[False, np.abs(np.diff(v.values)) < 1e-6]
    grp = np.cumsum(~same)
    run = pd.Series(same).groupby(grp).transform("sum").values + 1
    return float(np.mean(run >= min_len))


def assess_station(l0m_dir, stn_dir):
    from lib import PROMICE_toolbox as pt
    site = stn_dir[3:]
    if not os.path.isfile(GAPS):
        return None
    win = pd.read_csv(GAPS, parse_dates=["start", "end"])
    win = win[win.site == site]
    if len(win) == 0:
        return win
    L = load_l0m(f"{l0m_dir}/{stn_dir}.csv")
    L1 = L.copy()
    try:
        L1 = pt.filter_zero_gradient(L1.copy())
    except Exception as e:
        print("  filter_zero_gradient failed:", repr(e))
    removed = L[L1_FROZEN].notna() & L1[L1_FROZEN].isna() if all(c in L1.columns for c in L1_FROZEN) else None
    C = load_carra(site)
    rows = []
    for w in win.itertuples():
        v = w.variable
        if v not in L.columns:
            continue
        x = L[v].loc[w.start:w.end]
        n = int(x.notna().sum())
        if n == 0:
            continue
        ev = dict(site=site, variable=v, start=w.start, end=w.end, hours=int(w.hours), values=n,
                  median=round(float(x.median()), 3), share_zero=round(float((x == 0).mean()), 3))
        lo, hi = RANGE.get(v, (-np.inf, np.inf))
        ev["out_of_range"] = round(float(((x < lo) | (x > hi)).mean()), 3)
        ev["l1_frozen_filter_removes"] = round(float(removed[v].loc[w.start:w.end].mean()), 3) if removed is not None and v in removed.columns else np.nan
        min_len = 24 if v in ("ISWR", "OSWR", "NR", "HW1", "HW2", "V") or v.startswith("TS") else 6
        ev["flat_share"] = round(flat_share(x, min_len), 3)
        ev["carra_r"] = ev["carra_bias"] = ev["carra_median"] = np.nan
        if C is not None and v in CARRA_VAR and n >= 72:
            c = C[CARRA_VAR[v]].reindex(x.index)
            m = x.notna() & c.notna()
            if m.sum() >= 48 and x[m].std() > 0 and c[m].std() > 0:
                ev["carra_r"] = round(float(np.corrcoef(x[m], c[m])[0, 1]), 3)
                ev["carra_bias"] = round(float((x[m] - c[m]).mean()), 2)
                ev["carra_median"] = round(float(c[m].median()), 2)
        ev["verdict"], ev["reason"] = verdict(v, ev, n)
        rows.append(ev)
    return pd.DataFrame(rows)


def verdict(v, e, n):
    if e["out_of_range"] >= 0.2:
        return "supported", f"{e['out_of_range']:.0%} of the values are outside {RANGE[v]}"
    if e["l1_frozen_filter_removes"] >= 0.8:
        return "already removed by L1", f"the L1 frozen-value filter already removes {e['l1_frozen_filter_removes']:.0%}"
    if e["flat_share"] >= 0.6:
        return "supported", f"{e['flat_share']:.0%} of the hours are flat runs (sensor stuck)"
    if v in ("VW1", "VW2") and e["median"] < 0.3 and e["carra_median"] > 2.5:
        return "supported", f"logger wind median {e['median']} m/s while CARRA median {e['carra_median']} m/s"
    if v.startswith("TA") and e["carra_r"] < 0.5 and abs(e["carra_bias"]) > 6:
        return "supported", f"r={e['carra_r']}, bias {e['carra_bias']} degC against CARRA"
    if v == "P" and (abs(e["carra_bias"]) > 12 or (e["carra_r"] < 0.4 and n >= 120)):
        return "supported", f"pressure bias {e['carra_bias']} hPa, r={e['carra_r']} against CARRA"
    if v == "ISWR" and e["carra_r"] < 0.4 and n >= 120:
        return "supported", f"r={e['carra_r']} against CARRA ssrd"
    if not np.isnan(e["carra_r"]) and e["carra_r"] >= 0.8:
        return "not supported", f"values plausible (r={e['carra_r']} against CARRA)"
    if e["out_of_range"] == 0 and (np.isnan(e["flat_share"]) or e["flat_share"] < 0.1) and e["share_zero"] < 0.05:
        return "not supported", "no frozen values, none out of range, no independent evidence of a fault"
    return "unclear", "mixed evidence"


def flags(write):
    all_ = pd.read_csv(ASSESSMENT)
    sup = all_[all_.verdict == "supported"].copy()
    sup["start"] = pd.to_datetime(sup.start, utc=True)
    sup["end"] = pd.to_datetime(sup.end, utc=True)
    out = []
    for (site, var), g in sup.groupby(["site", "variable"]):
        g = g.sort_values("start")
        cur = None
        for r in g.itertuples():
            if cur is not None and r.start - cur["t1"] <= pd.Timedelta(hours=1):
                cur["t1"] = max(cur["t1"], r.end)
                cur["n"] += 1
                cur["reasons"].add(r.reason.split(" ")[0] + " " + r.reason.split(" ")[1] if len(r.reason.split(" ")) > 1 else r.reason)
            else:
                if cur is not None:
                    out.append(cur)
                cur = dict(site=site, variable=var, t0=r.start, t1=r.end, n=1, reasons={r.reason})
        if cur is not None:
            out.append(cur)
    fl = pd.DataFrame(out)
    fl["flag"] = "NAN"
    fl["reason"] = fl.reasons.map(lambda r: sorted(r)[0].replace(",", ";"))
    print(len(fl), "flag rows for", fl.site.nunique(), "sites;", int(sup.hours.sum()), "hours")
    if write:
        # append-only: the hand-edited flag files keep their formatting; rows of an earlier run of this tool are replaced
        for site, g in fl.groupby("site"):
            path = f"metadata/flags/{site}.csv"
            raw = open(path, "rb").read().decode("utf-8")
            eol = "\r\n" if "\r\n" in raw else "\n"
            keep = [l for l in raw.splitlines() if "logger-first review" not in l]
            lines = [f"{r.t0:%Y-%m-%dT%H:%M:%S}+00:00,{r.t1:%Y-%m-%dT%H:%M:%S}+00:00,{r.variable},NAN,"
                     f"in the logger file but absent from the C-level file; {r.reason} (logger-first review 2026-09)," for r in g.itertuples()]
            while keep and keep[-1].strip() == "":
                keep.pop()
            write_bytes(path, (eol.join(keep + lines) + eol).encode("utf-8"))
            print("  wrote", path, len(lines), "rows")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "assess":
        # usage: assess [<L0M dir> [<station dir names...>]]  (default: L0M and every station of the gaps table)
        l0m_dir = sys.argv[2] if len(sys.argv) > 2 else "L0M"
        os.makedirs(OUT, exist_ok=True)
        stations = sys.argv[3:]
        if not stations:
            gaps = pd.read_csv(GAPS)
            stations = sorted(f[:-4] for f in os.listdir(l0m_dir)
                              if f.endswith(".csv") and f[:2].isdigit() and f[3:-4] in set(gaps.site.unique()))
        for s in stations:
            print("assessing", s, flush=True)
            r = assess_station(l0m_dir, s)
            if r is not None and len(r):
                if os.path.isfile(ASSESSMENT):
                    prev = pd.read_csv(ASSESSMENT)
                    r = pd.concat([prev[prev.site != r.site.iloc[0]], r], ignore_index=True)
                r.to_csv(ASSESSMENT, index=False)
                print(r.verdict.value_counts().to_dict())
    elif cmd == "flags":
        flags("--write" in sys.argv)

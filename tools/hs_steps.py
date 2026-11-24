# -*- coding: utf-8 -*-
"""Steps of the surface height (HS1, HS2) of the L1 hourly files, and the adjustments that remove them.

The surface height has to be continuous: a step in HS is a boom or sensor that was moved (visits) or a processing artefact (the
C-level files). Steps of HW (the instrument height) are normal, the arm is moved at the visits; HS must not follow them.

A step is a change between two consecutive valid hours of a sensor (6 h running median) that is
  - larger than 0.2 m (gap of at most 6 h) / 0.25 m (up to a day) (0.25 and 0.3 if the other sensor has no data) / 0.3 m + 0.06 m x sqrt(days) (longer gaps), after subtracting the
    change that the monthly climatology of the station expects over the gap, and
  - persistent: the median of the 4 days after differs from the median of the 4 days before by the same sign and at least 60 % of it.
Rules:
  - gap of at most 24 h in November to March (nobody visits the station): artefact of the HW series, removed in HW (HW1/HW2 add);
  - other steps: a visit, removed in HS (HS1/HS2 add);
  - gaps of more than 24 h are only corrected at accumulation sites, or at the ablation sites if the gap is in October to April;
  - the change of the other sensor over the same windows is subtracted (a change seen by both sensors is the surface or a common move and is
    kept); only the sensor that departs more from the expected change is corrected. Exception: the same large change (more than 0.5 m
    beyond the climatology) of both sensors over a gap of more than 5 days is a boom raised at a visit and is removed from both.
Hours where HW is frozen for 14 days or more (removed by the filter) and the windows of the NAN flags on HW are ignored.

Usage (repository root): python tools/hs_steps.py            -> proposal in metadata/logger_first/hs_steps_proposal.csv
                         python tools/hs_steps.py --write    -> also writes the rows between the markers
                                                               '# hs_steps.py begin' / '# hs_steps.py end' of metadata/adjustments/<site>.csv
                         python tools/hs_steps.py --check    -> applies the proposal to the L1 HS and lists the steps that remain
The rows are increments on the HS (or HW) of the L1 as it was built. Run on an L1 that already contains the rows of the block, the tool only
proposes what is left, and `--write` APPENDS these rows to the block (the rows already there are kept). `--write --reset` rebuilds the blocks
from scratch: use it only on an L1 built WITHOUT the block (otherwise the earlier rows are lost).
"""
import os
import sys
import glob
import warnings
warnings.simplefilter("ignore")
import numpy as np
import pandas as pd

ABLATION = {"JAR1", "JAR2", "JAR3", "KULU", "SwissCamp", "SwissCamp10m", "PetermannELA", "PetermannGlacier", "SMS-PET",
            "SMS1", "SMS2", "SMS3", "SMS4", "SMS5"}
BEGIN = "# hs_steps.py begin"
END = "# hs_steps.py end"
SKIP = {   # windows treated by other rows (swap, sensor lowered, flags): (site, start, end)
    ("CrawfordPoint1", "2010-05-09", "2011-05-04"),
    ("LAR2", "2010-05-02", "2010-12-10"),
}


def load(f):
    fields = None
    with open(f, encoding="utf-8") as fh:
        for l in fh:
            if l.startswith("# fields"):
                fields = l.split("=", 1)[1].strip().split(",")
                break
    use = [c for c in ["timestamp", "HW1", "HW2", "HS1", "HS2"] if c in fields]
    df = pd.read_csv(f, comment="#", header=None, names=fields, usecols=use, na_values=["", "-999"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    return df.set_index("timestamp").asfreq("h")


def mask_frozen(d, min_h=14 * 24):
    """HS NaN where the HW of the same sensor repeats the same value for min_h hours or more"""
    for k in "12":
        hw, hs = "HW" + k, "HS" + k
        if hw not in d or hs not in d:
            continue
        eq = (d[hw].diff().abs() < 1e-6).values
        i, n = 0, len(eq)
        while i < n:
            if eq[i]:
                j = i
                while j < n and eq[j]:
                    j += 1
                if j - i >= min_h:
                    d.iloc[i - 1:j, d.columns.get_loc(hs)] = np.nan
                i = j
            else:
                i += 1
    return d


def mask_flags(d, flagfile):
    if not os.path.isfile(flagfile):
        return d
    fl = pd.read_csv(flagfile, comment="#", skipinitialspace=True)
    fl = fl[fl.flag.astype(str).str.strip() == "NAN"]
    for _, r in fl.iterrows():
        for v in str(r.variable).split():
            if v in ("HW1", "HW2"):
                hs = "HS" + v[-1]
                if hs in d:
                    t0 = pd.Timestamp(str(r.t0).strip(), tz="UTC") if str(r.t0).strip() not in ("", "nan") else d.index[0]
                    t1 = pd.Timestamp(str(r.t1).strip(), tz="UTC") if str(r.t1).strip() not in ("", "nan") else d.index[-1]
                    d.loc[t0:t1, hs] = np.nan
    return d


def climatology(d):
    clim = {}
    for v in ("HS1", "HS2"):
        if v not in d:
            continue
        dd = d[v].resample("D").mean()
        ch = dd.diff().where(dd.index.to_series().diff() == pd.Timedelta("1D")).clip(-0.3, 0.3)
        clim[v] = ch.groupby(ch.index.month).mean().reindex(range(1, 13)).fillna(0)
    return clim


def detect(site, d, clim):
    rows = []
    for v in ("HS1", "HS2"):
        if v not in d or d[v].notna().sum() < 200:
            continue
        o = "HS2" if v == "HS1" else "HS1"
        s = d[v].rolling(6, center=True, min_periods=3).median().dropna()
        idx = s.index
        dt = (idx[1:] - idx[:-1]) / pd.Timedelta("1D")
        dv = s.values[1:] - s.values[:-1]
        for k in np.where(np.abs(dv) > 0.12)[0]:
            g = dt[k]
            t_prev, t_next = idx[k], idx[k + 1]
            if any(a == site and pd.Timestamp(b, tz="UTC") <= t_next <= pd.Timestamp(c, tz="UTC") for a, b, c in SKIP):
                continue
            vb = d[v].loc[t_prev - pd.Timedelta("4D"):t_prev]
            va = d[v].loc[t_next:t_next + pd.Timedelta("4D")]
            if vb.notna().sum() < 12 or va.notna().sum() < 12:
                continue
            dp = va.median() - vb.median()
            if np.sign(dp) != np.sign(dv[k]) or abs(dp) < 0.6 * abs(dv[k]):
                continue
            # the other sensor over the same windows: a change that both sensors see is the surface (or a common move) and is kept
            dpo = np.nan
            if o in d:
                ob = d[o].loc[t_prev - pd.Timedelta("4D"):t_prev]
                oa = d[o].loc[t_next:t_next + pd.Timedelta("4D")]
                if ob.notna().sum() >= 12 and oa.notna().sum() >= 12:
                    dpo = oa.median() - ob.median()
            exp = 0.0
            if g > 1:
                days = pd.date_range(t_prev.normalize(), t_next.normalize(), freq="D")
                exp = float(clim[v].loc[days.month[:-1]].sum()) if len(days) > 1 else 0.0
            if dpo == dpo and g > 5 and abs(dp - dpo) < 0.15:
                # both sensors made the same large change over a long gap (a boom raised at the visit): continuity says the surface
                # did not do that; both are corrected, but only if the change is beyond what the climatology of the station allows
                exc = dp - exp
                thr = 0.5 + 0.002 * g
                if abs(exc) < thr:
                    continue
            elif dpo == dpo:
                exc = dp - dpo
                # only the sensor that departs more from the expected change is corrected (the other one is the reference)
                if abs(dp - exp) < abs(dpo - exp) or (abs(dp - exp) == abs(dpo - exp) and v == "HS2"):
                    continue
            else:
                exc = dp - exp
            if dpo == dpo and g > 5 and abs(dp - dpo) < 0.15:
                pass
            elif g <= 0.25:
                thr = 0.2 if dpo == dpo else 0.25
            elif g <= 1:
                thr = 0.25 if dpo == dpo else 0.3
            else:
                thr = 0.3 + 0.06 * np.sqrt(g)
            if abs(exc) < thr:
                continue
            ok, why = True, ""
            if g > 1 and site in ABLATION:
                gap_months = set(pd.date_range(t_prev.normalize(), t_next.normalize(), freq="D").month)
                if gap_months & {5, 6, 7, 8, 9}:
                    ok, why = False, "ablation site: the gap contains the melt season"
            winter = t_next.month in (11, 12, 1, 2, 3)
            target = "HW" if (g <= 1 and winter) else "HS"
            rows.append(dict(site=site, sensor=v, t_prev=t_prev, t_next=t_next, gap_d=round(g, 2), step=round(dp, 2), expected=round(exp, 2),
                             excess=round(exc, 2), other=round(dpo, 2) if dpo == dpo else np.nan, applied=ok, why=why, target=target,
                             variable=("HW" if target == "HW" else "HS") + v[-1], value=round(-exc if target == "HS" else exc, 2)))
    return rows


def cluster(t):
    """merges steps of the same sensor less than 3 days apart (keeps the largest)"""
    keep = []
    for _, g in t.groupby(["site", "sensor"]):
        g = g.sort_values("t_prev")
        last = None
        for i, r in g.iterrows():
            if last is not None and (r.t_prev - t.loc[last, "t_next"]) < pd.Timedelta("3D"):
                if abs(r.excess) > abs(t.loc[last, "excess"]):
                    keep.remove(last)
                    keep.append(i)
                    last = i
                continue
            keep.append(i)
            last = i
    return t.loc[sorted(keep)].sort_values(["site", "sensor", "t_prev"]).reset_index(drop=True)


def run(only):
    out = []
    for f in sorted(glob.glob("L1/hourly/*.csv")):
        site = os.path.basename(f)[:-4]
        if only and site not in only:
            continue
        d = load(f)
        if "HS1" not in d or d.HS1.notna().sum() < 200:
            continue
        # name of the adjustment/flag files: station name with spaces
        name = {os.path.basename(x)[:-4].replace(" ", ""): os.path.basename(x)[:-4] for x in glob.glob("metadata/adjustments/*.csv")}.get(site, site)
        d = mask_frozen(d)
        d = mask_flags(d, "metadata/flags/" + name + ".csv")
        # several passes: merging steps less than 3 days apart keeps only the largest, the others show up in the next pass on the corrected series
        for it in range(4):
            rows = detect(site, d, climatology(d))
            if not rows:
                break
            r = cluster(pd.DataFrame(rows))
            r["pass"] = it + 1
            out += r.to_dict("records")
            for _, x in r[r.applied].iterrows():
                hs = "HS" + x.sensor[-1]
                d.loc[x.t_next:, hs] = d.loc[x.t_next:, hs] + (x.value if x.target == "HS" else -x.value)
            if not r.applied.any():
                break
        print(site, len(out), flush=True)
    t = pd.DataFrame(out)
    return t.sort_values(["site", "sensor", "t_next"]).reset_index(drop=True) if len(t) else t


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


def clear_blocks(keep_names):
    """removes the block of an earlier run from the adjustment files that no longer get rows"""
    for p in glob.glob("metadata/adjustments/*.csv"):
        name = os.path.basename(p)[:-4]
        if name in keep_names:
            continue
        s = open(p, encoding="utf-8", newline="").read()
        if BEGIN not in s:
            continue
        eol = "\r\n" if "\r\n" in s else "\n"
        s = s.replace("\r\n", "\n")
        a, b = s.index(BEGIN), s.index(END) + len(END)
        s = s[:a].rstrip("\n") + "\n" + s[b:].lstrip("\n")
        write_bytes(p, s.replace("\n", eol).encode("utf-8"))
        print("block removed:", p)


def write_rows(t):
    names = {os.path.basename(x)[:-4].replace(" ", ""): os.path.basename(x)[:-4] for x in glob.glob("metadata/adjustments/*.csv")}
    reset = "--reset" in sys.argv
    if reset:
        clear_blocks({names.get(x, x) for x in t[t.applied].site})
    for site, g in t[t.applied].groupby("site"):
        name = names.get(site, site)
        p = "metadata/adjustments/" + name + ".csv"
        raw = open(p, encoding="utf-8", newline="").read() if os.path.isfile(p) else "t0,t1,variable,adjust_function,adjust_value,comment\n"
        eol = "\r\n" if "\r\n" in raw else "\n"
        s = raw.replace("\r\n", "\n")
        kept = []
        if BEGIN in s:
            a, b = s.index(BEGIN), s.index(END) + len(END)
            if not reset:
                kept = [l for l in s[a:b].split("\n") if l.strip() and not l.startswith("#")]
            s = s[:a].rstrip("\n") + "\n" + s[b:].lstrip("\n")
        lines = [BEGIN,
                 "# written by tools/hs_steps.py: steps of the surface height (HS) removed; a boom moved at a visit is removed in HS (HW keeps it),",
                 "# a step of HW in November to March within a day is an artefact of the C-level processing and is removed in HW. Rerun the tool after a rebuild."]
        lines += kept
        for _, r in g.sort_values("t_next").iterrows():
            lines.append("%s,,%s,add,%.2f,%s of %s: %+.2f m (%+.2f m relative to the other sensor and the climatology) over a gap of %.1f d" % (
                r.t_next.strftime("%Y-%m-%dT%H:%M:%S+00:00"), r.variable, r.value,
                "step removed in HS (boom moved)" if r.target == "HS" else "winter artefact removed in HW",
                r.sensor, r.step, r.excess, r.gap_d))
        lines.append(END)
        s = s.rstrip("\n") + "\n\n" + "\n".join(lines) + "\n"
        write_bytes(p, s.replace("\n", eol).encode("utf-8"))
        print("rows written:", p, len(g))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    t = run(args)
    os.makedirs("metadata/logger_first", exist_ok=True)
    t.to_csv("metadata/logger_first/hs_steps_proposal.csv", index=False)
    print(len(t), "steps,", int(t.applied.sum()), "applied")
    if "--write" in sys.argv:
        write_rows(t)

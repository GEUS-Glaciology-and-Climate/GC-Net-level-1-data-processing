# -*- coding: utf-8 -*-
"""Compare the field-reported wind-sensor heights (metadata/maintenance summary/*.csv, columns W1/W2 before/after) with HW1/HW2 of the L1
hourly files and write

  metadata/instrument_height_reference_check.csv   one row per reported value that does not agree with the L1, with a verdict and a comment
  metadata/instrument_height_pair_anomalies.csv    periods in which HW2-HW1 of the L1 is negative, ~0 or implausible

Matching: the L1 levels before/after a visit are the medians of 6 h values on each side of the largest step of HW within +-20 days of the
report date (reports are dated to the day, the visit may be a few days off); if there is no step the median of the window is used.
Verdicts (tolerance 0.4 m: the snow surface moves and the report is not at the same hour):
  copy           the 'after' value is identical to the 'before' value while the L1 shows a boom move: the 'after' was not measured
  spacing        W2-W1 of the report differs by more than 0.25 m from the median spacing reported at the station: one of the two is wrong
  common_offset  both sensors differ from the L1 by the same amount (+-0.25 m): offset of the report or of the L1
  differs        everything else with |report - L1| > 0.4 m
Manual comments (MANUAL below) come from looking at every flagged visit (+-45 days of HW1/HW2 with the reported values).
Run from the repository root:  python tools/check_instrument_height_references.py   (no network; reads the local maintenance summaries)
"""
import os, glob
import numpy as np, pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WIN = pd.Timedelta("20D")
TOL = 0.4

# (site, 'YYYY-MM-DD' of the report): comment (no commas, the file is a csv)
MANUAL = {
 ("Summit", "2001-06-10"): "W2 after 2.88 is a typo: the spacing to W1 after (2.80) would be 0.08 m; the L1 has 2.55 / 3.6 after the raise",
 ("Summit", "2005-05-26"): "L1 HW2 drops by 0.9 m on 2005-05-05 and HW1 sits in the blind zone (0.05 m); the reported 1.55 m is the level of April: the step of L1 HW2 is an artefact",
 ("South Dome", "2001-05-05"): "W2 1.06 is probably 1.66 (typo): the spacing to W1 would be 0.48 m while the station spacing is 1.05-1.1 m and the L1 has 1.59",
 ("South Dome", "2011-05-30"): "the report says HW1 < HW2 but the L1 has HW1 > HW2 (4.8 / 3.9): HW1 and HW2 are swapped in the L1 (see instrument_height_pair_anomalies.csv)",
 ("Saddle", "2003-05-01"): "after maintenance 1.03 / 2.07: the L1 has HW1 > HW2 (1.97 / 1.1) from 2003-04 to 2004-05: HW1 and HW2 are swapped in the L1",
 ("Saddle", "2004-06-12"): "L1 HW2 is in the blind zone (0.1 m) before the visit and jumps by 5.2 m; spacing after 1.8 m in the L1 against 0.85 m reported: HW2 of the L1 is probably too high or the report is wrong",
 ("NASA-SE", "2001-06-06"): "before = after (1.28 / 2.49): the L1 has 4.11 / 5.33 with the same spacing (1.22) and no step around the date; the report is 2.83 m below the L1 for both sensors: stale report or offset L1",
 ("NASA-SE", "2003-05-10"): "after = before (0.0 / 1.25): the L1 shows the boom raised by 5.2 m on the date; the after was not measured. The before values (boom on the snow) agree with the L1",
 ("NASA-SE", "2004-06-11"): "before 1.78 / 2.98 is 2.4 m below the L1 (4.19 / 5.18) with no step in the L1 for 45 days: not credible (accumulation would be 3.5 m in a year); the after values agree",
 ("NASA-SE", "1999-04-21"): "before = after in the report but the L1 HW2 drops 0.75 m on the day (3.86 to 3.09) and HW1 does not: HW2 was lowered at this visit",
 ("DYE-2", "2000-05-12"): "after = before: the L1 shows a raise of 2.4 m on the day (both sensors): the after was not measured",
 ("NASA-E", "2001-06-08"): "W2 after = W2 before and W2a-W1a = -0.23: the after values are not usable; the L1 shows a raise of 2.4 m and agrees with the 2003 report",
 ("NASA-E", "2011-06-02"): "L1 HW1 -0.1 m and HW2 +0.7 m at the visit with spacing 0.9 before and 1.8 after against 1.4 reported: the sensors were not moved together or one level is wrong",
 ("NASA-E", "2022-05-27"): "both sensors are 0.6 m above the L1 and the L1 is flat for 6 weeks: constant offset of the report (other reference) or of the L1",
 ("Crawford Point 1", "1998-05-30"): "before 0.47 / 1.16 has a spacing of 0.69 m (1.2 m at all other dates); the L1 step is on 1998-06-09 (10 days after the report date and the photo of 1998-05-31) and is a decrease while the report is an increase",
 ("Crawford Point 1", "1999-05-25"): "before 0.98 / 1.60 has a spacing of 0.62 m (1.2 m after); the L1 starts after the visit and agrees with the after values",
 ("Crawford Point 1", "2000-04-06"): "before = after: both sensors 0.35 m below the L1 while the L1 agrees with the reports of 1999-05 and 2001-05: the date of the report may be a few months off",
 ("Crawford Point 1", "2002-05-08"): "W1 agrees but W2 (2.88) is 1.16 m below the L1 (4.04): the L1 spacing is 2.26 m against 1.20 reported: HW2 of the L1 is 1.16 m too high from 2001-12 to 2002-11 (see the continuity rows of the adjustments)",
 ("Crawford Point 1", "2005-05-02"): "the after values 0.58 / 1.78 are the level before the raise of 2005-05-03 (L1 0.89 / 1.89 before and 3.55 / 5.57 after): the report is dated the day before the visit",
 ("Crawford Point 1", "2003-04-19"): "the before values (1.15 / 2.35) are the level of the previous year; the after values agree",
 ("Swiss Camp", "2013-05-15"): "the reports of 2013-2018 are +1.0 (+1.0 to +1.1 for 2015-2018) above the L1 HW1 and 1.0-1.7 above HW2: either the L1 HW is 1 m too low since 2012-2013 (HW1 down to 0.14 m is below the range of the sonic ranger) or the reports use another reference; 2011 agrees to 0.05 m",
 ("Swiss Camp", "2014-05-07"): "see 2013-05-15",
 ("Swiss Camp", "2015-05-13"): "see 2013-05-15",
 ("Swiss Camp", "2016-05-15"): "see 2013-05-15",
 ("Swiss Camp", "2017-05-14"): "see 2013-05-15",
 ("Swiss Camp", "2018-05-05"): "see 2013-05-15",
 ("JAR1", "2003-04-26"): "HW2 agrees (+0.1) but HW1 of the L1 is 0.9 m above the report before and after: L1 spacing 0.18 m against 1.20 reported (HW1 too high from 2002-09 to 2003-04)",
 ("JAR1", "2005-05-08"): "L1 before the visit: HW1 0.94 / HW2 2.65 (spacing 1.7 m); after 0.44 / 1.7 (1.2 m): the sensors were not moved by the same amount or one level before is wrong; the reported W1 before 2.03 does not fit either",
 ("Humboldt", "2011-06-01"): "the report after 3.06 / 4.29 equals the L1 of 2003 (3.10 / 4.25); the L1 is 1.6 / 2.9 and flat for 6 weeks: report copied from 2003 or the raise is not in the L1",
 ("Humboldt", "2018-05-24"): "L1 flat at 1.36 / 2.75 and report 2.70 for W1 (+1.34 as in 2011); the logger clock is 254 d off at this visit",
 ("Petermann Glacier", "2003-05-06"): "L1 HW1 = HW2 (identical series): one sensor is duplicated in the L1; the report has 1.85 / 3.09 before and 0.77 after",
 ("Petermann Glacier", "2004-05-09"): "L1 HW1 = HW2 (identical series)",
 ("CP2", "1999-05-28"): "L1 HW1 before is in the blind zone (0.1-0.5 m)",
 ("CP2", "2000-06-03"): "L1 HW2 jumps +1.65 m as reported (+1.64) but HW1 does not move (1.5 before and after) while the report has 0.44 to 2.10: L1 HW1 before the visit is wrong; all four CP2 reports are 0.3-0.4 m above L1 HW2",
 ("CP2", "1998-05-30"): "L1 +1.0 m for HW1 as reported (+1.09); the L1 is 0.2-0.4 m below the report",
 ("NASA-U", "1999-05-13"): "before 0.50 / 1.80: the L1 has no HW1 before the visit; the after values are 0.75-1.05 m above the L1 after",
 ("JAR1", "2011-05-08"): "ablation site: L1 HW is flat for a month after the visit but jumps by 0.5 m on 2011-06-15; HW2 1.76 reported against 1.26 in the L1 (spacing 0.34 m in the L1 against 1.21 reported)",
 ("JAR1", "2012-05-09"): "L1 HW1 / HW2 0.48 / 1.59 against 1.07 / 2.45 reported (+0.6 / +0.9) with the L1 rising 0.3 m per week by melt from 2012-05-17 on: the level at the visit is not in the L1 (gap)",
 ("JAR2", "2004-05-25"): "HW2 of the L1 is within 0.1 m of HW1 (spacing -0.06 m from 2001-08 to 2005-04) while the report has a spacing of 1.44 m: L1 HW2 is a copy of HW1 or its offset is wrong",
 ("JAR2", "2011-06-21"): "L1 HW1 and HW2 are 1.2 and 1.2 m (identical) on the report date, then rise by melt: spacing 0 in the L1 against 1.22 reported; the sensors are also swapped in the L1 from 2011-05-31",
 ("Crawford Point 1", "2012-05-01"): "W1 after 2.53 against 3.14 in the L1 (flat): +0.6 offset; W2 after 3.72 has no L1 (HW2 is gone from 2012-03)",
 ("DYE-2", "2004-06-13"): "both sensors 0.3-0.4 m above the L1 after the visit; spacing 1.12 reported against 0.99 in the L1",
 ("Saddle", "2011-05-10"): "W2 after 3.73 against 3.28 in the L1 (+0.45) while W1 after 2.13 has no L1 (HW1 missing): report spacing 1.60 m is too large for the station (1.2 m)",
 ("Swiss Camp 10m", "2013-05-26"): "reported by K. Steffen: W1 1.24 m and the lower arm underside 0.94 m above the snow; the L1 has 2.0 m (+0.76)",
 ("NASA-U", "2011-06-01"):"both sensors 0.6-0.7 m below the L1 with no step in the L1: the after values are the level before a lowering or the report is offset",
}


def load(site):
    f = os.path.join(ROOT, "L1", "hourly", site.replace(" ", "") + ".csv")
    if not os.path.exists(f):
        return None
    fields = None
    with open(f, encoding="utf-8") as fh:
        for l in fh:
            if l.startswith("# fields"):
                fields = l.split("=", 1)[1].strip().split(",")
                break
    use = [c for c in ["timestamp", "HW1", "HW2"] if c in fields]
    d = pd.read_csv(f, comment="#", header=None, names=fields, usecols=use, na_values=["", "-999"])
    d["timestamp"] = pd.to_datetime(d["timestamp"], utc=True)
    return d.set_index("timestamp")


def levels(d, v, t, jump_min=0.25):
    if v not in d:
        return (np.nan, np.nan, False)
    s = d[v].loc[t - WIN:t + WIN].dropna()
    if len(s) < 10:
        return (np.nan, np.nan, False)
    h = s.resample("6h").median().dropna()
    dv = h.diff().abs().where(h.index.to_series().diff() < pd.Timedelta("7D"))
    # a side without data (the L1 starts after the visit or ends before it) cannot be compared
    has_b, has_a = (s.index < t - pd.Timedelta("2D")).sum() >= 10, (s.index > t + pd.Timedelta("2D")).sum() >= 10
    if dv.notna().sum() == 0 or dv.max() < jump_min:
        m = float(s.median())
        return (m if has_b else np.nan, m if has_a else np.nan, False)
    i = h.index.get_loc(dv.idxmax())
    b, a = float(h.iloc[max(0, i - 8):i].median()), float(h.iloc[i:i + 8].median())
    return (b if (has_b or i >= 8) else np.nan, a, True)


def check_reports():
    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, "metadata", "maintenance summary", "*.csv"))):
        site = os.path.basename(f)[:-4]
        d = load(site)
        if d is None:
            continue
        o = pd.read_csv(f)
        if "date" not in o:
            continue
        o["date"] = pd.to_datetime(o["date"], format="mixed", utc=True, errors="coerce")
        recs = []
        for _, r in o.iterrows():
            if pd.isna(r["date"]):
                continue
            g = lambda c: r.get(c) / 100 if pd.notna(r.get(c)) else np.nan
            rec = dict(site=site, date=r["date"], W1b=g("W1 before (cm)"), W1a=g("W1 after (cm)"), W2b=g("W2 before (cm)"), W2a=g("W2 after (cm)"))
            if all(pd.isna(rec[k]) for k in ("W1b", "W1a", "W2b", "W2a")):
                continue
            for k in (1, 2):
                rec[f"L{k}b"], rec[f"L{k}a"], rec[f"jump{k}"] = levels(d, f"HW{k}", r["date"])
            recs.append(rec)
        if not recs:
            continue
        t = pd.DataFrame(recs)
        sp = pd.concat([t.W2b - t.W1b, t.W2a - t.W1a]).dropna()
        sp = sp[(sp > 0.3) & (sp < 3)]
        typ = float(sp.median()) if len(sp) else np.nan
        for _, r in t.iterrows():
            key = (site, r.date.strftime("%Y-%m-%d"))
            for side, sd in (("b", "before"), ("a", "after")):
                spr = r[f"W2{side}"] - r[f"W1{side}"]
                for k in (1, 2):
                    w, l = r[f"W{k}{side}"], r[f"L{k}{side}"]
                    if pd.isna(w) or pd.isna(l):
                        continue
                    diff = w - l
                    if abs(diff) <= TOL:
                        continue
                    other = r[f"W{3-k}{side}"] - r[f"L{3-k}{side}"]
                    verdict = "differs"
                    if side == "a" and pd.notna(r[f"W{k}b"]) and abs(w - r[f"W{k}b"]) < 0.005 and (r[f"jump{k}"] or abs(r[f"L{k}a"] - r[f"L{k}b"]) > 0.5):
                        verdict = "copy"
                    elif pd.notna(spr) and pd.notna(typ) and abs(spr - typ) > 0.25:
                        verdict = "spacing"
                    elif pd.notna(other) and abs(other - diff) < 0.25:
                        verdict = "common_offset"
                    rows.append(dict(site=site, date=key[1], value=f"W{k} {sd}", reported_m=round(w, 2), L1_m=round(l, 2), diff_m=round(diff, 2),
                                     verdict=verdict, comment=MANUAL.get(key, "")))
    out = pd.DataFrame(rows)
    out.to_csv(os.path.join(ROOT, "metadata", "instrument_height_reference_check.csv"), index=False)
    print(out.verdict.value_counts().to_string())


def pair_anomalies():
    an = []
    for f in sorted(glob.glob(os.path.join(ROOT, "L1", "hourly", "*.csv"))):
        site = os.path.basename(f)[:-4]
        d = load(site)
        if d is None or "HW1" not in d or "HW2" not in d:
            continue
        spc = (d.HW2 - d.HW1).dropna()
        if len(spc) < 100:
            continue
        m = spc.resample("30D").median().dropna()
        n = spc.resample("30D").count().reindex(m.index)
        m = m[n >= 48]
        run = None

        def close(run):
            if run and run[0] != "ok":
                an.append(dict(site=site, kind=run[0], start=run[1].strftime("%Y-%m-%d"), end=run[2].strftime("%Y-%m-%d"),
                               median_HW2_minus_HW1=round(float(np.median(run[3])), 2)))
        for t0, v in m.items():
            lab = "HW1_above_HW2" if v < -0.1 else ("identical" if abs(v) < 0.05 else ("spacing_below_0.5" if v < 0.5 else ("spacing_above_2" if v > 2.0 else "ok")))
            if run and run[0] == lab and (t0 - run[2]).days <= 70:
                run[2] = t0
                run[3].append(v)
            else:
                close(run)
                run = [lab, t0, t0, [v]]
        close(run)
    pd.DataFrame(an).to_csv(os.path.join(ROOT, "metadata", "instrument_height_pair_anomalies.csv"), index=False)
    print(len(an), "pair anomalies")


def photo_scale():
    """Scale of the photogrammetric heights (metadata/photogrammetry_*_concat.csv, Wz1/Wz2 in units of the 0.277 m reference) that makes
    them agree with the L1: ratio L1 HW / Wz for photos taken at least 2 days away from a boom move; compared with the scale used in
    tools/read_plot_GCNet_heights_bav.py (0.45/0.277 = 1.62, 1.1 at Tunu-N, 1.3 at NASA-U / Humboldt / Saddle)."""
    import re
    alias = {"CP1": "Crawford Point 1", "DY2": "DYE-2", "EGP": "EastGRIP", "NAU": "NASA-U", "HUM": "Humboldt", "SUM": "Summit", "GIT": "GITS",
             "JR3": "JAR3", "NSE": "NASA-SE", "TUN": "Tunu-N", "JAR": "JAR1", "JR2": "JAR2", "NAE": "NASA-E", "SDM": "South Dome", "NEM": "NEEM",
             "SWC": "Swiss Camp", "SW1": "Swiss Camp 10m", "SDL": "Saddle", "NGP": "NGRIP", "PET": "Petermann ELA", "CP2": "CP2"}
    used = {"Tunu-N": 1.1, "NASA-U": 1.3, "Humboldt": 1.3, "Saddle": 1.3}
    f = pd.read_csv(os.path.join(ROOT, "metadata", "photogrammetry_20220726T150919_instrument_height_files_concat.csv"))
    f["site"] = f.site.replace(alias)
    rows, cache = [], {}
    for _, r in f.iterrows():
        m = re.search(r"(\d{4})[ _-](\d{2})[ _-](\d{2})", r.filename)
        if not m:
            continue
        date = pd.Timestamp(int(m[1]), int(m[2]), int(m[3]), tz="UTC")
        if r.site not in cache:
            cache[r.site] = load(r.site)
        d = cache[r.site]
        if d is None:
            continue
        for k in (1, 2):
            w = r[f"Wz{k}"]
            if not (w > 0.2):
                continue
            x = d[f"HW{k}"].loc[date - pd.Timedelta("2D"):date + pd.Timedelta("2D")].dropna()
            if len(x) < 20:
                continue
            h = x.resample("6h").median().dropna()
            if len(h) > 2 and h.diff().abs().max() > 0.4:
                continue
            rows.append(dict(site=r.site, ratio=float(x.median()) / w))
    t = pd.DataFrame(rows)
    g = t.groupby("site").ratio.describe(percentiles=[.25, .5, .75])[["count", "25%", "50%", "75%"]].round(2)
    g.columns = ["n_photos_sensors", "ratio_q25", "ratio_median", "ratio_q75"]
    g["scale_used_in_plot"] = [used.get(i, round(0.45 / 0.277, 2)) for i in g.index]
    g.to_csv(os.path.join(ROOT, "metadata", "photogrammetry_scale_check.csv"))
    print(g.to_string())


if __name__ == "__main__":
    check_reports()
    pair_anomalies()
    photo_scale()

# -*- coding: utf-8 -*-
"""Writes metadata/calibration_overview.md: every calibration factor that is applied to the radiation channels and to the pressure,
station by station, and whether it equals what the instrument tables document.

Read from the repository (nothing is hardcoded but the documented tables):
  - the [calibration.<var>] and [[calibration_period]] blocks of every logger-file configuration file (L0/*/*/*.toml)
  - metadata/adjustments/*.csv rows with multiply / add on ISWR, OSWR, NR, P (and the time_shift / swap rows, counted)
  - metadata/c_level_corrections.csv
  - the documented values: metadata/calibration factors/calfac_originally_used.txt (station default: SWin, SWref, NetRad pos / neg, pressure
    offset) and calfac_qcheck_matlab.csv (LiCor factor of the reflected-radiation sensor, 2014-2019)

A factor is DOCUMENTED when it equals the table (ISWR = SWin; OSWR = SWref x LiCor, with LiCor 0.934 unless the table says otherwise;
NR = the two net-radiometer factors; P = the pressure offset) within 1 %. Anything else is listed as NOT DOCUMENTED, with the reason the configuration file
gives. Run from the repository root:  python tools/calibration_overview.py
"""
import glob, os, re, sys, tomllib, collections
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())


# station, channel, period, action, where, evidence, independent check (CARRA ssrd / sp are not assimilated for radiation; keep in sync with release_note_2026.md section 8)
UNDOCUMENTED = [
    ("NASA-U", "ISWR", "2018-05-22 on", "x1.15", "`calibration_period` in the 2018, 2021, 2023 configuration files",
     "new radiometers installed 2018-05-22/23 (field book), program scale not recorded; ISWR/CARRA falls 1.07 to 0.88 with OSWR/CARRA unchanged, albedo 0.95-0.98", "CARRA ssrd"),
    ("NASA-U", "OSWR", "1998-1999, 2003-2018", "scale 182, then 198.64 (= 71.918 x 2.762)", "configuration files, `c_level_corrections.csv`",
     "raw scale gives summer albedo 0.30, 0.84 with the factor; Jason file albedo 0.78", "albedo, C-level overlap"),
    ("Petermann Glacier", "ISWR, OSWR", "2002-2006", "scale 73.5 for both (was 186-189)", "configuration files of the 5 CR10X files",
     "ISWR/CARRA 2.0-2.5 with the former scales, 0.89-0.98 with 73.5; V11 holds 73.5 in 2002 only; NR = a ISWR - b OSWR gives b/a 1.03-1.18 (same factor for the pair); no table, T_calib_pet.dat of 2003 not in the repository", "CARRA ssrd, net radiation"),
    ("Crawford Point 1", "ISWR", "2005 to 2010-05-09, then on", "x1.139, x1.105", "`metadata/adjustments/Crawford Point 1.csv`",
     "spring albedo 0.83 in 1995-2004 (8 springs 0.81-0.84, network 0.82-0.86), 0.94-0.99 from 2005 and 0.89-0.96 after 2010; no service documented", "CARRA ssrd says ISWR (ISWR/CARRA 1.05-1.12 to 0.88-1.05, OSWR/CARRA flat)"),
    ("Swiss Camp", "OSWR", "1995-1997; 2012-05-10 on", "x1.055; x0.926", "`metadata/adjustments/Swiss Camp.csv`",
     "spring albedo 0.807 in 1998-2012 (documented calibration), 0.75 in 1995-97 and 0.87 after the 2012 swap; the 10 m tower stays at its summer albedo", "CARRA ssrd says OSWR; 10 m tower"),
    ("Crawford Point 1, Swiss Camp", "ISWR, OSWR", "2012-01-01 / 2012-05-10 on", "channels swapped, x0.934 moves to ISWR, x1/0.934 to OSWR", "`swap_with_OSWR` + `calibration_period`",
     "swap found by the albedo (1.0 after 2012) and not reported; the factor placement reproduces the C-level hour by hour", "C-level overlap"),
    ("LAR1", "OSWR", "2011-11-15 on", "x1.285", "`metadata/adjustments/LAR1.csv`",
     "albedo steps 0.90 to 0.70 at the 2011-11-14 service with ISWR unchanged (field notes McGrath document the service, not the sensor)", "none (CARRA does not cover Antarctica)"),
    ("NASA-E, GITS, NGRIP", "OSWR", "1999-2011", "documented x 0.934 (66.0789, 186.8, 66.714)", "configuration files",
     "the LiCor factor is documented for 2014-2019 only; V11 equals it hour by hour in later years; the scales fitted to the C-level (5-7 % noise) gave albedo drifts", "V11, albedo"),
    ("JAR2", "ISWR, OSWR", "2000-2013", "83.633, 71.162", "configuration files", "the C-level equals these CR10X factors, no table", "C-level overlap"),
    ("GITS", "ISWR", "2012-2021 (CR1000)", "scale 77 (table 200)", "configuration files", "logger header; the C-level would give 1800 W/m2 peaks", "plausibility"),
    ("Crawford Point 1, JAR3", "P", "CP1 1999-05 to 2010-05, JAR3 from 2002-05", "multiply 1.8112 add -671.66; multiply 1.7796 add -648.88", "adjustments",
     "pressure amplitude half the true one, cause unknown", "CARRA sp, 7 peer stations (slope 1.05 and 1.01)"),
    ("Summit", "P", "2016-05-22 on", "500 + 1.3043 x (P - 600)", "adjustments", "CS106 read with CS105 constants (program not in the repository)", "NOAA GML, peer stations"),
    ("NASA-U", "P", "1999-2005, 2016 on", "add -30, -15, -40", "adjustments (issue #46)", "offsets by comparison with neighbours, cause unknown", "peer stations"),
    ("10 stations", "all", "see section C", "`time_shift` rows", "adjustments", "day from CARRA sp, hour from CARRA ssrd; two-stage method", "CARRA (sp assimilated: dating only)"),
]


def documented():
    d = pd.read_csv("metadata/calibration factors/calfac_originally_used.txt", skipinitialspace=True)
    d["key"] = d.site.map(norm)
    q = pd.read_csv("metadata/calibration factors/calfac_qcheck_matlab.csv", skipinitialspace=True)
    q["key"] = q.site.map(norm)
    lic = q.groupby("key").LiCor.agg(lambda s: sorted(set(s)))
    return d.set_index("key"), lic


def span(years):
    y = sorted(set(years))
    return f"{y[0]}" if y[0] == y[-1] else f"{y[0]}-{y[-1]}"


def why(text):
    """one short reason from the free text of a configuration file `source` field"""
    t = (text or "").strip()
    if not t:
        return "no reason recorded"
    if t.startswith("differs: C-level"):
        return "fitted to the C-level overlap"
    if "CARRA" in t:
        return "CARRA ssrd"
    if "header" in t.lower():
        return "logger header"
    if "Jason" in t:
        return "Jason C-level file"
    return t[:70].replace("|", "/")


def close(a, b, tol=0.01):
    return a is not None and b is not None and b != 0 and abs(a / b - 1) <= tol


def main():
    doc, lic = documented()
    out = ["# Calibration overview (generated by `tools/calibration_overview.py`)", "",
           "Every factor below is read from the configuration files / metadata files; **documented** means equal (within 1 %) to the instrument tables in "
           "`metadata/calibration factors` (ISWR = SWin; OSWR = SWref x LiCor factor, 0.934 where the table has none; NR = the two net-radiometer "
           "factors; P = the offset written by the logger program). **Not documented** = the factor comes from the C-level overlap, the albedo or "
           "CARRA, and the reason is in the `source` field of the configuration file or in the comment of the adjustment row.", ""]
    # ---- A. configuration file scales
    rows = collections.defaultdict(lambda: collections.defaultdict(list))   # (station, var) -> value -> [(year, file)]
    src = {}
    for p in sorted(glob.glob("L0/*/*/*.toml")):
        st = p.split(os.sep)[1][3:] if os.sep in p else p.split("/")[1][3:]
        base = os.path.basename(p)[:-5]
        m = re.match(r"(\d{4})", base)
        yr = int(m.group(1)) if m else 0
        d = tomllib.load(open(p, "rb"))
        for v in ("ISWR", "OSWR", "NR", "P"):
            c = d.get("calibration", {}).get(v)
            if not c:
                continue
            if "scale" in c:
                key = (round(c["scale"], 4),)
            elif "scale_pos" in c:
                key = (round(c["scale_pos"], 3), round(c["scale_neg"], 3))
            else:
                continue
            if v == "P":
                key = (c.get("add", 0), c.get("scale", 1))
            rows[(st, v)][key].append((yr, base))
            src[(st, v, key)] = c.get("source", "")
    out += ["## A. Scales in the logger-file configuration files", "",
            "| Station | Variable | Documented | Scale used (years, number of files) | Status |", "|---|---|---|---|---|"]
    n_doc = n_not = 0
    for (st, v) in sorted(rows):
        k = norm(st.replace("10m", ""))
        d = doc.loc[k] if k in doc.index else None
        li = lic.get(k, [0.934]) if k in lic.index else [0.934]
        if d is not None:
            if v == "ISWR": ref = [d.SWin]
            elif v == "OSWR": ref = sorted({d.SWref * x for x in li} | {d.SWref})
            elif v == "NR": ref = [(d.NetRadPos, d.NetRadNeg)]
            else: ref = [(d.PressureOffset, 1)]
            reftxt = " / ".join(str(round(x, 3)) if not isinstance(x, tuple) else f"{x[0]} / {x[1]}" for x in ref)
        else:
            ref, reftxt = [], "no table"
        parts, nd = [], 0
        for key, lst in sorted(rows[(st, v)].items(), key=lambda kv: min(y for y, _ in kv[1])):
            if d is None:
                ok = None
            elif v == "NR":
                kp, kn = (key[0], key[1]) if len(key) == 2 else (key[0], key[0])
                ok = any(close(kp, r[0]) and close(kn, r[1]) for r in ref)
            elif v == "P":
                ok = any(abs(key[0] - r[0]) < 1e-6 and abs(key[1] - 1) < 1e-6 for r in ref)
            else:
                ok = any(close(key[0], r) for r in ref)
            tag = {True: "ok", False: "NOT", None: "?"}[ok]
            extra = f" [{why(src.get((st, v, key), ''))}]" if ok is False else ""
            parts.append(f"{'/'.join(str(x) for x in key)} ({span([y for y, _ in lst])}, {len(lst)}) {tag}{extra}")
            nd += ok is False
        if d is None:
            status = "no table for this station"
        else:
            status = "all documented" if nd == 0 else f"{nd} scale(s) not documented"
            n_doc += nd == 0
            n_not += nd > 0
        out.append(f"| {st} | {v} | {reftxt} | {'; '.join(parts)} | {status} |")
    out += ["", f"({n_doc} station-variables fully documented, {n_not} with at least one scale that is not; ok = equals the table, NOT = differs, ? = no table.)", ""]
    # ---- B. calibration_period
    cp = collections.defaultdict(list)
    for p in sorted(glob.glob("L0/*/*/*.toml")):
        st = p.split("/")[1][3:] if "/" in p else p.split(os.sep)[1][3:]
        d = tomllib.load(open(p, "rb"))
        for b in d.get("calibration_period", []):
            cp[(st, b["variable"], str(b["start"])[:10], str(b["end"])[:10], b["multiply"], b.get("reason", ""))].append(os.path.basename(p))
    out += ["## B. Factors that change inside a file (`[[calibration_period]]`)", "",
            "| Station | Variable | From | To | Multiply | Files | Reason |", "|---|---|---|---|---|---|---|"]
    for (st, v, a, b, m, r), fl in sorted(cp.items()):
        out.append(f"| {st} | {v} | {a} | {b[:10] if not b.startswith('2100') else 'open'} | {m} | {len(fl)} | {r[:230]} |")
    out.append("")
    # ---- C. adjustments
    out += ["## C. Adjustments of the measurement (`metadata/adjustments`)", "",
            "| Station | Variable | Function | From | To | Value | Comment |", "|---|---|---|---|---|---|---|"]
    ts = collections.Counter(); sw = collections.Counter()
    for f in sorted(glob.glob("metadata/adjustments/*.csv")):
        st = os.path.basename(f)[:-4]
        try:
            d = pd.read_csv(f, comment="#", skip_blank_lines=True, dtype=str).fillna("")
        except Exception as e:
            out.append(f"| {st} | (parse error: {e}) | | | | | |")
            continue
        d.columns = [c.strip() for c in d.columns]
        for _, r in d.iterrows():
            fn, var = r["adjust_function"].strip(), r["variable"].strip()
            if fn == "time_shift":
                ts[st] += 1
            elif fn.startswith("swap") and var in ("ISWR", "OSWR"):
                out.append(f"| {st} | {var} | {fn} | {r['t0'].strip()[:10]} | {r['t1'].strip()[:10]} | | {r['comment'].strip()[:200]} |")
            elif fn in ("multiply", "add") and var in ("ISWR", "OSWR", "NR", "P"):
                out.append(f"| {st} | {var} | {fn} | {r['t0'].strip()[:10]} | {r['t1'].strip()[:10]} | {r['adjust_value'].strip()} | {r['comment'].strip()[:200]} |")
    out += ["", "Clock corrections (`time_shift` rows): " + ", ".join(f"{k} {v}" for k, v in sorted(ts.items())) + ".", ""]
    # ---- D. C-level corrections
    out += ["## D. Corrections of C-level values (`metadata/c_level_corrections.csv`)", ""]
    d = pd.read_csv("metadata/c_level_corrections.csv", comment="#")
    out += ["| Station | Variable | From | To | Multiply | Reason |", "|---|---|---|---|---|---|"]
    for _, r in d.iterrows():
        out.append(f"| {r['site']} | {r['variable']} | {str(r['t0'])[:10]} | {'' if pd.isna(r['t1']) else str(r['t1'])[:10]} | {r['multiply']} | {str(r['reason'])[:200]} |")
    out.append("")
    out += ["## E. Decisions that no document supports (kept by hand, in the order of the evidence they rest on)", "",
            "| Station | Channel | Period | What is applied | Where | Evidence | Independent check |", "|---|---|---|---|---|---|---|"]
    out += [("| " + " | ".join(r) + " |") for r in UNDOCUMENTED]
    out.append("")
    open("metadata/calibration_overview.md", "w", encoding="utf-8").write("\n".join(out))
    print("written metadata/calibration_overview.md", len(out), "lines")


if __name__ == "__main__":
    main()

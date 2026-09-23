# -*- coding: utf-8 -*-
"""Read the CR10X / CR10 / 21X logger programs stored under L0/ (EDLOG source .CSI and downloads
.DLD) and write what they say about the instruments to metadata/logger_programs/:

  programs.csv       one line per program: logger, execution interval, output arrays and the
                     number of columns they write, pressure sensor implied by the barometer constants
  measurements.csv   every measurement instruction: input location, label, multiplier, offset, comment
  output_arrays.csv  output array id, time columns and the list of averaged / sampled input locations
  notes.csv          comment lines that mention sensors, ranges, calibrations or modifications

Run from the repository root:  python tools/logger_programs.py
Raw L0 files are only read.
"""
import os
import re
import collections
import pandas as pd

MEAS = {  # instruction -> (name, {role: parameter number})
    1: ("Volt (SE)", dict(reps=1, rng=2, chan=3, loc=4, mult=5, off=6)),
    2: ("Volt (DIFF)", dict(reps=1, rng=2, chan=3, loc=4, mult=5, off=6)),
    3: ("Pulse", dict(reps=1, chan=2, cfg=3, loc=4, mult=5, off=6)),
    4: ("Excite,Delay,Volt(SE)", dict(reps=1, rng=2, chan=3, exch=4, delay=5, exmv=6, loc=7, mult=8, off=9)),
    5: ("AC Half Bridge", dict(reps=1, rng=2, chan=3, exch=4, exmv=5, loc=6, mult=7, off=8)),
    6: ("Full Bridge", dict(reps=1, rng=2, chan=3, exch=4, exmv=5, loc=6, mult=7, off=8)),
    11: ("107 Temp Probe", dict(reps=1, chan=2, exch=3, loc=4, mult=5, off=6)),
    12: ("207 RH Probe", dict(reps=1, rng=2, chan=3, loc=4, mult=5, off=6)),
    13: ("Thermocouple (SE)", dict(reps=1, rng=2, chan=3, tc=4, ref=5, loc=6, mult=7, off=8)),
    14: ("Thermocouple (DIFF)", dict(reps=1, rng=2, chan=3, tc=4, ref=5, loc=6, mult=7, off=8)),
    10: ("Battery Voltage", dict(loc=1)),
    17: ("Panel Temperature", dict(loc=1)),
    105: ("SDI-12 recorder", dict(addr=1, cmd=2, port=3, loc=4, mult=5, off=6)),
    16: ("Temperature RTD", dict(reps=1, r0=2, loc=3, mult=4, off=5)),
}
OUT = {70: "Sample", 71: "Average", 72: "Totalize", 73: "Maximize", 74: "Minimize", 75: "Std dev"}
KEYWORDS = re.compile(r"barom|cs10[56]|vaisala|pressure|range|mult|calib|kipp|li.?cor|pyran|net ?rad|q7|humid|cs500|hmp|"
                      r"wind|young|met.?one|sonic|snow|thermocouple|battery|antenna|thermistor|prt|sensor|instrument|"
                      r"added|modified|correct|offset|gain|flag", re.I)
BARO = re.compile(r"pressure|barom|cs10[56]", re.I)


def fnum(x):
    try:
        return float(str(x).replace("--", ""))
    except (TypeError, ValueError):
        return None


def parse_program(path):
    ext = os.path.splitext(path)[1].lower()
    lines = open(path, "rb").read().decode("latin-1").splitlines()
    logger = ""
    m = re.search(r"\{?(CR10X|CR10|21X|CR23X|CR21X|CR510|CR500)\}?", "\n".join(lines[:5]), re.I)
    if m:
        logger = m.group(1).upper()
    notes, insts, labels, scan = [], [], [], []
    cur, table = None, 1
    is_csi = ext == ".csi" or any(l.strip().startswith("*Table") for l in lines[:60])
    if is_csi:
        for ln in lines:
            s = ln.rstrip()
            mt = re.match(r"^\*Table (\d)", s)
            if mt:
                table, cur = int(mt.group(1)), None
                continue
            me = re.match(r"^\s*0?\d:\s+(\d+(?:\.\d+)?)\s+Execution Interval", s)
            if me:
                scan.append((table, float(me.group(1))))
                continue
            mi = re.match(r"^\s*(\d+):\s+(.*?)\s*\(P(\d+)\)", s)
            if mi and not s.startswith(" "):
                cur = dict(seq=int(mi.group(1)), table=table, code=int(mi.group(3)), params={}, comments=[], labels={})
                insts.append(cur)
                continue
            if s.startswith(";"):
                c = s.lstrip("; ").strip()
                if c:
                    notes.append(c)
                    if cur is not None:
                        cur["comments"].append(c)
                continue
            mp = re.match(r"^\s*(\d+):\s+(\S+)\s*(.*)$", s)
            if mp and cur is not None and s.startswith(" "):
                cur["params"][int(mp.group(1))] = mp.group(2)
                ml = re.search(r"\[\s*([^\]]*?)\s*\]", mp.group(3))
                if ml:
                    cur["labels"][int(mp.group(1))] = ml.group(1)
        if "-Final Storage Labels-" in "\n".join(lines):
            seg = "\n".join(lines).split("-Final Storage Labels-")[1]
            for l in seg.splitlines():
                mm = re.match(r"^(\d+),([^,~]+)(?:~\d+)?(?:,\d+)?$", l.strip())
                if mm and int(mm.group(1)) >= 1:
                    labels.append(mm.group(2))
    else:
        table = 0
        for ln in lines:
            s = ln.strip()
            if s.startswith(";:"):
                labels += [x for x in re.split(r"\s*:\s*", s[1:]) if x.strip()]
            elif s.startswith(";") and s[1:].strip():
                notes.append(s[1:].strip())
        table = 0
        for ln in lines:
            s = ln.strip()
            ms = re.match(r"^SCAN RATE\s+([\d.]+)", s)
            if ms:
                table += 1
                scan.append((table, float(ms.group(1))))
                cur = None
                continue
            mi = re.match(r"^(\d+):P(\d+)$", s)
            if mi:
                cur = dict(seq=int(mi.group(1)), table=max(table, 1), code=int(mi.group(2)), params={}, comments=[], labels={})
                insts.append(cur)
                continue
            mp = re.match(r"^(\d+):(-?[\d.]+(?:--)?)\s*$", s)
            if mp and cur is not None:
                cur["params"][int(mp.group(1))] = mp.group(2)
    return dict(logger=logger, scan=scan, insts=insts, labels=labels, notes=notes)


def time_columns(code):
    """number of time columns written by Real Time (P77): year, day, hour-minute, seconds flags"""
    s = str(code).replace(".0", "").zfill(4)
    return sum(1 for ch in s[-3:] if ch == "1") if len(s) >= 3 else 2


def summarize(path):
    p = parse_program(path)
    meas, arrays, cur = [], [], None
    for it in p["insts"]:
        c = it["code"]
        if c in MEAS:
            roles = MEAS[c][1]
            g = lambda r: it["params"].get(roles[r]) if r in roles else None
            meas.append(dict(table=it["table"], seq=it["seq"], instruction=f"P{c} {MEAS[c][0]}", reps=g("reps"), input_location=g("loc"),
                             label=it["labels"].get(roles.get("loc"), ""), multiplier=g("mult"), offset=g("off"),
                             comment=" | ".join(it["comments"][:3])))
        elif c in (80, 84):
            cur = dict(table=it["table"], array_id=fnum(it["params"].get(2)), outputs=[], time_code="")
            arrays.append(cur)
        elif c == 77 and cur is not None:
            cur["time_code"] = str(it["params"].get(1))
        elif c in OUT and cur is not None:
            reps = int(fnum(it["params"].get(1)) or 1)
            loc = it["params"].get(3 if c in (73, 74) else 2)
            cur["outputs"].append((OUT[c], reps, loc))
    return p, meas, arrays


def pressure_sensor(meas):
    """barometer type from the multiplier of the pressure measurement: CS105 0.184 (600-1060 hPa), CS106 0.240 (500-1100)"""
    found = set()
    for m in meas:
        txt = f"{m['label']} {m['comment']}"
        mult = fnum(m["multiplier"])
        if mult is not None and BARO.search(txt):
            if abs(mult - 0.184) < 1e-3:
                found.add("CS105 (mult 0.184, range 600-1060 hPa)")
            elif abs(mult - 0.24) < 1e-3:
                found.add("CS106 (mult 0.240, range 500-1100 hPa)")
    if not found:   # DLD files carry no labels: look for the two characteristic barometer multipliers
        for m in meas:
            mult = fnum(m["multiplier"])
            if mult is not None and abs(mult - 0.184) < 1e-6 and fnum(m["offset"]) in (200.0, 600.0, 0.0):
                found.add("CS105 (mult 0.184, range 600-1060 hPa)")
            if mult is not None and abs(mult - 0.24) < 1e-6:
                found.add("CS106 (mult 0.240, range 500-1100 hPa)")
    return "; ".join(sorted(found))


def main():
    idx, ins, arr, notes = [], [], [], []
    for root, dirs, files in os.walk("L0"):
        if "processed_bav" in root:
            continue
        for f in sorted(files):
            if os.path.splitext(f)[1].lower() not in (".csi", ".dld"):
                continue
            path = os.path.join(root, f).replace("\\", "/")
            stn = path.split("/")[1]
            try:
                p, meas, arrays = summarize(path)
            except Exception as e:
                idx.append(dict(station=stn, file=f, path=path, error=repr(e)))
                continue
            arr_txt = []
            for a in arrays:
                if a["array_id"] is None:
                    continue
                n_out = sum(o[1] for o in a["outputs"])
                n_t = time_columns(a["time_code"]) if a["time_code"] else 2
                arr_txt.append(f"{a['array_id']:g}:{1 + n_t + n_out} columns")
                arr.append(dict(station=stn, file=f, table=a["table"], array_id=a["array_id"], time_code=a["time_code"],
                                n_outputs=n_out, expected_columns_in_data_file=1 + n_t + n_out,
                                outputs=";".join(f"{o[0]}x{o[1]}@loc{o[2]}" for o in a["outputs"])))
            idx.append(dict(station=stn, file=f, path=path, type=os.path.splitext(f)[1].lower(), logger=p["logger"],
                            execution_interval=";".join(f"table {t}: {s:g} s" for t, s in p["scan"]),
                            n_measurements=len(meas), output_arrays=" | ".join(arr_txt),
                            pressure_sensor=pressure_sensor(meas), first_comment_lines=" | ".join(p["notes"][:3])[:250]))
            for m in meas:
                ins.append(dict(station=stn, file=f, **m))
            for n in p["notes"]:
                if KEYWORDS.search(n):
                    notes.append(dict(station=stn, file=f, note=n[:300]))
    os.makedirs("metadata/logger_programs", exist_ok=True)
    pd.DataFrame(idx).to_csv("metadata/logger_programs/programs.csv", index=False)
    pd.DataFrame(ins).to_csv("metadata/logger_programs/measurements.csv", index=False)
    pd.DataFrame(arr).to_csv("metadata/logger_programs/output_arrays.csv", index=False)
    pd.DataFrame(notes).drop_duplicates().to_csv("metadata/logger_programs/notes.csv", index=False)
    print(len(idx), "programs,", len(ins), "measurement instructions,", len(arr), "output arrays,", len(notes), "notes")


if __name__ == "__main__":
    main()

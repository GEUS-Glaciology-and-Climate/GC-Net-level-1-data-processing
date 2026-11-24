# -*- coding: utf-8 -*-
"""Corrections of the instrument height HW (levels that disagree with the field reports, the field books or the sensor spacing) written as
rows of metadata/adjustments/<site>.csv and metadata/flags/<site>.csv between the markers '# hw_corrections.py begin' / '# hw_corrections.py end'.
The evidence of each correction is in the comment of its rows and in release_note_2026.md (section 5, instrument heights).

HW is the height of the anemometers: a step of HW at a boom lift is real and is kept. The surface height HS = HW[first valid] - HW + HS rows has to
stay as it was, so each correction of the level of HW by +delta over [t0, t1] is paired with an HS row of +delta over the same hours (HS = HW[first] - HW
falls by delta; the pair puts it back; the rows apply to the hours t0 to t1 included in both passes of adjust_data). Stations whose HS is built
with the automatic shifts of augment_data (Summit, NASA-SE, Tunu-N, EastGRIP, LAR1, JAR1, JAR2, Petermann ELA, NGRIP, SMS) follow the steps of
HW by themselves: there a pair is only written when the HS of the old L1 was corrected by a manual HS row (pair=True).

Usage (repository root):  python tools/hw_corrections.py          lists what would be written
                          python tools/hw_corrections.py --write   writes the blocks (idempotent: a block is replaced, not appended)
"""
import os
import sys
import time

BEGIN = "# hw_corrections.py begin"
END = "# hw_corrections.py end"

# site (file name of the metadata), variable, t0, t1 ('' = to the end of the record), delta (m), pair with an HS row, evidence (no commas)
ADJ = [
    ("Humboldt", "HW1", "2011-05-15T00:00:00+00:00", "", 1.40, True,
     "L1 HW1 was 1.46 / 1.34 / 1.40 m below the report of 2011-06-01 (3.06) / the report of 2018-05-24 (2.70) / the field book of 2022-06-19 (wind sensor axis 1.66) while the raw logger HW1 is within 0.12 m of all three: the manual row of 2009-05-15 (-1.8) put HW1 1.4 m too low"),
    ("Humboldt", "HW2", "2011-05-15T00:00:00+00:00", "", 1.36, True,
     "L1 HW2 was 1.36 m below the report of 2011-06-01 (4.29) and the spacing to HW1 would be 0 after the correction of HW1 (field book 2022: wind sensors 1.25 m apart)"),
    ("Swiss Camp", "HW1", "2012-06-01T00:00:00+00:00", "", 1.04, True,
     "reports of 2013 to 2018 (2.68 / 1.40 / 1.37 / 1.82 / 1.18 m) are 1.02 to 1.09 m above the L1 HW1 which went down to 0.14 m (below the range of the sonic ranger); 2011 agreed to 0.02 m: the offset appears in the gap of 2011-07 to 2012-06"),
    ("Swiss Camp", "HW2", "2012-06-01T00:00:00+00:00", "", 1.35, True,
     "report of 2018-05-05 (2.22 m) is 1.35 m above the L1 HW2 (2013: 1.70 m)"),
    ("Crawford Point 1", "HW2", "2001-12-31T14:00:00+00:00", "2002-12-31T14:00:00+00:00", -1.06, True,
     "the source changes from the C-level to the logger at 2001-12-31 14 UTC and HW2 - HW1 jumps from 1.20 to 2.22 m in mid winter (an artefact); report of 2002-05-08 W1 1.68 / W2 2.88 and photograph of 2002-05-24 give a spacing of 1.2 to 1.3 m"),
    ("Summit", "HW1", "2005-05-04T20:00:00+00:00", "2005-05-26T06:00:00+00:00", 0.37, True,
     "the 'shift to match field notes' row of HW1 ends on 2005-05-04 19 UTC but the boom is raised on 2005-05-26: the extension removes an artefactual step of -0.36 m (report of 2005-05-26 before the visit W1 0.32)"),
    ("Summit", "HW2", "2005-05-04T22:00:00+00:00", "2005-05-26T06:00:00+00:00", 0.84, False,
     "the 'shift to match field notes' row of HW2 ends on 2005-05-04 21 UTC but the boom is raised on 2005-05-26: the extension removes an artefactual step of -0.84 m (report of 2005-05-26 before the visit W2 1.55 = the level of April)"),
]

# lines of the adjustment files that are switched off: (site, exact line, reason)
DISABLE = [
    ("Humboldt", "2023-01-01T00:00:00+00:00,,HW1,add,-1.2,Not reported. Manual shift suggested by bav.",
     "its purpose was the -1.2 m step of HS1 in 2023, which came from the HW1 rows of 2002 to 2009 (corrected above); the raw HW1 is continuous through 2023 (1.52 in 2022-11 to 1.27 in 2023-03)"),
]

# flags: HW2 identical to HW1 hour by hour (one series duplicated in the source): site, variable, t0, t1, comment
FLAGS = [
    ("Petermann Glacier", "HW2", "2002-06-14T00:00:00+00:00", "2006-05-02T00:00:00+00:00", "HW2 is a copy of HW1 (identical in 100 % of the hours: one sonic ranger in the C-level file)"),
    ("KULU", "HW2", "1999-07-01T00:00:00+00:00", "2000-09-30T00:00:00+00:00", "HW2 is a copy of HW1 (identical in 100 % of the hours in the logger files)"),
    ("Petermann ELA", "HW2", "2003-05-25T00:00:00+00:00", "2003-07-09T00:00:00+00:00", "HW2 identical to HW1 hour by hour for 635 h (a copy)"),
    ("Petermann ELA", "HW2", "2007-03-24T00:00:00+00:00", "2007-04-11T00:00:00+00:00", "HW2 identical to HW1 hour by hour for 371 h (a copy)"),
    ("JAR1", "HW2", "2010-02-27T00:00:00+00:00", "2010-04-14T00:00:00+00:00", "HW2 identical to HW1 hour by hour for 168 h (a copy)"),
]


def block_adj(rows):
    out = [BEGIN, "# written by tools/hw_corrections.py (2026-11-24): corrections of the level of HW with the matching HS row that leaves HS unchanged"]
    for site, var, t0, t1, d, pair, why in rows:
        out.append("%s,%s,%s,add,%+.2f,%s" % (t0, t1, var, d, why))
        if pair:
            hs = "HS" + var[-1]
            out.append("%s,%s,%s,add,%+.2f,pair of the %s row above: HS = HW[first] - HW is kept as it was" % (t0, t1, hs, d, var))
    out.append(END)
    return out


def block_flags(rows):
    out = [BEGIN]
    for site, var, t0, t1, why in rows:
        out.append("%s,%s,%s,NAN,%s (2026-11-24),"  % (t0, t1, var, why))
    out.append(END)
    return out


def put_block(path, lines, disable=()):
    s = open(path, encoding="utf-8", newline="").read()
    eol = "\r\n" if "\r\n" in s else "\n"
    s = s.replace("\r\n", "\n")
    if BEGIN in s:
        a, b = s.index(BEGIN), s.index(END) + len(END)
        s = s[:a].rstrip("\n") + "\n" + s[b:].lstrip("\n")
    for line, why in disable:
        if line in s:
            s = s.replace(line, "# 2026-11-24 switched off by tools/hw_corrections.py: %s\n# %s" % (why, line))
        elif ("# " + line) not in s:
            print("WARNING: line to switch off not found in", path)
    s = s.rstrip("\n") + "\n\n" + "\n".join(lines) + "\n"
    data = s.replace("\n", eol).encode("utf-8")
    for k in range(20):      # the folder is synced/scanned by other programs: a write can fail briefly with 'Invalid argument'
        try:
            with open(path, "wb") as f:
                f.write(data)
            return
        except OSError:
            time.sleep(1.5)
    raise OSError("could not write " + path)


if __name__ == "__main__":
    write = "--write" in sys.argv
    sites = sorted({r[0] for r in ADJ} | {d[0] for d in DISABLE})
    for site in sites:
        rows = [r for r in ADJ if r[0] == site]
        lines = block_adj(rows)
        p = os.path.join("metadata", "adjustments", site + ".csv")
        print(p)
        print("\n".join("   " + l[:200] for l in lines))
        if write:
            put_block(p, lines, [(d[1], d[2]) for d in DISABLE if d[0] == site])
    for site in sorted({r[0] for r in FLAGS}):
        rows = [r for r in FLAGS if r[0] == site]
        lines = block_flags(rows)
        p = os.path.join("metadata", "flags", site + ".csv")
        print(p)
        print("\n".join("   " + l[:200] for l in lines))
        if write:
            put_block(p, lines)

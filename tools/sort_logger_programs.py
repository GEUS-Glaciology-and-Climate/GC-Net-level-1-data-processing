# -*- coding: utf-8 -*-
"""Moves logger PROGRAM files (.dld/.DLD, .csi/.CSI - the instructions the datalogger runs, not raw data) that sit
loose among the raw data files into a single 'Logger programs' folder per station, next to (not inside)
'CR10X logger files' etc. Most stations already have such a folder (case varies: 'Logger programs' /
'logger programs'); this only picks up files that are NOT already under one.

Nothing is deleted and no raw DATA file is touched (registered CR10X/CR1000 files are matched by exact name in
CR10X_file_registry.csv / the station header and are never .dld/.csi). tools/logger_programs.py already finds
program files anywhere in L0 (os.walk), so moving them does not break it.

Only the standard numbered station directories (L0/<NN>-<name>/) are touched; top-level folders that are not one
station's own tree (L0/DataLogger Programs, L0/Swiss Camp Science tower) are left alone.

Usage (repository root): python tools/sort_logger_programs.py [--write]
Without --write, prints what would be moved (a dry run) rather than moving anything.
"""
import os
import sys
import shutil

EXT = (".dld", ".csi")


def target_dir(stn_dir):
    """the station's existing 'Logger programs' folder (any case), or 'Logger programs' if none exists yet"""
    for name in os.listdir(stn_dir):
        if name.lower() == "logger programs" and os.path.isdir(os.path.join(stn_dir, name)):
            return os.path.join(stn_dir, name)
    return os.path.join(stn_dir, "Logger programs")


def main(write):
    n_move, n_skip = 0, 0
    for stn_dir in sorted(d for d in os.listdir("L0") if d[:2].isdigit() and os.path.isdir(os.path.join("L0", d))):
        base = os.path.join("L0", stn_dir)
        dest = target_dir(base)
        for root, dirs, files in os.walk(base):
            if "logger program" in os.path.basename(root).lower():
                continue   # already sorted into a 'Logger program(s)' folder of its own, leave it where it is
            for f in files:
                if not f.lower().endswith(EXT):
                    continue
                src = os.path.join(root, f)
                dst = os.path.join(dest, f)
                if os.path.exists(dst):
                    print(f"SKIP (name clash with {dst}): {src}")
                    n_skip += 1
                    continue
                print(f"{src}  ->  {dst}")
                n_move += 1
                if write:
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(src, dst)
    print(f"\n{n_move} file(s) {'moved' if write else 'to move'}, {n_skip} skipped (name clash)" + ("" if write else " -- dry run, pass --write to apply"))


if __name__ == "__main__":
    main("--write" in sys.argv)

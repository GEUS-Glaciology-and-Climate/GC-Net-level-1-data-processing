# -*- coding: utf-8 -*-
"""
Level 0 -> L0M: stacks the raw logger files of every station into one NEAD file (L0M/<station>.csv).

L0M contains logger data only: nothing from the C-level files (they fill the gaps at L1), no filtering and no convention
conversion. Every raw file (CR1000 or CR10X, including Swiss Camp 10 m's year-embedded CR10X format) is read and
calibrated through its own <file>.toml sidecar (liblogger.read_configured_files; tools/generate_logger_configs.py
writes these) - a file without one is simply skipped, so a new one only needs a .toml next to it, no code change.
Two things are not yet on this path:
    Swiss Camp 10 m CR27 files                     libgcnet.load_old_logger_file (its own hardcoded parser)
    transmissions (L0 data, after the last         liblogger.read_transmissions
        logger record; nothing is downloaded)
Values are calibrated as soon as they are read (the .toml's [calibration] table), so L0M already holds physical units.
For every station the file each value comes from is written to L0M/provenance/ and illustrated in figures/L0_sources/.
"""
import numpy as np
import pandas as pd
import os
from lib import libgcnet as gc
from lib import liblogger
from lib import write_nead
# path to save raw L0 downloaded from envidat
path = "./L0/"
# path to save merged nead + c level files
mcpath = "./L0M/"
os.makedirs(mcpath, exist_ok=True)

# path to ini/header files for NEAD outputs
l0inipath = "./L0/L0_ini/"
# transmissions received before the envidat API was closed (used after the last logger record)
backup_transmissions = path + "backup_transmissions_20230111/"

# Get sorted list of all non-hidden sub-directories in L0 folder
L0dirs = np.array(sorted(f for f in os.listdir(path) if "-" in f))


# %% Loop through each station, read the logger files and stack them
for i in range(len(L0dirs)):
    print("--------------------------------")
    print("Now Processing Directory: ", L0dirs[i])
    # the file structure of raw campbell data files
    datadir = path + L0dirs[i] + "/CR1000 logger files/"
    cr10xdir = path + L0dirs[i] + "/CR10X logger files/"
    configfile = l0inipath + L0dirs[i] + "_header.ini"
    site = L0dirs[i][3:]
    # make path for the merged nead file
    mcoutfile = mcpath + L0dirs[i]

    # ---- the logger files, one reader for any type (via each file's own .toml); None when the station has none
    print("\nLooking for CR1000 logger files:")
    df_cr1000, prov_cr1000 = (None, None)
    if os.path.isdir(datadir):
        df_cr1000, prov_cr1000 = liblogger.read_configured_files(datadir, priority="earliest_first")

    print("\nLooking for CR10X logger files:")
    df_cr10x_swc, df_cr10x, prov_cr10x = None, None, None
    if os.path.isdir(cr10xdir):
        try:
            # cumulative downloads overlap: the most recent file wins where they do, every timestamp appears once
            df_cr10x, prov_cr10x = liblogger.read_configured_files(cr10xdir, priority="latest_first")
            if df_cr10x is not None:
                print(f"  {df_cr10x.notna().sum().sum()} calibrated values from {prov_cr10x.stack().nunique()} file(s)")
        except Exception as e:
            # do not lose the whole run for one station: it is written from its other logger files
            print("!!!!! Reading the configured CR10X files of", site, "failed:", repr(e), "-- CR10X data NOT used !!!!!")
            df_cr10x = None

    df_cr27 = None
    if site == "Swiss Camp 10m":
        print("\nLoading CR27 logger files")
        df_cr27 = gc.load_old_logger_file()

    # ---- putting the logger files together
    if site == "Swiss Camp 10m":
        # three loggers in succession: the newest has priority where two of them have the same hour, so that every timestamp
        # appears once (a repeated timestamp used to be averaged at L1, junk rows included)
        dfm, prov = liblogger.combine_sources([(df_cr1000, "CR1000"),
                                               (df_cr10x, prov_cr10x),
                                               (df_cr27, "CR27 and older files")])
    else:
        # CR1000 data have priority, the CR10X files fill what the CR1000 files do not have
        dfm, prov = liblogger.combine_sources([(df_cr1000, "CR1000"),
                                               (df_cr10x, prov_cr10x)])

    # ---- transmissions are L0 data too (nothing is downloaded any more: the envidat API is gone). They stand in for the
    # logger files after the last logger record; earlier than that the C-level files fill the gaps at L1.
    tr, tr_label = liblogger.read_transmissions(site, path + L0dirs[i] + "/transmissions/",
                                                backup_transmissions,
                                                after=dfm.index.max() if dfm is not None else None)
    if tr is not None:
        print("Transmissions used after the last logger record:", tr_label, tr.index.min(), "->", tr.index.max(), len(tr), "records")
        dfm, prov = liblogger.stack_sources([(dfm, prov), (tr, tr_label)])

    # ---- output
    # The C-level files are NOT used here: L0M is the stack of the logger files and nothing else.
    # (they fill the gaps at L1, GC-Net-level-1-data-processing.py, where the conversions they need are made and illustrated;
    # here they are only drawn as a grey line in the origin plots)
    if dfm is None:
        print("No logger files for station:", L0dirs[i],
              "- no L0M file (its data come from the C-level files at L1)")
        continue

    dfm["timestamp"] = pd.to_datetime(dfm.index, utc=True)
    write_nead.write_nead(dfm, configfile, mcoutfile)

    # which file every value comes from: table for L1 and illustration
    try:
        fields = [f for f in write_nead.get_config_list_str(configfile, "fields")
                  if f != "timestamp" and f in dfm.columns and f in prov.columns]
        uniq = ~dfm.index.duplicated(keep="first")
        print("Origin of the values in L0M (all variables, hours):\n", prov[fields].stack().value_counts().to_string())
        os.makedirs("L0M/provenance", exist_ok=True)
        liblogger.source_windows(prov[fields]).to_csv("L0M/provenance/" + L0dirs[i] + "_source_windows.csv", index=False)
        # the C-level data are read for the illustration only (grey line: differences with the previous versions); they are not used in L0M
        c_level, _ = liblogger.read_c_level(L0dirs[i], path)
        liblogger.plot_sources(site, dfm.loc[uniq, fields], prov.loc[uniq, fields], c_level, "figures/L0_sources/" + L0dirs[i] + ".png")
    except Exception as e:
        print("Origin plot / provenance failed for", site, ":", repr(e))

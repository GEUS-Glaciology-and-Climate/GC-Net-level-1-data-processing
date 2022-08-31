#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:54:18 2022

@author: Jason, Maiken, Baptiste

https://github.com/GEUS-Glaciology-and-Climate/pyNEAD

"""

import nead
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
import numpy as np
import pandas as pd
from datetime import datetime
import os
from os import path
import write_nead
import libgcnet as gc

path = "./L0/"

site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)[15:16]
# you can select a site by specifying f.e.:
# site_list  = site_list.iloc[2:3,:]
# site_list  = site_list.iloc[7:8,:]
site_list = site_list.iloc[2:3, :]  # Crawford Point 1

for site, ID in zip(site_list.Name, site_list.ID):
    print("# " + str(ID) + " " + site)
    filename = "L1/" + str(ID).zfill(2) + "-" + site + ".csv"

    # %% Jason's output file
    cconfigfile = "./L0//C level Jason/c_file_header_jeb.ini"
    c_file_header_str = write_nead.get_config_list_str(cconfigfile, "fields")
    cfiledir_jeb = path + "/C level Jason/" + str(ID).zfill(2) + "c.dat"

    dfc_jeb = gc.read_c_file(cfiledir_jeb, c_file_header_str)
    dfc_jeb.index = pd.to_datetime(dfc_jeb.index, utc=True)

    plt.figure()
    dfc_jeb[["HS1", "HS2", "HW1", "HW2"]].plot()
    plt.title(site)

    # %% Compiling Jason's intermediate files
    dfc_raw = pd.DataFrame()
    for year in range(1998, 2005):
        print(year)
        dfc_raw = dfc_raw.append(
            pd.read_csv(
                "C:/Users/bav/GitHub/JEB_GC-Net-master/output/"
                + str(ID).zfill(2)
                + "_"
                + str(year)
                + "c.dat",
                header=None,
                delim_whitespace=True,
            )
        )

    dfc_raw.columns = c_file_header_str[: len(dfc_raw.columns)]
    dfc_raw["date"] = pd.to_datetime(dfc_raw["year"], format="%Y") + pd.to_timedelta(
        dfc_raw["DoY"] - 1, unit="d"
    )
    dfc_raw = dfc_raw.set_index("date")

    plt.figure()
    dfc_raw[["HW1", "HW2"]].plot()
    plt.title("as in files 15_<year>c.dat")
    plt.figure()
    dfc_jeb[["HW1", "HW2"]].plot()
    plt.title("as in file 15c.dat")

    # %% As in the envidat files
    l0inipath = "./L0N_ini/"
    cfiledir = (
        "L0/" + str(ID).zfill(2) + "-" + site + "/C file/" + str(ID).zfill(2) + "c.dat"
    )

    cconfigfile = l0inipath + "c_file_header.ini"
    c_file_header_str = write_nead.get_config_list_str(cconfigfile, "fields")
    dfc = gc.read_c_file(cfiledir, c_file_header_str)
    dfc.index = pd.to_datetime(dfc.index, utc=True)

    flag1 = dfc.HS1.notnull() & dfc.HW1.isnull()
    flag2 = dfc.HS2.notnull() & dfc.HW2.isnull()

    plt.figure()
    dfc.loc[flag1][["HS1", "HS2", "HW1", "HW2"]].plot()
    dfc.loc[flag2][["HS1", "HS2", "HW1", "HW2"]].plot()
    plt.title(site)

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

th = 1  # line thickness
font_size = 22
plt.rcParams["font.size"] = font_size
plt.rcParams["axes.facecolor"] = "w"
plt.rcParams["axes.edgecolor"] = "k"
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 1
plt.rcParams["grid.color"] = "#cccccc"
plt.rcParams["legend.facecolor"] = "w"
plt.rcParams["mathtext.default"] = "regular"
plt.rcParams["grid.linewidth"] = th
plt.rcParams["axes.linewidth"] = th  # set the value globally
plt.rcParams["figure.figsize"] = 12, 10
plt.rcParams["legend.framealpha"] = 0.8


site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)
# you can select a site by specifying f.e.:
# site_list  = site_list.iloc[2:3,:]
# site_list  = site_list.iloc[7:8,:]
# site_list  = site_list.iloc[2:3,:] # Crawford Point 1

for site, ID in zip(site_list.Name, site_list.ID):
    print("# " + str(ID) + " " + site)
    filename = "L1/" + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        print("Warning: No file for station " + str(ID) + " " + site)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df[df == -999] = np.nan
    df["time"] = pd.to_datetime(df.timestamp)
    df = df.set_index("time")

    #% read observed instrument height data
    try:
        url = (
            "https://docs.google.com/spreadsheets/d/172LNxgYevqwO892zrc98UDMAVTQmJ0XZB5kmMLme4GM/gviz/tq?tqx=out:csv&sheet="
            + site.replace(" ", "%20")
        )
        pd.read_csv(url).to_csv("metadata/maintenance summary/" + site + ".csv")
    except:
        print("Cannot download maintenance summary. Using local file.")
        pass

    obs_df = pd.read_csv("metadata/maintenance summary/" + site + ".csv")
    obs_df["date"] = pd.to_datetime(obs_df["date"], utc=True)
    obs_df = obs_df.set_index("date")
    useful_columns = [
        "W1 before (cm)",
        "W1 after (cm)",
        "W2 before (cm)",
        "W2 after (cm)",
        "T1 before (cm)",
        "T1 after (cm)",
        "T2 before (cm)",
        "T2 after (cm)",
    ]
    if obs_df[useful_columns].notnull().sum().sum() == 0:
        print("no intrument height reported at ", site)
        continue
    obs_df[useful_columns] = obs_df[useful_columns] / 100
    # finding last index with observed instrument height:
    t_end = obs_df[useful_columns].last_valid_index()

    fig = plt.figure()
    ax = plt.subplot(111)

    sym_size = 20
    mult = 0.6
    # Plotting observed instrument heights
    obs_df["W1 before (cm)"].plot(
        ax=ax,
        marker=">",
        linestyle="None",
        markerfacecolor="none",
        markersize=sym_size * mult,
        c="C0",
        label="HW1 obs before",
    )
    obs_df["W2 before (cm)"].plot(
        ax=ax,
        marker=">",
        linestyle="None",
        markerfacecolor="none",
        markersize=sym_size * mult,
        c="C1",
        label="HW2 obs before",
    )
    obs_df["W1 after (cm)"].plot(
        ax=ax,
        marker="<",
        linestyle="None",
        markerfacecolor="none",
        markersize=sym_size * mult,
        c="C0",
        label="HW1 obs after",
    )
    obs_df["W2 after (cm)"].plot(
        ax=ax,
        marker="<",
        linestyle="None",
        markerfacecolor="none",
        markersize=sym_size * mult,
        c="C1",
        label="HW2 obs after",
    )

    obs_df["T1 before (cm)"].plot(
        ax=ax,
        marker=">",
        linestyle="None",
        markerfacecolor="none",
        markersize=sym_size * mult,
        c="C2",
        label="HT1 obs before",
    )
    obs_df["T2 before (cm)"].plot(
        ax=ax,
        marker=">",
        linestyle="None",
        markerfacecolor="none",
        markersize=sym_size * mult,
        c="C3",
        label="HT2 obs before",
    )
    obs_df["T1 after (cm)"].plot(
        ax=ax,
        marker="<",
        linestyle="None",
        markerfacecolor="none",
        markersize=sym_size * mult,
        c="C2",
        label="HT1 obs afer",
    )
    obs_df["T2 after (cm)"].plot(
        ax=ax,
        marker="<",
        linestyle="None",
        markerfacecolor="none",
        markersize=sym_size * mult,
        c="C3",
        label="HT2 obs after",
    )

    df["HW1"].plot(ax=ax, c="C0", label="HW1")
    df["HW2"].plot(ax=ax, c="C1", label="HW2")

    ax.set_xlim(df.index[0] - pd.Timedelta(days=60), t_end + pd.Timedelta(days=90))
    plt.ylabel("Height above surface (m)")
    plt.title(site + " profile instrument heights")
    plt.legend()
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

    plt.savefig(
        "figures/L1_overview/instrument_height_assessment/"
        + site
        + "_height_comparison.png",
        bbox_inches="tight",
        dpi=250,
    )
    print(
        "![](../figures/L1_overview/instrument_height_assessment/"
        + site.replace(" ", "%20")
        + "_height_comparison.png)"
    )

#%run tools/tocgen.py out/L1_intrument_heights.md out/L1_intrument_heights_toc.md

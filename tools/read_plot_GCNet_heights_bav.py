# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""


import nead
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import os
from os import path
os.chdir('..')

name_alias = {
    "CP1": "Crawford Point 1", "DY2": "DYE2",
    "EGP": "E-GRIP", "NAU": "NASA-U",
    "HUM": "Humboldt", "SUM": "Summit",
    "GIT": "GITS", "JR3": "JAR3",
    "NSE": "NASA-SE", "TUN": "Tunu-N",
    "JAR": "JAR1", "JR2": "JAR2",
    "NAE": "NASA-E", "SDM": "South Dome",
    "NEM": "NEEM", "SWC": "Swiss Camp",
    "SW1": "Swiss Camp 10m", "SDL": "Saddle",
    "NGP": "NGRIP", "PET": "Petermann ELA", "CP2": "CP2",
}

site_list = pd.read_csv("L1/GC-Net_location.csv", header=0, skipinitialspace=True)
# uncomment for use at specific sites
# All station names: 'Swiss Camp 10m', 'Swiss Camp', 'Crawford Point 1', 'NASA-U',
# 'GITS', 'Humboldt', 'Summit', 'Tunu-N', 'DYE2', 'JAR1', 'Saddle',
# 'South Dome', 'NASA-E', 'CP2', 'NGRIP', 'NASA-SE', 'KAR', 'JAR 2',
# 'KULU', 'Petermann ELA', 'NEEM', 'E-GRIP'
site_list = site_list.loc[site_list.Name.values == 'NASA-SE',:]

for site, ID in zip(site_list.Name, site_list.ID):
    print("# " + str(ID) + " " + site)
    filename = "L1/hourly/" + site.replace(" ", "") + ".csv"
    if not path.exists(filename):
        print("Warning: No file for station " + str(ID) + " " + site)
        # continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df[df == -999] = np.nan
    df["time"] = pd.to_datetime(df.timestamp)
    df = df.set_index("time")

    # read observed instrument height data
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
    obs_df["date"] = pd.to_datetime(obs_df["date"], format='mixed', utc=True)
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
        # continue
    obs_df[useful_columns] = obs_df[useful_columns] / 100

    # read photogrammetry heights
    df_photo = pd.read_csv(
        "metadata/photogrammetry_20220726T150919_instrument_height_files_concat.csv"
    )
    df_photo = df_photo.replace({"site": name_alias})
    df_photo = df_photo.loc[df_photo.site == site, :]
    for var in ["month", "day", "Wz1", "Wz2", "THz1", "THz2"]:
        df_photo[var] = pd.to_numeric(df_photo[var], errors="coerce").values
    df_photo.loc[df_photo.month.isnull(), "month"] = np.round(df_photo.month.mean())
    df_photo.loc[df_photo.day.isnull(), "day"] = np.round(df_photo.day.mean())
    df_photo["date"] = pd.to_datetime(df_photo[["year", "month", "day"]])
    df_photo = df_photo.set_index("date").drop(columns=["site", "year", "month", "day"])

    # df_photo[['Wz1','Wz2','THz1','THz2']] = df_photo[['Wz1','Wz2','THz1','THz2']].values

    df_photo_m = pd.read_csv("metadata/photogrammetry_instrument_height_20220425.csv")
    df_photo_m = df_photo_m.replace({"site": name_alias})
    df_photo_m = df_photo_m.loc[df_photo_m.site == site, :]
    df_photo_m["date"] = pd.to_datetime(df_photo_m[["year", "month", "day"]])
    df_photo_m = df_photo_m.set_index("date").drop(
        columns=["site", "year", "month", "day"]
    )

    fig = plt.figure(figsize=(20, 6))
    ax = plt.subplot(1,2,1) 

    sym_size = 10

    plt.plot(np.nan,np.nan,'w',label='adjusted from sonic rangers:')
    df["HW1"].plot(ax=ax, c="C0", label="HW1")
    df["HW2"].plot(ax=ax, c="C1", label="HW2")
    
    # Plotting observed instrument heights
    if obs_df[useful_columns].notnull().sum().sum() > 0:
        plt.plot(np.nan,np.nan,'w',label='from field reports:')
        obs_df["W1 before (cm)"].plot(
            ax=ax,
            marker=">",
            linestyle="None",
            markerfacecolor="C0",
            markersize=sym_size,
            markeredgecolor='k',
            label="HW1 before maintenance",
        )
        obs_df["W2 before (cm)"].plot(
            ax=ax,
            marker=">",
            linestyle="None",
            markerfacecolor="C1",
            markersize=sym_size,
            markeredgecolor='k',
            label="HW2 before maintenance",
        )
        obs_df["W1 after (cm)"].plot(
            ax=ax,
            marker="<",
            linestyle="None",
            markerfacecolor="C0",
            markersize=sym_size,
            markeredgecolor='k',
            label="HW1 after maintenance",
        )
        obs_df["W2 after (cm)"].plot(
            ax=ax,
            marker="<",
            linestyle="None",
            markerfacecolor="C1",
            markersize=sym_size,
            markeredgecolor='k',
            label="HW2 after maintenance",
        )

    scale = 0.45/0.277
    if site == 'Tunu-N':
        scale = 1.1
    if site == 'NASA-U':
        scale = 1.3
    if site == 'Humboldt':
        scale = 1.3
    if site == 'Saddle':
        scale = 1.3
    plt.plot(np.nan,np.nan,'w',label='from photos:')
    if df_photo[["Wz1", "Wz2"]].notnull().sum().sum() > 0:
        if site == 'Summit':
            df_photo.loc[df_photo.Wz1*scale>5.2, 'Wz1'] = np.nan
            df_photo.loc[df_photo.Wz2*scale>5.2, 'Wz2'] = np.nan
            df_photo.loc['1999', 'Wz1'] = np.nan
            df_photo.loc['1999', 'Wz2'] = np.nan
            ind =  (df_photo.index.year == 2005) & (df_photo.Wz2<0.6)
            df_photo.loc[ind, 'Wz2'] = np.nan

        (df_photo.Wz1*scale).plot(
            ax=ax, marker="o", markerfacecolor="C0",
            markeredgecolor='k',  linestyle="None", label='HW1')
        (df_photo.Wz2*scale).plot(
            ax=ax, marker="o", markerfacecolor="C1",
            markeredgecolor='k', linestyle="None", label='HW2')
    # if df_photo[["THz1", "THz2"]].notnull().sum().sum() > 0:
    #     (df_photo[["Wz1", "Wz2", "THz1", "THz2"]]*0.45/0.277).plot(
    #         ax=ax, marker="o", linestyle="None"
    #     )
    if df_photo_m[["Wz1", "Wz2", "THz1", "THz2"]].notnull().sum().sum() > 0:
        df_photo_m[["Wz1", "Wz2", "THz1", "THz2"]].plot(
            ax=ax, marker="x", linestyle="None"
        )

    plt.ylabel("Instrument heights (m)")
    plt.ylim(0, df[["HW1","HW2"]].max().max()*1.2)
    plt.xlabel("Year")
    plt.title(site)
    plt.legend()
    plt.grid()
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

    plt.savefig(
        "figures/L1_overview/instrument_height_assessment/"
        + site.replace(" ", "")
        + "_height_comparison.png",
        bbox_inches="tight",
        dpi=250,
    )
    print(
        "![](../figures/L1_overview/instrument_height_assessment/"
        + site.replace(" ", "")
        + "_height_comparison.png)"
    )

#%run tools/tocgen.py out/L1_intrument_heights.md out/L1_intrument_heights_toc.md

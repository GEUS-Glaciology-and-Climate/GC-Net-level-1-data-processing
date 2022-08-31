# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import os, sys
import PROMICE_toolbox as ptb
import matplotlib.pyplot as plt
import pandas as pd
import nead
import os.path
import numpy as np
from os import path

path_to_L0N = "L0M/"
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)
# print(site_list)
site_list = site_list.iloc[8:9, :]  # DYE-2
for site, ID in zip(site_list.Name, site_list.ID):
    plt.close("all")
    print("# " + str(ID) + " " + site)
    filename = path_to_L0N + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        print("Warning: No file for station " + str(ID) + " " + site)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp).dt.tz_localize("UTC")
    df = df.set_index("timestamp")
    df = df.resample("H").mean()

# %% loading Samira's data
df_ucalg = pd.read_excel(
    "C:/Users/bav/OneDrive - Geological survey of Denmark and Greenland/Data/Dye-2/Samimi 2016 Dye-2/AWS_Samimi_Marshall_Dye2_Summer2016.xlsx",
    skiprows=5,
)
df_ucalg.columns = [
    "time",
    "decimal day",
    "record",
    "Battery",
    "logger T",
    "airT",
    "RH",
    "Pressure",
    "SW in",
    "SW out",
    "CNR1TK",
    "LW in",
    "LW out",
    "windspd",
    "winddir",
    "std winddir",
]
df_ucalg["time"] = pd.to_datetime(df_ucalg.time, utc=True) + pd.Timedelta(hours=2)
df_ucalg = df_ucalg.set_index("time").resample("H").mean()

fig = plt.figure()
(df.P).plot(label="GC-Net")
df_ucalg.Pressure.plot(label="U.Calg.")
plt.xlim(df_ucalg.index[0], df_ucalg.index[-1])
plt.legend()
plt.title("Mean difference " + str((df_ucalg.Pressure - df.P).mean()))
fig.savefig("side analysis/Dye-2_pressure.png")

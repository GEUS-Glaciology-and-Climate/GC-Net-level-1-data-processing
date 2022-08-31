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

site = "08-DYE2"
ID = "08"
site = "06-Summit"
ID = "06"
sitename = "Summit"
ds = nead.read("./L0M/" + site + ".csv", index_col=0)
#% convert nead format to Pandas dataframe
df = ds.to_dataframe()

print(df.columns)

for column in df.columns:
    print(column)
    if column[-2:] != "qc":  # ignore quality control columns
        df[column] = pd.to_numeric(df[column])
        df[column][df[column] <= -999] = np.nan

df["date"] = pd.to_datetime(df.index)
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["hour"] = df["date"].dt.hour
df["time"] = pd.to_datetime(df[["year", "month", "day", "hour"]])

#% read observed instrument height data
obs_df = pd.read_excel(
    "./metadata/GCNet_maintenance.xlsx", sheet_name=sitename, engine="openpyxl"
)
print(obs_df)

obs_df["Date (dd-mm-yyyy HH:MM)"] = pd.to_datetime(obs_df["Date (dd-mm-yyyy HH:MM)"])
# obs_df.index = pd.to_datetime(obs_df.time)

# % importing other data files
import xarray as xr

# data received from Koni on 10102018
# df_org = xr.open_dataset("C://Users/bav/OneDrive - Geological survey of Denmark and Greenland//Data/AWS/GC-Net//10102018_jaws/"+ID+"c.dat_Req1828.nc").to_dataframe().reset_index('nbnd')

# data received from Koni on 20190501
df_ks = pd.read_csv(
    "C://Users/bav/OneDrive - Geological survey of Denmark and Greenland//Data/AWS/GC-Net//20190501/"
    + ID
    + "c.dat_Req1957",
    skiprows=54,
    sep=" ",
)

header = pd.read_csv(
    "C://Users/bav/OneDrive - Geological survey of Denmark and Greenland//Data/AWS/GC-Net//20190501/"
    + ID
    + "c.dat_Req1957",
    nrows=53,
    header=None,
)
df_ks[df_ks == 999] = np.nan
year = df_ks.iloc[:, 1].astype(str)
juliandate = np.floor(df_ks.iloc[:, 2]).astype(int).astype(str)
day_frac = df_ks.iloc[:, 2] - np.floor(df_ks.iloc[:, 2])
df_ks["date"] = pd.to_datetime(year + "-" + juliandate, format="%Y-%j") + np.array(
    [pd.Timedelta(days=x) for x in day_frac.astype(float).values]
)
df_ks = df_ks.set_index("date")

df_ks.columns = header.iloc[1:, 0].values
df_ks["wind_sensor_height_1"] = df_ks["45 WindSensorHeight1 [m]"]
df_ks["wind_sensor_height_2"] = df_ks["46 WindSensorHeight2 [m]"]

df_org = pd.read_csv(
    "C://Users/bav/GitHub/JEB_GC-Net-master/output/" + ID + "c.dat",
    header=None,
    delim_whitespace=True,
)
df_org[df_org == 999] = np.nan
df_org.columns = [
    "ID",
    "year",
    "DoY",
    "ISWR",
    "OSWR",
    "NSWR",
    "TA1",
    "TA2",
    "TA3",
    "TA4",
    "RH1",
    "RH2",
    "VW1",
    "VW2",
    "DW1",
    "DW2",
    "P",
    "HS1",
    "HS2",
    "TS1",
    "TS2",
    "TS3",
    "TS4",
    "TS5",
    "TS6",
    "TS7",
    "TS8",
    "TS9",
    "TS10",
    "V",
    "VW1_std",
    "VW2_std",
    "HW1",
    "HW2",
    "Alb",
    "unkown",
    "QC1",
    "QC2",
    "QC3",
    "QC4",
]

year = df_org.iloc[:, 1].astype(str)
juliandate = np.floor(df_org.iloc[:, 2]).astype(int).astype(str)
day_frac = df_org.iloc[:, 2] - np.floor(df_org.iloc[:, 2])
day_frac = df_org.iloc[:, 2] - np.floor(df_org.iloc[:, 2])
df_org["date"] = pd.to_datetime(year + "-" + juliandate, format="%Y-%j") + np.array(
    [pd.Timedelta(days=x) for x in day_frac.astype(float).values]
)
df_org = df_org.set_index("date")
df_org["wind_sensor_height_1"] = df_org.iloc[:, 32]
df_org["wind_sensor_height_2"] = df_org.iloc[:, 33]

# %%
# plt.figure()
# df_org.iloc[:,i].plot()
# plt.title(str(i)+' '+df_org.columns[i])
# i=i+1
# surface height 17 & 18
#%% plotting
fig = plt.figure()
ax = plt.subplot(111)


df_org.wind_sensor_height_1.plot(c="C2", marker="x", label="JEB files")
df_org.wind_sensor_height_2.plot(c="C3", marker="x", label="JEB files")
df_ks.wind_sensor_height_1.plot(c="C4", marker="o", label="CIRES files")
df_ks.wind_sensor_height_2.plot(c="C5", marker="o", label="CIRES files")
df.HW1.plot(c="C0", label="HW1", linewidth=2)
df.HW2.plot(c="C1", label="HW2", linewidth=2)

# Plotting observed instrument heights
plt.plot(
    obs_df["Date (dd-mm-yyyy HH:MM)"],
    obs_df["W1 before (cm)"] / 100,
    "*",
    markerfacecolor="none",
    markersize=26,
    c="C0",
    label="HW1 obs",
)
plt.plot(
    obs_df["Date (dd-mm-yyyy HH:MM)"],
    obs_df["W2 before (cm)"] / 100,
    "*",
    markerfacecolor="none",
    markersize=26,
    c="C1",
    label="HW2 obs",
)

plt.plot(
    obs_df["Date (dd-mm-yyyy HH:MM)"],
    obs_df["T1 before (cm)"] / 100,
    "o",
    markerfacecolor="none",
    markersize=26,
    c="C0",
    label="HT1 obs",
)
plt.plot(
    obs_df["Date (dd-mm-yyyy HH:MM)"],
    obs_df["T2 before (cm)"] / 100,
    "o",
    markerfacecolor="none",
    markersize=26,
    c="C1",
    label="HT2 obs",
)

# plt.xlim(datetime(1996, 4, 1) ,t1=datetime(end_year, 6, 21))
plt.ylabel("m")
plt.title(site + " profile instrument heights")
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import os, sys
# import PROMICE_toolbox as ptb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import nead
import os.path
from os import path
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import requests
import tocgen

os.chdir('..')

# %% L0 overview
path_to_L0N = "L0M/"
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0, skipinitialspace=True)
f = open("out/L0_overview.md", "w")
def Msg(txt):
    f = open("out/L0_overview.md", "a")
    print(txt)
    f.write(txt + "\n")
    
for site, ID in zip(site_list.Name, site_list.ID):
    plt.close("all")
    Msg("# " + str(ID) + " " + site)

    filename = path_to_L0N + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        print("Warning: No file for station " + str(ID) + " " + site)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)
    site = site.replace(" ", "")

    # % plotting variables
    def new_fig():
        fig, ax = plt.subplots(6, 1, sharex=True, figsize=(15, 15))
        plt.subplots_adjust(
            left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.2, hspace=0.05
        )
        return fig, ax

    fig, ax = new_fig()
    count = 0
    count_fig = 0
    for i, var in enumerate(df.columns):
        if var[-2:] == "qc":
            continue
        if var[-3:] == "max":
            continue
        if var[-5:] == "stdev":
            continue
        # print(var)

        if var + "_qc" in df.columns:
            print(var)

            for qc_code in np.flip(np.unique(df[var + "_qc"])):
                df.loc[df[var + "_qc"] == qc_code, var].plot(ax=ax[count])
        else:
            df[var].plot(ax=ax[count])

        ax[count].set_ylabel(var)
        ax[count].grid()

        ax[count].set_xlim((df.index[0], df.index[-1]))
        count = count + 1

        if count == 6:
            ax[0].set_title(site)
            plt.savefig(
                "figures/L0_diagnostic/" + str(ID) + "_" + site + "_" + str(count_fig),
                bbox_inches="tight",
            )
            Msg(
                "![](../figures/L0_diagnostic/"
                + str(ID)
                + "_"
                + site
                + "_"
                + str(count_fig)
                + ".png)"
            )
            count_fig = count_fig + 1
            fig, ax = new_fig()
            count = 0
    if (count < 6) & (count>0):
        count = count - 1
        ax[count].xaxis.set_tick_params(which="both", labelbottom=True)

        for k in range(count + 1, len(ax)):
            ax[k].set_axis_off()
        ax[0].set_title(site)
        plt.savefig(
            "figures/L0_diagnostic/" + str(ID) + "_" + site + "_" + str(count_fig),
            bbox_inches="tight",
        )
        Msg(
            "![](../figures/L0_diagnostic/"
            + str(ID)
            + "_"
            + site
            + "_"
            + str(count_fig)
            + ".png)"
        )
tocgen.processFile("out/L0_overview.md", "out/L0_overview_toc.md")
# %% L1 overview
site_list = pd.read_csv("L1/GC-Net_location.csv", header=0)[24:25]
# f = open("out/L1_overview.md", "w")
def Msg(txt):
    f = open("out/L1_overview.md", "a")
    print(txt)
    f.write(txt + "\n")
for site, ID in zip(site_list.Name, site_list.ID):
    plt.close("all")
    Msg("# " + str(ID) + " " + site)
    site = site.replace(" ", "")
    filename = "L1/hourly/" + site + ".csv"
    filename_d = "L1/daily/" + site + "_daily.csv"
    if not path.exists(filename):
        Msg("Warning: No file for station " + str(ID) + " " + site)
        continue
    df = nead.read(filename).to_dataframe().reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)

    df_d = nead.read(filename_d).to_dataframe().reset_index(drop=True)
    df_d.timestamp = pd.to_datetime(df_d.timestamp)
    df_d = df_d.set_index("timestamp").replace(-999, np.nan)
    
    # % plotting variables
    def new_fig():
        fig, ax = plt.subplots(6, 1, sharex=True, figsize=(15, 15))
        plt.subplots_adjust(
            left=0.1, right=0.9, top=0.95, bottom=0.1, wspace=0.2, hspace=0.05
        )
        plt.suptitle(site)
        return fig, ax

    fig, ax = new_fig()
    count = 0
    count_fig = 0
    for i, var in enumerate(df.columns):
        if var[-2:] == "qc":
            continue
        if var[-3:] == "max":
            continue
        if var[-3:] == "min":
            continue
        if var[-4:] == "flag":
            continue
        if var[-5:] == "stdev":
            continue
        if var.endswith("std"):
            continue
        if var.endswith("V"):
            continue
        if var.endswith("TA5"):
            continue
        if var in ['IUVR','ILWR']:
            continue
        if df[var].isnull().all():
            continue
        
        # print(var)
        if var == 'DTS1':
            var = [v for v in df.columns if v.startswith('DTS')]
        elif 'DTS' in var:
            continue
        elif var == 'TS1':
            var = [v for v in df.columns if v.startswith('TS')]
            var.reverse()
            if var[0] == 'TS_10m':
                var = var[1:]
                var.append('TS_10m')
        elif var.startswith('TS'):
            continue
        elif var == 'HS1':
            var = [v for v in ['HS1','HS2','HS_combined'] if v in df.columns]
        elif var in ['HS2','HS_combined']:
            continue
        elif (var == 'HW1') & ('HW2' in df.columns):
            var = ['HW1','HW2']
        elif var in ['HW2']:
            continue

        if isinstance(var, str):
            df[var].plot(ax=ax[count], label='hourly')
            df_d[var].plot(ax=ax[count], drawstyle="steps-post", label='daily')
            ax[count].set_ylabel(var)
            ax[count].legend(fontsize="x-small")
        else:
            df[var].plot(ax=ax[count])
            if len(var)>4:
                ax[count].legend(fontsize="x-small", ncol=2)
            else:
                ax[count].legend(fontsize="x-small")
        
        ax[count].grid()
        ax[count].set_xlim((df.index[0], df.index[-1]))
        count = count + 1
        if count == 6:
            plt.savefig(
                "figures/L1_overview/all_variables/"
                + str(ID)
                + "_"
                + site
                + "_"
                + str(count_fig),
                bbox_inches="tight",
            )
            Msg(
                "![](../figures/L1_overview/all_variables/"
                + str(ID)
                + "_"
                + site
                + "_"
                + str(count_fig)
                + ".png)"
            )
            count_fig = count_fig + 1
            if var != df.columns[-1]:
                fig, ax = new_fig()
                count = 0
    if count < 6:
        ax[count].xaxis.set_tick_params(which="both", labelbottom=True)
        for k in range(count, len(ax)):
            ax[k].set_axis_off()
        plt.savefig(
            "figures/L1_overview/all_variables/"
            + str(ID)
            + "_"
            + site
            + "_"
            + str(count_fig),
            bbox_inches="tight",
        )
        Msg(
            "![](../figures/L1_overview/all_variables/"
            + str(ID)
            + "_"
            + site
            + "_"
            + str(count_fig)
            + ".png)"
        )

# tocgen.processFile("out/L1_overview.md", "out/L1_overview_toc.md")

# %% data availability
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)
fig, ax = plt.subplots(1,1, figsize=(9,12))
plt.subplots_adjust(
        left=0.27, right=0.97, top=0.98, bottom=0.1, wspace=0.2, hspace=0.05
    )
count = 0
col = ['tab:orange', 'tab:red','tab:blue', 'tab:pink',]
xtick_loc = np.array([1.5])
for site, ID in zip(site_list.Name, site_list.ID):
    site = site.replace(" ", "")
    filename = "L1/" + str(ID).zfill(2) + "-" + site + "_daily.csv"
    if not path.exists(filename):
        print("Warning: No file for station " + str(ID) + " " + site)
        continue
    df = nead.read(filename).to_dataframe().reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)
    if 'ISWR' in df.columns:
        df['rad'] = df[['ISWR','OSWR']].mean(axis=1)
    else: 
        df['rad'] = np.nan
    df['t'] = df[['TA'+str(i) for i in range(1,5) if 'TA'+str(i) in df.columns]].mean(axis=1)
    df['rh'] = df[['RH'+str(i) for i in range(1,3) if 'RH'+str(i) in df.columns]].mean(axis=1)
    df['ws'] = df[['VW'+str(i) for i in range(1,3) if 'VW'+str(i) in df.columns]].mean(axis=1)
    print(site, np.round(df['t'].notnull().sum()/df['t'].shape[0]*100, 1),
          np.round(df['rh'].notnull().sum()/df['t'].shape[0]*100, 1),
          np.round(df['ws'].notnull().sum()/df['t'].shape[0]*100, 1),
          np.round(df['rad'].notnull().sum()/df['t'].shape[0]*100, 1))
    for i, var in enumerate(['rad','t','rh','ws']):
        # print(site, var,df[var].first_valid_index(), df[var].last_valid_index())
        tmp = df[var].notnull() *(-count + (i-2)/8)
        tmp[tmp==0] = np.nan
        plt.plot(tmp.index, tmp.values, color = col[i], marker='s',markersize=2)
        count = count+1
plt.yticks(np.arange(len(site_list.Name))*(-4) - 1.5,
           site_list.Name, fontsize=18)
plt.xticks([pd.to_datetime(str(y)) for y in range(1990,2025,5)],
           [(str(y)) for y in range(1990,2025,5)], 
           fontsize=18)
plt.plot(np.nan,np.nan, color = col[0], label='shortwave irradiance', linewidth = 4.5)
plt.plot(np.nan,np.nan, color = col[1], label='temperature', linewidth = 4.5)
plt.plot(np.nan,np.nan, color = col[2], label='humidity', linewidth = 4.5)
plt.plot(np.nan,np.nan, color = col[3], label='wind', linewidth = 4.5)
plt.legend(loc='lower left')
plt.grid(axis='x')
plt.minorticks_on()
plt.grid(which='minor', color='lightgray', linestyle=':')
plt.ylim(-count+1/4, 1)
plt.xlim(pd.to_datetime('1990'),pd.to_datetime('2023'))
plt.xlabel('Year')
plt.tick_params(labelbottom=True, which="both", labeltop=True, bottom=True, top=True)
for y in np.arange(len(site_list.Name))*(-4) - 3.65:
  ax.axhline(y=y, color='gray', alpha=0.5)
fig.savefig(
    "figures/L1_overview/data_availability.png",
    bbox_inches="tight",
    dpi=300
)

# %% L1 temperature overview
plt.close("all")
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)
for site, ID in zip(site_list.Name, site_list.ID):
    variable_list = np.array(["TA1", "TA2", "TA3", "TA4"])

    print("# " + str(ID) + " " + site)
    site = site.replace(" ", "")
    filename = "L1/" + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        print("Warning: No file for station " + str(ID) + " " + site)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)

    # % plotting variables
    fig, ax = plt.subplots(4, 1, sharex=True, figsize=(15, 15))
    plt.subplots_adjust(
        left=0.1, right=0.9, top=0.95, bottom=0.1, wspace=0.2, hspace=0.05
    )
    plt.suptitle(site)
    count = 0
    count_fig = 0
    if len(variable_list) == 0:
        variable_list = df.columns
    else:
        variable_list = variable_list[np.isin(variable_list, df.columns.values)]
    for i, var in enumerate(variable_list):
        df[var].plot(ax=ax[count])
        ax[count].set_ylabel(var)
        ax[count].grid()
        # ax[count].axes.xaxis.set_major_formatter(years_fmt)
        # ax[count].axes.xaxis.set_major_locator(years)
        # ax[count].axes.xaxis.set_minor_locator(months)
        ax[count].set_xlim((df.index[0], df.index[-1]))
        count = count + 1
    plt.savefig(
        "figures/L1_overview/air_temperature_diagnostic/"
        + str(ID)
        + "_"
        + site
        + "_temperature",
        bbox_inches="tight",
    )
    print(
        "![](../figures/L1_overview/air_temperature_diagnostic/"
        + str(ID)
        + "_"
        + site
        + "_temperature.png)"
    )
tocgen.processFile("out/L1_air_temperature_overview.md", "out/L1_air_temperature_overview_toc.md")

# %% L1 temperature TC vs C1000 comp
# plt.close('all')
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)
for site, ID in zip(site_list.Name, site_list.ID):

    print("# " + str(ID) + " " + site)
    site = site.replace(" ", "")

    filename = "L1/" + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        print("Warning: No file for station " + str(ID) + " " + site)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)
    if "TA2" not in df.columns:
        df["TA2"] = np.nan
    # % plotting variables
    fig = plt.figure(figsize=(15, 15))
    plt.suptitle(site)

    ax1 = fig.add_axes([0.1, 0.55, 0.5, 0.4])
    df["TA1"].plot(ax=ax1, label="TA1")
    df["TA3"].plot(ax=ax1, label="TA3")
    (df["TA1"] - df["TA3"]).plot(ax=ax1, label="TA1-TA3")
    ax1.set_ylabel("Air temperature \n Lower level")
    ax1.grid()
    ax1.legend()

    ax2 = fig.add_axes([0.65, 0.55, 0.32, 0.4])
    ax2.plot(df["TA1"], df["TA3"], marker=".", linestyle="None")
    ax2.annotate(
        "ME = %0.2f" % (df["TA1"] - df["TA3"]).mean(),
        (0.05, 0.9),
        xycoords="axes fraction",
        fontweight="bold",
    )
    ax2.annotate(
        "ME = %0.2f" % (df["TA1"] - df["TA4"]).mean(),
        (0.05, 0.8),
        xycoords="axes fraction",
    )
    ax2.plot([-50, 10], [-50, 10], "k")
    ax2.set_xlabel("TA1")
    ax2.set_ylabel("TA3")
    ax2.grid()

    ax3 = fig.add_axes([0.1, 0.1, 0.5, 0.4])
    df["TA2"].plot(ax=ax3, label="TA2")
    df["TA4"].plot(ax=ax3, label="TA4")
    (df["TA2"] - df["TA4"]).plot(ax=ax3, label="TA2-TA4")
    # (df['TA2']-df['TA3']).plot(ax=ax3, label = 'TA2-TA3')
    ax3.set_ylabel("Air temperature \n Lower level")
    ax3.grid()
    ax3.legend()

    ax4 = fig.add_axes([0.65, 0.1, 0.32, 0.4])
    ax4.plot(df["TA2"], df["TA4"], marker=".", linestyle="None")
    ax4.annotate(
        "ME = %0.2f" % (df["TA2"] - df["TA4"]).mean(),
        (0.05, 0.9),
        xycoords="axes fraction",
        fontweight="bold",
    )
    ax4.plot([-50, 10], [-50, 10], "k")
    ax4.set_xlabel("TA2")
    ax4.set_ylabel("TA4")
    ax4.grid()
    # break
    fig.savefig(
        "figures/L1_overview/air_temperature_diagnostic/"
        + str(ID)
        + "_"
        + site
        + "_temperature_diag",
        bbox_inches="tight",
    )
    print(
        "![](figures/L1_overview/air_temperature_diagnostic/"
        + str(ID)
        + "_"
        + site
        + "_temperature_diag.png)"
    )

# %% Compare two variables
var1 = 'VW1'
var2 = 'VW2'
# plt.close("all")
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)
site_list = site_list.loc[site_list.Name.values == 'NASA-E',:]
for site, ID in zip(site_list.Name, site_list.ID):
    print("# " + str(ID) + " " + site)
    site = site.replace(" ", "")
    filename = "L1/" + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        print("Warning: No file for station " + str(ID) + " " + site)
        continue

    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)
    if var2 not in df.columns:
        df[var2] = np.nan
    #  plotting variables
    fig = plt.figure(figsize=(15, 7))
    plt.suptitle(site)

    ax1 = fig.add_axes([0.1, 0.15, 0.5, 0.8])
    df[var1].plot(ax=ax1, label=var1)
    df[var2].plot(ax=ax1, label=var2)
    if 'TA' in var1:
        fact=100
    else:
        fact=100
    ((df[var1] - df[var2])*fact).resample('W').mean().plot(ax=ax1, label="(%s-%s)x%i"%(var1,var2,fact))
    ax1.set_ylabel(var1.replace('1','').replace('2',''))
    ax1.grid()
    ax1.legend()
    # if var1=='RH1':
    #     ax1.set_ylim(-10,120)

    ax2 = fig.add_axes([0.65, 0.15, 0.32, 0.8])
    ax2.plot(df[var1], df[var2], marker=".", linestyle="None")
    ax2.annotate(
        "ME = %0.2f" % (df[var1] - df[var2]).mean(),
        (0.05, 0.9),
        xycoords="axes fraction",
        fontweight="bold",
    )
    ax2.plot([20, 100], [20, 100], "k")
    ax2.set_xlabel(var1)
    ax2.set_ylabel(var2)
    ax2.grid()

    # break
    fig.savefig(
        "figures/L1_overview/variable_comparisons/" + str(ID) + "_" + site + "_"+var1+'_'+var2, bbox_inches="tight"
    )
    # print('![](figures/L1_overview/air temperature diagnostic/'+str(ID)+'_'+site+'_temperature.png)')

    # %% Time shift search
plt.close("all")
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)
from pandas.tseries.offsets import DateOffset

for site, ID in zip(site_list.Name, site_list.ID):

    print("# " + str(ID) + " " + site)
    filename = "L1/" + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        print("Warning: No file for station " + str(ID) + " " + site)
        continue

    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)

    # plt.figure()
    for year in df.index.year.unique()[:-1]:
        df1 = df.loc[df.index.year == year, :].resample("H").mean().copy()
        df2 = df.loc[df.index.year == year + 1, :].resample("H").mean().copy()
        df2.index = df2.index - DateOffset(years=1)
        msk = df2.index.intersection(df1.index)
        df1 = df1.loc[msk, :]
        df2 = df2.loc[msk, :]
        df1 = df1[~df1.index.duplicated(keep="first")].fillna(0)
        df2 = df2[~df2.index.duplicated(keep="first")].fillna(0)

        if (df1["ISWR"] != 0).any() and (df2["ISWR"] != 0).any():
            lags, cor, _, _ = plt.xcorr(
                df1["ISWR"].values,
                df2["ISWR"].values,
                usevlines=False,
                maxlags=20,
                normed=True,
                linestyle="-",
                label=str(year) + " vs " + str(year + 1),
            )
            if lags[cor.argmax()] != 0:
                print(year, "max cor at", lags[cor.argmax()], "timesteps")
                fig = plt.figure(figsize=(15, 7))
                plt.suptitle(
                    site + ": max cor at " + str(lags[cor.argmax()]) + " timesteps"
                )
                ax1 = fig.add_axes([0.1, 0.15, 0.8, 0.8])
                df1["ISWR"].plot(ax=ax1, label=str(year))
                df2["ISWR"].plot(ax=ax1, label=str(year + 1))
                ax1.set_ylabel("ISWR")
                ax1.grid()
                ax1.legend()
    # plt.grid()

    # plt.legend()

    # fig.savefig('figures/L1_overview/'+str(ID)+'_'+site+'_ISWR_diag',bbox_inches='tight')

# %% radiation overview
plt.close("all")
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0, skipinitialspace=(True))
site_list = site_list.loc[site_list.Name.values == 'JAR2',:]

for site, ID in zip(site_list.Name, site_list.ID):

    print("# " + str(ID) + " " + site)
    site_org = site
    site = site.replace(" ", "")
    filename = "L1/" + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        print("Warning: No file for station " + str(ID) + " " + site)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)
    if 'OSWR' not in df.columns:
        print('No radiation measurement')
    df["albedo"] = df.OSWR / df.ISWR
    msk = (df.OSWR < 100) | (df.ISWR < 100)
    df.loc[msk, "albedo"] = np.nan

    # Calculating zenith and hour angle of the sun
    deg2rad = np.pi / 180
    ZenithAngle_rad = df.SZA * deg2rad

    sundown = df.SZA >= 90
    df["isr_toa"] = 1372 * np.cos(
        ZenithAngle_rad
    )  # Incoming shortware radiation at the top of the atmosphere
    df.loc[sundown, "isr_toa"] = 0

    #  plotting variables
    fig, ax = plt.subplots(3, 1, sharex=True, figsize=(15, 15))
    plt.subplots_adjust(
        left=0.1, right=0.9, top=0.95, bottom=0.1, wspace=0.2, hspace=0.05
    )
    plt.suptitle(site)

    for count, var in enumerate(["ISWR", "OSWR", "albedo"]):
        if var in ["ISWR", "OSWR"]:
            df["isr_toa"].plot(ax=ax[count], color="r", alpha=0.5)
        df[var].plot(ax=ax[count])
        if var =='albedo':
            df[var].resample('D').mean().plot(ax=ax[count])

        ax[count].set_ylabel(var)
        ax[count].grid()
        ax[count].set_xlim((df.index[0], df.index[-1]))
        count = count + 1
    plt.savefig(
        "figures/L1_overview/radiation_assessment/" + str(ID) + "_" + site + "_albedo",
        bbox_inches="tight",
    )
    print(
        "![](figures/L1_overview/radiation_ assessment/"
        + str(ID)
        + "_"
        + site
        + "_albedo.png)"
    )


# %run tocgen.py out/L1_overview.md out/L1_overview_toc.md

# %% Plot some variables
plt.close('all')
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0, skipinitialspace=(True))
site_list = site_list.loc[site_list.Name == 'JAR2']

for site, ID in zip(site_list.Name, site_list.ID):

    filename = "L1/" + str(ID).zfill(2) + "-" + site.replace(" ", "") + ".csv"
    filename = "L0M/" + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        print("Warning: No file " + filename)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index('timestamp')
    print("# " + str(ID) + " " + site)
    df[['TA1','TA2']].plot()
#%% Surface height overview
plt.close('all')
site_list = pd.read_csv("L1/GC-Net_location.csv", header=0, skipinitialspace=(True))
from sklearn.linear_model import LinearRegression

fig, ax = plt.subplots(4, 5, figsize=(13, 14))
ax = ax.flatten()
plt.subplots_adjust(
    left=0.08, right=0.99, top=0.97, bottom=0.05, wspace=0.33, hspace=0.27
)
count = 0
ABC = 'ABCDEFGHIJKLMNOPQRST'.lower()
for site, ID in zip(site_list.Name, site_list.ID):
    # if site in ['Swiss Camp 10m', 'Aurora', 'KULU', 'JAR3', 'LAR1', 'LAR2', 'LAR3', 'KAR']:
    #     continue

    filename = "L1/daily/" + site.replace(" ", "") + "_daily.csv"
    if not path.exists(filename):
        print("Warning: No file " + filename)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    if df.loc[df.HS1.last_valid_index(),'HS1']<0:
        continue
    print("# " + str(ID) + " " + site)

    df = (
        df.set_index("timestamp")
        .replace(-999, np.nan)
        .interpolate(limit=7)
    )
    # plotting height
    df.HS1.plot(ax=ax[count], label='Surface height 1')
    df.HS2.plot(ax=ax[count], label='Surface height 2')
    
    for var in  ['HS1','HS2']:
        X = df.index.values.astype(float)
        Y = df[var].values
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(X[~np.isnan(X+Y)].reshape(-1, 1),
                             Y[~np.isnan(X+Y)].reshape(-1, 1))  # perform linear regression
        Y_pred = linear_regressor.predict(pd.DatetimeIndex(['2000-01-01', '2001-01-01']).values.astype(float).reshape(-1,1))
        print(-Y_pred[0] + Y_pred[-1])
        df[var+'_fit'] = linear_regressor.predict(X.reshape(-1,1))
        # df[var+'_fit'].plot(lw=0.5, ax=ax[count])

    ax[count].set_title("("+ABC[count] + ") " + site, fontsize=14)
    ax[count].set_xlabel("")
    # if count == 12:
    #     ax[count].set_xticks([pd.to_datetime(str(y)) for y in range(2000,2025,3)],
    #                          [(str(y)) for y in range(2000,2025,3)])
    #     from matplotlib.ticker import AutoMinorLocator
    #     minor_locator = AutoMinorLocator(3)
    #     ax[count].xaxis.set_minor_locator(minor_locator)
    # if count == 13:
    #     ax[count].set_xticks([pd.to_datetime(str(y)) for y in range(2000,2025,5)],
    #                          [(str(y)) for y in range(2000,2025,5)])
    #     from matplotlib.ticker import AutoMinorLocator
    #     minor_locator = AutoMinorLocator(5)
    #     ax[count].xaxis.set_minor_locator(minor_locator)
    ax[count].set_xticks([pd.to_datetime(str(y)) for y in range(1990,2022,10)])
    from matplotlib.ticker import AutoMinorLocator
    minor_locator = AutoMinorLocator(10)
    ax[count].xaxis.set_minor_locator(minor_locator)
    if count in [16]:
        ax[count].set_xticks(pd.to_datetime(['2000','2000-07-01','2001','2001-07-01'], format='mixed'))
        from matplotlib.ticker import AutoMinorLocator
        minor_locator = AutoMinorLocator(6)
        ax[count].xaxis.set_minor_locator(minor_locator)
    if count in [1, 12, 13, 14]:
        ax[count].set_xticks([pd.to_datetime(str(y)) for y in range(1990,2022,5)])
        from matplotlib.ticker import AutoMinorLocator
        minor_locator = AutoMinorLocator(5)
        ax[count].xaxis.set_minor_locator(minor_locator)
    if count in [17]:
        ax[count].set_xticks([pd.to_datetime(str(y)) for y in range(1990,2022,2)])
        from matplotlib.ticker import AutoMinorLocator
        minor_locator = AutoMinorLocator(2)
        ax[count].xaxis.set_minor_locator(minor_locator)
    if count in [15, 18,19,20]:
        ax[count].set_xticks([pd.to_datetime(str(y)) for y in range(2000,2022,1)])
        from matplotlib.ticker import AutoMinorLocator
        minor_locator = AutoMinorLocator(12)
        ax[count].xaxis.set_minor_locator(minor_locator)

    ax[count].grid()
    ax[count].set_xlim(df.HS1.first_valid_index(), df.HS1.last_valid_index())
    ax[count].tick_params(axis='both', which='major', labelsize=14)
    ax[count].xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    count = count + 1
ax[0].legend(loc='upper center', bbox_to_anchor=(2.7,1.4), ncol=2, fontsize =14)
fig.text(0.5, 0.02, "Year", ha="center", va="center", fontsize=14)
fig.text(0.02, 0.5,
    "Surface height relative to installation (m)",
    fontsize=14,
    ha="center",
    va="center",
    rotation="vertical",
)
fig.savefig("figures/L1_overview/HS_overview_accum.png", bbox_inches="tight", dpi=300)

# plt.close('all')
site_list = pd.read_csv("L1/GC-Net_location.csv", header=0, skipinitialspace=(True))

fig, ax = plt.subplots(4, 3, figsize=(12, 10))
ax = ax.flatten()
plt.subplots_adjust(
    left=0.08, right=0.99, top=0.97, bottom=0.06, wspace=0.27, hspace=0.35
)
count = 0
for site, ID in zip(site_list.Name, site_list.ID):
    if site in [ 'KULU', 'KAR', 'SMS5']:
        continue

    filename = "L1/daily/" + site.replace(" ", "") + "_daily.csv"
    if not path.exists(filename):
        print("Warning: No file " + filename)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    if df.loc[df.HS1.last_valid_index(),'HS1']>0:
        continue
    print("# " + str(ID) + " " + site)

    df = (
        df.set_index("timestamp")
        .replace(-999, np.nan)
        .interpolate(limit=7)
    )
    # plotting height
    df.HS1.plot(ax=ax[count], label='Surface height 1')
    if 'HS2' in df.columns:
        df.HS2.plot(ax=ax[count], label='Surface height 2')
    ax[count].set_title("("+ABC[count] + ") " + site, fontsize=14)
    ax[count].set_xlabel("")
    ax[count].grid()
    
    ax[count].set_xticks([pd.to_datetime(str(y)) for y in range(1990,2022,5)])
    from matplotlib.ticker import AutoMinorLocator
    minor_locator = AutoMinorLocator(5)
    ax[count].xaxis.set_minor_locator(minor_locator)
    if count in [0, 4,5,7,8,9,10,11]:
        ax[count].set_xticks([pd.to_datetime(str(y)) for y in range(1990,2022,1)])
        from matplotlib.ticker import AutoMinorLocator
        minor_locator = AutoMinorLocator(12)
        ax[count].xaxis.set_minor_locator(minor_locator)
    ax[count].tick_params(axis='both', which='major', labelsize=14)
    ax[count].xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax[count].set_xlim(df.HS1.first_valid_index(), df.HS1.last_valid_index())
    count = count + 1
ax[0].legend(loc='upper center', bbox_to_anchor=(1.9,1.5), ncol=2, fontsize =14)
fig.text(0.5, 0.02, "Year", ha="center", va="center", fontsize=14)
fig.text(0.02, 0.5,
    "Surface height relative to installation (m)",
    fontsize=14,
    ha="center",
    va="center",
    rotation="vertical",
)
fig.savefig("figures/L1_overview/HS_overview_abl.png", bbox_inches="tight", dpi=300)

# %% Ablation JAR transect

plt.close('all')
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0, skipinitialspace=(True))

fig, ax = plt.subplots(1, 1, figsize=(17, 10))
# ax = ax.flatten()
ax = [ax]
# plt.subplots_adjust(
#     left=0.05, right=0.99, top=0.92, bottom=0.08, wspace=0.15, hspace=0.5
# )
count = 0
import matplotlib
cmap = matplotlib.cm.get_cmap('tab10')

i = 0
for site, ID in zip(site_list.Name, site_list.ID):
    if site not in [ 'Swiss Camp', 'JAR1','JAR2','JAR3', 'SMS1','SMS2','SMS3','SMS4']:
        continue
    site = site.replace(" ", "")

    filename = "L1/" + str(ID).zfill(2) + "-" + site + "_daily.csv"
    if not path.exists(filename):
        print("Warning: No file " + filename)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)

    print("# " + str(ID) + " " + site)
    
    try:
        df = (
            df.set_index("timestamp")
            .replace(-999, np.nan)
            .interpolate(limit=7)
        ).loc['2002-02-01':'2002-12-01',:]
    except:
        continue
    if df.size==0:
        print('no data for ',site)
        continue
    # plotting height
    (df.HS1 - df.loc[df.HS1.first_valid_index(), 'HS1']).plot(ax=ax[count], c=cmap(i/7), label=site)
    if ('HS2' in df.columns):
        if df.HS2.first_valid_index() is not None:
            (df.HS2 - df.loc[df.HS2.first_valid_index(), 'HS2']).plot(ax=ax[count], c=cmap(i/7), label='_nolegend:_')
    i = i+1
    ax[count].set_xlabel("Year", fontsize =14)
    ax[count].set_ylabel("Surface height relative to installation (m)", fontsize =14)
    ax[count].grid()
    ax[count].set_xlim(df.HS1.first_valid_index(), df.HS1.last_valid_index())
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
ax[0].legend(loc='lower left', fontsize =14)
fig.savefig("figures/L1_overview/HS_JAR_transect.png", bbox_inches="tight")



#%% Data availability
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)  # .iloc[7:,:]
plt.close("all")
for site, ID in zip(site_list.Name, site_list.ID):
    filename = "L1/" + str(ID).zfill(2) + "-" + site.replace(" ", "") + ".csv"
    if not path.exists(filename):
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)

    df_m = df.resample("M").count() / 31 / 24 * 100
    cols = [
        col
        for col in [
            "ISWR",
            "OSWR",
            "NR",
            "TA1",
            "TA2",
            "TA3",
            "TA4",
            "RH1",
            "RH2",
            "VW1",
            "DW1",
            "VW2",
            "DW2",
            "P",
            "HW1",
            "HW2",
        ]
        if col in df_m.columns
    ]
    cols.reverse()
    df_m = df_m[cols]

    fig = plt.figure(figsize=(12, 5))
    plt.pcolor(df_m.transpose(), cmap="magma")
    major_ticks = [d for d in df_m.index if d.month == 1]
    ticks_labels = [d.year for d in df_m.index if d.month == 1]

    plt.xticks(
        np.arange(np.where(df_m.index == major_ticks[0])[0], len(major_ticks) * 12, 12),
        ticks_labels,
    )
    ax = plt.gca()
    ax.set_xticks(np.arange(0, len(df_m.index), 1), minor=True)
    plt.xticks(rotation=45)
    plt.yticks(np.arange(0.5, len(df_m.columns), 1), df_m.columns)
    plt.colorbar(label="Data availability (%)")
    plt.title(site)
    fig.savefig(
        "figures/L1_overview/data_availability_" + site.replace(" ", "_") + ".png",
        bbox_inches="tight",
    )
    print(
        "![](../figures/L1_overview/data_availability_"
        + site.replace(" ", "_")
        + ".png)"
    )


#%% Data quantity
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0).iloc[:-3,:]
plt.close("all")
df_all =pd.DataFrame()
for site, ID in zip(site_list.Name, site_list.ID):
    site = site.replace(" ", "")
    print(site)
    filename = "L1/" + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)
    df['site'] = site
    cols = [
        "site",
        "ISWR",
        "OSWR",
        "TA1",
        "TA2",
        "RH1",
        "RH2",
        "VW1",
        "DW1",
        "VW2",
        "DW2",
        "P",
    ]
    for col in cols:
        if col not in df.columns:
            df[col] = np.nan
    df = df[cols]
    df_all = df_all.append(df)

df_all.count().mean()/365/24

# %% Converting back to old format to run jaws
plt.close("all")
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0).iloc[1:2]

import json

with open("metadata/original_columns.json") as json_file:
    field_list = json.load(json_file)

fields = pd.DataFrame(field_list.items(), columns=["org_name", "nead_name"])

import os
import importlib.util
import sys

spec = importlib.util.spec_from_file_location(
    "module.name",
    "C:/Users/bav/AppData/Local/Continuum/anaconda3/lib/site-packages/jaws/jaws.py",
)
jaws = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = jaws
spec.loader.exec_module(jaws)

for site, ID in zip(site_list.Name, site_list.ID):
    filename = "L1/" + str(ID).zfill(2) + "-" + site.replace(" ", "") + ".csv"
    if not path.exists(filename):
        # print('Warning: No file for station '+str(ID)+' '+site)
        continue
    i = i + 1
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)
    df["year"] = df.index.year
    df["julian_decimal_time"] = df.index.dayofyear + df.index.hour / 24
    df["station_number"] = ID

    filename = "%02i_old_format.dat" % ID
    try:
        os.remove(filename)
    except:
        pass
    with open(filename, "a") as the_file:
        the_file.write("Data avaiable from 1995 147.0417 to 2018 142.5000 1\n")
        k = 0
        var_list = list()
        for i in fields.index.values:
            if fields.loc[i, "nead_name"] in df.columns:
                the_file.write("%i %s\n" % (k, fields.loc[i, "org_name"]))
                var_list.append(fields.loc[i, "nead_name"])
                k = k + 1
        the_file.write("\n")
    df.loc["2010":"2011", var_list].to_csv(
        filename, mode="a", index=False, header=False, sep=" ", na_rep=999
    )

    args = jaws.parse_args(
        [filename, "out.nc", "-D 9", "--flx"]
    )  #'--rigb', '--merra'])
    jaws.main(args)
    stations = jaws.get_stations()

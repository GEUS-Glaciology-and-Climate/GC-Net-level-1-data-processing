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

# Set the locator


# %% L0 overview
path_to_L0N = "L0M/"
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0, skipinitialspace=True)
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
        # if site != 'E-GRIP':
        #     ax[count].axes.xaxis.set_major_formatter(years_fmt)
        #     ax[count].axes.xaxis.set_major_locator(years)
        # ax[count].axes.xaxis.set_minor_locator(months)
        ax[count].set_xlim((df.index[0], df.index[-1]))
        count = count + 1

        if count == 6:
            ax[0].set_title(site)
            plt.savefig(
                "figures/L0_diagnostic/" + str(ID) + "_" + site + "_" + str(count_fig),
                bbox_inches="tight",
            )
            print(
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
    if count < 6:
        count = count - 1
        ax[count].xaxis.set_tick_params(which="both", labelbottom=True)
        # if site != "E-GRIP":
        #     ax[count].axes.xaxis.set_major_formatter(years_fmt)
        #     ax[count].axes.xaxis.set_major_locator(years)
            # ax[count].axes.xaxis.set_minor_locator(months)
        for k in range(count + 1, len(ax)):
            ax[k].set_axis_off()
        ax[0].set_title(site)
        plt.savefig(
            "figures/L0_diagnostic/" + str(ID) + "_" + site + "_" + str(count_fig),
            bbox_inches="tight",
        )
        print(
            "![](../figures/L0_diagnostic/"
            + str(ID)
            + "_"
            + site
            + "_"
            + str(count_fig)
            + ".png)"
        )
# %run tools/tocgen.py out/L0_overview.md out/L0_overview_toc.md

# %% L1 overview
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)

for site, ID in zip(site_list.Name, site_list.ID):
    plt.close("all")
    print("# " + str(ID) + " " + site)
    site = site.replace(" ", "")
    filename = "L1/" + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        print("Warning: No file for station " + str(ID) + " " + site)
        continue
    df = nead.read(filename).to_dataframe().reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index("timestamp").replace(-999, np.nan)

    df_d = nead.read(filename[:-4]+'_daily.csv').to_dataframe().reset_index(drop=True)
    df_d.timestamp = pd.to_datetime(df_d.timestamp)
    df_d = df_d.set_index("timestamp").replace(-999, np.nan)
    
    # df =df.loc['2019':,:]
    if df.shape[0] == 0:
        print("no data since 2019")
        continue
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
        # print(var)

        df[var].plot(ax=ax[count])
        df_d[var].plot(ax=ax[count], drawstyle="steps-post")
        ax[count].set_ylabel(var)
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
            print(
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
        for k in range(count + 1, len(ax)):
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
        print(
            "![](../figures/L1_overview/all_variables/"
            + str(ID)
            + "_"
            + site
            + "_"
            + str(count_fig)
            + ".png)"
        )

# %run tools/tocgen.py out/L1_overview.md out/L1_overview_toc.md

# %% data availability
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)[:-3]
fig, ax = plt.subplots(1,1, figsize=(7,10))
plt.subplots_adjust(
        left=0.27, right=0.97, top=0.98, bottom=0.1, wspace=0.2, hspace=0.05
    )
count = 0
col = ['tab:red','tab:green','tab:blue','tab:orange']
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
    df['t'] = df[['TA1','TA2','TA3','TA4']].mean(axis=1)
    df['rh'] = df[['RH1','RH2']].mean(axis=1)
    df['ws'] = df[['VW1','VW2']].mean(axis=1)

    for i, var in enumerate(['rad','t','rh','ws']):
        # print(site, var,df[var].first_valid_index(), df[var].last_valid_index())
        tmp = df[var].notnull() *(-count + (i-1.5)/3)
        tmp[tmp==0] = np.nan
        plt.plot(tmp.index, tmp.values, color = col[i], marker='s',markersize=2.5)
        count = count+1
plt.yticks(np.arange(len(site_list.Name))*(-4) - 1.5,
           site_list.Name)

plt.plot(np.nan,np.nan, color = col[0], label='radiation', linewidth = 4.5)
plt.plot(np.nan,np.nan, color = col[1], label='temperature', linewidth = 4.5)
plt.plot(np.nan,np.nan, color = col[2], label='humidity', linewidth = 4.5)
plt.plot(np.nan,np.nan, color = col[3], label='wind', linewidth = 4.5)
plt.legend(loc='lower left')

plt.ylim(-count-1, 1)
plt.xlim(pd.to_datetime('1990'),pd.to_datetime('2023'))
plt.grid()
fig.savefig(
    "figures/L1_overview/data_availability.png",
    bbox_inches="tight",
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
        "![](figures/L1_overview/air_temperature_diagnostic/"
        + str(ID)
        + "_"
        + site
        + "_temperature.png)"
    )
# %run tocgen.py out/L1_overview.md out/L1_overview_toc.md

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

# %% RH1 vs RH2
plt.close("all")
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
    if "RH2" not in df.columns:
        df["RH2"] = np.nan
    #  plotting variables
    fig = plt.figure(figsize=(15, 7))
    plt.suptitle(site)

    ax1 = fig.add_axes([0.1, 0.15, 0.5, 0.8])
    df["RH1"].plot(ax=ax1, label="RH1")
    df["RH2"].plot(ax=ax1, label="RH2")
    (df["RH1"] - df["RH2"]).plot(ax=ax1, label="RH1-RH2")
    ax1.set_ylabel("Relative Humidity (%)")
    ax1.grid()
    ax1.legend()

    ax2 = fig.add_axes([0.65, 0.15, 0.32, 0.8])
    ax2.plot(df["RH1"], df["RH2"], marker=".", linestyle="None")
    ax2.annotate(
        "ME = %0.2f" % (df["RH1"] - df["RH2"]).mean(),
        (0.05, 0.9),
        xycoords="axes fraction",
        fontweight="bold",
    )
    ax2.plot([20, 100], [20, 100], "k")
    ax2.set_xlabel("RH1")
    ax2.set_ylabel("RH2")
    ax2.grid()

    # break
    fig.savefig(
        "figures/L1_overview/" + str(ID) + "_" + site + "_RH_diag", bbox_inches="tight"
    )
    # print('![](figures/L1_overview/air temperature diagnostic/'+str(ID)+'_'+site+'_temperature.png)')
    
# %% upper vs lower level test
plt.close("all")
var1 = 'RH1'
var2 = 'RH2'

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
    df = df[[var1,var2]].resample('D').mean()
    if var2 not in df.columns:
        df[var2] = np.nan
    #  plotting variables
    fig = plt.figure(figsize=(15, 7))
    plt.suptitle(site)

    ax1 = fig.add_axes([0.1, 0.15, 0.5, 0.8])
    df[var1].plot(ax=ax1, label=var1)
    df[var2].plot(ax=ax1, label=var2)
    (df[var1] - df[var2]).plot(ax=ax1, label="TA1-TA2")
    ax1.set_ylabel("Temperature (degC)")
    ax1.grid()
    ax1.legend()

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
        "figures/L1_overview/" + str(ID) + "_" + site + "_TA_diag", bbox_inches="tight"
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
# site_list = site_list.loc[site_list.Name.values == 'Crawford Point 1',:]

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

#%% Surface height overview
plt.close('all')
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0, skipinitialspace=(True))

fig, ax = plt.subplots(4, 5, figsize=(17, 10))
ax = ax.flatten()
plt.subplots_adjust(
    left=0.05, right=0.99, top=0.94, bottom=0.12, wspace=0.15, hspace=0.5
)
count = 0
for site, ID in zip(site_list.Name, site_list.ID):
    if site in ['Swiss Camp 10m', 'Aurora', 'KULU', 'JAR3', 'LAR1', 'LAR2', 'LAR3', 'KAR']:
        continue
    print("# " + str(ID) + " " + site)
    site = site.replace(" ", "")

    filename = "L1/" + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        print("Warning: No file " + filename)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = (
        df.set_index("timestamp")
        .replace(-999, np.nan)
        .interpolate(limit=24 * 7)
        .resample("D")
        .mean()
    )
    # plotting height
    df.HS1.plot(ax=ax[count])
    df.HS2.plot(ax=ax[count])
    ax[count].set_title(str(ID) + " " + site)
    ax[count].set_xlabel("")
    ax[count].grid()
    if ID == 0:
        ax[count].set_xlim('2010','2020')
    count = count + 1
for k in range(count, len(ax)):
    ax[k].set_axis_off()
for k in [13,17,18,19]:
    ax[k].tick_params('x', labelrotation=45)
fig.savefig("figures/L1_overview/HS_overview.png", bbox_inches="tight")


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
site_list = pd.read_csv("metadata/GC-Net_location.csv", header=0)  # .iloc[7:,:]
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

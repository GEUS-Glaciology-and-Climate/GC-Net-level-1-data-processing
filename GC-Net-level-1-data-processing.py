# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:00:14 2020

tip list:
    for plots in spyder command prompte
    %matplotlib inline
    for plots in a new window
    %matplotlib qt
@author: bav
"""
import os, sys
import PROMICE_toolbox as ptb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import os.path
import numpy as np
import jaws_tools
import tocgen
from os import path
import nead

class CustomError(Exception):
    pass

if not hasattr(nead, 'build_header_obj'):
    raise CustomError('Please install the latest version of pyNEAD. \nVisit https://github.com/GEUS-Glaciology-and-Climate/pyNEAD/') 

try:
    os.mkdir("figures")
    os.mkdir("figures/L1_data_treatment")
    os.mkdir("out")
except:
    print("figures and output folders already exist")

f = open("out/Report.md", "w")
def Msg(txt):
    f = open("out/Report.md", "a")
    print(txt)
    f.write(txt + "\n")

path_to_L0 = "L0M/"
site_list = pd.read_csv("L1/GC-Net_location.csv", header=0, skipinitialspace=True)
# print(site_list)

# uncomment for use at specific sites
# All station names: 'Swiss Camp 10m', 'Swiss Camp', 'Crawford Point 1', 'NASA-U',
# 'GITS', 'Humboldt', 'Summit', 'Tunu-N', 'DYE-2', 'JAR1', 'Saddle',
# 'South Dome', 'NASA-E', 'CP2', 'NGRIP', 'NASA-SE', 'KAR', 'JAR2',
# 'KULU', 'Petermann ELA', 'NEEM', 'EastGRIP'
# site_list = site_list.loc[site_list.Name.values == 'JAR1',:]

for site, ID in zip(site_list.Name, site_list.ID):
    plt.close("all")
    Msg("# " + str(ID) + " " + site)
    filename = path_to_L0 + str(ID).zfill(2) + "-" + site + ".csv"
    if not path.exists(filename):
        Msg("Warning: No file for station " + str(ID) + " " + site)
        continue
    
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df = df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp, utc=True)
    df = df.set_index("timestamp")

    # removing unneeded fields
    col_drop = [f for f in df.columns if '_min' in f] + \
        [f for f in df.columns if '_max' in f] + \
            [f for f in df.columns if '_stdev' in f]+ \
                [f for f in df.columns if '_std' in f]
    df = df.drop(columns=col_drop)
            
    if site == "Swiss Camp 10m":
        df["TA2"] = np.nan
        df["TA4"] = np.nan

    if "HW1" not in df.columns:
        df.loc[df.HS1>900,"HS1"] = np.nan
        df["HW1"] = 2 + df["HS1"].max() - df["HS1"]
    if ("HW2" not in df.columns) & ('HS2' in df.columns):
        df.loc[df.HS2>900,"HS2"] = np.nan
        df["HW2"] = 3.4 + df["HS2"].max() - df["HS2"]
    df = df.resample("H").mean()

    Msg("## Manual flagging of data at " + site)
    df_out = ptb.flag_data(df,
                           site,
                            var_list=['HW1','HW2'], 
                           )

    Msg("## Adjusting data at " + site)
    # we start by adjusting and filtering all variables except surface height
    df_v4 = ptb.adjust_data(df_out, site,
                            # var_list=['HW1','HW2'], 
                            skip_var=["HS1", "HS2"])
    # Applying standard filters again
    df_v4 = df_v4.resample("H").asfreq()
    df_v5 = ptb.filter_data(df_v4, site)
    # ptb.plot_flagged_data(df_v5, df_out, site,
    #                         # var_list=['HW1','HW2'], 
    #                         )
    df_v5 = ptb.remove_flagged_data(df_v5)

    # correction of the net radiometer for windspeed
    if 'NR' in df_v5.columns:
        df_v5 = ptb.correct_net_rad(df_v5,site)

    # interpolating short gaps and calculating added variables
    df_v5b = ptb.augment_data(
        df_v5,
        site_list.loc[site_list.Name == site, "Latitude (°N)"].values[0],
        site_list.loc[site_list.Name == site, "Longitude (°E)"].values[0],
        site_list.loc[site_list.Name == site, "Elevation (wgs84 m)"].values[0],
        site,
    )
    # plt.figure()
    # ax1=plt.subplot(2,1,1)
    # df_v5b[['HW1','HW2']].plot(ax=ax1)
    # ax2=plt.subplot(2,1,2)
    # df_v5b[['HS1','HS2']].plot(ax=ax2)
    # ax1.set_title(site)
    # print(wtf)

    if df_v5b[[v for v in df_v5b.columns if 'TS' in v]].notnull().any().any():
        df_v6 = ptb.therm_depth(df_v5b, site)
    else:
        df_v6= df_v5b.copy()

    # removing empty rows:
    useful_var_list = [
        "ISWR",  "OSWR", "NR", "TA1", "TA2", "TA3", "TA4",  "RH1" "RH2", "P",
    ] + ["TS" + str(i) for i in range(1, 11)]
    ind_first = df_v6[
        [v for v in useful_var_list if v in df_v6.columns]
    ].first_valid_index()
    df_v6 = df_v6.loc[ind_first:, :]

    if len(df_v6) > 0:
        # get info related to the new fields
        (
            units,
            display_description,
            database_fields,
            database_fields_data_types,
        ) = ptb.field_info(df_v6.reset_index().columns)
        
        df_v6.attrs['averaging'] = 'hourly'

        # build header object
        header_obj = nead.build_header_obj(
            df_v6.reset_index(),
            metadata=ds.attrs,
            units=units,
            display_description=display_description,
            database_fields=database_fields,
            database_fields_data_types=database_fields_data_types,
        )


        # formatting and saving to file
        df_v6_formatted = df_v6.copy()
        col = [c for c in df_v6_formatted.columns if c not in ['latitude','longitude', 'elevation','timestamp']]
        df_v6_formatted[col] = df_v6_formatted[col].map(lambda x: \
                                         '' if np.isnan(x) \
                                             else '0' if abs(x)<0.005 \
                                             else '1' if abs(x-1)<0.005 \
                                             else '%0.2f'%x)
            
        df_v6_formatted['elevation'] = df_v6_formatted['elevation'].map(lambda x: \
                                         '' if np.isnan(x) else '%0.0f'%x)
        for col in ['latitude','longitude']:
            df_v6_formatted[col] = df_v6_formatted[col].map(lambda x: \
                                             '' if np.isnan(x) else '%0.3f'%x)
        print('writing hourly values')
        nead.write(
            df_v6_formatted.reset_index(),
            header_obj,
            "L1/hourly/" + site.replace(" ", "") + ".csv",
        )

        # daily average
        print('calculating daily averages')
        df_v7 = ptb.daily_average(df_v6)

        # write ini file
        header_obj = nead.build_header_obj(
            df_v7.reset_index(),
            metadata=ds.attrs,
            units=units,
            display_description=display_description,
            database_fields=database_fields,
            database_fields_data_types=database_fields_data_types,
        )
        
        # formatting and saving to file
        col = [c for c in df_v7.columns if c not in ['latitude','longitude', 'elevation','timestamp']]
        df_v7[col] = df_v7[col].map(lambda x: \
                                         '' if np.isnan(x) \
                                             else '0' if abs(x)<0.005 \
                                             else '1' if abs(x-1)<0.005 \
                                             else '%0.2f'%x)

        df_v7['elevation'] = df_v7['elevation'].map(lambda x: \
                                         '' if np.isnan(x) else '%0.0f'%x)
        for col in ['latitude','longitude']:
            df_v7[col] = df_v7[col].map(lambda x: '' if np.isnan(x) else '%0.3f'%x)
        print('writing daily averages')
        nead.write(
            df_v7.reset_index(),
            header_obj,
            "L1/daily/" + site.replace(" ", "") + "_daily.csv",
        )
        
tocgen.processFile("out/Report.md", "out/report_with_toc.md")
f.close()

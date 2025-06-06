# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import os
import time
import matplotlib.pyplot as plt
import libgcnet as gc
import glob
import write_nead
from datetime import datetime
import nead
import pytz
import json

# path to save raw L0 downloaded from envidat
path = "./L0/"
# path to save merged nead + c level files
mcpath = "./L0M/"
# path to ini/header files for NEAD outputs
l0inipath = "./L0/L0_ini/"

# Get sorted list of all non-hidden sub-directories in L0 folder
L0dirs = np.array(sorted([f for f in os.listdir(path) if not f.startswith(".")]))
msk = np.core.defchararray.find(L0dirs, ".zip") == -1
L0dirs = L0dirs[msk]
msk = np.core.defchararray.find(L0dirs, "Jason") == -1
L0dirs = L0dirs[msk]

# Create the directory to put the merged L0 + C level files (variable mcpath)
try:
    os.mkdir(mcpath)
except OSError:
    print("Data already exists or creating directory %s failed (permission?)" % mcpath)
else:
    print("Successfully created the directory %s " % mcpath)

# %% Loop through each station, read pandas dataframe and do the merging
metadata = pd.read_csv('L1/GC-Net_location.csv', skipinitialspace=True)

for i in range(len(L0dirs)):
    print("--------------------------------")
    print("Now Processing Directory: ", L0dirs[i])
    # the file structure of raw campbell data files
    datadir = path + L0dirs[i] + "/CR1000 logger files/"
    # get 2 digit station number from numered station directory
    cfilenum = str(L0dirs[i])[:2]
    # define path to historical C level file in L0 directory
    cfiledir_jeb = path + "/C level Jason/" + cfilenum + "c.dat"
    cfiledir = path + L0dirs[i] + "/C file/" + cfilenum + "c.dat"
    configfile = l0inipath + L0dirs[i] + "_header.ini"
    site = L0dirs[i][3:]

    # make path for merged C-level and Campbell nead file
    mcoutfile = mcpath + L0dirs[i]
    # get list and sort all non-hidden files in station directory
    if os.path.exists(datadir):
        allL0files = sorted([f for f in os.listdir(datadir) if not f.startswith(".")])

        # print files found in station folder:
        print("Merging the files found in the station directory:")
        [print(ii) for ii in allL0files]

        # Argos stations have 2 or 3 files per year. Find the number of unique years
        # by searching the the files containing string "Table046"
        # these are present for both ARGOS and GOES stations
        L0files = [s for s in allL0files if "Table046" in s]
        nyears = len(L0files)  # number of unique years
        print("Number of Unique years = ", nyears)

        # loop through yearly raw data files
        for j in range(nyears - 1):  # minus 1 because we index two files including j+1
            print(" ")
            print("###############################################################")
            print("Now processing files: ", L0files[j], " and ", L0files[j + 1])

            # Check if file j is ARGOS format (has a Table048)
            GOESstr = "Table046.dat"  # single file for goes stations (or first part for argos)
            ARGOSstr = "Table048.dat"  # second part of data table for ARGOS stations
            oldARGOSstr = (
                "Table050.dat"  # third part of table present in old style ARGOS
            )

            # for first dataframe check for argos files (second and third parts of table)
            df1_table48file = str(L0files[j]).replace(
                GOESstr, ARGOSstr
            )  # path and filename of a standard argos data file
            df1_table50file = str(L0files[j]).replace(
                GOESstr, oldARGOSstr
            )  # path and filename of an old style argos data file
            df1_argos_bool = os.path.isfile(
                datadir + df1_table48file
            )  # boolean True if standard argos station (2 parts of table)
            df1_oldargos_bool = os.path.isfile(
                datadir + df1_table50file
            )  # boolean True if old style argos station (3 parts of table)
            # for second data frame check for argos files (second and third parts of table)
            df2_table48file = str(L0files[j + 1]).replace(GOESstr, ARGOSstr)
            df2_table50file = str(L0files[j + 1]).replace(GOESstr, oldARGOSstr)
            df2_argos_bool = os.path.isfile(datadir + df2_table48file)
            df2_oldargos_bool = os.path.isfile(datadir + df2_table50file)

            # if processing the first year, AWS data is dataframe df1
            nan_string = ["NAN", -7999]  # strings to replace with NaN in csv files
            if j == 0:
                # if this is the first file in the station directory we read the first file
                df1_p1 = pd.read_csv(
                    datadir + L0files[j],
                    sep=",",
                    dtype=None,
                    header=0,
                    parse_dates=[0],
                    skiprows=[ii for ii in (0, 2, 3)],
                    na_values=nan_string,
                )
                # index by the timestamp
                df1_p1.set_index(df1_p1["TIMESTAMP"])
                pd.to_datetime(df1_p1.index, utc=True)

                if df1_oldargos_bool:
                    # old argos stations have three different tables per timestamp row (called 046, 048, and 050)
                    # for this condition we read all three tables and horizontally concatenate according to the timestamp index
                    df1_p3 = pd.read_csv(
                        datadir + df1_table50file,
                        sep=",",
                        dtype=None,
                        header=0,
                        parse_dates=[0],
                        skiprows=[ii for ii in (0, 2, 3)],
                        na_values=nan_string,
                    )
                    # index by the timestamp
                    df1_p3.set_index(df1_p3["TIMESTAMP"])
                    pd.to_datetime(df1_p3.index, utc=True)
                    # read part 2 of table
                    df1_p2 = pd.read_csv(
                        datadir + df1_table48file,
                        sep=",",
                        dtype=None,
                        header=0,
                        parse_dates=[0],
                        skiprows=[ii for ii in (0, 2, 3)],
                        na_values=nan_string,
                    )
                    df1_p2.set_index(df1_p2["TIMESTAMP"])
                    pd.to_datetime(df1_p2.index, utc=True)
                    df1 = pd.concat([df1_p1, df1_p2, df1_p3], axis=1)
                    df1 = df1.loc[:, ~df1.columns.duplicated()]

                elif df1_argos_bool and not df1_oldargos_bool:
                    # this is the more modern and standard ARGOS station format with 2 Tables per hourly timestamp index (046 and 048)
                    df1_p2 = pd.read_csv(
                        datadir + df1_table48file,
                        sep=",",
                        dtype=None,
                        header=0,
                        parse_dates=[0],
                        skiprows=[ii for ii in (0, 2, 3)],
                        na_values=nan_string,
                    )
                    df1_p2.set_index(df1_p2["TIMESTAMP"])
                    pd.to_datetime(df1_p2.index, utc=True)
                    df1 = pd.concat([df1_p1, df1_p2], axis=1)
                    df1 = df1.loc[:, ~df1.columns.duplicated()]
                else:
                    # this is the GOES station standard with only one data Table (046)
                    df1 = df1_p1

                # standardize column header names before merge
                df1 = gc.nameLevel0col(df1)
            # else take previous merged dataframe
            else:
                # if not the first file continue concatonating to the merged file
                df1 = dfm
            # read next file in station directory
            df2_p1 = pd.read_csv(
                datadir + L0files[j + 1],
                sep=",",
                dtype=None,
                header=0,
                parse_dates=[0],
                skiprows=[ii for ii in (0, 2, 3)],
                na_values=nan_string,
                encoding="latin-1",
            )
            df2_p1.set_index(df2_p1["TIMESTAMP"])

            # implement old ARGOS/ARGOS/GOES case structure for the files being merged
            # this means there are 3 separate tables for a single "row" in the processed data
            if df2_oldargos_bool and df2_argos_bool:
                print("and")
                print(
                    "Now processing files: ", df1_table48file, " and ", df2_table48file
                )
                print("and")
                print(
                    "Now processing files: ", df1_table50file, " and ", df2_table50file
                )
                # old argos stations have three different tables per timestamp row (called 046, 048, and 050)
                # for this condition we read all three tables and horizontally concatenate according to the timestamp index
                df2_p3 = pd.read_csv(
                    datadir + df2_table50file,
                    sep=",",
                    dtype=None,
                    header=0,
                    parse_dates=[0],
                    skiprows=[ii for ii in (0, 2, 3)],
                    na_values=nan_string,
                )
                # index by the timestamp
                df2_p3.set_index(df2_p3["TIMESTAMP"])
                pd.to_datetime(df2_p3.index, utc=True)
                # read part 2 of table
                df2_p2 = pd.read_csv(
                    datadir + df2_table48file,
                    sep=",",
                    dtype=None,
                    header=0,
                    parse_dates=[0],
                    skiprows=[ii for ii in (0, 2, 3)],
                    na_values=nan_string,
                )
                df2_p2.set_index(df2_p2["TIMESTAMP"])
                pd.to_datetime(df2_p2.index, utc=True)
                df2 = pd.concat([df2_p1, df2_p2, df2_p3], axis=1)
                df2 = df2.loc[:, ~df2.columns.duplicated()]
            elif df2_argos_bool and not df2_oldargos_bool:
                print("and")
                print(
                    "Now processing files: ", df1_table48file, " and ", df2_table48file
                )
                # this is the more modern and standard ARGOS station format with 2 Tables per hourly timestamp index (046 and 048)
                df2_p2 = pd.read_csv(
                    datadir + df2_table48file,
                    sep=",",
                    dtype=None,
                    header=0,
                    parse_dates=[0],
                    skiprows=[ii for ii in (0, 2, 3)],
                    na_values=nan_string,
                )
                df2_p2.set_index(df2_p2["TIMESTAMP"])
                pd.to_datetime(df2_p2.index, utc=True)
                df2 = pd.concat([df2_p1, df2_p2], axis=1)
                df2 = df2.loc[:, ~df2.columns.duplicated()]
            else:
                # this is the GOES station standard with only one data Table (046)
                df2 = df2_p1
            # standardize column header names before vertical concatenate
            df2 = gc.nameLevel0col(df2)

            print(
                "File 1: Start: ",
                df1["timestamp"].iloc[0],
                " End: ",
                df1["timestamp"].iloc[-1],
            )
            print("Number of records = ", len(df1["timestamp"]))
            print(
                "File 2: Start: ",
                df2["timestamp"].iloc[0],
                " End: ",
                df2["timestamp"].iloc[-1],
            )
            print("Number of records = ", len(df2["timestamp"]))
            dfm = pd.concat([df1, df2]).drop_duplicates(subset=["timestamp"])
            # dfm = dfm[~dfm.index.duplicated(keep='first')]
            # print(dfm)
        starttime = dfm["timestamp"].iloc[0]
        endtime = dfm["timestamp"].iloc[-1]
        print("-------------------------------------------------------------------")
        print("Merge Complete.")
        print("Merged File: Start: ", starttime, " End: ", endtime)
        print("Number of records = ", len(dfm["timestamp"]))
        print("The following columns have been extracted:")
        print(dfm.dtypes)

        # the ini file with the nead header for each station (determines which variables are output in the nead)

        ##### calibrate data based on header scale_factor, scale_factor_neg, and add_value
        # get string list of fields in output nead file
        fields = write_nead.get_config_list_str(configfile, "fields")
        print(fields)
        for var in fields:
            if var not in dfm.columns:
                dfm[var] = np.nan
        # get list of add_value offset calibrations
        add_value = write_nead.get_config_list(configfile, "add_value")
        # calibrate add_value for all fields
        dfm = gc.calibrate_add_value(dfm, fields, add_value)
        # get list of scale_factor values for all fields
        scale_factor = write_nead.get_config_list(configfile, "scale_factor")
        # calibrate scale_factor for all fields
        dfm = gc.calibrate_scale_factor(dfm, fields, scale_factor)
        # get list of scale_factor_neg values for all fields
        scale_factor_neg = write_nead.get_config_list(configfile, "scale_factor_neg")
        # calibrate scale_factor_neg for all fields
        dfm = gc.calibrate_scale_factor_neg(dfm, fields, scale_factor_neg)

        # if possible download and append the transmission
        print('\nTransmissions:')
        date_end = dfm.timestamp.iloc[-1].strftime("%Y-%m-%d")
        date_now = datetime.now().strftime("%Y-%m-%d")  # current date and time
                
        
        if date_end < metadata.loc[metadata.Name == site,'LastValidDate'].values[0]:
            print('Fetching latest transmission.')
            dfm = gc.get_transmission(site, 
                                   date_end, 
                                   date_now, 
                                   dfm, 
                                   path + L0dirs[i] + "/transmissions/",
                                   )
        else:
            print('Station decommissioned. No transmission.')

        starttime = pytz.utc.localize(starttime)
    else:
        dfm = []
        starttime = []

    # tries to read CR10X logger files
    print('\nLooking for CR10X logger files:')
    cr10x_info = pd.read_csv('L0/L0_ini/CR10X_all_station.ini',
                             skipinitialspace=True)
    cr10x_info = cr10x_info.loc[cr10x_info.site == site,:]
    if len(cr10x_info) > 0:
        file_list = os.listdir(path + L0dirs[i] + '/CR10X logger files')
        df_cr10x = pd.DataFrame()
        plt.figure()
        plt.title('CR10X files at SWC10m')
        dfm.set_index('timestamp').ISWR.plot()
        for f in file_list:
            print('Reading',f)
            tmp = pd.read_csv(path + L0dirs[i] + '/CR10X logger files/' + f,
                              header=None,
                              names = cr10x_info.var_list.values[0].replace( ' ','').split(','))
            tmp['timestamp'] = pd.to_datetime(tmp.year * 100000 + tmp.day_of_year * 100 + tmp.hour/100 ,
                                              format='%Y%j%H', utc=True)
            tmp[tmp==-6999] = np.nan
            # shortwave radiation calibration
            tmp.ISWR = tmp.ISWR * cr10x_info.calib_ISWR.values[0]
            tmp.OSWR = tmp.OSWR * cr10x_info.calib_OSWR.values[0]
            tmp.set_index('timestamp').ISWR.plot()
            # net radiation calibration
            msk_pos = tmp.NR>0
            tmp.loc[msk_pos, 'NR'] = tmp.loc[msk_pos, 'NR'] *cr10x_info.calib_NR_pos.values[0]
            msk_neg = tmp.NR<0
            tmp.loc[msk_neg, 'NR'] = tmp.loc[msk_neg, 'NR'] *cr10x_info.calib_NR_neg.values[0]
            df_cr10x = pd.concat([df_cr10x, tmp])
            
        print("Merging CR10X and CR1000 logger files dataframes")
        dfm = dfm.set_index("timestamp")
        df_cr10x = df_cr10x.set_index("timestamp")
        dfm = pd.concat([df_cr10x, dfm])
    else:
        print('No header specified for CR10X logger files')
    
    # if swiss camp 10 m loading old logger files
    if i == 0:
        print("\nLoading CR27 logger files")
        df_old = gc.load_old_logger_file()
        dfm = pd.concat([df_old, dfm])
        print("\nMerging CR10X and CR1000 logger files dataframes")

        
    # read and merge historical c-level file
    print('\n\nLooking for C-level files to fill the gaps')
    if os.path.isfile(cfiledir):
        cconfigfile = l0inipath + "c_file_header.ini"
        c_file_header_str = write_nead.get_config_list_str(cconfigfile, "fields")
        dfc = gc.read_c_file(cfiledir, c_file_header_str)
        dfc.index = pd.to_datetime(dfc.index, utc=True)
        
        if os.path.isfile(cfiledir_jeb):
            cconfigfile = "./L0//C level Jason/c_file_header_jeb.ini"
            c_file_header_str = write_nead.get_config_list_str(cconfigfile, "fields")
            dfc_jeb = gc.read_c_file(cfiledir_jeb, c_file_header_str)
            dfc_jeb.index = pd.to_datetime(dfc_jeb.index, utc=True)
            
            TS_col = [v for v in dfc_jeb.columns if 'TS' in v]
            dfc_jeb[TS_col] = dfc.loc[dfc_jeb.index[0]:dfc_jeb.index[-1] , TS_col]
            if isinstance(starttime, datetime):
                try:
                    starttime = pytz.utc.localize(starttime)
                except:
                    pass
                needed_dfc_jeb = dfc_jeb[
                    : np.minimum(starttime, max(dfc_jeb.index)) - pd.Timedelta(hours=1)
                ]
                print("Using the following part of the C-file: ", needed_dfc_jeb)
                msk = needed_dfc_jeb.HS1.notnull() & needed_dfc_jeb.HW1.isnull()
                needed_dfc_jeb.loc[msk, "HW1"] = -needed_dfc_jeb.loc[msk, "HS1"]
                needed_dfc_jeb.loc[msk, "HW2"] = -needed_dfc_jeb.loc[msk, "HS2"]
                end_c_file = np.minimum(starttime, max(dfc_jeb.index))
            else:
                needed_dfc_jeb = dfc_jeb
                print("Using the following part of the C-file: ", needed_dfc_jeb)
                msk = needed_dfc_jeb.HS1.notnull() & needed_dfc_jeb.HW1.isnull()
                needed_dfc_jeb.loc[msk, "HW1"] = -needed_dfc_jeb.loc[msk, "HS1"]
                needed_dfc_jeb.loc[msk, "HW2"] = -needed_dfc_jeb.loc[msk, "HS2"]
                end_c_file = max(dfc_jeb.index)
        else:
            end_c_file = []

        if not end_c_file:
            end_c_file = dfc.index[0]
        if isinstance(starttime, datetime):
            needed_dfc = dfc[end_c_file : starttime - pd.Timedelta(hours=1)]
        else:
            needed_dfc = dfc

        print("Using the following part of the C-file: ", needed_dfc)
        msk = needed_dfc.HS1.notnull() & needed_dfc.HW1.isnull()
        needed_dfc.loc[msk, "HW1"] = needed_dfc.loc[msk, "HS1"].max()-needed_dfc.loc[msk, "HS1"]
        needed_dfc.loc[msk, "HW2"] = needed_dfc.loc[msk, "HS2"].max()-needed_dfc.loc[msk, "HS2"]

        print("Merging with logger files dataframe:", dfm)
        if len(dfm) == 0:
            dfmc = needed_dfc
        elif os.path.isfile(cfiledir_jeb):
            dfm = dfm.set_index("timestamp")
            dfm.index = pd.to_datetime(dfm.index,utc=True)
            needed_dfc.index = pd.to_datetime(needed_dfc.index,utc=True)
            needed_dfc_jeb.index = pd.to_datetime(needed_dfc_jeb.index,utc=True)
            dfmc = pd.concat([needed_dfc_jeb, needed_dfc, dfm])
            del needed_dfc_jeb
        else:
            dfm = dfm.set_index("timestamp")
            dfmc = pd.concat([needed_dfc, dfm])
        dfmc["timestamp"] = pd.to_datetime(dfmc.index, utc=True)
        write_nead.write_nead(dfmc, configfile, mcoutfile)
    else:
        print("No C level file Found for station: ", L0dirs[i])
        if len(dfm)>0:
            print("Writing L0N to L0M")
            dfm["timestamp"] = pd.to_datetime(dfm.index, utc=True)
            write_nead.write_nead(dfm, configfile, mcoutfile)

    # clear dfm from memory before next station
    # del dfm
    
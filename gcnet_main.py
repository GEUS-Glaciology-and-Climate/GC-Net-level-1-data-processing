
import numpy as np
import pandas as pd
import os
import time
import matplotlib.pyplot as plt
from libgcnet import *
import glob
from write_nead import *

##################################### MAIN ####################################

##Define file to get links for GC-net Level 0 files on Envidat
linkfile = "./envidat_gcnet_links.csv"

# path to save raw L0 downloaded from envidat
path = "./L0/"
# path to save merged nead files
mpath = "./L0N/"
# path to ini/header files for NEAD outputs
l0inipath = "./L0N_ini/"

# create directory to store L0 raw data downloaded from envidat (variable path)
try:
    # make new directory in current directory called L0
    os.mkdir(path)
    # only download data if new directory was created (in try)
    #Download and unzip L0 files from CKAN API on Envidat
    getLevel0(linkfile)
except OSError:
    # Don't download data if the file already exists or other error
    print ("Data already exists or creating directory %s failed (permission?)" % path)
else:
    print ("Successfully downloaded L0 data to %s " % path)

# Get sorted list of all non-hidden sub-directories in L0 folder
L0dirs = sorted([f for f in os.listdir(path) if not f.startswith('.')])

# Create the directory to put the merged L0 files (variable mpath)
try:
    os.mkdir(mpath)
except OSError:
    print ("Data already exists or creating directory %s failed (permission?)" % mpath)
else:
    print ("Successfully created the directory %s " % mpath)

# Loop through each station, read pandas dataframe and do the merging
for i in range(len(L0dirs))  :
    print('--------------------------------')
    print('Now Processing Directory: ',L0dirs[i])
    # the file structure of raw campbell data files
    datadir = path+L0dirs[i]+'/Campbell logger files/'
    #get list and sort all non-hidden files in station directory
    allL0files = sorted([f for f in os.listdir(datadir) if not f.startswith('.')])

    #print files found in station folder:
    print('Merging the files found in the station directory:')
    [print(ii) for ii in allL0files]

    # Argos stations have 2 or 3 files per year. Find the number of unique years
    # by searching the the files containing string "Table046"
    # these are present for both ARGOS and GOES stations
    L0files = [s for s in allL0files if "Table046" in s]
    nyears = len(L0files)     # number of unique years
    print("Number of Unique years = ",nyears)
    #loop through yearly raw data files
    for j in range(nyears-1): # minus 1 because we index two files including j+1

        print('###############################################################')
        print('Now processing files: ',L0files[j],' and ',L0files[j+1])

        # Check if file j is ARGOS format (has a Table048)
        GOESstr     = "Table046.dat"    # single file for goes stations (or first part for argos)
        ARGOSstr    = "Table048.dat"    # second part of data table for ARGOS stations
        oldARGOSstr = "Table050.dat"    # third part of table present in old style ARGOS

        # for first dataframe check for argos files (second and third parts of table)
        df1_table48file = str(L0files[j]).replace(GOESstr,ARGOSstr)    #path and filename of a standard argos data file
        df1_table50file = str(L0files[j]).replace(GOESstr,oldARGOSstr) #path and filename of an old style argos data file
        df1_argos_bool = os.path.isfile(datadir+df1_table48file)       #boolean True if standard argos station (2 parts of table)
        df1_oldargos_bool = os.path.isfile(datadir+df1_table50file)    #boolean True if old style argos station (3 parts of table)
        # for second data frame check for argos files (second and third parts of table)
        df2_table48file = str(L0files[j+1]).replace(GOESstr,ARGOSstr)
        df2_table50file = str(L0files[j+1]).replace(GOESstr,oldARGOSstr)
        df2_argos_bool = os.path.isfile(datadir+df2_table48file)
        df2_oldargos_bool = os.path.isfile(datadir+df2_table50file)

        # if processing the first year, AWS data is dataframe df1
        nan_string = ["NAN",-7999]   #strings to replace with NaN in csv files
        if j==0:
            # if this is the first file in the station directory we read the first file
            df1_p1 = pd.read_csv(datadir+L0files[j],sep=',',dtype=None,header=0,parse_dates=[0],skiprows=[ii for ii in (0,2,3)],na_values=nan_string)
            # index by the timestamp
            df1_p1.set_index(df1_p1["TIMESTAMP"])
            pd.to_datetime(df1_p1.index)

            if df1_oldargos_bool:
                # old argos stations have three different tables per timestamp row (called 046, 048, and 050)
                # for this condition we read all three tables and horizontally concatenate according to the timestamp index
                df1_p3 = pd.read_csv(datadir+df1_table50file,sep=',',dtype=None,header=0,parse_dates=[0],skiprows=[ii for ii in (0,2,3)],na_values=nan_string)
                # index by the timestamp
                df1_p3.set_index(df1_p3["TIMESTAMP"])
                pd.to_datetime(df1_p3.index)
                # read part 2 of table
                df1_p2 = pd.read_csv(datadir+df1_table48file,sep=',',dtype=None,header=0,parse_dates=[0],skiprows=[ii for ii in (0,2,3)],na_values=nan_string)
                df1_p2.set_index(df1_p2["TIMESTAMP"])
                pd.to_datetime(df1_p2.index)
                df1 = pd.concat([df1_p1,df1_p2,df1_p3],axis=1)
                df1 = df1.loc[:,~df1.columns.duplicated()]

            elif df1_argos_bool and not df1_oldargos_bool:
                # this is the more modern and standard ARGOS station format with 2 Tables per hourly timestamp index (046 and 048)
                df1_p2 = pd.read_csv(datadir+df1_table48file,sep=',',dtype=None,header=0,parse_dates=[0],skiprows=[ii for ii in (0,2,3)],na_values=nan_string)
                df1_p2.set_index(df1_p2["TIMESTAMP"])
                pd.to_datetime(df1_p2.index)
                df1 = pd.concat([df1_p1,df1_p2],axis=1)
                df1 = df1.loc[:,~df1.columns.duplicated()]
            else:
                # this is the GOES station standard with only one data Table (046)
                df1 = df1_p1

            # standardize column header names before merge
            df1 = nameLevel0col(df1)
        #else take previous merged dataframe
        else:
            # if not the first file continue concatonating to the merged file
            df1=dfm
        #read next file in station directory
        df2_p1 = pd.read_csv(datadir+L0files[j+1],sep=',',dtype=None,header=0,parse_dates=[0],skiprows=[ii for ii in (0,2,3)],na_values=nan_string)
        df2_p1.set_index(df2_p1["TIMESTAMP"])
        pd.to_datetime(df2_p1.index)
        # implement old ARGOS/ARGOS/GOES case structure for the files being merged
        if df2_oldargos_bool and df2_argos_bool:
            print('and')
            print('Now processing files: ',df1_table48file,' and ',df2_table48file)
            print('and')
            print('Now processing files: ',df1_table50file,' and ',df2_table50file)
            # old argos stations have three different tables per timestamp row (called 046, 048, and 050)
            # for this condition we read all three tables and horizontally concatenate according to the timestamp index
            df2_p3 = pd.read_csv(datadir+df2_table50file,sep=',',dtype=None,header=0,parse_dates=[0],skiprows=[ii for ii in (0,2,3)],na_values=nan_string)
            # index by the timestamp
            df2_p3.set_index(df2_p3["TIMESTAMP"])
            pd.to_datetime(df2_p3.index)
            # read part 2 of table
            df2_p2 = pd.read_csv(datadir+df2_table48file,sep=',',dtype=None,header=0,parse_dates=[0],skiprows=[ii for ii in (0,2,3)],na_values=nan_string)
            df2_p2.set_index(df2_p2["TIMESTAMP"])
            pd.to_datetime(df2_p2.index)
            df2 = pd.concat([df2_p1,df2_p2,df2_p3],axis=1)
            df2 = df2.loc[:,~df2.columns.duplicated()]
        elif df2_argos_bool and not df2_oldargos_bool:
            print('and')
            print('Now processing files: ',df1_table48file,' and ',df2_table48file)
            # this is the more modern and standard ARGOS station format with 2 Tables per hourly timestamp index (046 and 048)
            df2_p2 = pd.read_csv(datadir+df2_table48file,sep=',',dtype=None,header=0,parse_dates=[0],skiprows=[ii for ii in (0,2,3)],na_values=nan_string)
            df2_p2.set_index(df2_p2["TIMESTAMP"])
            pd.to_datetime(df2_p2.index)
            df2 = pd.concat([df2_p1,df2_p2],axis=1)
            df2 = df2.loc[:,~df2.columns.duplicated()]
        else:
            # this is the GOES station standard with only one data Table (046)
            df2 = df2_p1
        # standardize column header names before vertical concatenate
        df2 = nameLevel0col(df2)

        print('File 1: Start: ',df1["timestamp"].iloc[0],' End: ',df1["timestamp"].iloc[-1])
        print('Number of records = ',len(df1["timestamp"]))
        print('File 2: Start: ',df2["timestamp"].iloc[0],' End: ',df2["timestamp"].iloc[-1])
        print('Number of records = ',len(df2["timestamp"]))
        dfm = pd.concat([df1,df2]).drop_duplicates(subset=["timestamp"])
        #dfm = dfm[~dfm.index.duplicated(keep='first')]
        #print(dfm)
    print('-------------------------------------------------------------------')
    print('Merge Complete.')
    print('Merged File: Start: ',dfm["timestamp"].iloc[0],' End: ',dfm["timestamp"].iloc[-1])
    print('Number of records = ',len(dfm["timestamp"]))
    print('The following columns have been extracted:')
    print(dfm.dtypes)
    #or print it nicely with columns separators
    #print(*dfm.columns,sep=',')

    # # # # # # #Plot parameters for each station as merging occurs
    # plt.figure()
    # plt.subplot(2,1,1)
    # plt.plot(dfm["timestamp"],dfm["P"])
    # plt.subplot(2,1,2)
    # plt.plot(dfm["timestamp"],dfm["V"])
    # plt.show()

    #### TO DO
    #filter stages
    #read and merge c-level file



    #make path/name of merged nead file the same as raw data directory
    coutfile = mpath+L0dirs[i]
    # the ini file with the nead header for each station (determines which variables are output in the nead)
    headerfile = l0inipath+L0dirs[i]+'_header.ini'
    #print('Outputting merged dataframe to nead: ',coutfile)

    #write dfm to NEAD file coutfile using header headerfile
    write_nead(dfm, headerfile, coutfile)
    # INSERT FUNCTION TO OUTPUT csv data in correct column order
    #dfm.to_csv(path_or_buf=coutfile,columns=())

    #clear dfm from memory before next station
    del dfm

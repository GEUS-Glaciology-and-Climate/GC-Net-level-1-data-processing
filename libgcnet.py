import sys
import time
import os
import numpy as np
import pandas as pd
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen
from zipfile import ZipFile
from urllib.request import urlopen
import zipfile
import matplotlib.pyplot as plt

############################### Function to download data from envidat#########
def getunzip(resource_link):
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4cGRIMG5qUkk1VmJVSzNQVlFkM1dXYnBibDYzYXNaV1kxejJpcWx1RmpfUlBJSzdRaHBrMHpHWVZhaF9TVU5peUgtcnR2aHpabm5XR3Z3VSIsImlhdCI6MTYwNTAwMjU0OX0.RR7BYrDQnCI_NAri2YCwpVqShX_cru-CsRGpkqeguvE"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJ5Nk8wVEN1QkJuVklmaFhkb0hpU3IxQVF4M3FKRkJua0tJaW1GY1JsYXQxMDNNTkFqNXZyRnk0UHFxVi1IeVpEZm11dUZKRXFjSTZjYllWSSIsImlhdCI6MTYxNTQ3MTE2M30.ls5BYHNW7LiXeax0gaQ0vkZpafL_zKAfKhLTiEXSCHQ"
    base_path = "./L0"
    output_path = os.path.join(base_path, resource_link.rsplit("/", 1)[1])
    print(output_path)
    chunk_size = 32 * 1024
    print("1. Requesting resource {0}...".format(resource_link))
    request = Request(resource_link)
    # Add token if necessary
    if token:
        print("\t * Adding token {0}...".format(token[0:7]))
        request.add_header("Authorization", token)
    # Make the HTTP request.
    print("\t * Performing HTTP request...")
    try:
        response = urlopen(request)
        if response:
            print("\t * Got response code {0}...".format(response.code))
            code = response.code
    except HTTPError as e:
        code = e.getcode()
        print("\t * ERROR * code {0}, {1}".format(code, e))
        # if code != 200:
        #    print("\t * Got response code {0}...".format(response.code))
        return -1
    # Save the zip file
    print("2. Saving resource at {0}...".format(output_path))
    with open(output_path, "wb") as fd:
        count = 0
        while True:
            count += 1

            if count % 200 == 0:
                print(
                    "\t\t\t ... downloading {0} KB ... ".format(
                        chunk_size * count / 1024
                    )
                )
            chunk = response.read(chunk_size)
            if not chunk:
                break
            fd.write(chunk)
    print(
        "\t * Written file aprox. {0} MB  ".format(
            round(chunk_size * count / 1024 / 1024)
        )
    )
    # Uncompress the zip file
    print("3. Uncompressing data file {0}...".format(output_path))
    # extract_path = os.path.join(base_path, resource_link.rsplit('/', 1)[1].rsplit('.')[0])
    extract_path = base_path
    time.sleep(3)
    zf = ZipFile(output_path, "r")
    zf.extractall(extract_path)
    print("\t * Extracted files to {0} ".format(extract_path))
    print("\t * Removing file {0} ".format(output_path))
    rmcomm = "rm " + output_path
    os.system(rmcomm)
    # remove MACOS folder that is part of zips
    # os.system('rm -r ./data/__MACOSX')
    print(" --- DONE --- ")


####################### Function to read station link csv and download L0 data##
def getLevel0(linkfile):
    ##Read CSV 'envidat_gcnet_links.csv' containing download link URLs
    linkarr = np.genfromtxt(linkfile, delimiter=",", dtype=None, encoding="utf-8")
    # Loop through all download links and download and unzip data
    for i in range(len(linkarr)):
        # index urls and download / unzip file for station i
        link = linkarr[i]
        getunzip(link)


###################### Function to change the name of Pandas Columns ###########
######### changes from raw campbel names to standard Field name for NEAD
######### also merges possible variations of column name ####
def nameLevel0col(dfm):
    # first make everything lowercase
    dfm.columns = [c.lower() for c in dfm.columns]

    variable_aliases = {
        "sw_in_avg(1)": "ISWR",
        "sw_in_avg": "ISWR",
        "sw_ref_avg(1)": "OSWR",
        "sw_ref_avg": "OSWR",
        "net_rad_avg": "NR",
        "t_air_avg(1)": "TA3",
        "t_air_avg(2)": "TA4",
        "t_air1_avg": "TA3",
        "t_air2_avg": "TA4",
        "tc_air_avg(1)": "TA1",
        "tc_air_avg": "TA1",
        "tc_air_avg(2)": "TA2",
        "rh_avg(1)": "RH1",
        "rh_avg(2)": "RH2",
        "u_avg(1)": "VW1",
        "u_avg(2)": "VW2",
        "dir_avg(1)": "DW1",
        "dir_avg(2)": "DW2",
        "dir1_avg": "DW1",
        "dir2_avg": "DW2",
        "pressure_avg": "P",
        "sd_1_avg": "HW1",
        "sd_2_avg": "HW2",
        "tc_air_max": "TA1_max",
        "tc_air_min": "TA1_min",
        "u_max(1)": "VW1_max",
        "u_max(2)": "VW2_max",
        "u_std(1)": "VW1_stdev",
        "u_std(2)": "VW2_stdev",
        "sw_in_max(1)": "ISWR_max",
        "sw_in_max": "ISWR_max",
        "sw_in_std(1)": "ISWR_std",
        "sw_in_std": "ISWR_std",
        "net_rad_std": "NR_std",
        "tc_air_max(1)": "TA1_max",
        "tc_air_max(2)": "TA2_max",
        "tc_air_min(1)": "TA1_min",
        "tc_air_min(2)": "TA2_min",
        "battery": "V",
        "batt_volt": "V",
        "tref_avg": "TA5",
        "tc_snow_avg(1)": "TS1",
        "tc_snow_avg(2)": "TS2",
        "tc_snow_avg(3)": "TS3",
        "tc_snow_avg(4)": "TS4",
        "tc_snow_avg(5)": "TS5",
        "tc_snow_avg(6)": "TS6",
        "tc_snow_avg(7)": "TS7",
        "tc_snow_avg(8)": "TS8",
        "tc_snow_avg(9)": "TS9",
        "tc_snow_avg(10)": "TS10",
        "tc_snow_avg(10)": "TS10",
        "uv_avg": "IUVR",
        "l_in_avg": "ILWR",
        "t_surf1_avg": "Tsurf1",
        "t_surf2_avg": "Tsurf2",
    }

    target_var = np.array(list(variable_aliases.keys()))
    # ind = np.isin(target_var, dfm.columns)
    # print("Warning:", target_var[~ind], "are not in the L0 data file")
    ind = np.isin(dfm.columns, target_var)
    missing_var = (~ind & ~np.isin(dfm.columns,
                                   ['timestamp', 'record', 'loggerid', 
                                    'year', 'day_of_year', 'hour',
                                    'val(1)', 'val(2)', 'val(3)', 'val(4)']))
    if any(missing_var) > 0:
        
        print(
            "====> Warning:",
            dfm.columns[missing_var],
            "are in the L0 data file but not in the dataframe",
        )
        print(wtf)
    dfm = dfm.rename(columns=variable_aliases)
    return dfm


### This functions takes the merged dataframe dfm and adds offset add_value
### to each field in the string list fields
### returns the modified dfm
def calibrate_add_value(dfm, fields, add_value):
    # loop through length-1 because we dont add to timestamp
    for i in range(len(fields) - 1):
        i = i + 1  # we don't want to add to timestamp so we start at index 1
        dfm[fields[i]] = dfm[fields[i]] + add_value[i]
    return dfm


### This functions takes the merged dataframe dfm and multiples scale_factor
### to positive values (>0) in each field in the string list fields
### returns the modified dfm
def calibrate_scale_factor(dfm, fields, scale_factor):
    # loop through length-1 because we dont add to timestamp
    for i in range(len(fields) - 1):
        i = i + 1  # we don't want to add to timestamp so we start at index 1
        # col = dfm[fields[i]]
        # col[col>0]=col[col>0]*scale_factor[i]
        # dfm[fields[i]]=col
        # make multiplation in place for locations greater than 0
        dfm.loc[dfm[fields[i]] > 0, fields[i]] *= scale_factor[i]
    return dfm


### This functions takes the merged dataframe dfm and multiples scale_factor_neg
### to negative values (<0) in each field in the string list fields
### returns the modified dfm
def calibrate_scale_factor_neg(dfm, fields, scale_factor_neg):
    # loop through length-1 because we dont add to timestamp
    for i in range(len(fields) - 1):
        i = i + 1  # we don't want to add to timestamp so we start at index 1
        # col = dfm[fields[i]]
        # col[col<0]=col[col<0]*scale_factor_neg[i]
        # dfm[fields[i]]=col
        dfm.loc[dfm[fields[i]] < 0, fields[i]] *= scale_factor_neg[i]
    return dfm


def read_c_file(c_file_path, c_file_header_str):
    print("Now reading: ", c_file_path)
    dfc = pd.read_csv(
        c_file_path,
        sep="\s+",
        names=c_file_header_str,
        header=None,
        na_values=[999.0, -999, 999.99, 999.999],
    )
    # define timestamp from Year and DoY (fractional ordinal day)
    dfc["timestamp"] = pd.to_datetime(dfc.year, format="%Y") + pd.to_timedelta(
        dfc.DoY - 1, unit="d"
    )
    # round to the nearest hour (there is some remainder from fractional day)
    dfc["timestamp"] = dfc["timestamp"].dt.round("H")
    dfc = dfc.set_index("timestamp")
    # pd.to_datetime(dfc.index)
    # remove any possible duplicate datetimes
    dfc = dfc[~dfc.index.duplicated(keep="first")]
    dfc = dfc.sort_index()
    # dfc = pd.concat([df1,df2]).drop_duplicates(subset=["timestamp"])
    return dfc

import requests
import nead

def get_transmission(site, date_end, date_now, dfm, local_path):
    # as of 2023-01-11, transmissions are not available anymore from Envidat
    # we just use that last available transimission file for the stations
    # that could not be visited in 2021 and 2022 (last available transmission
    # 2022-09-20)
    
    # envidat_alias = {
    #     "Swiss Camp 10m": "swisscamp_10m_tower",
    #     "Swiss Camp": "swisscamp",
    #     "Crawford Point 1": "crawfordpoint",
    #     "NASA-U": "nasa_u",
    #     "GITS": "gits",
    #     "Humboldt": "humboldt",
    #     "Summit": "summit",
    #     "Tunu-N": "tunu_n",
    #     "DYE2": "dye2",
    #     "JAR1": "jar1",
    #     "JAR2": "jar2",
    #     "Saddle": "saddle",
    #     "South Dome": "southdome",
    #     "NASA-E": "nasa_east",
    #     "NASA-SE": "nasa_southeast",
    #     "Petermann ELA": "petermann",
    #     "NEEM": "neem",
    #     "E-GRIP": "east_grip",
    # }
    # try:
    #     os.mkdir(local_path)
    # except:
    #     pass
    
    
    # remote_url = (
    #     "https://www.envidat.ch/data-api/gcnet/nead/"
    #     + envidat_alias[site]
    #     + "/end/-999/"
    #     + date_end
    #     + "/"
    #     + date_now
    #     + "/"
    # )

    local_file = local_path + site + ".csv"
    # print("requesting transmissions from", date_end, "to", date_now)
    # print("url:", remote_url)

    # try:
    #     data = requests.get(remote_url)
    #     # Save file data to local copy
    #     with open(local_file, "wb") as file:
    #         file.write(data.content)
    #     dft = nead.read(local_file).to_dataframe()
    #     print(
    #         "received transmission from",
    #         dft["timestamp"].iloc[0],
    #         dft["timestamp"].iloc[-1],
    #     )
    #     dft["timestamp"] = pd.to_datetime(dft["timestamp"], utc=True)
    #     dfm["timestamp"] = pd.to_datetime(dfm["timestamp"], utc=True)
    #     dft = dft.set_index("timestamp")
    #     dfm = dfm.set_index("timestamp")

    #     dfm = pd.concat([dfm, dft]).reset_index()
    # except:
    #     print("download failed")
    print("reading last transmission file available")
        # pass
    try:
        dft = nead.read(local_file).to_dataframe()
        print(
            "received transmission from",
            dft["timestamp"].iloc[0],
            dft["timestamp"].iloc[-1],
        )
        dft["timestamp"] = pd.to_datetime(dft["timestamp"], utc=True)
        dfm["timestamp"] = pd.to_datetime(dfm["timestamp"], utc=True)
        dft = dft.set_index("timestamp")
        dfm = dfm.set_index("timestamp")
        dft.columns = dft.columns.str.replace('NSWR','NR')
        dfm = pd.concat([dfm, dft]).reset_index()

    except:
        print("could not read local file")
        pass
    return dfm


def load_old_logger_file(plot=True):
    df_all = pd.DataFrame()
    
    # plt.close('all')
    if plot:
        fig, ax = plt.subplots(2,3, figsize=(16,9))
        ax=ax.flatten()
        CB_color_cycle = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', 
                          '#984ea3', '#999999', '#e41a1c', '#dede00']
    file_list = os.listdir('L0/00-Swiss Camp 10m/CR27 logger files/')
    for year in range(1995, 1999):
        path = 'L0/00-Swiss Camp 10m/CR27 logger files/'
        filename = [f for f in file_list if f.startswith(str(year))][-1]
        year_start = year-1
        
        file1 = open(path + filename, 'r')
        Lines = file1.readlines()
        Lines_met = [];     Lines_rad = []
        count = 0;
        # Strips the newline character
        for i, line in enumerate(Lines):   
            if line.startswith('205') or line.startswith('202') or line.startswith('206'):
                count += 1
                Lines_met.append(line[4:])
                current_day = int(Lines_met[-1].split(',')[0])
                current_hour = int(Lines_met[-1].split(',')[1])
        
            if line.startswith('103') and count>0:
                if current_hour == 2400:
                    current_hour = 0
                    current_day = current_day +1
                        
                Lines_rad.append(str(current_day) + ',' + str(current_hour) + ',' + line[4:])
                current_hour = current_hour+100
        
        with open('L0/00-Swiss Camp 10m/CR27 logger files/processed_bav/' +  filename[:-4] + '_met_3h.csv', 'w') as f:
            f.write('day_of_year,hour,VW1,TA1,TA2,RH1,VW2,TA1_max,TA2_max,RH1_max,' \
                    + 'VW1_min,TA1_min,TA2_min,RH1_min,DW1,unkw\n')
            
            for line in Lines_met:
                if line.count(',') <= 5:
                    # then format is jd,time,wind,wmax,tair,wdir
                    tmp = line.replace('\n','').split(',')
                    line = ','.join([tmp[0], tmp[1], tmp[2], tmp[4], '', '',  tmp[3], '', '', '','','', '', '', tmp[5],  '\n'])
                
                if line.count(',') < 15:
                    line = line[:-1] + ','*(15-line.count(',')) + '\n'
                f.write(line)
        
        with open('L0/00-Swiss Camp 10m/CR27 logger files/processed_bav/'  +  filename[:-4] + '_rad_h.csv', 'w') as f:
            f.write('day_of_year,hour,r1,r2,r3,NR\n')
            
            for line in Lines_rad:
                # if line.count(',') < 27:
                #     line = line[:-1] + ','*(27-line.count(',')) + '\n'
                f.write(line)
        
        
        df_met = pd.read_csv('L0/00-Swiss Camp 10m/CR27 logger files/processed_bav/'  +  filename[:-4] + '_met_3h.csv', index_col = False)
        df_met[df_met==-6999] = np.nan
        df_met['year'] = year_start
        yr_shift = df_met.index.values[df_met.day_of_year.diff()<-1]
        if len(yr_shift) == 1:
            df_met.loc[yr_shift[0]:, 'year'] = year_start +1
        elif len(yr_shift) == 2:
            df_met.loc[:yr_shift[0], 'year'] = year_start -1
            df_met.loc[yr_shift[0]:yr_shift[1], 'year'] = year_start
            df_met.loc[yr_shift[1]:, 'year'] = year_start +1
        else:
            print(wtf)
        df_met['timestamp'] = pd.to_datetime(df_met.year * 100000 + df_met.day_of_year * 100 + df_met.hour/100 , utc=True, format='%Y%j%H')
            
        # correction for wrong offset during winter 95/96
        msk= df_met.TA1 > 300
        df_met.loc[msk, ['TA1', 'TA1_max', 'TA1_min']] = df_met.loc[msk, ['TA1', 'TA1_max', 'TA1_min']] - 400
        df_met = df_met.set_index('timestamp')
        
        # convert UUB thermister reading to temperature      
        for var in ['TA1', 'TA1_max', 'TA1_min']:
            df_met[var] = -9.0763671 + 0.704343 * df_met[var] \
                + 0.00919 * (df_met[var]**2) + 0.000137 * (df_met[var]**3) \
                + 0.00000116676 * (df_met[var]**4) + 0.00000000400674*(df_met[var]**5)
        
        df_rad = pd.read_csv('L0/00-Swiss Camp 10m/CR27 logger files/processed_bav/'  + filename[:-4] + '_rad_h.csv', index_col = False)
        df_rad[df_rad==-6999] = np.nan
        df_rad['year'] = year_start
        yr_shift = df_rad.index.values[df_rad.day_of_year.diff()<-1]
        if len(yr_shift) == 1:
            df_rad.loc[yr_shift[0]:, 'year'] = year_start +1
        elif len(yr_shift) == 2:
            df_rad.loc[:yr_shift[0], 'year'] = year_start -1
            df_rad.loc[yr_shift[0]:yr_shift[1], 'year'] = year_start
            df_rad.loc[yr_shift[1]:, 'year'] = year_start +1
        else:
            print(wtf)
        
        df_rad['timestamp'] = pd.to_datetime(df_rad.year * 100000 + df_rad.day_of_year * 100 + df_rad.hour/100 , utc=True, format='%Y%j%H')
        df_rad = df_rad.set_index('timestamp')
    
        # convert Li-Core mV to W/m2
        df_rad['ISWR'] = df_rad.r1 * 106.49
        df_rad['ISWR2'] = df_rad.r2 * 105.89
        df_rad['OSWR'] = df_rad.r3 * 105.92
        # convert net radiation mv to W/m2
        # new net radiation sensor in 97 (old one from Boulder)	
        # df_rad['NR'] = df_rad.net * 13.3
        msk_pos = df_rad.NR>0
        df_rad.loc[msk_pos, 'NR'] = df_rad.loc[msk_pos, 'NR'] * 13.3*1.182
        msk_neg = df_rad.NR<0
        df_rad.loc[msk_neg, 'NR'] = df_rad.loc[msk_neg, 'NR'] * 13.3*0.962
        
        print('\n', filename[:-4], 'met data')
        print('start date', df_met.index[0])
        print('end date', df_met.index[-1])
        print('resolution', np.unique(np.diff(df_met.index)))
        
        print('\n', filename[:-4], 'radiation data')
        print('start date', df_rad.index[0])
        print('end date', df_rad.index[-1])
        print('resolution', np.unique(np.diff(df_rad.index)))
    
        # interpolating to hourly values
        df_met = df_met.resample('H').mean().ffill(limit=3)
        
        # plotting
        if plot:
            if year != 1998:
                df_rad.OSWR.plot(ax=ax[0], label='_nolegend_', color=CB_color_cycle[year-1995])
            df_rad.ISWR.plot(ax=ax[0], label='_nolegend_', color=CB_color_cycle[year-1995])
            df_rad.NR.plot(ax=ax[1],label='_nolegend_',  color=CB_color_cycle[year-1995])
            df_met.TA1.plot(ax=ax[2], label='_nolegend_', color=CB_color_cycle[year-1995])
            df_met.RH1.plot(ax=ax[3], label='_nolegend_', color=CB_color_cycle[year-1995])
            df_met.VW1.plot(ax=ax[4], label='_nolegend_', color=CB_color_cycle[year-1995])
            df_met.DW1.plot(ax=ax[5], label='_nolegend_', color=CB_color_cycle[year-1995])
            i=0
            ax[i].plot(np.nan, np.nan, label =  filename, color=CB_color_cycle[year-1995])
        
        # adding to table
        if len(df_all) == 0:
            df_all = df_met[['VW1', 'TA1', 'TA2', 'RH1', 'VW2', 'TA1_max', 
                             'TA2_max', 'RH1_max', 'VW1_min', 'TA1_min', 'TA2_min',
                             'RH1_min', 'DW1']]
            df_all = pd.concat((df_all, df_rad[['ISWR', 'ISWR2', 'OSWR', 'NR',]]))
        else:
            df_all = pd.concat((df_all, df_met[['VW1', 'TA1', 'TA2', 'RH1', 'VW2', 
                                           'TA1_max', 'TA2_max', 'RH1_max', 
                                           'VW1_min', 'TA1_min', 'TA2_min', 
                                           'RH1_min', 'DW1']]))
            df_all = pd.concat((df_all, df_rad[['ISWR', 'ISWR2', 'OSWR', 'NR',]]))
    
    # %% 
    filename = '1993_KLIMA.DAT'
    year_start = 1993
    
    file1 = open(path + filename, 'r')
    Lines = file1.readlines()
    Lines_met = []
    Lines_rad = []
    count = 0
    count2 = 0
    # Strips the newline character
    for i, line in enumerate(Lines):   
        if line.startswith('205') or line.startswith('202') or line.startswith('206'):
            count += 1
            Lines_met.append(line[4:])
            count2 = 0
            current_day = int(Lines_met[-1].split(',')[0])
            current_hour = int(Lines_met[-1].split(',')[1])
    
        if line.startswith('103') and count>0:
            count2 += 1
            if current_hour == 2400:
                current_hour = 0
                current_day = current_day +1
                    
            Lines_rad.append(str(current_day) + ',' + str(current_hour) + ',' + line[4:])
            current_hour = current_hour+10
    
    with open('L0/00-Swiss Camp 10m/CR27 logger files/processed_bav/' +  filename[:-4] + '_met_3h.csv', 'w') as f:
        f.write('day_of_year,hour,VW1,VW1_max,TA1,DW1\n')
        for line in Lines_met:
            f.write(line)
    
    with open('L0/00-Swiss Camp 10m/CR27 logger files/processed_bav/'  +  filename[:-4] + '_rad_h.csv', 'w') as f:
        f.write('day_of_year,hour,r1,r2,r3,NR\n')
        for line in Lines_rad:
            f.write(line)
    
    df_met = pd.read_csv('L0/00-Swiss Camp 10m/CR27 logger files/processed_bav/'  +  filename[:-4] + '_met_3h.csv', index_col = False)
    df_met[df_met==-6999] = np.nan
    df_met['year'] = year_start
    yr_shift = df_met.index.values[df_met.day_of_year.diff()<-1]
    if len(yr_shift) == 1:
        df_met.loc[yr_shift[0]:, 'year'] = year_start +1
    elif len(yr_shift) == 2:
        df_met.loc[:yr_shift[0], 'year'] = year_start -1
        df_met.loc[yr_shift[0]:yr_shift[1], 'year'] = year_start
        df_met.loc[yr_shift[1]:, 'year'] = year_start +1
    elif len(yr_shift) == 0:
        df_met['year'] = year_start
    else:
        print(wtf)
    df_met['timestamp'] = pd.to_datetime(df_met.year * 100000 + df_met.day_of_year * 100 + df_met.hour/100 , utc=True, format='%Y%j%H')
        
    # correction for wrong offset during winter 95/96
    msk= df_met.TA1 > 300
    df_met.loc[msk, ['TA1']] = df_met.loc[msk, ['TA1']] - 400
    df_met = df_met.set_index('timestamp')
    
    # convert UUB thermister reading to temperature      
    a=-9.0763671
    b=0.704343
    c=0.00919
    d=0.000137
    e=0.00000116676
    f=0.00000000400674
    for var in ['TA1']:
        df_met[var] = a + b * df_met[var] \
            + c * (df_met[var]**2) + d * (df_met[var]**3) \
            + e * (df_met[var]**4) + f*(df_met[var]**5)
    
    df_rad = pd.read_csv('L0/00-Swiss Camp 10m/CR27 logger files/processed_bav/'  + filename[:-4] + '_rad_h.csv', index_col = False)
    df_rad[df_rad==-6999] = np.nan
    df_rad['year'] = year_start
    yr_shift = df_rad.index.values[df_rad.day_of_year.diff()<-1]
    if len(yr_shift) == 1:
        df_rad.loc[yr_shift[0]:, 'year'] = year_start +1
    elif len(yr_shift) == 2:
        df_rad.loc[:yr_shift[0], 'year'] = year_start -1
        df_rad.loc[yr_shift[0]:yr_shift[1], 'year'] = year_start
        df_rad.loc[yr_shift[1]:, 'year'] = year_start +1
    elif len(yr_shift) == 0:
        df_met['year'] = year_start
    else:
        print(wtf)
    df_met.to_csv('L0/00-Swiss Camp 10m/CR27 logger files/processed_bav/'  + filename[:-4] + '_met_3h.csv',  sep=' ', float_format='%.3f',
                  index=False)
    
    df_rad['timestamp'] = pd.to_datetime(df_rad.year * 10000000 + df_rad.day_of_year * 10000 + df_rad.hour , utc=True, format='%Y%j%H%M')
    df_rad = df_rad.set_index('timestamp')
    
    # convert Li-Core mV to W/m2
    df_rad['ISWR'] = df_rad.r1 * 106.49
    df_rad['ISWR2'] = df_rad.r2 * 105.89
    df_rad['OSWR'] = df_rad.r3 * 105.92
    # convert net radiation mv to W/m2
    # new net radiation sensor in 97 (old one from Boulder)	
    # df_rad['NR'] = df_rad.net * 13.3
    msk_pos = df_rad.NR>0
    df_rad.loc[msk_pos, 'NR'] = df_rad.loc[msk_pos, 'NR'] * 13.3*1.182
    msk_neg = df_rad.NR<0
    df_rad.loc[msk_neg, 'NR'] = df_rad.loc[msk_neg, 'NR'] * 13.3*0.962
    df_rad.iloc[:,0] = df_rad.iloc[:,0] + df_rad.iloc[:,1]/24000
    df_rad[['day_of_year', 'ISWR', 'ISWR2', 'OSWR', 'NR']].to_csv('L0/00-Swiss Camp 10m/CR27 logger files/processed_bav/'  + filename[:-4] + '_rad_h.csv',  sep=' ', float_format='%.3f',
                  index=False)
    print('\n', filename, 'met data')
    print('start date', df_met.index[0])
    print('end date', df_met.index[-1])
    print('resolution', np.unique(np.diff(df_met.index)))
    
    print('\n', filename, 'radiation data')
    print('start date', df_rad.index[0])
    print('end date', df_rad.index[-1])
    print('resolution', np.unique(np.diff(df_rad.index)))
       
    df_all = pd.concat((df_all, df_met[[ 'VW1', 'VW1_max', 'TA1', 'DW1']]))
    df_all = pd.concat((df_all, df_rad.resample('H',label='right').mean()[['ISWR', 'ISWR2', 'OSWR', 'NR',]]))
    
    # %% 
    ################################## 3 hours ################################### 
    filename = '1993_MET_91-93_3h_doy.hh.DAT'
    df_93 = pd.read_csv(path+filename, sep = ' ')
    df_93['year'] = 1991
    yr_shift = df_93.index.values[df_93.JD.diff()<-1]
    df_93.loc[yr_shift[0]:yr_shift[1], 'year'] = 1991+1
    df_93.loc[yr_shift[1]:, 'year'] = 1991+2
    df_93['timestamp'] = pd.to_datetime(df_93.year * 100000 \
                            + np.trunc(df_93.JD) * 100 \
                            + (df_93.JD-np.trunc(df_93.JD))*100 , utc=True, format='%Y%j%H')
    df_93 = df_93.set_index('timestamp').drop(columns=['JD','year'])
    print('\n', filename)
    print('start date', df_93.index[0])
    print('end date', df_93.index[-1])
    print('resolution', np.unique(np.diff(df_93.index)))
    # interpolating to hourly values
    df_93 = df_93.resample('H').mean().ffill(limit=3)
    df_all = pd.concat((df_all, df_93))
    ############################ 3 hours ##################################### 
    filename='1993_MET_90_3h_doy.hh.DAT'
    df_90 = pd.read_csv(path+filename, sep = ' ')
    df_90['year'] = 1990
    df_90['timestamp'] = pd.to_datetime(df_90.year * 100000 \
                            + np.trunc(df_90.JD) * 100 \
                            + (df_90.JD-np.trunc(df_90.JD))*100 , utc=True, format='%Y%j%H')
    df_90 = df_90.set_index('timestamp').drop(columns=['JD','year'])
    print('\n', filename)
    print('start date', df_90.index[0])
    print('end date', df_90.index[-1])
    print('resolution', np.unique(np.diff(df_90.index)))
    # interpolating to hourly values
    df_93 = df_93.resample('H').mean().ffill(limit=3)
    df_all = pd.concat((df_all, df_90))
    
    ############################ 3 hours ##################################### 
    filename='1994_T_W_R_93-94_3h.DAT'
    df_94_twr = pd.read_csv(path + filename, header=None, delim_whitespace=True)
    df_94_twr=df_94_twr.rename(columns={0:'JD', 1:'VW1', 2:'VW1_max', 
                                        3:'DW1', 4:'TA1', 5:'ISWR', 6:'ISWR2',
                                        7:'OSWR', 8:'alb1', 9:'alb2', 10:'NR', 
                                        11:'ILWR'})
    df_94_twr['year'] = 1993
    yr_shift = df_94_twr.index.values[df_94_twr.JD.diff()<-1]
    df_94_twr.loc[yr_shift[0]:, 'year'] = 1993+1
    
    df_94_twr['timestamp'] = pd.to_datetime(df_94_twr.year * 100000 \
                            + np.trunc(df_94_twr.JD) * 100 \
                            + np.round((df_94_twr.JD-np.trunc(df_94_twr.JD))*24) ,
                            utc=True, format='%Y%j%H')
    df_94_twr = df_94_twr.set_index('timestamp').drop(columns=['JD','year'])
    print('\n', filename)
    print('start date', df_94_twr.index[0])
    print('end date', df_94_twr.index[-1])
    print('resolution', np.unique(np.diff(df_94_twr.index)))
    # interpolating to hourly values
    df_94_twr = df_94_twr.resample('H').mean().ffill(limit=3)
    df_all = pd.concat((df_all, df_94_twr))
    ############################ 3 h #######################################
    filename = '1993_TOWER.DAT'
    df_1993_tower = pd.read_csv(path + filename, header=None)
    df_1993_tower[df_1993_tower==-6999] = np.nan
    df_1993_tower['year'] = 1993-1
    yr_shift = df_1993_tower.index.values[df_1993_tower[1].diff()<-1]
    df_1993_tower.loc[yr_shift[0]:, 'year'] = 1993
    df_1993_tower['timestamp'] = pd.to_datetime(df_1993_tower['year'] * 100000 \
                            + df_1993_tower[1] * 100 \
                            + df_1993_tower[2]/100 ,
                            utc=True, format='%Y%j%H')
    df_1993_tower = df_1993_tower.set_index('timestamp').drop(columns=[0,1,2])
    df_1993_tower = df_1993_tower.rename(columns={3:'VW1', 4: 'VW1_max', 5:'TA1', 6:'DW1'})
    df_1993_tower.TA1 = np.nan
    df_1993_tower.loc[df_1993_tower.VW1>30, ['VW1','VW1_max']] = np.nan
    print('\n', filename)
    print('start date', df_1993_tower.index[0])
    print('end date', df_1993_tower.index[-1])
    print('resolution', np.unique(np.diff(df_1993_tower.index)))
    # interpolating to hourly values
    df_1993_tower = df_1993_tower.resample('H').mean().ffill(limit=3)
    df_all = pd.concat((df_all, df_1993_tower))
    
    ########################### hourly ########################################### 
    filename = '1991_TOWER_90-91_10m.DAT'
    df_91 = pd.read_fwf(path + filename,
                     widths = [15, 10, 9, 9, 9, 9],
                     header=None)
    df_91 =df_91.rename(columns={0:'timestamp', 1:'TA1', 2:'VW1', 3:'DW1', 4:'P', 5:'RH1'})
    df_91['timestamp'] = pd.to_datetime(df_91['timestamp'], utc=True, format='%d.%m.%y %H:%M')
    df_91 = df_91.set_index('timestamp')
    print('\n', filename)
    print('start date', df_91.index[0])
    print('end date', df_91.index[-1])
    print('resolution', np.unique(np.diff(df_91.index)))
    df_all = df_91.resample('H',label='right').mean().combine_first(df_all)
    
    ############################ hourly ###################################### 
    filename= '1994_RAD_ALL_93-94_h.DAT'
    df_94_rad = pd.read_csv(path + filename,  delim_whitespace=True)
    df_94_rad[df_94_rad.ISWR<0] = np.nan
    df_94_rad[df_94_rad.ISWR2<0] = np.nan
    df_94_rad[df_94_rad.OSWR<0] = np.nan
    df_94_rad[df_94_rad.NR<-1000] = np.nan
    df_94_rad['year'] = 1993
    yr_shift = df_94_rad.index.values[df_94_rad.JD.diff()<-1]
    df_94_rad.loc[yr_shift[0]:, 'year'] = 1993+1
    
    df_94_rad['timestamp'] = pd.to_datetime(df_94_rad.year * 100000 \
                            + np.trunc(df_94_rad.JD) * 100 \
                            + np.round((df_94_rad.JD-np.trunc(df_94_rad.JD))*24) ,
                            utc=True, format='%Y%j%H')
    df_94_rad = df_94_rad.set_index('timestamp',drop=False).drop(columns=['JD','year'])
    print('\n', filename)
    print('start date', df_94_rad.index[0])
    print('end date', df_94_rad.index[-1])
    print('resolution', np.unique(np.diff(df_94_rad.index[df_94_rad.index.notnull()])))
    df_all = df_94_rad.combine_first(df_all)
    
    ######################### 30 min ####################################### 
    filename = '1990_RAD90.DAT'
    df_rad90 = pd.read_csv(path + filename, 
                           delim_whitespace=True, header=None)
    df_rad90[df_rad90==-999] = np.nan
    df_rad90 = df_rad90.rename(columns={0:'year', 1:'month', 2:'day',3:'hour',4:'minute'})
    df_rad90.year = df_rad90.year+1900  
    df_rad90['timestamp'] = pd.to_datetime(df_rad90[['year','month','day','hour','minute']], utc = True)
    df_rad90 = df_rad90.set_index('timestamp').drop(columns=['year','month','day','hour','minute'])
    df_rad90.columns=['ISWR','SZA?','ISWR2','OSWR','OSWR2','alb1','alb2','SZA?','LWR1','LWR2','LWR','NR','NR2','ISWR3','alb3','alb4']
    df_rad90 = df_rad90.drop(columns=['SZA?', 'alb1','alb2', 'alb3','alb4'])

    print('\n', filename)
    print('start date', df_rad90.index[0])
    print('end date', df_rad90.index[-1])
    print('resolution', np.unique(np.diff(df_rad90.index[df_rad90.index.notnull()])))

    ######################### 30 min #######################################
    filename='1990_SYNO90.DAT'
    df_syno = pd.read_csv(path+filename, 
                           delim_whitespace=True, header=None)
    df_syno[df_syno==-99.9] = np.nan
    df_syno = df_syno.rename(columns={0:'day', 1:'month', 2:'hour',3:'minute'})
    df_syno['year'] = 1990
    df_syno['timestamp'] = pd.to_datetime(df_syno[['year','month','day','hour','minute']], utc = True)
    df_syno = df_syno.set_index('timestamp').drop(columns=['year','month','day','hour','minute'])
    df_syno.columns=['TA1','?','VW1','DW1','P','RH1']
    print('\n', filename)
    print('start date', df_syno.index[0])
    print('end date', df_syno.index[-1])
    print('resolution', np.unique(np.diff(df_syno.index[df_syno.index.notnull()])))
    
    df_syno = df_syno.resample('H', label='right').mean()                  
    df_rad90 = pd.concat((df_rad90, df_syno))
    df_all = pd.concat((df_all, df_rad90))
    
    df_all = df_all.sort_index()
    
    df_all = df_all.drop(columns=['timestamp','year'])
    df_all = df_all.groupby(level=0).mean()
    # tmp = ( (df_all.groupby(level=0).mean() != df_all.groupby(level=0).max()) & df_all.groupby(level=0).max().notnull())
    
    # plt.plot(df_syno['RH1'].values,df_syno['?'].values,marker='.',linestyle='None')
    
    # # plt.close('all')
    # varlist = df_rad90.columns
    # df_rad90[[v for v in varlist if 'ISWR' in v]].plot()
    # df_rad90[[v for v in varlist if 'OSWR' in v]].plot()
    # df_rad90[[v for v in varlist if 'NR' in v]].plot()
    # df_rad90[[v for v in varlist if 'LWR' in v]].plot()
    # df_rad90[[v for v in varlist if 'SZA' in v]].plot()
    # %% Plotting
    # plt.close('all')
    # fig, ax = plt.subplots(2,3, figsize=(16,9))
    # ax=ax.flatten()
    if plot:
        def plot_var(var, i):
            if var in df_met.columns: ax[i].plot(df_met.index, df_met[var], 'red')
            if var in df_rad.columns: ax[i].plot(df_rad.index, df_rad[var], 'red')
            if var in df_1993_tower.columns: ax[i].plot(df_1993_tower.index, df_1993_tower[var], 'gray')
            if var in df_93.columns: ax[i].plot(df_93.index, df_93[var], 'green')
            if var in df_90.columns: ax[i].plot(df_90.index, df_90[var], 'orange')
            if var in df_91.columns: ax[i].plot(df_91.index, df_91[var], 'magenta',alpha=0.5)
            if var in df_94_twr.columns: ax[i].plot(df_94_twr.index, df_94_twr[var], 'cyan',alpha=0.5)
            if var in df_94_rad.columns: ax[i].plot(df_94_rad.timestamp.values, df_94_rad[var].values, 'green',alpha=0.5)
            if var in df_rad90.columns: ax[i].plot(df_rad90.index.values, df_rad90[var].values, 'purple',alpha=0.5)
        ts = pd.to_datetime(df_all.index.values)
        ax[0].plot(ts, df_all.ISWR, marker='x', color='lightgray', zorder=0, linestyle='None')
        ax[0].plot(ts, df_all.OSWR, marker='x', color='lightgray', zorder=0, linestyle='None')
        ax[1].plot(ts, df_all.NR, marker='x', color='lightgray', zorder=0, linestyle='None')
        ax[2].plot(ts, df_all.TA1, marker='x', color='lightgray', zorder=0, linestyle='None')
        ax[3].plot(ts, df_all.RH1, marker='x', color='lightgray', zorder=0, linestyle='None')
        ax[4].plot(ts, df_all.VW1, marker='x', color='lightgray', zorder=0, linestyle='None')
        ax[5].plot(ts, df_all.DW1, marker='x', color='lightgray', zorder=0, linestyle='None')
        # ax[0].plot(df_all.index, df_all.P6], marker='x', color='lightgray', zorder=0, linestyle='None')
        plot_var('ISWR',0)
        plot_var('OSWR',0)
        plot_var('NR',1)
        plot_var('TA1',2)
        plot_var('RH1',3)
        plot_var('VW1',4)
        plot_var('DW1',5)
        # plot_var('P',6)
        for i, var in enumerate(['SWR','NR','TA','RH','VW','DW']):
            ax[i].set_ylabel(var)
        plt.suptitle(' ')
        i=0
        ax[i].plot(np.nan, np.nan, 'red', label = '1993_KLIMA')
        ax[i].plot(np.nan, np.nan,  'green', label = '1993_MET_91-93_3h_doy.hh.DAT')
        ax[i].plot(np.nan, np.nan,  'gray', label = '1993_TOWER.DAT')
        ax[i].plot(np.nan, np.nan,  'orange', label = '1991_TOWER_90_10m.DAT')
        ax[i].plot(np.nan, np.nan,  'magenta',alpha=0.5, label = '1991_TOWER_90-91_10m.DAT')
        ax[i].plot(np.nan, np.nan,  'cyan',alpha=0.5, label = '1994_T_W_R_93-94_3h.DAT')
        ax[i].legend(loc='upper center', bbox_to_anchor=(1.5, 1.4), ncol=4)
        for i in range(6):
            ax[i].set_xlim(pd.to_datetime('1990'),pd.to_datetime('1999'))
        # plt.suptitle('Old logger files at SwissCamp 10m')
    return df_all
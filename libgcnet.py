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

############################### Function to download data from envidat#########
def getunzip(resource_link):
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4cGRIMG5qUkk1VmJVSzNQVlFkM1dXYnBibDYzYXNaV1kxejJpcWx1RmpfUlBJSzdRaHBrMHpHWVZhaF9TVU5peUgtcnR2aHpabm5XR3Z3VSIsImlhdCI6MTYwNTAwMjU0OX0.RR7BYrDQnCI_NAri2YCwpVqShX_cru-CsRGpkqeguvE'
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJ5Nk8wVEN1QkJuVklmaFhkb0hpU3IxQVF4M3FKRkJua0tJaW1GY1JsYXQxMDNNTkFqNXZyRnk0UHFxVi1IeVpEZm11dUZKRXFjSTZjYllWSSIsImlhdCI6MTYxNTQ3MTE2M30.ls5BYHNW7LiXeax0gaQ0vkZpafL_zKAfKhLTiEXSCHQ'
    base_path = "./L0"
    output_path = os.path.join(base_path, resource_link.rsplit('/', 1)[1])
    print(output_path)
    chunk_size = 32 * 1024
    print("1. Requesting resource {0}...".format(resource_link))
    request = Request(resource_link)
    # Add token if necessary
    if token:
        print("\t * Adding token {0}...".format(token[0:7]))
        request.add_header('Authorization', token)
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
        #if code != 200:
        #    print("\t * Got response code {0}...".format(response.code))
        return -1
    # Save the zip file
    print("2. Saving resource at {0}...".format(output_path))
    with open(output_path, 'wb') as fd:
        count = 0
        while True:
            count += 1

            if count % 200 == 0:
                print("\t\t\t ... downloading {0} KB ... ".format(chunk_size * count / 1024))
            chunk = response.read(chunk_size)
            if not chunk:
                break
            fd.write(chunk)
    print("\t * Written file aprox. {0} MB  ".format(round(chunk_size * count / 1024 /1024)))
    # Uncompress the zip file
    print("3. Uncompressing data file {0}...".format(output_path))
    #extract_path = os.path.join(base_path, resource_link.rsplit('/', 1)[1].rsplit('.')[0])
    extract_path = base_path
    time.sleep(3)
    zf = ZipFile(output_path,'r')
    zf.extractall(extract_path)
    print("\t * Extracted files to {0} ".format(extract_path))
    print("\t * Removing file {0} ".format(output_path))
    rmcomm = 'rm '+output_path
    os.system(rmcomm)
    #remove MACOS folder that is part of zips
    #os.system('rm -r ./data/__MACOSX')
    print(" --- DONE --- ")



####################### Function to read station link csv and download L0 data##
def getLevel0(linkfile):
    ##Read CSV 'envidat_gcnet_links.csv' containing download link URLs
    linkarr = np.genfromtxt(linkfile,delimiter=',',dtype=None,encoding='utf-8')
    #Loop through all download links and download and unzip data
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

    # change incoming sw (some stations have (1))
    try:
        dfm=dfm.rename(columns={"sw_in_avg(1)":"ISWR"})
    except:
        print("Error changing sw_in_avg(1) column")

    # change incoming sw
    try:
        dfm=dfm.rename(columns={"sw_in_avg":"ISWR"})
    except:
        print("Error changing sw_in_avg column")

    # change outgoing sw
    try:
        dfm=dfm.rename(columns={"sw_ref_avg(1)":"OSWR"})
    except:
        print("Error changing sw_ref_avg(1) column")

    # change outgoing sw alternate form
    try:
        dfm=dfm.rename(columns={"sw_ref_avg":"OSWR"})
    except:
        print("Error changing sw_ref_avg column")

    # change net radiation
    try:
        dfm=dfm.rename(columns={"net_rad_avg":"NSWR"})
    except:
        print("Error changing net_rad_avg column")

    # change cs500 temperature 1
    try:
        dfm=dfm.rename(columns={"t_air_avg(1)":"TA3"})
    except:
        print("Error changing t_air_avg(1) column")

    # change cs500 temperature 2
    try:
        dfm=dfm.rename(columns={"t_air_avg(2)":"TA4"})
    except:
        print("Error changing t_air_avg(2) column")

    # change cs500 temperature 1 (alternate name)
    try:
        dfm=dfm.rename(columns={"t_air1_avg":"TA3"})
    except:
        print("Error changing t_air1_avg column")

    # change cs500 temperature 2 (alternate name)
    try:
        dfm=dfm.rename(columns={"t_air2_avg":"TA4"})
    except:
        print("Error changing t_air2_avg column")

    # change thermocouple 1
    try:
        dfm=dfm.rename(columns={"tc_air_avg(1)":"TA1"})
    except:
        print("Error changing tc_air_avg(1) column")

    # change thermocouple 1 (alternate)
    try:
        dfm=dfm.rename(columns={"tc_air_avg":"TA1"})
    except:
        print("Error changing tc_air_avg column")

    # change thermocouple 2
    try:
        dfm=dfm.rename(columns={"tc_air_avg(2)":"TA2"})
    except:
        print("Error changing tc_air_avg(2) column")

    # change relative humidity 1
    try:
        dfm=dfm.rename(columns={"rh_avg(1)":"RH1"})
    except:
        print("Error changing rh_avg(1) column")

    # change relative humidity 2
    try:
        dfm=dfm.rename(columns={"rh_avg(2)":"RH2"})
    except:
        print("Error changing rh_avg(2) column")

    # change windspeed 1
    try:
        dfm=dfm.rename(columns={"u_avg(1)":"VW1"})
    except:
        print("Error changing u_avg(1) column")

    # change windspeed 2
    try:
        dfm=dfm.rename(columns={"u_avg(2)":"VW2"})
    except:
        print("Error changing u_avg(2) column")

    # change wind direction 1
    try:
        dfm=dfm.rename(columns={"dir_avg(1)":"DW1"})
    except:
        print("Error changing dir_avg(1) column")

    # change wind direction 2
    try:
        dfm=dfm.rename(columns={"dir_avg(2)":"DW2"})
    except:
        print("Error changing dir_avg(2) column")

    # change wind direction 1 (alternate)
    try:
        dfm=dfm.rename(columns={"dir1_avg":"DW1"})
    except:
        print("Error changing dir1_avg column")

    # change wind direction 2 (alternate)
    try:
        dfm=dfm.rename(columns={"dir2_avg":"DW2"})
    except:
        print("Error changing dir2_avg column")

    # change pressure
    try:
        dfm=dfm.rename(columns={"pressure_avg":"P"})
    except:
        print("Error changing pressure_avg column")

    # change sonic height 1
    try:
        dfm=dfm.rename(columns={"sd_1_avg":"HW1"})
    except:
        print("Error changing sd_1_avg column")

    # change sonic height 2
    try:
        dfm=dfm.rename(columns={"sd_2_avg":"HW2"})
    except:
        print("Error changing sd_2_avg column")

    # change thermocouple max
    try:
        dfm=dfm.rename(columns={"tc_air_max":"TA1_max"})
    except:
        print("Error changing tc_air_max column")

    # change thermocouple min
    try:
        dfm=dfm.rename(columns={"tc_air_min":"TA1_min"})
    except:
        print("Error changing tc_air_min column")

    # change windspeed max 1
    try:
        dfm=dfm.rename(columns={"u_max(1)":"VW1_max"})
    except:
        print("Error changing u_max(1) column")

    # change windspeed max 2
    try:
        dfm=dfm.rename(columns={"u_max(2)":"VW2_max"})
    except:
        print("Error changing u_max(2) column")

    # change windspeed std 1
    try:
        dfm=dfm.rename(columns={"u_std(1)":"VW1_stdev"})
    except:
        print("Error changing u_std(1) column")

    # change windspeed std 2
    try:
        dfm=dfm.rename(columns={"u_std(2)":"VW2_stdev"})
    except:
        print("Error changing u_std(2) column")

    # change incoming shortwave max
    try:
        dfm=dfm.rename(columns={"sw_in_max(1)":"ISWR_max"})
    except:
        print("Error changing sw_in_max(1) column")

    # change incoming shortwave max (alternate)
    try:
        dfm=dfm.rename(columns={"sw_in_max":"ISWR_max"})
    except:
        print("Error changing sw_in_max column")

    # change incoming shortwave standard deviation
    try:
        dfm=dfm.rename(columns={"sw_in_std(1)":"ISWR_std"})
    except:
        print("Error changing sw_in_std(1) column")

    # change incoming shortwave standard deviation (alternate form)
    try:
        dfm=dfm.rename(columns={"sw_in_std":"ISWR_std"})
    except:
        print("Error changing sw_in_std column")

    # change net radiation standard deviation
    try:
        dfm=dfm.rename(columns={"net_rad_std":"NSWR_std"})
    except:
        print("Error changing net_rad_std column")

    # change thermocouple max 1
    try:
        dfm=dfm.rename(columns={"tc_air_max(1)":"TA1_max"})
    except:
        print("Error changing tc_air_max(1) column")

    # change thermocouple max 2
    try:
        dfm=dfm.rename(columns={"tc_air_max(2)":"TA2_max"})
    except:
        print("Error changing tc_air_max(2) column")

    # change thermocouple min 1
    try:
        dfm=dfm.rename(columns={"tc_air_min(1)":"TA1_min"})
    except:
        print("Error changing tc_air_min(1) column")

    # change thermocouple min 2
    try:
        dfm=dfm.rename(columns={"tc_air_min(2)":"TA2_min"})
    except:
        print("Error changing tc_air_min(2) column")

    # change battery voltage
    try:
        dfm=dfm.rename(columns={"battery":"V"})
    except:
        print("Error changing battery column")

    # change battery voltage (alternate)
    try:
        dfm=dfm.rename(columns={"batt_volt":"V"})
    except:
        print("Error changing batt_volt column")

    # change reference temperature
    try:
        dfm=dfm.rename(columns={"tref_avg":"TA5"})
    except:
        print("Error changing tref_avg column")
    # change names of 10 snow temperatures
    try:
        dfm=dfm.rename(columns={"tc_snow_avg(1)":"TS1"})
    except:
        print("Error changing tc_snow_avg(1) column")
    try:
        dfm=dfm.rename(columns={"tc_snow_avg(2)":"TS2"})
    except:
        print("Error changing tc_snow_avg(2) column")
    try:
        dfm=dfm.rename(columns={"tc_snow_avg(3)":"TS3"})
    except:
        print("Error changing tc_snow_avg(3) column")
    try:
        dfm=dfm.rename(columns={"tc_snow_avg(4)":"TS4"})
    except:
        print("Error changing tc_snow_avg(4) column")
    try:
        dfm=dfm.rename(columns={"tc_snow_avg(5)":"TS5"})
    except:
        print("Error changing tc_snow_avg(5) column")
    try:
        dfm=dfm.rename(columns={"tc_snow_avg(6)":"TS6"})
    except:
        print("Error changing tc_snow_avg(6) column")
    try:
        dfm=dfm.rename(columns={"tc_snow_avg(7)":"TS7"})
    except:
        print("Error changing tc_snow_avg(7) column")
    try:
        dfm=dfm.rename(columns={"tc_snow_avg(8)":"TS8"})
    except:
        print("Error changing tc_snow_avg(8) column")
    try:
        dfm=dfm.rename(columns={"tc_snow_avg(9)":"TS9"})
    except:
        print("Error changing tc_snow_avg(9) column")
    try:
        dfm=dfm.rename(columns={"tc_snow_avg(10)":"TS10"})
    except:
        print("Error changing tc_snow_avg(10) column")
    #return new dataframe
    return dfm

### This functions takes the merged dataframe dfm and adds offset add_value
### to each field in the string list fields
### returns the modified dfm
def calibrate_add_value(dfm,fields,add_value):
    # loop through length-1 because we dont add to timestamp
    for i in range(len(fields)-1):
        i = i+1 #we don't want to add to timestamp so we start at index 1
        dfm[fields[i]]=dfm[fields[i]]+add_value[i]
    return dfm

### This functions takes the merged dataframe dfm and multiples scale_factor
### to positive values (>0) in each field in the string list fields
### returns the modified dfm
def calibrate_scale_factor(dfm,fields,scale_factor):
    # loop through length-1 because we dont add to timestamp
    for i in range(len(fields)-1):
        i = i+1 #we don't want to add to timestamp so we start at index 1
        #col = dfm[fields[i]]
        #col[col>0]=col[col>0]*scale_factor[i]
        #dfm[fields[i]]=col
        #make multiplation in place for locations greater than 0
        dfm.loc[dfm[fields[i]] > 0,fields[i]] *= scale_factor[i]
    return dfm

### This functions takes the merged dataframe dfm and multiples scale_factor_neg
### to negative values (<0) in each field in the string list fields
### returns the modified dfm
def calibrate_scale_factor_neg(dfm,fields,scale_factor_neg):
    # loop through length-1 because we dont add to timestamp
    for i in range(len(fields)-1):
        i = i+1 #we don't want to add to timestamp so we start at index 1
        #col = dfm[fields[i]]
        #col[col<0]=col[col<0]*scale_factor_neg[i]
        #dfm[fields[i]]=col
        dfm.loc[dfm[fields[i]] < 0,fields[i]] *= scale_factor_neg[i]
    return dfm

def read_c_file(c_file_path,c_file_header_str):
    print('Now reading: ',c_file_path)
    dfc = pd.read_csv(c_file_path,sep='\s+',names=c_file_header_str,header=None,na_values=[999.0, -999,999.99,999.999])
    # define timestamp from Year and DoY (fractional ordinal day)
    dfc['timestamp'] = pd.to_datetime(dfc.year,format='%Y') + pd.to_timedelta(dfc.DoY - 1, unit='d')
    # round to the nearest hour (there is some remainder from fractional day)
    dfc['timestamp']=dfc['timestamp'].dt.round('H')
    dfc = dfc.set_index("timestamp")
    #pd.to_datetime(dfc.index)
    # remove any possible duplicate datetimes
    dfc = dfc[~dfc.index.duplicated(keep='first')]
    dfc = dfc.sort_index()
    #dfc = pd.concat([df1,df2]).drop_duplicates(subset=["timestamp"])
    return dfc

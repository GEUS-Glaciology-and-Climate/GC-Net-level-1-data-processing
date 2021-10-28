# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:00:14 2020

@author: bav
"""
# %matplotlib inline
# %matplotlib qt
import os, sys
import PROMICE_toolbox as ptb
import matplotlib.pyplot as plt
import pandas as pd
import nead
import os.path
import numpy as np
from os import path
try:
    os.mkdir('figures')
    os.mkdir('figures/L1_data_treatment')
    os.mkdir('out')
except:
    print('figures and output folders already exist')

# sys.stdout = open("Report.md", "w")

#path_to_L0N = 'L0N/'
path_to_L0N = 'L0M/'
site_list = pd.read_csv('metadata/GC-Net_location.csv',header=0)
# print(site_list)
site_list = site_list.iloc[6:7,:]
for site, ID in zip(site_list.Name,site_list.ID):
    print('# '+str(ID)+ ' ' + site)
    filename = path_to_L0N+str(ID).zfill(2)+'-'+site+'.csv'
    if not path.exists(filename):
        print('Warning: No file for station '+str(ID)+' '+site)
        continue
    ds =nead.read(filename)
    df = ds.to_dataframe()
    df=df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp).dt.tz_localize('UTC')
    df = df.set_index('timestamp')
    df=df.resample('H').mean()

    # Time shifts:
    df = ptb.time_shifts(df, site)

    # Applying standard filters
    df_out = ptb.filter_data(df, site, remove_data = False)

    print('## Manual flagging of data at '+site)
    df_out = ptb.flag_data(df_out, site, remove_data = False)

    # ptb.plot_flagged_data(df_out, site)

    # Calculating surface height from wind sensor height
    df_out['HS1'] = df_out.HW1[df_out.HW1.first_valid_index()] - df_out.HW1
    df_out['HS2'] = df_out.HW2[df_out.HW2.first_valid_index()] - df_out.HW2

    print('## Adjusting data at '+site)
    df_v4 = ptb.adjust_data(df_out, site)

    if len(df_v4)>0:
        # get info related to the new fields
        units, display_description, database_fields, database_fields_data_types = \
          ptb.field_info(df_v4.reset_index().columns)

        # write ini file
        nead.write_header('L1_ini/'+str(ID).zfill(2)+'-'+site+'_header.ini',
                          df_v4.reset_index(),
                          metadata =  ds.attrs,
                          units = units,
                          display_description = display_description,
                          database_fields = database_fields,
                          database_fields_data_types = database_fields_data_types)

         # saving to file
        nead.write(df_v4.fillna(-999).reset_index(), 'L1_ini/'+str(ID).zfill(2)+'-'+site+'_header.ini',
                   'L1/'+str(ID).zfill(2)+'-'+site+'.csv')

#%run tocgen.py Report.md Report_toc.md
# sys.stdout.close()

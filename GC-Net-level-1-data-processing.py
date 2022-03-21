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

# sys.stdout = open("out/Report.md", "w")

path_to_L0N = 'L0M/'
site_list = pd.read_csv('metadata/GC-Net_location.csv',header=0)
# print(site_list)
# site_list = site_list.iloc[8:9,:] # DYE-2
site_list = site_list.iloc[6:7,:] # Summit
# site_list = site_list.iloc[7:8,:] 

for site, ID in zip(site_list.Name,site_list.ID):
    plt.close('all')
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
    df_out = ptb.filter_data(df, site)

    print('## Manual flagging of data at '+site)
    df_out = ptb.flag_data(df_out, site)

    ptb.plot_flagged_data(df_out, site)
    df_out = ptb.remove_flagged_data(df_out)
    
    print('## Adjusting data at '+site)
    # we start by adjusting and filtering the height of the wind sensors
    df_v4 = ptb.adjust_data(df_out, site, ['HW1', 'HW2'])
    
    # Calculating surface height from wind sensor height
    df_v4['HS1'] = df_v4.HW1[df_v4.HW1.first_valid_index()] - df_v4.HW1
    df_v4['HS2'] = df_v4.HW2[df_v4.HW2.first_valid_index()] - df_v4.HW2
    if 'HW1_qc' not in df_out.columns:
        df_v4['HW1_qc'] = ''
    if 'HW2_qc' not in df_out.columns:
        df_v4['HW2_qc'] = ''
    df_v4.loc[df_v4['HW1_qc']=="CHECKME", 'HS1'] = np.nan
    df_v4.loc[df_v4['HW2_qc']=="CHECKME", 'HS2'] = np.nan
    
    print('## Adjusting data at '+site)
    # we then adjust and filter all other variables than height of the wind sensors
    df_v5 = ptb.adjust_data(df_v4, site, skip_var = ['HW1', 'HW2'])
    
    if len(df_v5)>0:
        # get info related to the new fields
        units, display_description, database_fields, database_fields_data_types = \
          ptb.field_info(df_v5.reset_index().columns)

        # write ini file
        nead.write_header('L1_ini/'+str(ID).zfill(2)+'-'+site+'_header.ini',
                          df_v5.reset_index(),
                          metadata =  ds.attrs,
                          units = units,
                          display_description = display_description,
                          database_fields = database_fields,
                          database_fields_data_types = database_fields_data_types)

         # saving to file
        nead.write(df_v5.fillna(-999).reset_index(), 'L1_ini/'+str(ID).zfill(2)+'-'+site+'_header.ini',
                   'L1/'+str(ID).zfill(2)+'-'+site+'.csv')

#%run tocgen.py out/Report.md out/Report_toc.md
# sys.stdout.close()

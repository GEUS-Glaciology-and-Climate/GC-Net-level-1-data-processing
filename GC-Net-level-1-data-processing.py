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
from os import path
try:
    os.mkdir('figures')
    os.mkdir('out')
except:
    print('figures and output folders already exist')

sys.stdout = open("out/Report.md", "w")

path_to_L0N = 'L0N/'
site_list = pd.read_csv('metadata/GC-Net_location.csv',header=0)
# site_list = site_list.iloc[19:,:]
for site, ID in zip(site_list.Name,site_list.ID):
    print('# '+str(ID)+ ' ' + site)
    filename = path_to_L0N+str(ID).zfill(2)+'-'+site+'.csv'
    if not path.exists(filename):
        print('Warning: No file for station '+str(ID)+' '+site)
        continue
    df =nead.read(filename).to_dataframe()
    df=df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp).dt.tz_localize('UTC')
    df = df.set_index('timestamp')
    print('## Removing erroneous data at '+site)
    df_out = ptb.flag_data(df, site, plot=True, remove_data = True)
    
    print('## Adjusting data at '+site)
    df_v4 = ptb.adjust_data(df_out, site)
                    
    if len(df)>0:
        # saving to file
        nead.write(df_v4.fillna(-999).reset_index(), 'L0N_ini/'+str(ID).zfill(2)+'-'+site+'_header.ini', 
                   'L1/'+str(ID).zfill(2)+'-'+site+'.csv')

%run tocgen.py out/Report.md out/Report_toc.md

# sys.stdout.close()

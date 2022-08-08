# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""


import nead
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import os
from os import path

name_alias = {'CP1':'Crawford Point 1', 'DY2': 'DYE2', 'EGP':'E-GRIP',
              'NAU':'NASA-U', 'HUM':'Humboldt', 'SUM':'Summit', 'GIT':'GITS',
              'JR3':'JAR3', 'NSE':'NASA-SE', 'TUN':'Tunu-N', 'JAR':'JAR1',
              'JR2':'JAR2', 'NAE':'NASA-E', 'SDM':'South Dome', 'NEM':'NEEM',
              'SWC':'Swiss Camp', 'SW1':'Swiss Camp 10m', 'SDL':'Saddle',
              'NGP':'NGRIP', 'PET':'Petermann ELA', 'CP2':'Crawford Point 2'}

site_list = pd.read_csv('metadata/GC-Net_location.csv',header=0, skipinitialspace = True)
# uncomment for use at specific sites
# All station names: 'Swiss Camp 10m', 'Swiss Camp', 'Crawford Point 1', 'NASA-U',
       # 'GITS', 'Humboldt', 'Summit', 'Tunu-N', 'DYE2', 'JAR1', 'Saddle',
       # 'South Dome', 'NASA-E', 'CP2', 'NGRIP', 'NASA-SE', 'KAR', 'JAR 2',
       # 'KULU', 'Petermann ELA', 'NEEM', 'E-GRIP'
# site_list = site_list.loc[site_list.Name.values == 'NASA-E',:]

for site, ID in zip(site_list.Name,site_list.ID):
    print('# '+str(ID)+ ' ' + site)
    filename = 'L1/'+str(ID).zfill(2)+'-'+site.replace(' ','')+'.csv'
    if not path.exists(filename):
        print('Warning: No file for station '+str(ID)+' '+site)
        # continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df=df.reset_index(drop=True)
    df[df == -999] = np.nan
    df['time'] = pd.to_datetime(df.timestamp)
    df = df.set_index('time')

    # read observed instrument height data
    try:      
        url = 'https://docs.google.com/spreadsheets/d/172LNxgYevqwO892zrc98UDMAVTQmJ0XZB5kmMLme4GM/gviz/tq?tqx=out:csv&sheet='+site.replace(' ','%20')
        pd.read_csv(url).to_csv('metadata/maintenance summary/'+site+'.csv')
    except:
        print('Cannot download maintenance summary. Using local file.')
        pass

    obs_df = pd.read_csv('metadata/maintenance summary/'+site+'.csv')    
    obs_df['date'] = pd.to_datetime(obs_df['date'], utc=True)
    obs_df = obs_df.set_index('date')
    useful_columns = ['W1 before (cm)', 'W1 after (cm)',
                  'W2 before (cm)','W2 after (cm)',
                  'T1 before (cm)','T1 after (cm)',
                  'T2 before (cm)','T2 after (cm)']
    if obs_df[useful_columns].notnull().sum().sum() == 0:
        print('no intrument height reported at ', site)
        # continue
    obs_df[useful_columns] = obs_df[useful_columns]/100
    
    # read photogrammetry heights
    df_photo = pd.read_csv('metadata/photogrammetry_20220726T150919_instrument_height_files_concat.csv')
    df_photo = df_photo.replace({'site': name_alias})
    df_photo = df_photo.loc[df_photo.site==site, :]
    for var in ['month', 'day', 'Wz1','Wz2','THz1','THz2']:
        df_photo[var] = pd.to_numeric(df_photo[var], errors='coerce').values
    df_photo.loc[df_photo.month.isnull(), 'month'] = np.round(df_photo.month.mean())
    df_photo.loc[df_photo.day.isnull(), 'day'] = np.round(df_photo.day.mean())
    df_photo['date'] = pd.to_datetime(df_photo[['year','month','day']])
    df_photo = df_photo.set_index('date').drop(columns = ['site','year','month','day'])


    df_photo[['Wz1','Wz2','THz1','THz2']] = df_photo[['Wz1','Wz2','THz1','THz2']].values
    
    df_photo_m = pd.read_csv('metadata/photogrammetry_instrument_height_20220425.csv')
    df_photo_m = df_photo_m.replace({'site': name_alias})
    df_photo_m = df_photo_m.loc[df_photo_m.site==site, :]
    df_photo_m['date'] = pd.to_datetime(df_photo_m[['year','month','day']])
    df_photo_m = df_photo_m.set_index('date').drop(columns = ['site','year','month','day'])
    
        
    fig = plt.figure(figsize=(16,10))
    ax = plt.subplot(111)
       
    sym_size=20
    mult=0.6
    # Plotting observed instrument heights
    obs_df['W1 before (cm)'].plot(ax=ax, marker = '>', linestyle = 'None',
              markerfacecolor='none', markersize=sym_size*mult,c='C0',label='HW1 obs before')
    obs_df['W2 before (cm)'].plot(ax=ax, marker = '>', linestyle = 'None',
              markerfacecolor='none', markersize=sym_size*mult,c='C1',label='HW2 obs before')
    obs_df['W1 after (cm)'].plot(ax=ax, marker = '<', linestyle = 'None',
              markerfacecolor='none', markersize=sym_size*mult,c='C0',label='HW1 obs after')
    obs_df['W2 after (cm)'].plot(ax=ax, marker = '<', linestyle = 'None',
              markerfacecolor='none', markersize=sym_size*mult,c='C1',label='HW2 obs after')
    
    obs_df['T1 before (cm)'].plot(ax=ax, marker = '>', linestyle = 'None',
              markerfacecolor='none', markersize=sym_size*mult,c='C2',label='HT1 obs before')
    obs_df['T2 before (cm)'].plot(ax=ax, marker = '>', linestyle = 'None',
              markerfacecolor='none', markersize=sym_size*mult,c='C3',label='HT2 obs before')
    obs_df['T1 after (cm)'].plot(ax=ax, marker = '<', linestyle = 'None',
              markerfacecolor='none', markersize=sym_size*mult,c='C2',label='HT1 obs afer')
    obs_df['T2 after (cm)'].plot(ax=ax, marker = '<', linestyle = 'None',
              markerfacecolor='none', markersize=sym_size*mult,c='C3',label='HT2 obs after')
    
    df_photo[['Wz1','Wz2','THz1','THz2']].plot(ax=ax, marker='o', linestyle='None')
    df_photo_m[['Wz1','Wz2','THz1','THz2']].plot(ax=ax, marker='x', linestyle='None')

    df['HW1'].plot(ax =ax, c='C0',label='HW1')
    df['HW2'].plot(ax =ax, c='C1',label='HW2')
    
    plt.ylabel('Height above surface (m)')
    plt.title(site+' profile instrument heights')
    plt.legend()
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    plt.savefig('figures/L1_overview/instrument_height_assessment/'+site.replace(' ','')+'_height_comparison.png', bbox_inches='tight',dpi=250)
    print('![](../figures/L1_overview/instrument_height_assessment/'+site.replace(' ','')+'_height_comparison.png)')

#%run tools/tocgen.py out/L1_intrument_heights.md out/L1_intrument_heights_toc.md


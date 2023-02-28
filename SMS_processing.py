# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import os 
import pandas as pd
import numpy as np

list_files = os.listdir('L0/25-SMS1')
list_files.remove('raw')
list_files.remove('SMS02-03-2.DAT')
list_files.remove('SMS02-03.DAT')
df_all = pd.DataFrame()
for file in list_files:
    df= pd.read_csv('L0/25-SMS1/'+file)
    if df.shape[1] == 11:
        df.columns =['id', 'year', 'day', 'hour', 'TA1',
               'TA2', 'RH1', 'VW1',
               'DW1', 'VW1_max', 'HW1']
        df['V'] = np.nan
    if df.shape[1] == 12:
        df.columns =['id', 'year', 'day', 'hour', 'TA1',
               'TA2', 'RH1', 'VW1',
               'DW1', 'VW1_max', 'HW1', 'V']

    df['minutes'] = df.hour - np.trunc(df.hour/100)*100
    df['hour'] = np.trunc(df.hour/100)
    df['timestamp'] = pd.to_datetime(df.year * 10000000 + df.day * 10000 + df.hour*100 + df.minutes , utc=True, format='%Y%j%H%M', errors='coerce')
    df = df.drop(columns=['day','year','hour','id'])
    print(file, df.shape[1])
    if file == list_files[0]:
        df_all = df
    else:
        df_all = pd.concat((df_all,df))

df_all = df_all.set_index('timestamp')
df_all[df_all<-6000] = np.nan
df_all = df_all.drop(columns=['minutes'])
df_all = df_all.sort_index()
df_all[['TA2','TA1']].plot()
#%%
import write_nead
write_nead.write_nead(df_all.reset_index(), 
                      'L0/L0_ini/25-SMS1.ini',
                      'L0M/25-SMS1')



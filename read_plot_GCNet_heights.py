#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:54:18 2022

@author: Jason, Miaken

https://github.com/GEUS-Glaciology-and-Climate/pyNEAD

"""

import nead
import matplotlib.pyplot as plt
# import seaborn as sns; sns.set()
import numpy as np
import pandas as pd
# import math
from datetime import datetime
import os

# -------------------------------- chdir
if os.getlogin() == 'jason':
    base_path = '/Users/jason/Dropbox/AWS/GC-Net-level-1-data-processing/'
    z_path='/Users/jason/Dropbox/GCNet_photogrammetry/output/'

os.chdir(base_path)


site='06-Summit'
site='08-DYE2' ; site_name2="DYE-2"
# site='02-Crawford Point 1' ; site_name2="CP1"

ds = nead.read("./L1/"+site+".csv", index_col=0)
print(ds)
#%% convert nead format to Pandas dataframe
df=ds.to_dataframe()

print(df.columns)

for column in df.columns:
    print(column)
    if column[-2:]!='qc': # ignore quality control columns
        df[column] = pd.to_numeric(df[column])
        df[column][df[column]<=-999]=np.nan

# t0=datetime(1996,5,25,23); t1=datetime(1999,12,31,1)

# df_nead['date']=df_nead.index.strftime("%Y-%m-%d")
df['date'] = pd.to_datetime(df.index)

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['hour'] = df['date'].dt.hour
df["time"]=pd.to_datetime(df[['year', 'month', 'day', 'hour']])

df = df.loc[df['time']<'2000-01-01',:] 

#%% diagnostic

plt.title(site+' profile instrument heights')
plt.plot(df['HW1'],c='C0',label='HW1')
plt.plot(df['HW2'],c='C1',label='HW2')
plt.legend()

#%% diagnostic
plt.title(site+' snow heights')
plt.plot(df['HS1'],c='C0',label='HS1')
plt.plot(df['HS2'],c='C1',label='HS2')
plt.legend()

#%% read instrument height data
from glob import glob

files = sorted(glob(z_path+"*.csv"), reverse=False)

z_df=pd.read_csv(files[0])
for i,file in enumerate(files[1:]):
    print(i,file)
    z_df = pd.concat([z_df,pd.read_csv(files[i])])

z_df["time"]=pd.to_datetime(z_df[['year', 'month', 'day']])
z_df.index = pd.to_datetime(z_df.time)

t0=datetime(1996,5,25,23); t1=datetime(1999,12,31,1)

# df_nead['date']=df_nead.index.strftime("%Y-%m-%d")

# df_nead = df_nead.loc[df_nead['time']<'1997-01-01',:] 


#%% read observed instrument height data

obs_df = pd.read_excel('./metadata/GCNet_maintenance.xlsx',sheet_name=site_name2,engine='openpyxl')
print(obs_df)

obs_df["Date (dd-mm-yyyy HH:MM)"]=pd.to_datetime(obs_df['Date (dd-mm-yyyy HH:MM)'])
#obs_df.index = pd.to_datetime(obs_df.time)

#%% graphics parameters

th=1 #line thickness
font_size=22
plt.rcParams["font.size"] = font_size
plt.rcParams['axes.facecolor'] = 'w'
plt.rcParams['axes.edgecolor'] = 'k'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 1
plt.rcParams['grid.color'] = "#cccccc"
plt.rcParams["legend.facecolor"] ='w'
plt.rcParams["mathtext.default"]='regular'
plt.rcParams['grid.linewidth'] = th
plt.rcParams['axes.linewidth'] = th #set the value globally
plt.rcParams['figure.figsize'] = 12, 10
plt.rcParams["legend.framealpha"] = 0.8

end_year=2006
# end_year=2019 # I just get an error when trying to extend
t0=datetime(1996, 4, 1) ; t1=datetime(end_year, 6, 21)

fig = plt.figure()
ax = plt.subplot(111)

plt.plot(df['HW1'][t0:t1],c='C0',label='HW1')
plt.plot(df['HW2'][t0:t1],c='C1',label='HW2')

sym_size=20

mult=1.3
# Plotting observed instrument heights
plt.plot(obs_df["Date (dd-mm-yyyy HH:MM)"],obs_df['W1 before (cm)']/100,'*',
         markerfacecolor='none', markersize=sym_size*mult,c='C0',label='HW1 obs')
plt.plot(obs_df["Date (dd-mm-yyyy HH:MM)"],obs_df['W2 before (cm)']/100,'*',
         markerfacecolor='none', markersize=sym_size*mult,c='C1',label='HW2 obs')

plt.plot(obs_df["Date (dd-mm-yyyy HH:MM)"],obs_df['T1 before (cm)']/100,'o',
         markerfacecolor='none', markersize=sym_size*mult,c='C0',label='HT1 obs')
plt.plot(obs_df["Date (dd-mm-yyyy HH:MM)"],obs_df['T2 before (cm)']/100,'o',
         markerfacecolor='none', markersize=sym_size*mult,c='C1',label='HT2 obs')

#plt.plot(obs_df['HW2'][t0:t1],'o',c='C1',label='HW2')

# plt.plot(df['HS1'][t0:t1],label='HS1')
# plt.plot(df['HS2'][t0:t1],label='HS2')
# plt.plot(df['HW2']-df['HW1'],label='HW2 minus HW1')
# for i in range(len(z_df)): # Should it not be Wz1 and Wz2, not THz1, THz2?
#     if z_df.year[i]<=end_year:
#         mult=0.5
#         plt.plot(datetime(z_df.year[i],z_df.month[i],z_df.day[i]),z_df.THz1[i],
#                  's', markersize=sym_size, markerfacecolor='none',
#                  markeredgewidth=1.5, markeredgecolor='C0')
#         plt.text(datetime(z_df.year[i],z_df.month[i],z_df.day[i]),z_df.THz1[i],
#                 z_df.time[i].strftime('%Y %m %d'),c='k',rotation=45,fontsize=font_size*mult)#,label='THz1')
#         plt.plot(datetime(z_df.year[i],z_df.month[i],z_df.day[i]),z_df.THz2[i],
#                  's', markersize=sym_size, markerfacecolor='none',
#                  markeredgewidth=1.5, markeredgecolor='C1')
#         plt.text(datetime(z_df.year[i],z_df.month[i],z_df.day[i]),z_df.THz2[i],
#                 z_df.time[i].strftime('%Y %m %d'),c='k',rotation=45,fontsize=font_size*mult)

plt.ylabel('m')
plt.title(site+' profile instrument heights')
# plt.legend()
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

ly='x'

if ly=='x':
    plt.show()
    
if ly=='p':
    plt.savefig('./Figs/'+site+'_height_comparison.png', bbox_inches='tight',dpi=250)#



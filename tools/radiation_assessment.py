# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import os, sys
import PROMICE_toolbox as ptb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import nead
import os.path
from os import path
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
# Set the locator
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y')

# %% L1 temperature overview
plt.close('all')
site_list = pd.read_csv('metadata/GC-Net_location.csv',header=0)#.iloc[:1]
for site, ID in zip(site_list.Name,site_list.ID):
    variable_list = np.array(['ISWR', 'OSWR', 'albedo'])

    print('# '+str(ID)+ ' ' + site)
    site = site.replace(' ','')
    filename = 'L1/'+str(ID).zfill(2)+'-'+site+'.csv'
    if not path.exists(filename):
        print('Warning: No file for station '+str(ID)+' '+site)
        continue
    ds = nead.read(filename)
    df = ds.to_dataframe()
    df=df.reset_index(drop=True)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.set_index('timestamp').replace(-999,np.nan)
    
    df['albedo'] = df.OSWR/df.ISWR
    msk = (df.OSWR<100) | (df.ISWR<100)
    df.loc[msk, 'albedo'] = np.nan
    
    # % plotting variables
    fig, ax = plt.subplots(4,1,sharex=True, figsize=(15,15))
    plt.subplots_adjust(left = 0.1, right=0.9, top = 0.95, bottom = 0.1, wspace=0.2, hspace=0.05)
    plt.suptitle(site)
    count = 0
    count_fig = 0
    if len(variable_list)==0:
        variable_list = df.columns
    else:
        variable_list = variable_list[np.isin(variable_list, df.columns.values)]
    for i, var in enumerate(variable_list):       
        df[var].plot(ax=ax[count])
        ax[count].set_ylabel(var)
        ax[count].grid()
        # ax[count].axes.xaxis.set_major_formatter(years_fmt)
        # ax[count].axes.xaxis.set_major_locator(years)
        # ax[count].axes.xaxis.set_minor_locator(months)
        ax[count].set_xlim((df.index[0],df.index[-1]))
        count=count+1
    plt.savefig('figures/L1_overview/radiation_assessment/'+str(ID)+'_'+site+'_albedo',bbox_inches='tight')
    print('![](figures/L1_overview/radiation_ assessment/'+str(ID)+'_'+site+'_albedo.png)')


# %run tocgen.py out/L1_overview.md out/L1_overview_toc.md
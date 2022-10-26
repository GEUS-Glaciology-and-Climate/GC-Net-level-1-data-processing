# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""

import os, sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%% Comparison of the logger files and calibration factors to the "tow_all" processed files
plt.close('all')
yr = 2000
df2 = pd.read_csv('CR10X logger files/'+str(yr)+'_sc10m.dat', header=None)
df2 = df2.drop(columns=[0])
# .astype(str).replace(to_replace = "\.0+$",value = "", regex = True).replace(to_replace = "^0\.",value = ".", regex = True).replace(to_replace = "^-0\.",value = "-.", regex = True).to_csv('tmp.dat',index=None,header=None,line_terminator="")
df2['timestamp'] = pd.to_datetime(df2.iloc[:,0] * 100000 + df2.iloc[:,1] * 100 + df2.iloc[:,2]/100 , format='%Y%j%H')
df2 = df2.set_index('timestamp')
df2 = df2.drop(columns=[1,2,3])
df2[df2==-6999] = np.nan
df2.columns = ['ISWR','OSWR','NR',
               'TA1',    'TA2',    'RH1',    'RH2',     'VW1',     'VW2',
               'TA1_max','TA2_max','RH1_max','RH2_max', 'VW1_max', 'VW2_max',
               'TA1_min','TA2_min','RH1_min','RH2_min', 'VW1_min', 'VW2_min',
               'DW1','DW2']

# calibration:
# shortwave radiation
df2.ISWR = df2.ISWR *106.49
df2.OSWR = df2.OSWR *105.89
# net radiation
msk_pos = df2.NR>0
df2.loc[msk_pos, 'NR'] = df2.loc[msk_pos, 'NR'] *8.02
msk_neg = df2.NR<0
df2.loc[msk_neg, 'NR'] = df2.loc[msk_neg, 'NR'] *12.12

df2.loc[df2.ISWR<0, 'ISWR'] = np.nan
df2.loc[df2.OSWR<0, 'OSWR'] = np.nan
df2.loc[df2.VW1>1000, 'VW1'] = np.nan
df2.loc[df2.VW2>1000, 'VW2'] = np.nan
df2['alb'] = np.maximum(0, df2.OSWR/df2.ISWR)

print('processed/' + str(yr) + '_tow_all.dat')
df = pd.read_fwf('processed/' + str(yr) + '_tow_all.dat', header=None, 
                 widths=[6, 9, 8, 8, 5, 8, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
                         6, 6, 6, 6,6, 6, 8, 8])
for i in range(df.shape[1]):
    df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], errors='coerce')
    
tmp =np.modf(df.iloc[:,1])
df['timestamp'] = pd.to_datetime(df.iloc[:,0]* 100000 + tmp[1] * 100 + np.round(tmp[0]*24) , format='%Y%j%H')
df = df.set_index('timestamp')
df[df==-6999] = np.nan
df.columns = ['year','doy','ISWR','OSWR','alb','NR', 'TA1','TA1_max','TA1_min','TA2','TA2_max',
              'TA2_min', 'RH1','RH1_max','RH1_min','RH2','RH2_max','RH2_min', 
              'VW1','VW1_max','VW1_min', 'VW2','VW2_max','VW2_min','DW1','DW2']
df.alb = df.alb/100
df.loc[df.VW1>1000, 'VW1'] = np.nan
df.loc[df.VW2>1000, 'VW2'] = np.nan

msk = np.intersect1d(df2.index, df.index)
df = df.loc[msk,:]
df2 = df2.loc[msk,:]
# plotting
fig, ax = plt.subplots(2,3, figsize=(16,9))
ax=ax.flatten()
df2[['ISWR','OSWR']].plot(ax=ax[0])
df2.NR.plot(ax=ax[1])
df2[['TA1',    'TA2']].plot(ax=ax[2])
df2[['RH1',    'RH2']].plot(ax=ax[3])
df2[['VW1',     'VW2']].plot(ax=ax[4])
df2[['DW1','DW2']].plot(ax=ax[5])
plt.suptitle('Logger file')

fig, ax = plt.subplots(2,3, figsize=(16,9))
ax=ax.flatten()
df[['ISWR','OSWR']].plot(ax=ax[0])
df.NR.plot(ax=ax[1])
df[['TA1',    'TA2']].plot(ax=ax[2])
df[['RH1',    'RH2']].plot(ax=ax[3])
df[['VW1',     'VW2']].plot(ax=ax[4])
df[['DW1','DW2']].plot(ax=ax[5])
plt.suptitle('Processed file')

fig, ax = plt.subplots(4,4, figsize=(16,9))
ax=ax.flatten()

for i, var in enumerate(['ISWR','OSWR','alb','NR', 'TA1','TA2','TA1_min','TA2_max','TA1_max', 'RH1','RH2', 'VW1','VW2', 'DW1','DW2']):
    ax[i].plot(df[var], df2[var], marker='.',linestyle='None')
    ax[i].plot([df[var].min(), df[var].max()],[df[var].min(), df[var].max()],color='k')
    ax[i].set_title(var)

#%% Comparison of the logger files and calibration factors to the "tow_all" processed files
plt.close('all')
for yr in range(2008,2014):
    df2 = pd.read_csv('CR10X logger files/'+str(yr)+'_sc10m.dat', header=None)
    df2 = df2.drop(columns=[0])
    # .astype(str).replace(to_replace = "\.0+$",value = "", regex = True).replace(to_replace = "^0\.",value = ".", regex = True).replace(to_replace = "^-0\.",value = "-.", regex = True).to_csv('tmp.dat',index=None,header=None,line_terminator="")
    df2['timestamp'] = pd.to_datetime(df2.iloc[:,0] * 100000 + df2.iloc[:,1] * 100 + df2.iloc[:,2]/100 , format='%Y%j%H')
    df2 = df2.set_index('timestamp')
    df2 = df2.drop(columns=[1,2,3])
    df2[df2==-6999] = np.nan
    df2.columns = ['ISWR','OSWR','NR',
                   'TA1',    'TA2',    'RH1',    'RH2',     'VW1',     'VW2',
                   'TA1_max','TA2_max','RH1_max','RH2_max', 'VW1_max', 'VW2_max',
                   'TA1_min','TA2_min','RH1_min','RH2_min', 'VW1_min', 'VW2_min',
                   'DW1','DW2']
    
    # calibration:
    # shortwave radiation
    df2.ISWR = df2.ISWR *106.49
    df2.OSWR = df2.OSWR *105.89
    # net radiation
    msk_pos = df2.NR>0
    df2.loc[msk_pos, 'NR'] = df2.loc[msk_pos, 'NR'] *8.02
    msk_neg = df2.NR<0
    df2.loc[msk_neg, 'NR'] = df2.loc[msk_neg, 'NR'] *12.12
    
    df2.loc[df2.ISWR<0, 'ISWR'] = np.nan
    df2.loc[df2.OSWR<0, 'OSWR'] = np.nan
    df2.loc[df2.VW1>1000, 'VW1'] = np.nan
    df2.loc[df2.VW2>1000, 'VW2'] = np.nan
    df2['alb'] = np.maximum(0, df2.OSWR/df2.ISWR)
    
    print('processed/' + str(yr) + '_rad.dat')
    # if yr >1998:
    df = pd.read_csv('processed/' + str(yr) + '_rad.dat', header=None, delim_whitespace=True)
    for i in range(df.shape[1]):
        df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], errors='coerce')
        
    tmp =np.modf(df.iloc[:,1])
    df['timestamp'] = pd.to_datetime(df.iloc[:,0]* 100000 + tmp[1] * 100 + np.round(tmp[0]*24) , format='%Y%j%H')
    df = df.set_index('timestamp')
    df[df==-6999] = np.nan
    df.columns = ['year','doy','ISWR','OSWR','NR']
    # else:
    #     df = pd.read_csv('processed/' + str(yr) + '_rad.dat', delim_whitespace=True)
    #     df['timestamp'] = pd.to_datetime(1998* 100000 + tmp[1] * 100 + np.round(tmp[0]*24) , format='%Y%j%H')
    #     df[df==-6999] = np.nan
    #     df.columns = ['doy','OSWR','ISWR','alb','NR']
    
    msk = np.intersect1d(df2.index, df.index)
    df = df.loc[msk,:]
    df2 = df2.loc[msk,:]
    # plotting
    fig, ax = plt.subplots(3,3, figsize=(16,9))
    ax=ax.flatten()
    df2.ISWR.plot(ax=ax[0])
    df2.OSWR.plot(ax=ax[1])
    df2.NR.plot(ax=ax[2])
    
    # fig, ax = plt.subplots(1,3, figsize=(16,9))
    ax=ax.flatten()
    df.ISWR.plot(ax=ax[3])
    df.OSWR.plot(ax=ax[4])
    df.NR.plot(ax=ax[5])
    
    # fig, ax = plt.subplots(3,1, figsize=(16,9))
    ax=ax.flatten()
    for i, var in enumerate(['ISWR','OSWR','NR']):
        ax[6+i].plot(df[var], df2[var], marker='.',linestyle='None')
        ax[6+i].plot([df[var].min(), df[var].max()],[df[var].min(), df[var].max()],color='k')
        ax[6+i].set_title(var)
    plt.suptitle(yr)
    
#%%
# c       pyranometer: up # 12875, channel 1, close to mast (cal. 106.49)
# c       pyranometer: down # 12798, channel 2, above down looking (cal. 105.89)
# c       net radiometer: #92263 (+)=8.02, (-)=12.12, channel 3
# c     
# c     two RM-Young, two CS500 temp/hum on hourly logging (now in 98)



# %% notes before 1998:
#     c   UUB coefficients for air temperature
# 	a=-9.0763671
# 	b=0.704343
# 	c=0.00919
# 	d=0.000137
# 	e=0.00000116676
# 	f=0.00000000400674
#     c     correction for wrong offset during winter 95/96
# 	if(t1(1).le.300.) goto 161
# 	t1(1)=t1(1)-400
# 	t1(2)=t1(2)-400
# 	t1(3)=t1(3)-400 
#   161	continue

# 	do 165 l=1,3
# c    convert UUB thermister reading to temperature      
# 	ta1(l)=a+b*t1(l)+c*(t1(l)**2)+d*(t1(l)**3)+e*(t1(l)**4)+
#      1  f*(t1(l)**5)
#   165	continue
# 	
# 	press=press+800.
# 	      
# 	write(3,2032) jd_t,(wind(n),n=1,3),(ta1(n),n=1,3),(t2(n),n=1,3),
#      1  (hum(n),n=1,3),wdir,press
#  2032   format(f9.3,9f7.2,3f7.1,f7.1,f7.1)
# 	goto 100

#   102 if(flag.eq.0) goto 100
# 	backspace (1)
# 	read(1,*,end=7000) ich,r1,r2,net

#%% for 1997
# c       pyranometer: up # 12875, channel 1, close to mast (cal. 106.49)
# c       pyranometer: down # 12798, channel 2, above down looking (cal. 105.89)
# c       net radiometer: #90094, channel 3
# c    convert net radiation mv to W/m2
# c	new net radiation sensor in 97 (old one from Boulder)	
# 	net(ii)=net(ii)*13.3
# both pos and neg

# for 1997-1996
# c       pyranometer: up # 12875, channel 1, close to mast (cal. 106.49)
# c       pyranometer: up # 12798, channel 2, above down looking (cal. 105.89)
# c       pyronometer: down # 12880, channel 3, down (cal. 105.92)
# c       net radiometer: #90094, channel 4
# c    convert net radiation mv to W/m2
# c	new net radiation sensor in 97 (old one from Boulder)	
# 	net=net*13.3

# c       net radiometer: #90094, channel 4
# c	pos: 13.3 * 1.182, neg: 13.3 * 0.962
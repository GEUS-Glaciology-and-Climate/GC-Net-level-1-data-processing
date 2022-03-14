# -*- coding: utf-8 -*-
"""
Created on 27-08-2020

Data treatment function for PROMICE weather station

GEUS (Geological Survey of Denmark and Greenland)

Contributors: Adrien Wehrlé, Jason E. Box, B. Vandecrux

"""
# -*- coding: utf-8 -*-

"""
Tools:
    - smooth
    - hampel
    - firstNonNan
    
tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import Counter
import math
import datetime
import pytz
import os
import warnings
import difflib

warnings.filterwarnings("ignore", category=RuntimeWarning)


def name_alias(name_in):
    
    promice_names = ['AirTemperature1C', 'AirTemperature2C','AirTemperature3C', 
                     'AirTemperature4C', 'RelativeHumidity1Perc', 'RelativeHumidity2Perc',
                     'AirPressurehPa','ShortwaveRadiationDownWm2', 'ShortwaveRadiationUpWm2', 
                     'WindSpeed1ms','WindSpeed2ms','WindDirection1deg','WindDirection2deg',
                     'SnowHeight(m)','SurfaceHeight(m)','SnowHeight1m', 'SnowHeight2m','NetRadiationWm2']
    gcnet_names = ['TA1', 'TA2', 'TA3', 
                   'TA4', 'RH1','RH2', 
                   'P', 'ISWR', 'OSWR',
                   'VW1','VW2','DW1','DW2'
                   'HS1','HS2','HS1', 'HS2','NSWR']
    
    try:
        index = promice_names.index(name_in)
        return gcnet_names[index]
    except:
        return None



def field_info(fields):

    field_list = 'timestamp,ISWR,ISWR_max,ISWR_std,OSWR,NSWR,NSWR_std,TA1,TA1_max,TA1_min,TA2,TA2_max,TA2_min,TA3,TA4,RH1,RH2,VW1,VW1_max,VW1_stdev,VW2,VW2_max,VW2_stdev,DW1,DW2,P,HS1,HS2,HW1,HW2,V,TA5,TS1,TS2,TS3,TS4,TS5,TS6,TS7,TS8,TS9,TS10'.split(',')

    units = 'time,V,V,V,V,V,V,Degrees C,Degrees C,Degrees C,Degrees C,Degrees C,Degrees C,Degrees C,Degrees C,%/100,%/100,m/s,m/s,m/s,m/s,m/s,m/s,Degrees,Degrees,mbar,m,m,m,m,m,m,m,m,m,m,m,m,m,m,V,Degrees C'.split(',')

    display_description = 'timestamp_iso,shortwave_incoming_radiation,shortwave_incoming_radiation_max,shortwave_incoming_radiation_stdev,shortwave_outgoing_radiation,net_radiation,net_radiation_stdev,air_temperature_1,air_temperature_1_max,air_temperature_1_min,air_temperature_2,air_temperature_2_max,air_temperature_2_min,air_temperature_cs500_air1,air_temperature_cs500_air2,relative_humidity_1,relative_humidity_2,wind_speed_1,wind_speed_u1_max,wind_speed_u1_stdev,wind_speed_2,wind_speed_u2_max,wind_speed_u2_stdev,wind_from_direction_1,wind_from_direction_2,air_pressure,snow_depth_1,snow_depth_2,height_wind_sensor_1,height_wind_sensor_2,battery_voltage,ref_temperature,snow_temperature_1,snow_temperature_2,snow_temperature_3,snow_temperature_4,snow_temperature_5,snow_temperature_6,snow_temperature_7,snow_temperature_8,snow_temperature_9,snow_temperature_10'.split(',')

    database_fields = 'timestamp_iso,swin,swin_maximum,swout,swout_minimum,netrad,netrad_maximum,airtemp1,airtemp1_maximum,airtemp1_minimum,airtemp2,airtemp2_maximum,airtemp2_minimum,airtemp_cs500air1,airtemp_cs500air2,rh1,rh2,windspeed1,windspeed_u1_maximum,windspeed_u1_stdev,windspeed2,windspeed_u2_maximum,windspeed_u2_stdev,winddir1,winddir2,pressure,sh1,sh2,hw1,hw2,battvolt,reftemp,ts1,ts2,ts3,ts4,ts5,ts6,ts7,ts8,ts9,ts10'.split(',')

    database_fields_data_types = 'timestamp,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real'.split(',')
    
    field_list = field_list + [s+'_qc' for s in field_list]
    units = units + ['-' for s in units]
    display_description = display_description + [s+'_quality_flag' for s in display_description]
    database_fields = database_fields + [s+'_quality_flag' for s in database_fields]
    database_fields_data_types = database_fields_data_types + ['int' for s in database_fields_data_types]

    ind = [field_list.index(s) for s in fields]
    
    return[ units[i] for i in ind], \
        [display_description[i] for i in ind], \
        [database_fields[i] for i in ind], \
        [database_fields_data_types[i] for i in ind]
            
      

def load_promice(path_promice):
    '''
    Loading PROMICE data for a given path into a DataFrame.
    + adding time index
    + calculating albedo
    + (optional) calculate RH with regard to water
    
    INTPUTS:
        path_promice: Path to the desired file containing PROMICE data [string]
    
    OUTPUTS:
        df: Dataframe containing PROMICE data for the desired settings [DataFrame]
    '''

    df = pd.read_csv(path_promice,delim_whitespace=True)
    df['time'] = df.Year * np.nan
    
    df['time'] = [datetime.datetime(y,m,d,h).replace(tzinfo=pytz.UTC) for y,m,d,h in zip(df['Year'].values,  df['MonthOfYear'].values, df['DayOfMonth'].values, df['HourOfDay(UTC)'].values)]
    df.set_index('time',inplace=True,drop=False)
        
    #set invalid values (-999) to nan 
    df[df==-999.0]=np.nan
    df['Albedo'] = df['ShortwaveRadiationUp(W/m2)'] / df['ShortwaveRadiationDown(W/m2)']
    df.loc[df['Albedo']>1,'Albedo']=np.nan
    df.loc[df['Albedo']<0,'Albedo']=np.nan
    df['SnowHeight(m)'] = 2.6 - df['HeightSensorBoom(m)']
    df['SurfaceHeight(m)'] = 1 - df['HeightStakes(m)']

    # df['RelativeHumidity_w'] = RH_ice2water(df['RelativeHumidity(%)'] ,
    #                                                    df['AirTemperature(C)'])

    return df


def flag_data(df, site, var_list = ['all']):
    '''
    Replace data within a specified variable, between specified dates by NaN.
    Reads from file "metadata/flags/<site>.csv".
    
    INTPUTS:
        df: PROMICE data with time index
        site: string of PROMICE site
        var_list: list of the variables for which data removal should be 
            conducted (default: all)
        plot: whether data removal should be plotted
    
    OUTPUTS:
        promice_data: Dataframe containing PROMICE data for the desired settings [DataFrame]
    '''    
    df_out = df.copy()
    if not os.path.isfile('metadata/flags/'+site+'.csv'):
        print('No erroneous data listed for '+site)
        return df
    
    flag_data = pd.read_csv('metadata/flags/'+site+'.csv')
    
    if var_list[0]=='all':
        var_list =  np.unique(flag_data.variable)
        
    print('Flagging data:')
    for var in var_list:
        if (var not in df_out.columns):
            print('Warning: '+var+' not found')
            continue
            
        if var+'_qc' not in df_out.columns:
            df_out[var+'_qc'] = 'OK'
        
        # df_out.loc[np.logical_and(np.isnan(df_out[var]), df_out[var+'_qc'] == 'OK'), var+'_qc'] = 'NAN'
            
        print('|start time|end time|variable|')
        print('|-|-|-|')
        for t0, t1,flag in zip(pd.to_datetime(flag_data.loc[flag_data.variable==var].t0), 
                               pd.to_datetime(flag_data.loc[flag_data.variable==var].t1),
                               flag_data.loc[flag_data.variable==var].flag):
            print('|'+str(t0) +'|'+ str(t1)+'|'+var+'|')

            df_out.loc[t0:t1, var+'_qc'] = flag

        print(' ')
        print('![Erroneous data at '+ site+'](figures/L1_data_treatment/'+site.replace(' ','_')+'_'+var+'_data_flagging.png)')
        print(' ')

    return df_out


def plot_flagged_data(df, site):
    '''
    Replace data within a specified variable, between specified dates by NaN.
    Reads from file "metadata/flags/<site>.csv".
    
    INTPUTS:
        df: PROMICE data with time index
        site: string of PROMICE site
        var_list: list of the variables for which data removal should be 
            conducted (default: all)
        plot: whether data removal should be plotted
    
    OUTPUTS:
        promice_data: Dataframe containing PROMICE data for the desired settings [DataFrame]
    '''    
       
    for var in df.columns:
        if var[-3:]=='_qc':
            if len(np.unique(df[var].values))>1:
                fig = plt.figure(figsize = (15,10))
                for flag in np.unique(df[var].values):
                    if flag == "OK":
                        df.loc[df[var]==flag, var[:-3]].plot(marker='o',linestyle='none', color ='green', label=flag)
                    elif flag == "CHECKME":
                        df.loc[df[var]==flag, var[:-3]].plot(marker='o',linestyle='none', color ='orange', label=flag)
                    elif flag == "OOL":
                        df.loc[df[var]==flag, var[:-3]].plot(marker='o',linestyle='none', color ='red', label=flag)
                    elif flag == "FROZEN":
                        df.loc[df[var]==flag, var[:-3]].plot(marker='o',linestyle='none', color ='blue', label=flag)
                    elif flag == "FROZEN_WS":
                        df.loc[df[var]==flag, var[:-3]].plot(marker='o',linestyle='none', color ='lightblue', label=flag)
                    else:
                        df.loc[df[var]==flag, var[:-3]].plot(marker='o',linestyle='none', label=flag)
                plt.title(site)
                plt.xlabel('Year')
                plt.ylabel(var[:-3])
                plt.legend() 
                plt.title(site)
                fig.savefig('figures/L1_data_treatment/'+site.replace(' ','_')+'_'+var[:-3]+'_data_flagging.png',dpi=70)



def remove_flagged_data(df):
    '''
    Remove flagged data
    '''
    for var in df.columns:
        if var[-3:]=='_qc':
            if len(np.unique(df[var].values))>1:
                msk = (df[var].values == 'OK') | (df[var].values == '')
                df.loc[~msk, var[:-3]] = np.nan
            df = df.drop(columns=[var])
    return df

def adjust_data(df, site, var_list = []):
    df_out = df.copy()
    if not os.path.isfile('metadata/adjustments/'+site+'.csv'):
        print('No data to fix at '+site)
        return df_out
    
    adj_info = pd.read_csv('metadata/adjustments/'+site+'.csv')
    adj_info=adj_info.sort_values(by=['variable','t0']) 
    adj_info.set_index(['variable','t0'],drop=False,inplace=True)

    if len(var_list) == 0:
        var_list = np.unique(adj_info.variable)

    for var in var_list:       
        if var not in df.columns:
            print(var+' not in datafile')
            continue

        print('### Adjusting '+var)
        print('|start time|end time|operation|value|')
        print('|-|-|-|-|')

        for t0, t1, func, val in zip(adj_info.loc[var].t0,
                                     adj_info.loc[var].t1,
                                     adj_info.loc[var].adjust_function,
                                     adj_info.loc[var].adjust_value):
            
            print('|'+str(t0)+'|'+str(t1)+'|'+func+'|'+str(val)+'|')
            if isinstance(t1, float):
                if np.isnan(t1):
                    t1 = df_out[var].index[-1].isoformat()
            if func == 'add': 
                df_out.loc[t0:t1,var] = df_out.loc[t0:t1,var].values + val
            if func == 'min_filter': 
                tmp = df_out.loc[t0:t1,var].values
                tmp[tmp<val] = np.nan
            if func == 'max_filter': 
                tmp = df_out.loc[t0:t1,var].values
                tmp[tmp>val] = np.nan
                df_out.loc[t0:t1,var] = tmp
            if func == 'upper_perc_filter': 
                tmp = df_out.loc[t0:t1,var].copy()
                df_w = df_out.loc[t0:t1,var].resample('14D').quantile(1-val/100)
                df_w = df_out.loc[t0:t1,var].resample('14D').var()
                for m_start,m_end in zip(df_w.index[:-2],df_w.index[1:]):
                    msk = (tmp.index >= m_start) & (tmp.index < m_end)
                    values_month = tmp.loc[msk].values
                    values_month[values_month<df_w.loc[m_start]] = np.nan
                    tmp.loc[msk] = values_month

                df_out.loc[t0:t1,var] = tmp.values
            if func == 'upper_range_filter': 
                tmp = df_out.loc[t0:t1,var].copy()
                df_max = df_out.loc[t0:t1,var].resample('14D').max()
                for m_start,m_end in zip(df_max.index[:-2], df_max.index[1:]):
                    msk = (tmp.index >= m_start) & (tmp.index < m_end)
                    lim = df_max.loc[m_start] - val
                    values_month = tmp.loc[msk].values
                    values_month[values_month < lim] = np.nan
                    tmp.loc[msk] = values_month

                df_out.loc[t0:t1,var] = tmp.values
                
            if func == 'rotate': 
                df_out.loc[t0:t1,var] = df_out.loc[t0:t1,var].values + val
                df_out.loc[t0:t1,var][df_out.loc[t0:t1,var]>360] = df_out.loc[t0:t1,var]-360

        if df[var].notna().any():
            fig = plt.figure(figsize=(10,5))
            df[var].plot(style='o',label='before adjustment')
            df_out[var].plot(style='o',label='after adjustment')  
            [plt.axvline(t,linestyle='--',color = 'red') for t in adj_info.loc[var].t0.values]
            plt.axvline(np.nan,linestyle='--', color = 'red', label='Adjustment times') 
            plt.xlabel('Year')
            plt.ylabel(var)
            plt.legend()
            plt.title(site)
            fig.savefig('figures/L1_data_treatment/'+site.replace(' ','_')+'_adj_'+var+'.jpeg',dpi=120, bbox_inches='tight')
            print(' ')
            print('![Adjusted data at '+ site +'](figures/L1_data_treatment/'+site.replace(' ','_')+'_adj_'+var+'.jpeg)')
            print(' ')

    return df_out


 
def filter_data(df, site, plot = True, remove_data = False):
    '''
    Applies standard filter on data.
    
    INTPUTS:
        df: PROMICE data with time index
        site: string of PROMICE site
        var_list: list of the variables for which data removal should be 
            conducted (default: all)
        plot: whether data removal should be plotted
    
    OUTPUTS:
        promice_data: Dataframe containing PROMICE data for the desired settings [DataFrame]
    '''    
    df_out = df.copy()
    
    # Limits filter:
    df_lim = pd.read_csv('metadata/limits.csv', sep='\s*,\s*',engine='python')
    df_lim.columns = ['site','var_lim','var_min','var_max']
    for site_lim, var, var_min, var_max in zip(df_lim.site, df_lim.var_lim, df_lim.var_min,df_lim.var_max):
        
        if site_lim == '*' or site_lim == site:
            if var in df_out.columns.values:
                ind = np.logical_or(df_out[var]>var_max,
                                    df_out[var]<var_min)
                if var+'_qc' in df_out.columns:
                    df_out.loc[ind,var+'_qc'] = "OOL"
                else:
                    df_out[var+'_qc'] = "OK"
                    df_out.loc[ind,var+'_qc'] = "OOL"
                
    # Filter #1: Frozen anemometer
    def filter_low_ws(df_out, var,thresh = 1, length_frozen = 48):
        ind = df_out[var].values<thresh

        if np.any(ind):
            no_wind_count = 0
            for i, val in enumerate(ind):
                if val:
                    no_wind_count = no_wind_count +1
                else:
                    if no_wind_count>0:
                        if no_wind_count<=length_frozen:
                            # gap less than 6 hours putting down the flag
                            ind[np.arange(i-no_wind_count,i+1)] = False
                            no_wind_count = 0
                        else: 
                            # too long period without wind, leaving flags up
                            no_wind_count = 0
        
            if var+'_qc' in df_out.columns:
                df_out.loc[ind,var+'_qc'] = "FROZEN_WS"
            else:
                df_out[var+'_qc'] = "OK"
                df_out.loc[ind,var+'_qc'] = "FROZEN_WS"
        return df_out
    for var in ['VW1','VW2']:
        if var in df_out.columns:
            df_out = filter_low_ws(df_out, var)

    # Filter #2: Frozen values
    def filter_zero_gradient(df_out, var,thresh = 0.000001, length_frozen = 6, not_in_dark_season = False):
        ind = np.abs(df_out[var].diff().values)<thresh
        
        if not_in_dark_season:
            dark_month = df_out['ISWR'].groupby(df_out.index.month).mean()<5
            ind_winter = np.isin(df_out.index.month, dark_month[dark_month].index)
            ind[ind_winter] = False

            
        if np.any(ind):
            no_wind_count = 0
            for i, val in enumerate(ind):
                if val:
                    no_wind_count = no_wind_count +1
                else:
                    if no_wind_count>0:
                        if no_wind_count<=length_frozen:
                            # gap less than 6 hours putting down the flag
                            ind[np.arange(i-no_wind_count,i+1)] = False
                            no_wind_count = 0
                        else: 
                            # too long period without wind, leaving flags up
                            no_wind_count = 0
        
            if var+'_qc' in df_out.columns:
                df_out.loc[ind,var+'_qc'] = "FROZEN"
            else:
                df_out[var+'_qc'] = "OK"
                df_out.loc[ind,var+'_qc'] = "FROZEN"
        return df_out
    for var in ['VW1','VW2','TA1','TA1','TA2','TA3','TA4','P','RH1','RH2']:
        if var in df_out.columns:
            df_out = filter_zero_gradient(df_out, var)
    for var in ['ISWR','OSWR']:
        if var in df_out.columns:
            df_out = filter_zero_gradient(df_out, var,
                                          thresh = 1,
                                          length_frozen=24,
                                          not_in_dark_season=True)
    # Filter #3: Thermocouples limited to -40oC
    for var in ['TA3','TA4']:
        if var in df_out.columns:
            df_out.loc[df[var]<-39.5,var+'_qc'] = "OOL"
    return df_out



def time_shifts(df, site):
    if site == 'Crawford Point 1':
        # df_org = df.copy()
        df_shifted = df['1990-01-01 16:00:00' :'1990-09-26 14:00:00'].copy()
        df_shifted.reset_index(inplace=True)

        df = df.drop(df['1990-01-01 16:00:00' :'1990-09-26 14:00:00'].index,axis=0)
        first_good_time = df.notna().any(axis=1).idxmax()
        df = df.drop(df[:first_good_time].index,axis=0)
        
        # starts again 2011-05-02 15:00:00
        df_shifted['timestamp'] = df_shifted.timestamp.values + pd.Timedelta(str(20*362+283)+" days")
        df_shifted.set_index('timestamp',inplace=True)
        
        # replacing only if no data already existing in the target period
        ind_replace = np.isnan(df[df_shifted.index[0]:df_shifted.index[-1]])
        time_replace = ind_replace[ind_replace].index
        df.loc[time_replace,:] = df_shifted.values
        
        # plt.figure()
        # df.HS2.plot(label='shifted')
        # df_org.HS2.plot(label='original')
    return df



def smooth(x,window_len=14,window='hanning'):
    """smooth the data using a window with requested size.
    
    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal 
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.
    
    input:
        x: the input signal 
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal
        
    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)
    
    see also: 
    
    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter
 
    TODO: the window parameter could be the window itself if an array instead of a string
    NOTE: length(output) != length(input), to correct this: return y[(window_len/2-1):-(window_len/2)] instead of just y.
    """

    if x.ndim != 1:
        raise ValueError("smooth only accepts 1 dimension arrays.")

    if x.size < window_len:
        raise ValueError("Input vector needs to be bigger than window size.")

    if window_len<3:
        return x

    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError("Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")


    s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
    #print(len(s))
    if window == 'flat': #moving average
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')

    return y[int(window_len/2-1):-int(window_len/2)]


def hampel(vals_orig, k=7*24, t0=3):
    '''
    vals: pandas series of values from which to remove outliers
    k: size of window (including the sample; 7 is equal to 3 on either side of value)
    '''
    #Make copy so original not edited
    vals=vals_orig.copy()    
    #Hampel Filter
    L= 1.4826
    rolling_median=vals.rolling(k).median()
    difference=np.abs(rolling_median-vals)
    median_abs_deviation=difference.rolling(k).median()
    threshold= t0 *L * median_abs_deviation
    outlier_idx=difference>threshold
    outlier_idx[0:round(k/2)]=False
    vals.loc[outlier_idx]=np.nan
    return(vals)

def firstNonNan(listfloats):
  if not np.any(~np.isnan(listfloats)):
      return np.nan
  for item in listfloats:
    if math.isnan(item) == False:
      return item



def combine_hs_dpt(df, site):
    # smoothing and filtering pressure transducer data
    df["DepthPressureTransducer_Cor_adj(m)"] = hampel(df["DepthPressureTransducer_Cor(m)"].interpolate(limit=72)).values
    df["SnowHeight_adj(m)"] = hampel(df["SnowHeight(m)"].interpolate(limit=72)).values
    df["SurfaceHeight_adj(m)"] = hampel(df["SurfaceHeight(m)"].interpolate(limit=72)).values
    
    
    # defining ice ablation period   
    smoothed_PT =  df['DepthPressureTransducer_Cor(m)'].interpolate(limit=72).rolling('7D', min_periods=1).mean().shift(-84, freq='h')
    smoothed_PT = smoothed_PT.rolling('7D', min_periods=1).mean().shift(-84, freq='h')
    ind_ablation = np.logical_and(smoothed_PT.diff().values <-0.00035, 
                                  np.isin(smoothed_PT.diff().index.month, [6, 7, 8, 9]))
    ind_ablation = np.concatenate((ind_ablation[2*84:], ind_ablation[:2*84]))# no idea why the array is still shifted
    ind_accumulation =  ~ind_ablation
       
    #adjusting Snow and Surface heights to the PT-derived height
    hs1=df["SnowHeight_adj(m)"].interpolate(limit=24*14).copy()
    hs2=df["SurfaceHeight_adj(m)"].interpolate(limit=24*14).copy()
    z=df["DepthPressureTransducer_Cor_adj(m)"].copy()

    from sklearn.linear_model import LinearRegression
    
    if np.any(~np.isnan(z)):
        Y = z.iloc[:].values.reshape(-1, 1)
        X = z.iloc[~np.isnan(Y)].index.astype(np.int64).values.reshape(-1, 1) 
        Y = Y[~np.isnan(Y)] 
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(X, Y)  # perform linear regression
        Y_pred = linear_regressor.predict(z.index.astype(np.int64).values.reshape(-1, 1) )
        plt.figure()
        plt.scatter(X, Y)
        plt.plot(z.index.astype(np.int64).values, Y_pred, color='red')
        plt.title('Removing intercept at '+site)
        plt.show()
        z = z-Y_pred[0]

    years = df.index.year.values
    ind_start = years.astype(int)
    ind_end =  years.astype(int)
    for i, y in enumerate(np.unique(years)):
    #for each year
        ind_yr = years==y
        ind_abl_yr = np.logical_and(ind_yr, ind_ablation)
        if np.any(ind_abl_yr):
            # if there are some ablation flagged for that year
            # then find begining and end
            ind_start[i] = np.argwhere(ind_abl_yr)[0][0]
            ind_end[i] = np.argwhere(ind_abl_yr)[-1]
            # hs1.iloc[ind_start[i]:ind_end[i]] = np.nan
           # during the ablation we can delete the data from SR1 unless there is no other sensor
        elif np.any(np.isin(df.index[ind_yr].month.values, [6, 7, 8])):
            # if there is any data from june-august that year
            # then use first and last day of JJA as ablation season
            ind_abl_yr = np.logical_and(ind_yr, np.isin(df.index.month.values, [6, 7, 8]))
            ind_start[i] = np.argwhere(ind_abl_yr)[0][0]
            ind_end[i] = np.argwhere(ind_abl_yr)[-1]
            ind_ablation[ind_start[i]:ind_end[i]] = True
            ind_accumulation[ind_start[i]:ind_end[i]] = False
        else:
            # otherwise left as nan
            ind_start[i] = -999
            ind_end[i] = -999
            continue
        
    plt.figure()
    # plt.plot(df.index, ind_ablation*(-10))
    ((smoothed_PT-smoothed_PT.mean())/1000).plot()
    ((z-z.mean())/1000).plot()
    
    smoothed_PT.diff().plot()
    plt.axhline(-0.00035)
    for i, y in enumerate(np.unique(years)):
        plt.axvspan(df.index[ind_start[i]],df.index[ind_end[i]], color='orange', alpha=0.1)
    
    plt.figure()
    df['SnowHeight(m)'].plot(color='darkgray',label='')
    df['SnowHeight_adj(m)'].plot(label='SnowHeight(m)')
    df['SurfaceHeight(m)'].plot(color='darkgray',label='')
    df['SurfaceHeight_adj(m)'].plot(label='SurfaceHeight(m)')
    df['DepthPressureTransducer_Cor(m)'].plot(color='darkgray',label='')
    df['DepthPressureTransducer_Cor_adj(m)'].plot(label='DepthPressureTransducer_Cor(m)')
    
    plt.legend()  
    plt.title(site)
    for i, y in enumerate(np.unique(years)):
        plt.axvspan(df.index[ind_start[i]],df.index[ind_end[i]], color='orange', alpha=0.1)
    

        # if np.any(~np.isnan(hs1.iloc[ind_start[i]:ind_end[i]])) or np.any(~np.isnan(z.iloc[ind_start[i]:ind_end[i]])):
            #  hs1.iloc[ind_start[i]:ind_end[i]] = np.nan
    # hs2 = hs2 - firstNonNan(hs2.values)
    
    plt.figure()
    z.plot()  
    hs1.plot()  
    hs2.plot()  
    plt.title(site)
    
    # adjusting hs1 at the end of each ablation period
    flag = 0
    for i, y in enumerate(np.unique(years)):
        # import pdb; pdb.set_trace()
        # and adjust the end of ablation SR1 height to the PT-derived height         
        if np.any(~np.isnan(z.iloc[(ind_end[i]-24*7):(ind_end[i]+24*7)])) :
            
            #if it is not the first year and that no adjustment has been done
            if (i > 0 or z.first_valid_index().month>=8) and flag == 0:
                # then we adjust the pressur transducer to SR2
                ind_first_nonan = z.index.get_loc(z.iloc[ind_start[i]:].first_valid_index())
                z = z - np.nanmean(z.iloc[ind_first_nonan:(ind_first_nonan+24*7)])  + \
                    np.nanmean(hs2.iloc[ind_first_nonan:(ind_first_nonan+24*7)])
                z.plot()  
                flag = 1
                
            if i == 0:
                flag = 1
                
            if ~np.isnan(np.nanmean(hs1.iloc[(ind_end[i]-24*7):(ind_end[i]+24*7)])): 
                # if hs1.first_valid_index().month>=8
                hs1.iloc[ind_end[i]:] = hs1.iloc[ind_end[i]:] - \
                    np.nanmean(hs1.iloc[(ind_end[i]-24*7):(ind_end[i]+24*7)])  + \
                        np.nanmean(z.iloc[(ind_end[i]-24*7):(ind_end[i]+24*7)])
            else:
                tmp1 = hs1.iloc[ind_end[i]:ind_start[i+1]].values
                tmp2 = hs2.iloc[ind_end[i]:ind_start[i+1]].values
                ind = ~np.isnan(tmp1+tmp2)
                
                hs1.iloc[ind_end[i]:] = hs1.iloc[ind_end[i]:] - \
                    np.nanmean(tmp1[ind])  +  np.nanmean(tmp2[ind])
                    
        # and adjust the end of ablation SR1 height to the SR2 height         
        elif np.any(~np.isnan(hs2.iloc[ind_end[i]:(ind_end[i]+24*7)])) :
            
            #if it is not the first year and that no adjustment has been done
            if i > 0 and flag == 0:
                # then we adjust the pressur SR2 to transducer
                ind_first_nonan = hs2.index.get_loc(hs2.iloc[ind_start[i]:].first_valid_index())
                if np.any(~np.isnan(z.iloc[ind_first_nonan:(ind_first_nonan+24*7)])):
                    hs2 = hs2 - np.nanmean(hs2.iloc[ind_first_nonan:(ind_first_nonan+24*7)])  + \
                        np.nanmean(z.iloc[ind_first_nonan:(ind_first_nonan+24*7)])
                else:
                    hs2 = hs2 - np.nanmean(hs2.iloc[ind_first_nonan:(ind_first_nonan+24*7)])  + \
                        np.nanmean(hs1.iloc[ind_first_nonan:(ind_first_nonan+24*7)])    
                flag = 1
            if i == 0:
                flag = 1
            hs1.iloc[ind_end[i]:] = hs1.iloc[ind_end[i]:] - \
                np.nanmean(hs1.iloc[ind_end[i]:(ind_end[i]+24*7)])  + \
                    np.nanmean(hs2.iloc[ind_end[i]:(ind_end[i]+24*7)])  
        
        if np.any(~np.isnan(z.iloc[(ind_end[i]-24*7):(ind_end[i]+24*7)])) :
            hs2.iloc[ind_start[i]:] = hs2.iloc[ind_start[i]:] - \
                np.nanmean(hs2.iloc[(ind_end[i]-24*7):(ind_end[i]+24*7)])  + \
                    np.nanmean(z.iloc[(ind_end[i]-24*7):(ind_end[i]+24*7)])
                   
        hs1.plot()
        hs2.plot()
        plt.axvline(hs1.index[ind_end[i]])
        
    df["SurfaceHeight1_adj(m)"] = hs1.interpolate(limit=7*24).values
    df["SurfaceHeight2_adj(m)"] = hs2.interpolate(limit=7*24).values
    df["DepthPressureTransducer_Cor_adj(m)"] = z.interpolate(limit=7*24).values

    # making a summary of the surface height
    df["SurfaceHeight_summary(m)"] = np.nan
   
    # in winter, both SR1 and SR2 are used
    df["SurfaceHeight_summary(m)"] = np.nanmean( df[["SurfaceHeight1_adj(m)","SurfaceHeight2_adj(m)"]].values, 
                                                axis = 1)
    
    # in ablation season we use SR2 instead of the SR1&2 average
    data_update = df["SurfaceHeight2_adj(m)"].interpolate(limit=72).values 
    ind_update = np.logical_and(ind_ablation,  ~np.isnan(data_update))
    df.loc[ind_update,"SurfaceHeight_summary(m)"] = data_update[ind_update]  

    # in ablation season we use pressure transducer over all other options
    data_update = df[ "DepthPressureTransducer_Cor_adj(m)"].interpolate(limit=72).values 
    ind_update = np.logical_and(ind_ablation, ~np.isnan(data_update))
    df.loc[ind_update,"SurfaceHeight_summary(m)"] = data_update[ind_update] 
    
    # plotting result
    f1 = plt.figure(figsize=(10, 8))    
    df["DepthPressureTransducer_Cor_adj(m)"].plot(label = 'Pressure transducer')
    df["SurfaceHeight1_adj(m)"].plot(label = 'SonicRanger1')
    df["SurfaceHeight2_adj(m)"].plot(label = 'SonicRanger2')
    df["SurfaceHeight_summary(m)"].plot(label = 'Summary',
             linestyle='--', linewidth=2, color = 'tab:red')
               
    plt.legend(prop={'size': 15})
    plt.xlabel('Year',size=20)
    plt.ylabel('Height (m)',size=20)
    plt.title(site,size=20)
    plt.grid()
    for i, y in enumerate(np.unique(years)):
        plt.axvspan(df.index[ind_start[i]],df.index[ind_end[i]], color='orange', alpha=0.1)
    f1.savefig('figures/L1_data_treatment/'+site+'_surface_height.png',dpi=90, bbox_inches='tight')
    print(' ')
    print('![Surface height adjustement at '+ site+'](figures/L1_data_treatment/'+site+'_surface_height.png)')
    print(' ')
            
    return df
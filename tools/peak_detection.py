# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import numpy as np
import statsmodels.api as sm
lowess = sm.nonparametric.lowess
np.random.seed(0)
x = np.random.uniform(low = -2*np.pi, high = 2*np.pi, size=500)
y = np.sin(x) + np.random.normal(size=len(x))
z = lowess(y, x)
w = lowess(y, x, frac=1./3, it)
plt.figure()
plt.scatter(x,y)
plt.plot(z[:,0],z[:,1],'r')
plt.plot(w[:,0],w[:,1],'g')

    #%%
    df_v4_bis.HS2.plot(label='HS2 auto')
    df_v5.HS1.plot(label='HS1 manual')
    df_v5.HS2.plot(label='HS2 manual')
    plt.legend()
    fig.savefig('figures/L1_data_treatment/'+site+'_HS_processing.jpeg')
    
    
    import numpy as np
    import statsmodels.api as sm
    
    def length_gaps(df, c = 'HS1'):
        s = df.index.to_series()
        #test missing values
        miss = df[c].isna()
        #create consecutive groups
        g = miss.ne(miss.shift()).cumsum()
        #aggregate minimal 
        m1 = s.groupby(g).min()
        #get minimal of next groups, last valueis replaced last value of index
        m2 = m1.shift(-1).fillna(df.index[-1])
        #get difference, convert to minutes
        out = m2.sub(m1).dt.total_seconds().div(60*60).astype(int)
        return g.map(out)
    
    
    length_series = length_gaps(df_v4, c='HS1')
    ind_too_short_data = (df_v4.HS1.notnull()) & (length_series<6)
    
    # removing data that are less 6 hours surrounded by NaNs
    df_v4.loc[ind_too_short_data, 'HS1'] = np.nan

    lowess = sm.nonparametric.lowess
    frac = 3/(df_v4.index[-1]-df_v4.index[0]).days
    z = lowess(df_v4.HS1.values, pd.to_numeric(df_v4.HS1.index.values),frac=frac,it=15)
    df_HS_smoothed = pd.DataFrame(z[:,1], index=pd.to_datetime(z[:,0]), columns=['HS'])
    
    ind_long_gap = (df_v4.HS1.isnull()) & (length_series>7*24)
    
    from scipy.signal import find_peaks

    fig, ax = plt.subplots(1,1,figsize=(15,15))
    df_v4.HS1.plot(ax=ax, label='HS1')
    for i in range(4):
        peaks = find_peaks(df_v4.HS1, threshold =0.01)
        peaks_left = find_peaks(df_v4.HS1.bfill(), threshold =0.01)
        peaks_right = find_peaks(df_v4.HS1.ffill(), threshold =0.01)

        if len(peaks[0])>0:
            df_v4.HS1.iloc[peaks[0]].plot(marker='x',linestyle='None', ax=ax, label='HS1')
            df_v4.iloc[peaks[0],df_v4.columns.get_loc('HS1')] = np.nan
        if len(peaks_left[0])>0:
            df_v4.HS1.iloc[peaks_left[0]].plot(marker='x',linestyle='None', ax=ax, label='HS1')
            df_v4.iloc[peaks_left[0],df_v4.columns.get_loc('HS1')] = np.nan
        if len(peaks_right[0])>0:
            df_v4.HS1.iloc[peaks_right[0]].plot(marker='x',linestyle='None', ax=ax, label='HS1')
            df_v4.iloc[peaks_right[0],df_v4.columns.get_loc('HS1')] = np.nan
    df_v4.HS1.plot(ax=ax, label='HS1',c='g', marker='o')
    # df_HS_smoothed.plot(ax=ax, c='r')
    # (ind_long_gap+0).plot(ax=ax)
    
    #%%
    df_v4_bis = ptb.surface_height_processor(df_v4.copy())
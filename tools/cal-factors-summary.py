# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import pandas as pd
import numpy as np
from nead import read
import os

list_dir = os.listdir(".")

for file in list_dir[1:-3]:
    df_cal = read(file)
    # TCAir, CS500 ,WindSpeed
    try:
        print(
            [file[3:-4]]
            + [
                df_cal[var].scale_factor
                for var in ["TA1", "TA3", "VW1", "ISWR", "OSWR", "NSWR"]
            ]
            + [df_cal["NSWR"].scale_factor_neg]
            + [df_cal["P"].add_value]
            + [df_cal["NSWR"].add_value]
        )
    except:
        pass

# df_all.to_csv('saved_calibration_factors.csv')

# -*- coding: utf-8 -*-
"""
Functions adapted from JAWS:
    https://github.com/jaws/jaws/blob/master/jaws/gcnet2nc.py
    
"""
import numpy as np
import pandas as pd
import xarray as xr
import sys

try:
    from metpy.units import units
    from metpy.calc import potential_temperature, density
    from metpy.calc import mixing_ratio_from_relative_humidity, specific_humidity_from_mixing_ratio
except ImportError:
    print('ImportError: No module named metpy.units')
    print('HINT: This is a known issue for a dependent package that occurs using pip installation in Python 2.7 \n'
          'To fix it, please perform either of below operations: \n'
          '1. Install jaws using conda as: conda install -c conda-forge jaws \n'
          '2. Upgrade to Python version >= 3.6 \n')
    print('If none of the above works for you, '
          'please inform the JAWS maintainers by opening an issue at https://github.com/jaws/jaws/issues.')

    sys.exit(1)

try:
    from jaws import common, sunposition, clearsky, tilt_angle, fsds_adjust
except ImportError:
    import common, sunposition, clearsky, tilt_angle, fsds_adjust


def extrapolate_temp(dataframe, target_height = 2):
    ht1 = dataframe['HW1']
    ht2 = dataframe['HW2']
    temp_ht1 = dataframe['TA1']
    temp_ht2 = dataframe['TA2']
    surface_temp = temp_ht1 - (((temp_ht2 - temp_ht1)/(ht2 - ht1))*(target_height - ht1))
    return surface_temp


def gradient_fluxes(df):  # This method is very sensitive to input data quality
    """Returns Sensible Heat Flux and Latent Heat Flux based on Steffen & DeMaria (1996) method"""
    g = 9.81  # m/s**2
    cp = 1005  # J/kg/K
    k = 0.4  # von Karman
    Lv = 2.50e6  # J/kg

    fillvalue = common.fillvalue_float

    ht_low, ht_high, ta_low, ta_high, wspd_low, wspd_high, rh_low, rh_high, phi_m, phi_h = ([] for _ in range(10))

    # Average temp from both sensors for height1 and height2
    ta1 = df.loc[:, ("ta_tc1", "ta_cs1")]
    ta2 = df.loc[:, ("ta_tc2", "ta_cs2")]
    df['ta1'] = ta1.mean(axis=1)
    df['ta2'] = ta2.mean(axis=1)

    # Assign low and high depending on height of sensors
    idx = 0
    while idx < len(df):
        if df['wind_sensor_height_1'][idx] == fillvalue or df['wind_sensor_height_2'][idx] == fillvalue:
            ht_low.append(np.nan)
            ht_high.append(np.nan)
            ta_low.append(df['ta1'][idx])
            ta_high.append(df['ta2'][idx])
            wspd_low.append(df['wspd1'][idx])
            wspd_high.append(df['wspd2'][idx])
            rh_low.append(df['rh1'][idx])
            rh_high.append(df['rh2'][idx])
        elif df['wind_sensor_height_1'][idx] > df['wind_sensor_height_2'][idx]:
            ht_low.append(df['wind_sensor_height_2'][idx])
            ht_high.append(df['wind_sensor_height_1'][idx])
            ta_low.append(df['ta2'][idx])
            ta_high.append(df['ta1'][idx])
            wspd_low.append(df['wspd2'][idx])
            wspd_high.append(df['wspd1'][idx])
            rh_low.append(df['rh2'][idx])
            rh_high.append(df['rh1'][idx])
        else:
            ht_low.append(df['wind_sensor_height_1'][idx])
            ht_high.append(df['wind_sensor_height_2'][idx])
            ta_low.append(df['ta1'][idx])
            ta_high.append(df['ta2'][idx])
            wspd_low.append(df['wspd1'][idx])
            wspd_high.append(df['wspd2'][idx])
            rh_low.append(df['rh1'][idx])
            rh_high.append(df['rh2'][idx])

        idx += 1

    # Convert lists to arrays
    ht_low = np.asarray(ht_low)
    ht_high = np.asarray(ht_high)
    ta_low = np.asarray(ta_low)
    ta_high = np.asarray(ta_high)
    wspd_low = np.asarray(wspd_low)
    wspd_high = np.asarray(wspd_high)
    rh_low = np.asarray(rh_low)
    rh_high = np.asarray(rh_high)
    ps = np.asarray(df['ps'].values)

    # Potential Temperature
    pot_tmp_low = potential_temperature(ps * units.pascal, ta_low * units.kelvin).magnitude
    pot_tmp_high = potential_temperature(ps * units.pascal, ta_high * units.kelvin).magnitude
    pot_tmp_avg = (pot_tmp_low + pot_tmp_high)/2
    ta_avg = (ta_low + ta_high)/2

    # Ri
    du = wspd_high-wspd_low
    du = np.asarray([fillvalue if i == 0 else i for i in du])
    pot_tmp_avg = np.asarray([fillvalue if i == 0 else i for i in pot_tmp_avg])
    ri = g*(pot_tmp_high - pot_tmp_low)*(ht_high - ht_low)/(pot_tmp_avg*du)

    # Phi
    for val in ri:
        if val < -0.03:
            phi = (1-18*val)**-0.25
            phi_m.append(phi)
            phi_h.append(phi/1.3)
        elif -0.03 <= val < 0:
            phi = (1-18*val)**-0.25
            phi_m.append(phi)
            phi_h.append(phi)
        else:
            phi = (1-5.2*val)**-1
            phi_m.append(phi)
            phi_h.append(phi)

    phi_e = phi_h

    # air density
    rho = density(ps * units.pascal, ta_avg * units.kelvin, 0).magnitude  # Use average temperature

    # SH
    ht_low = np.asarray([fillvalue if i == 0 else i for i in ht_low])
    num = np.asarray([-a1 * cp * k**2 * (b1 - c1) * (d1 - e1) for a1, b1, c1, d1, e1 in
           zip(rho, pot_tmp_high, pot_tmp_low, wspd_high, wspd_low)])
    dnm = [a2 * b2 * np.log(c2 / d2)**2 for a2, b2, c2, d2 in
           zip(phi_h, phi_m, ht_high, ht_low)]
    dnm = np.asarray([fillvalue if i == 0 else i for i in dnm])
    sh = num/dnm
    sh = [fillvalue if abs(i) >= 100 else i for i in sh]

    # Specific Humidity
    mixing_ratio_low = mixing_ratio_from_relative_humidity(rh_low, ta_low * units.kelvin, ps * units.pascal)
    mixing_ratio_high = mixing_ratio_from_relative_humidity(rh_high, ta_high * units.kelvin, ps * units.pascal)
    q_low = specific_humidity_from_mixing_ratio(mixing_ratio_low).magnitude
    q_high = specific_humidity_from_mixing_ratio(mixing_ratio_high).magnitude
    q_low = q_low/100  # Divide by 100 to make it in range [0,1]
    q_high = q_high/100

    # LH
    num = np.asarray([-a1 * Lv * k**2 * (b1 - c1) * (d1 - e1) for a1, b1, c1, d1, e1 in
           zip(rho, q_high, q_low, wspd_high, wspd_low)])
    dnm = [a2 * b2 * np.log(c2 / d2)**2 for a2, b2, c2, d2 in
           zip(phi_e, phi_m, ht_high, ht_low)]
    dnm = np.asarray([fillvalue if i == 0 else i for i in dnm])
    lh = num/dnm
    lh = [fillvalue if abs(i) >= 100 else i for i in lh]

    return sh, lh
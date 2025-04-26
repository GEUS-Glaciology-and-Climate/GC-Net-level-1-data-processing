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
    from metpy.calc import (
        mixing_ratio_from_relative_humidity,
        specific_humidity_from_mixing_ratio,
    )
except ImportError:
    print("ImportError: No module named metpy.units")
    print(
        "HINT: This is a known issue for a dependent package that occurs using pip installation in Python 2.7 \n"
        "To fix it, please perform either of below operations: \n"
        "1. Install jaws using conda as: conda install -c conda-forge jaws \n"
        "2. Upgrade to Python version >= 3.6 \n"
    )
    print(
        "If none of the above works for you, "
        "please inform the JAWS maintainers by opening an issue at https://github.com/jaws/jaws/issues."
    )

    sys.exit(1)

try:
    from jaws import common, sunposition, clearsky, tilt_angle, fsds_adjust
except ImportError:
    import common, sunposition, clearsky, tilt_angle, fsds_adjust





def gradient_fluxes(df):  # This method is very sensitive to input data quality
    """Returns Sensible Heat Flux and Latent Heat Flux based on Steffen & DeMaria (1996) method"""
    g = 9.81  # m/s**2
    cp = 1005  # J/kg/K
    k = 0.4  # von Karman
    Lv = 2.50e6  # J/kg

    # Average temp from both sensors for height1 and height2
    ta1 = df.loc[:, ("TA1", "TA3")]
    ta2 = df.loc[:, ("TA2", "TA4")]
    ta1 = ta1.mean(axis=1)
    ta2 = ta2.mean(axis=1)

    ht_low = df["HW1"].values
    ht_high = df["HW2"].values
    ta_low = ta1.values
    ta_high = ta2.values
    VW_low = df["VW1"].values
    VW_high = df["VW2"].values
    RH_low = df["RH1"].values
    RH_high = df["RH2"].values
    P = df["P"].values

    ind = ht_high < ht_low
    ht_low[ind] = df["HW2"].values[ind]
    ht_high[ind] = df["HW1"].values[ind]
    ta_low[ind] = ta2.values[ind]
    ta_high[ind] = ta1.values[ind]
    VW_low[ind] = df["VW2"].values[ind]
    VW_high[ind] = df["VW1"].values[ind]
    RH_low[ind] = df["RH2"].values[ind]
    RH_high[ind] = df["RH1"].values[ind]

    # Potential Temperature
    pot_tmp_low = potential_temperature(
        units.Quantity(P, "hPa"), units.Quantity(ta_low, "degC")
    ).magnitude
    pot_tmp_high = potential_temperature(
        units.Quantity(P, "hPa"), units.Quantity(ta_high, "degC")
    ).magnitude
    pot_tmp_avg = (pot_tmp_low + pot_tmp_high) / 2
    ta_avg = (ta_low + ta_high) / 2

    # Ri
    du = VW_high - VW_low
    du[du == 0] = np.nan
    pot_tmp_avg[pot_tmp_avg == 0] = np.nan
    ri = g * (pot_tmp_high - pot_tmp_low) * (ht_high - ht_low) / (pot_tmp_avg * du)

    # Phi
    phi_m = (1 - 5.2 * ri) ** -1
    phi_h = phi_m
    phi_m[ri < -0.03] = (1 - 18 * ri[ri < -0.03]) ** -0.25
    phi_h[ri < -0.03] = phi_m[ri < -0.03] / 1.3
    phi_m[(-0.03 <= ri) & (ri < 0)] = (1 - 18 * ri[(-0.03 <= ri) & (ri < 0)]) ** -0.25
    phi_h[(-0.03 <= ri) & (ri < 0)] = phi_m[(-0.03 <= ri) & (ri < 0)]
    phi_e = phi_h

    # air density
    RHo = density(
        P * units.hectopascal, ta_avg * units.degC, 0
    ).magnitude  # Use average temperature

    # SH
    ht_low[ht_low == 0] = np.nan
    num = -RHo * cp * k ** 2 * (pot_tmp_high - pot_tmp_low) * (VW_high - VW_low)

    dnm = phi_h * phi_m * np.log(ht_high / ht_low) ** 2
    dnm[dnm == 0] = np.nan
    sh = num / dnm
    sh[np.abs(sh) >= 100] = np.nan

    # Specific Humidity
    mixing_ratio_low = mixing_ratio_from_relative_humidity(
        units.Quantity(P, "hPa"), units.Quantity(ta_low, "degC"), RH_low
    )
    mixing_ratio_high = mixing_ratio_from_relative_humidity(
        units.Quantity(P, "hPa"), units.Quantity(ta_high, "degC"), RH_high
    )
    q_low = specific_humidity_from_mixing_ratio(mixing_ratio_low).magnitude
    q_high = specific_humidity_from_mixing_ratio(mixing_ratio_high).magnitude
    q_low = q_low / 100  # Divide by 100 to make it in range [0,1]
    q_high = q_high / 100

    # LH
    num = -RHo * Lv * k ** 2 * (q_high - q_low) * (VW_high - VW_low)
    dnm = phi_e * phi_m * np.log(ht_high / ht_low) ** 2
    dnm[dnm == 0] = np.nan
    lh = num / dnm
    lh[np.abs(lh) >= 100] = np.nan
    return -sh, -lh

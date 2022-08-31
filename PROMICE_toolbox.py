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

    promice_names = [
        "AirTemperature1C",
        "AirTemperature2C",
        "AirTemperature3C",
        "AirTemperature4C",
        "RelativeHumidity1Perc",
        "RelativeHumidity2Perc",
        "AirPressurehPa",
        "ShortwaveRadiationDownWm2",
        "ShortwaveRadiationUpWm2",
        "WindSpeed1ms",
        "WindSpeed2ms",
        "WindDirection1deg",
        "WindDirection2deg",
        "SnowHeight(m)",
        "SurfaceHeight(m)",
        "SnowHeight1m",
        "SnowHeight2m",
        "NetRadiationWm2",
    ]
    gcnet_names = [
        "TA1",
        "TA2",
        "TA3",
        "TA4",
        "RH1",
        "RH2",
        "P",
        "ISWR",
        "OSWR",
        "VW1",
        "VW2",
        "DW1",
        "DW2" "HS1",
        "HS2",
        "HS1",
        "HS2",
        "NSWR",
    ]

    try:
        index = promice_names.index(name_in)
        return gcnet_names[index]
    except:
        return None


def field_info(fields):
    field_list = "timestamp,ISWR,ISWR_max,ISWR_std,OSWR,OSWR_max,NSWR,NSWR_max,NSWR_std,TA1,TA1_max,TA1_min,TA2,TA2_max,TA2_min,TA3,TA4,RH1,RH2,VW1,VW1_max,VW1_stdev,VW2,VW2_max,VW2_stdev,DW1,DW2,P,HS1,HS2,HW1,HW2,V,TA5,TS1,TS2,TS3,TS4,TS5,TS6,TS7,TS8,TS9,TS10,Tsurf1,Tsurf2,IUVR,ILWR,SHF,LHF,TA2m,RH2m,VW10m,SAA,SZA".split(
        ","
    )

    units = "time,W/m^2,W/m^2,W/m^2,W/m^2,W/m^2,W/m^2,W/m^2,W/m^2,Degrees C,Degrees C,Degrees C,Degrees C,Degrees C,Degrees C,Degrees C,Degrees C,%/100,%/100,m/s,m/s,m/s,m/s,m/s,m/s,Degrees,Degrees,mbar,m,m,m,m,m,m,m,m,m,m,m,m,m,m,V,Degrees C,Degrees C,Degrees C,W/m^2,W/m^2,W/m^2,W/m^2,Degrees C,%/100,m/s,Degrees,Degrees".split(
        ","
    )

    display_description = "timestamp_iso,shortwave_incoming_radiation,shortwave_incoming_radiation_max,shortwave_incoming_radiation_stdev,shortwave_outgoing_radiation,shortwave_outgoing_radiation_max,net_radiation,net_radiation_maximum,net_radiation_stdev,air_temperature_1,air_temperature_1_max,air_temperature_1_min,air_temperature_2,air_temperature_2_max,air_temperature_2_min,air_temperature_cs500_air1,air_temperature_cs500_air2,relative_humidity_1,relative_humidity_2,wind_speed_1,wind_speed_u1_max,wind_speed_u1_stdev,wind_speed_2,wind_speed_u2_max,wind_speed_u2_stdev,wind_from_direction_1,wind_from_direction_2,air_pressure,snow_depth_1,snow_depth_2,height_wind_sensor_1,height_wind_sensor_2,battery_voltage,ref_temperature,snow_temperature_1,snow_temperature_2,snow_temperature_3,snow_temperature_4,snow_temperature_5,snow_temperature_6,snow_temperature_7,snow_temperature_8,snow_temperature_9,snow_temperature_10,surface_temperature_1,surface_temperature_2,incoming_uv_radiation,incoming_longwave_radiation,sensible_heat_flux,latent_heat_flux,air_temperature_2m,relative_humidity_2m,wind_speed_10m,solar_azimuth_angle,solar_zenith_angle".split(
        ","
    )

    database_fields = "timestamp_iso,swin,swin_maximum,swin_stdev,swout,swout_maximum,netrad,netrad_max,netrad_stdev,airtemp1,airtemp1_maximum,airtemp1_minimum,airtemp2,airtemp2_maximum,airtemp2_minimum,airtemp_cs500air1,airtemp_cs500air2,rh1,rh2,windspeed1,windspeed_u1_maximum,windspeed_u1_stdev,windspeed2,windspeed_u2_maximum,windspeed_u2_stdev,winddir1,winddir2,pressure,sh1,sh2,hw1,hw2,battvolt,reftemp,ts1,ts2,ts3,ts4,ts5,ts6,ts7,ts8,ts9,ts10,tsurf1,tsurf2,uvin,lwin,shf,lhf,airtemp_2m,rh_2m,windspeed_10m,solar_azimuth_angle,solar_zenith_angle".split(
        ","
    )

    database_fields_data_types = "timestamp,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real".split(
        ","
    )

    field_list = (
        field_list
        + [s + "_qc" for s in field_list]
        + [s + "_adj_flag" for s in field_list]
    )
    units = units + ["-" for s in units] + ["-" for s in units]
    display_description = (
        display_description
        + [s + "_quality_flag" for s in display_description]
        + [s + "_adj_flag" for s in display_description]
    )
    database_fields = (
        database_fields
        + [s + "_quality_flag" for s in database_fields]
        + [s + "_adj_flag" for s in database_fields]
    )
    database_fields_data_types = (
        database_fields_data_types
        + ["int" for s in database_fields_data_types]
        + ["int" for s in database_fields_data_types]
    )

    ind = [field_list.index(s) for s in fields]

    return (
        [units[i] for i in ind],
        [display_description[i] for i in ind],
        [database_fields[i] for i in ind],
        [database_fields_data_types[i] for i in ind],
    )


def load_promice(path_promice):
    """
    Loading PROMICE data for a given path into a DataFrame.
    + adding time index
    + calculating albedo
    + (optional) calculate RH with regard to water

    INTPUTS:
        path_promice: Path to the desired file containing PROMICE data [string]

    OUTPUTS:
        df: Dataframe containing PROMICE data for the desired settings [DataFrame]
    """

    df = pd.read_csv(path_promice, delim_whitespace=True)
    df["time"] = df.Year * np.nan

    df["time"] = [
        datetime.datetime(y, m, d, h).replace(tzinfo=pytz.UTC)
        for y, m, d, h in zip(
            df["Year"].values,
            df["MonthOfYear"].values,
            df["DayOfMonth"].values,
            df["HourOfDay(UTC)"].values,
        )
    ]
    df.set_index("time", inplace=True, drop=False)

    # set invalid values (-999) to nan
    df[df == -999.0] = np.nan
    df["Albedo"] = df["ShortwaveRadiationUp(W/m2)"] / df["ShortwaveRadiationDown(W/m2)"]
    df.loc[df["Albedo"] > 1, "Albedo"] = np.nan
    df.loc[df["Albedo"] < 0, "Albedo"] = np.nan
    df["SnowHeight(m)"] = 2.6 - df["HeightSensorBoom(m)"]
    df["SurfaceHeight(m)"] = 1 - df["HeightStakes(m)"]

    # df['RelativeHumidity_w'] = RH_ice2water(df['RelativeHumidity(%)'] ,
    #                                                    df['AirTemperature(C)'])

    return df


def Msg(txt):
    f = open("out/Report.md", "a")
    print(txt)
    f.write(txt + "\n")


def flag_data(df, site, var_list=["all"]):
    """
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
    """

    df_out = df.copy()
    if not os.path.isfile("metadata/flags/" + site + ".csv"):
        Msg("No erroneous data listed for " + site)
        return df

    flag_data = pd.read_csv("metadata/flags/" + site + ".csv", comment="#")

    flag_data.t0 = pd.to_datetime(flag_data.t0)
    flag_data.t0 = flag_data.t0.apply(
        lambda x: x.replace(tzinfo=pytz.utc).isoformat()
    ).values
    flag_data.loc[flag_data.t1.isnull(), "t1"] = df_out.index[-1].isoformat()
    flag_data.t1 = pd.to_datetime(flag_data.t1)
    flag_data.t1 = flag_data.t1.apply(
        lambda x: x.replace(tzinfo=pytz.utc).isoformat()
    ).values

    if var_list[0] == "all":
        var_list = np.unique(flag_data.variable)

    Msg("Flagging data:")
    for var in var_list:
        if var not in df_out.columns:
            Msg("Warning: " + var + " not found")
            continue

        if var + "_qc" not in df_out.columns:
            df_out[var + "_qc"] = "OK"

        # df_out.loc[np.logical_and(np.isnan(df_out[var]), df_out[var+'_qc'] == 'OK'), var+'_qc'] = 'NAN'

        Msg("|start time|end time|variable|")
        Msg("|-|-|-|")
        for t0, t1, flag in zip(
            pd.to_datetime(flag_data.loc[flag_data.variable == var].t0),
            pd.to_datetime(flag_data.loc[flag_data.variable == var].t1),
            flag_data.loc[flag_data.variable == var].flag,
        ):
            Msg("|" + str(t0) + "|" + str(t1) + "|" + var + "|")

            df_out.loc[t0:t1, var + "_qc"] = flag

        Msg(" ")
        Msg(
            "![Erroneous data at "
            + site
            + "](../figures/L1_data_treatment/"
            + site.replace(" ", "_")
            + "_"
            + var
            + "_data_flagging.png)"
        )
        Msg(" ")

    return df_out


def plot_flagged_data(df, site, tag=""):
    """
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
    """

    for var in df.columns:
        if var[-3:] == "_qc":
            df[var].values[df[var].isnull()] = "OK"
            flags_uni = np.unique(df[var].values.astype(str))
            if len(flags_uni) > 1:
                fig = plt.figure(figsize=(12, 8))
                for flag in flags_uni:
                    if flag == "OK":
                        df.loc[df[var] == flag, var[:-3]].plot(
                            marker="o", linestyle="none", color="green", label=flag
                        )
                    elif flag == "CHECKME":
                        df.loc[df[var] == flag, var[:-3]].plot(
                            marker="o", linestyle="none", color="orange", label=flag
                        )
                    elif flag == "OOL":
                        df.loc[df[var] == flag, var[:-3]].plot(
                            marker="o", linestyle="none", color="red", label=flag
                        )
                    elif flag == "FROZEN":
                        df.loc[df[var] == flag, var[:-3]].plot(
                            marker="o", linestyle="none", color="blue", label=flag
                        )
                    elif flag == "FROZEN_WS":
                        df.loc[df[var] == flag, var[:-3]].plot(
                            marker="o", linestyle="none", color="lightblue", label=flag
                        )
                    else:
                        try:
                            df.loc[df[var] == flag, var[:-3]].plot(
                                marker="o", linestyle="none", label=flag
                            )
                        except:
                            Msg("Could not plot flag: ", flag)
                plt.title(site)
                plt.xlabel("Year")
                plt.ylabel(var[:-3])
                plt.legend()
                plt.title(site)
                fig.savefig(
                    "figures/L1_data_treatment/"
                    + site.replace(" ", "_")
                    + "_"
                    + var[:-3]
                    + "_data_flagging"
                    + tag
                    + ".png",
                    dpi=70,
                )


def remove_flagged_data(df):
    """
    Remove flagged data
    """
    for var in df.columns:
        if var[-3:] == "_qc":
            df[var].values[df[var].isnull()] = "OK"
            if len(np.unique(df[var].values)) > 1:
                msk = (df[var].values == "OK") | (df[var].values == "")
                df.loc[~msk, var[:-3]] = np.nan
            df = df.drop(columns=[var])
    return df


import pytz


def adjust_data(df, site, var_list=[], skip_var=[]):
    df_out = df.copy()
    if not os.path.isfile("metadata/adjustments/" + site + ".csv"):
        Msg("No data to fix at " + site)
        return df_out

    adj_info = pd.read_csv(
        "metadata/adjustments/" + site + ".csv", comment="#", skipinitialspace=True
    )

    adj_info.t0 = pd.to_datetime(adj_info.t0)
    adj_info.t0 = adj_info.t0.apply(
        lambda x: x.replace(tzinfo=pytz.utc).isoformat()
    ).values
    adj_info.loc[adj_info.t1.isnull(), "t1"] = df_out.index[-1].isoformat()
    adj_info.t1 = pd.to_datetime(adj_info.t1)
    adj_info.t1 = adj_info.t1.apply(
        lambda x: x.replace(tzinfo=pytz.utc).isoformat()
    ).values

    # if "*" is given as variable then we append this adjustement for all variables
    for ind in adj_info.loc[adj_info.variable == "*", :].index:
        line_template = adj_info.loc[ind, :].copy()
        for var in df_out.columns:
            line_template.variable = var
            line_template.name = adj_info.index.max() + 1
            adj_info = adj_info.append(line_template)
        adj_info = adj_info.drop(labels=ind, axis=0)

    adj_info = adj_info.sort_values(by=["variable", "t0"])

    adj_info.loc[adj_info.adjust_function == "time_shift", :] = (
        adj_info.loc[adj_info.adjust_function == "time_shift", :]
        .sort_values(by="t0", ascending=False)
        .values
    )

    adj_info.set_index(["variable", "t0"], drop=False, inplace=True)

    if len(var_list) == 0:
        var_list = np.unique(adj_info.variable)
    else:
        adj_info = adj_info.loc[np.isin(adj_info.variable, var_list), :]
        var_list = np.unique(adj_info.variable)

    if len(skip_var) > 0:
        adj_info = adj_info.loc[~np.isin(adj_info.variable, skip_var), :]
        var_list = np.unique(adj_info.variable)

    for var in var_list:
        if (
            ("_qc" not in var)
            & ("_min" not in var)
            & ("_max" not in var)
            & ("_std" not in var)
            & ("_adj_flag" not in var)
            & ("_min" not in var)
        ):
            Msg("### Adjusting " + var)
            Msg("|start time|end time|operation|value|number of removed samples|")
            Msg("|-|-|-|-|-|")

        for t0, t1, func, val in zip(
            adj_info.loc[var].t0,
            adj_info.loc[var].t1,
            adj_info.loc[var].adjust_function,
            adj_info.loc[var].adjust_value,
        ):
            if (pd.to_datetime(t0) > df.index[-1]) | (pd.to_datetime(t1) < df.index[0]):
                continue

            # counting nan values before filtering
            if "_qc" not in var:
                nan_count_1 = np.sum(np.isnan(df_out.loc[t0:t1, var].values))

            if t1 < t0:
                Msg("Dates in wrong order")

            if func == "add":
                df_out.loc[t0:t1, var] = df_out.loc[t0:t1, var].values + val
                # flagging adjusted values
                if var + "_adj_flag" not in df_out.columns:
                    df_out[var + "_adj_flag"] = 0
                msk = df_out.loc[t0:t1, var].notnull()
                ind = df_out.loc[t0:t1, var].loc[msk].index
                df_out.loc[ind, var + "_adj_flag"] = 1

            if func == "multiply":
                df_out.loc[t0:t1, var] = df_out.loc[t0:t1, var].values * val
                if "DW" in var:
                    df_out.loc[t0:t1, var] = df_out.loc[t0:t1, var] % 360
                # flagging adjusted values
                if var + "_adj_flag" not in df_out.columns:
                    df_out[var + "_adj_flag"] = 0
                msk = df_out.loc[t0:t1, var].notnull()
                ind = df_out.loc[t0:t1, var].loc[msk].index
                df_out.loc[ind, var + "_adj_flag"] = 1

            if func == "min_filter":
                tmp = df_out.loc[t0:t1, var].values
                tmp[tmp < val] = np.nan
            if func == "max_filter":
                tmp = df_out.loc[t0:t1, var].values
                tmp[tmp > val] = np.nan
                df_out.loc[t0:t1, var] = tmp
            if func == "upper_perc_filter":
                tmp = df_out.loc[t0:t1, var].copy()
                df_w = df_out.loc[t0:t1, var].resample("14D").quantile(1 - val / 100)
                df_w = df_out.loc[t0:t1, var].resample("14D").var()
                for m_start, m_end in zip(df_w.index[:-2], df_w.index[1:]):
                    msk = (tmp.index >= m_start) & (tmp.index < m_end)
                    values_month = tmp.loc[msk].values
                    values_month[values_month < df_w.loc[m_start]] = np.nan
                    tmp.loc[msk] = values_month

                df_out.loc[t0:t1, var] = tmp.values

            if func == "biweekly_upper_range_filter":
                tmp = df_out.loc[t0:t1, var].copy()
                df_max = df_out.loc[t0:t1, var].resample("14D").max()
                for m_start, m_end in zip(df_max.index[:-2], df_max.index[1:]):
                    msk = (tmp.index >= m_start) & (tmp.index < m_end)
                    lim = df_max.loc[m_start] - val
                    values_month = tmp.loc[msk].values
                    values_month[values_month < lim] = np.nan
                    tmp.loc[msk] = values_month
                # remaining samples following outside of the last 2 weeks window
                msk = tmp.index >= m_end
                lim = df_max.loc[m_start] - val
                values_month = tmp.loc[msk].values
                values_month[values_month < lim] = np.nan
                tmp.loc[msk] = values_month
                # updating original pandas
                df_out.loc[t0:t1, var] = tmp.values

            if func == "hampel_filter":
                tmp = df_out.loc[t0:t1, var]
                tmp = hampel(tmp, k=7 * 24, t0=val)
                df_out.loc[t0:t1, var] = tmp.values

            if func == "grad_filter":
                tmp = df_out.loc[t0:t1, var].copy()
                msk = df_out.loc[t0:t1, var].copy().diff()
                tmp[np.roll(msk.abs() > val, -1)] = np.nan
                df_out.loc[t0:t1, var] = tmp

            if "swap_with_" in func:
                var2 = func[10:]
                val_var = df_out.loc[t0:t1, var].values.copy()
                val_var2 = df_out.loc[t0:t1, var2].values.copy()
                df_out.loc[t0:t1, var2] = val_var
                df_out.loc[t0:t1, var] = val_var2

            if func == "rotate":
                df_out.loc[t0:t1, var] = df_out.loc[t0:t1, var].values + val
                df_out.loc[t0:t1, var][df_out.loc[t0:t1, var] > 360] = (
                    df_out.loc[t0:t1, var] - 360
                )

            if func == "air_temp_sonic_correction":
                # finding the available air temp measurements
                tmp = df_out.loc[t0:t1, "TA" + var[-1]]
                tmp2 = df_out.loc[t0:t1, ["TA" + str(i) for i in range(1, 5)]].mean(
                    axis=1
                )
                tmp.loc[tmp.isnull()] = tmp2.loc[tmp.isnull()]
                tmp = tmp.interpolate(method="nearest", fill_value="extrapolate")

                df_out.loc[t0:t1, var] = df_out.loc[t0:t1, var].values * np.sqrt(
                    (tmp.values + 273.15) / 273.15
                )

            if func == "ice_to_water":
                tmp = df_out.loc[t0:t1, "TA" + var[-1]]
                tmp2 = df_out.loc[t0:t1, "TA" + str(int(var[-1]) % 2 + 1)]
                tmp.loc[tmp.isnull()] = tmp2.loc[tmp.isnull()].values
                tmp = tmp.interpolate(method="nearest", fill_value="extrapolate")
                df_out.loc[t0:t1, var] = RH_ice2water(
                    df_out.loc[t0:t1, var].values, tmp.values
                )

            if func == "water_to_ice":
                tmp = df_out.loc[t0:t1, "TA" + var[-1]]
                tmp2 = df_out.loc[t0:t1, "TA" + str(int(var[-1]) % 2 + 1)]
                tmp.loc[tmp.isnull()] = tmp2.loc[tmp.isnull()].values
                tmp = tmp.interpolate(method="nearest", fill_value="extrapolate")
                df_out.loc[t0:t1, var] = RH_water2ice(
                    df_out.loc[t0:t1, var].values, tmp.values
                )

            if func == "time_shift":
                t0 = pd.to_datetime(t0)
                t1 = pd.to_datetime(t1)

                if t1 + pd.Timedelta(hours=val) > df_out.index[-1]:
                    # case where the files needs to be extended to receive the shifted data
                    nb_new_rows = (
                        t1 + pd.Timedelta(hours=val) - df_out.index[-1]
                    ).total_seconds() / 3600
                    df_new_rows = df_out.iloc[-int(nb_new_rows) :, :].copy()
                    df_new_rows.loc[:, :] = np.NaN
                    df_new_rows.index = df_new_rows.index + (
                        t1 + pd.Timedelta(hours=val) - df_out.index[-1]
                    )
                    df_out = df_out.append(df_new_rows)

                df_out.loc[
                    t0 + pd.Timedelta(hours=val) : t1 + pd.Timedelta(hours=val), var
                ] = df_out.loc[t0:t1, var].values

                if val > 0:
                    if val < 10000:
                        # errasing data that existed during the time shift
                        df_out.loc[t0 : t0 + pd.Timedelta(hours=val), var] = np.nan
                    else:
                        # case of Crawford Point where only the shifted data should be errased
                        df_out.loc[t0:t1, var] = np.nan
                else:
                    df_out.loc[t1 + pd.Timedelta(hours=val) : t1, var] = np.nan

            if (
                ("_qc" not in var)
                & ("_min" not in var)
                & ("_max" not in var)
                & ("_std" not in var)
                & ("_adj_flag" not in var)
                & ("_min" not in var)
            ):
                nan_count_2 = np.sum(np.isnan(df_out.loc[t0:t1, var].values))
                Msg(
                    "|"
                    + str(t0)
                    + "|"
                    + str(t1)
                    + "|"
                    + func
                    + "|"
                    + str(val)
                    + "|"
                    + str(nan_count_2 - nan_count_1)
                    + "|"
                )

        if (
            df[var].notna().any()
            & ("_qc" not in var)
            & ("_min" not in var)
            & ("_max" not in var)
            & ("_std" not in var)
            & ("_adj_flag" not in var)
            & ("_min" not in var)
        ):
            fig = plt.figure(figsize=(12, 8))
            df[var].plot(style="o", label="before adjustment")
            df_out[var].plot(style="o", label="after adjustment")
            [
                plt.axvline(t, linestyle="--", color="red")
                for t in adj_info.loc[var].t0.values
            ]
            plt.axvline(np.nan, linestyle="--", color="red", label="Adjustment times")
            plt.xlabel("Year")
            plt.ylabel(var)
            plt.legend()
            plt.title(site)
            fig.savefig(
                "figures/L1_data_treatment/"
                + site.replace(" ", "_")
                + "_adj_"
                + var
                + ".jpeg",
                dpi=120,
                bbox_inches="tight",
            )
            Msg(" ")
            Msg(
                "![Adjusted data at "
                + site
                + "](../figures/L1_data_treatment/"
                + site.replace(" ", "_")
                + "_adj_"
                + var
                + ".jpeg)"
            )
            Msg(" ")

    return df_out


import jaws_tools
from progressbar import progressbar


def augment_data(df_in, latitude, longitude, elevation, site):
    # Interpolate small gaps in available variables
    # and add variables to the dataset:
    # Surface height HS
    # Sensible and Latent Heat Fluxes SHF & LHF
    # Solar azimuth and zenith angles
    # albedo

    df = df_in.copy()
    # Interpolation over gaps smaller than a week
    mask = df[["HW1", "HW2"]].copy()
    for i in ["HW1", "HW2"]:
        tmp = pd.DataFrame(df[i])
        tmp["new"] = (tmp.notnull() != tmp.shift().notnull()).cumsum()
        tmp["ones"] = 1
        mask[i] = (tmp.groupby("new")["ones"].transform("count") < 24 * 7) | df[
            i
        ].notnull()
    df[["HW1", "HW2"]] = df[["HW1", "HW2"]].interpolate().values
    df.loc[mask.HW1 == False, "HW1"] = np.nan
    df.loc[mask.HW2 == False, "HW2"] = np.nan

    fig = plt.figure()
    df_in.HW1.plot(
        label="HW1 original", marker="o", linestyle="None", color="turquoise"
    )
    df_in.HW2.plot(label="HW2 original", marker="o", linestyle="None", color="magenta")

    def fill_gap_HW(df, var_target="HW1", var_sec="HW2"):
        prev_no_nan = df[var_target].notnull().shift(1).fillna(False)
        is_nan = df[var_target].isnull()
        list_start_gaps = df.index[(prev_no_nan & is_nan)]

        prev_nan = df[var_target].isnull().shift(1).fillna(False)
        no_nan = df[var_target].notnull()
        list_end_gaps = df.index[(prev_nan & no_nan)]

        if len(list_end_gaps) < len(list_start_gaps):
            list_end_gaps = np.append(list_end_gaps, df.index[-1])
        df[var_target].plot(label=var_target + " interpolated")
        for start, end in zip(list_start_gaps, list_end_gaps):
            # we look at the month preceeding the gap
            # calculate the mean difference between the two heights during that time
            mean_diff = (
                df.loc[(start - pd.Timedelta(days=30)) : start, var_target]
                - df.loc[(start - pd.Timedelta(days=30)) : start, var_sec]
            ).mean()

            # and use that difference to adjust the secondary height to the height
            # that is to be gap-filled
            df.loc[start:end, var_target] = (
                df.loc[start:end, var_sec].values + mean_diff
            )
            df.loc[start:end, var_target].plot(
                label="__no_legend__", color="red", linewidth=2
            )
        df.loc[start:end, var_target].plot(
            label=var_target + " gap-filled", color="red", linewidth=2
        )
        return df[var_target].values

    try:
        df["HW1"] = fill_gap_HW(df, "HW1", "HW2")
        df["HW2"] = fill_gap_HW(df, "HW2", "HW1")
    except:
        pass

    plt.ylabel("Intrument height (m)")
    plt.title("Gap filling instrument height using the other level")
    plt.legend()
    fig.savefig("figures/L1_data_treatment/" + site + "_gap_filling_HW.png")

    # Creating surface height field
    if "HW1_qc" not in df.columns:
        df["HW1_qc"] = "OK"
    if "HW2_qc" not in df.columns:
        df["HW2_qc"] = "OK"
    if any(df.HW1.notnull()):
        ind1 = np.max(
            [
                df.HW1.first_valid_index(),
                df.HW1_qc.where(df.HW1_qc == "OK").first_valid_index(),
            ]
        )
        df["HS1"] = df.HW1[ind1] - df.HW1
    if any(df.HW2.notnull()):
        ind2 = np.max(
            [
                df.HW2.first_valid_index(),
                df.HW2_qc.where(df.HW2_qc == "OK").first_valid_index(),
            ]
        )
        df["HS2"] = df.HW2[ind2] - df.HW2

    df.loc[df["HW1_qc"] == "CHECKME", "HS1"] = np.nan
    df.loc[df["HW2_qc"] == "CHECKME", "HS2"] = np.nan
    # we then adjust and filter all surface height (could be replaced by an automated adjustment)
    df = adjust_data(df, site, ["HS1", "HS2"])

    # calculating SHF and LHF
    df["SHF"], df["LHF"] = jaws_tools.gradient_fluxes(df.copy())
    # interpolating variables at standard heights
    df["TA2m"] = jaws_tools.extrapolate_temp(
        df, var=["TA1", "TA2"], target_height=2, max_diff=5
    )
    df["RH2m"] = jaws_tools.extrapolate_temp(
        df, var=["RH1", "RH2"], target_height=2, max_diff=10
    )
    df["VW10m"] = jaws_tools.extrapolate_temp(
        df, var=["VW1", "VW2"], target_height=10, max_diff=5
    )

    # calculatin SZA and SAA with same script as for PROMICE stations
    doy = df.index.dayofyear.values
    hour = df.index.hour.values
    minute = df.index.minute.values
    lon = np.abs(longitude)
    deg2rad = np.pi / 180
    rad2deg = 1 / deg2rad

    d0_rad = 2 * np.pi * (doy + (hour + minute / 60) / 24 - 1) / 365

    Declination_rad = np.arcsin(
        0.006918
        - 0.399912 * np.cos(d0_rad)
        + 0.070257 * np.sin(d0_rad)
        - 0.006758 * np.cos(2 * d0_rad)
        + 0.000907 * np.sin(2 * d0_rad)
        - 0.002697 * np.cos(3 * d0_rad)
        + 0.00148 * np.sin(3 * d0_rad)
    )

    HourAngle_rad = 2 * np.pi * (((hour + minute / 60) / 24 - 0.5) - lon / 360)
    # ; - 15.*timezone/360.) ; NB: Make sure time is in UTC and longitude is positive when west! Hour angle should be 0 at noon.

    # This is 180 deg at noon (NH), as opposed to HourAngle.
    DirectionSun_deg = HourAngle_rad * 180 / np.pi - 180

    DirectionSun_deg[DirectionSun_deg < 0] += 360
    DirectionSun_deg[DirectionSun_deg < 0] += 360

    ZenithAngle_rad = np.arccos(
        np.cos(latitude * deg2rad) * np.cos(Declination_rad) * np.cos(HourAngle_rad)
        + np.sin(latitude * deg2rad) * np.sin(Declination_rad)
    )

    ZenithAngle_deg = ZenithAngle_rad * rad2deg
    df["SZA"] = ZenithAngle_deg
    df["SAA"] = DirectionSun_deg
    return df


# Filter frozen values
from scipy.ndimage import binary_dilation


def filter_zero_gradient(df_out):
    # default settings:
    thresh = 0.000001
    length_frozen = 6
    not_in_dark_season = False
    var_list = [
        "VW1",
        "VW2",
        "TA1",
        "TA1",
        "TA2",
        "TA3",
        "TA4",
        "P",
        "RH1",
        "RH2",
        "HW1",
        "HW2",
        "ISWR",
        "OSWR",
    ]
    for var in var_list:
        if var not in df_out.columns:
            continue
        if var in ["HW1", "HW2"]:
            length_frozen = 5 * 24
        if var in ["ISWR", "OSWR"]:
            thresh = 1
            length_frozen = 24
            not_in_dark_season = True

        ind = np.abs(df_out[var].diff().values) < thresh

        if not_in_dark_season:
            dark_month = df_out["ISWR"].groupby(df_out.index.month).mean() < 5
            ind_winter = np.isin(df_out.index.month, dark_month[dark_month].index)
            ind[ind_winter] = False

        if np.any(ind):
            no_wind_count = 0
            for i, val in enumerate(ind):
                if val:
                    no_wind_count = no_wind_count + 1
                else:
                    if no_wind_count > 0:
                        if no_wind_count <= length_frozen:
                            # gap less than length_frozen hours putting down the flag
                            ind[np.arange(i - no_wind_count, i + 1)] = False
                            no_wind_count = 0
                        else:
                            # too long period without wind, leaving flags up
                            no_wind_count = 0
            ind = binary_dilation(ind)

            if var + "_qc" in df_out.columns:
                df_out.loc[ind, var + "_qc"] = "FROZEN"
            else:
                df_out[var + "_qc"] = "OK"
                df_out.loc[ind, var + "_qc"] = "FROZEN"
    return df_out


def filter_data(df, site, plot=True, remove_data=False):
    """
    Applies standard filter on data.

    INTPUTS:
        df: PROMICE data with time index
        site: string of PROMICE site
        var_list: list of the variables for which data removal should be
            conducted (default: all)
        plot: whether data removal should be plotted

    OUTPUTS:
        promice_data: Dataframe containing PROMICE data for the desired settings [DataFrame]
    """
    df_out = df.copy()

    # Limits filter:
    df_lim = pd.read_csv("metadata/limits.csv", sep="\s*,\s*", engine="python")
    df_lim.columns = ["site", "var_lim", "var_min", "var_max"]
    for site_lim, var, var_min, var_max in zip(
        df_lim.site, df_lim.var_lim, df_lim.var_min, df_lim.var_max
    ):
        if site_lim == "*" or site_lim == site:
            if var in df_out.columns.values:
                ind = np.logical_or(df_out[var] > var_max, df_out[var] < var_min)
                if var + "_qc" in df_out.columns:
                    df_out.loc[ind, var + "_qc"] = "OOL"
                else:
                    df_out[var + "_qc"] = "OK"
                    df_out.loc[ind, var + "_qc"] = "OOL"

    # Isolated measurements filter
    msk1 = df_out.HW1.isnull().shift(2).fillna(False)
    msk2 = df_out.HW1.isnull().shift(1).fillna(False)
    msk3 = df_out.HW1.isnull().shift(-1).fillna(False)
    msk4 = df_out.HW1.isnull().shift(-2).fillna(False)
    msk = (msk2 & msk3) | (msk1 & msk3) | (msk2 & msk4)
    df_out.loc[msk, "HW1"] = np.nan
    msk1 = df_out.HW2.isnull().shift(2).fillna(False)
    msk2 = df_out.HW2.isnull().shift(1).fillna(False)
    msk3 = df_out.HW2.isnull().shift(-1).fillna(False)
    msk4 = df_out.HW2.isnull().shift(-2).fillna(False)
    msk = (msk2 & msk3) | (msk1 & msk3) | (msk2 & msk4)
    df_out.loc[msk, "HW2"] = np.nan

    return df_out


def hampel(vals_orig, k=7, t0=3):
    """
    vals: pandas series of values from which to remove outliers
    k: size of window (including the sample; 7 is equal to 3 on either side of value)
    """
    # Make copy so original not edited
    vals = vals_orig.copy()
    # Hampel Filter
    L = 1.4826
    rolling_median = vals.rolling(k).median()
    difference = np.abs(rolling_median - vals)
    median_abs_deviation = difference.rolling(k).median()
    threshold = t0 * L * median_abs_deviation
    outlier_idx = difference > threshold
    vals[outlier_idx] = np.nan
    return vals


def smooth(x, window_len=14, window="hanning"):
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

    if window_len < 3:
        return x

    if not window in ["flat", "hanning", "hamming", "bartlett", "blackman"]:
        raise ValueError(
            "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"
        )

    s = np.r_[x[window_len - 1 : 0 : -1], x, x[-2 : -window_len - 1 : -1]]
    # Msg(len(s))
    if window == "flat":  # moving average
        w = np.ones(window_len, "d")
    else:
        w = eval("np." + window + "(window_len)")

    y = np.convolve(w / w.sum(), s, mode="valid")

    return y[int(window_len / 2 - 1) : -int(window_len / 2)]


def hampel(vals_orig, k=7 * 24, t0=3):
    """
    vals: pandas series of values from which to remove outliers
    k: size of window (including the sample; 7 is equal to 3 on either side of value)
    """
    # Make copy so original not edited
    vals = vals_orig.copy()
    # Hampel Filter
    L = 1.4826
    rolling_median = vals.rolling(k).median()
    difference = np.abs(rolling_median - vals)
    median_abs_deviation = difference.rolling(k).median()
    threshold = t0 * L * median_abs_deviation
    outlier_idx = difference > threshold
    outlier_idx[0 : round(k / 2)] = False
    vals.loc[outlier_idx] = np.nan
    return vals


def firstNonNan(listfloats):
    if not np.any(~np.isnan(listfloats)):
        return np.nan
    for item in listfloats:
        if math.isnan(item) == False:
            return item


def surface_height_processor(df_v4):
    # Calculating surface height from wind sensor height
    df_v4["HS1"] = df_v4.HW1[df_v4.HW1.first_valid_index()] - df_v4.HW1
    df_v4["HS2"] = df_v4.HW2[df_v4.HW2.first_valid_index()] - df_v4.HW2
    if "HW1_qc" not in df_v4.columns:
        df_v4["HW1_qc"] = "OK"
    if "HW2_qc" not in df_v4.columns:
        df_v4["HW2_qc"] = "OK"
    df_v4.loc[df_v4["HW1_qc"] == "CHECKME", "HS1"] = np.nan
    df_v4.loc[df_v4["HW2_qc"] == "CHECKME", "HS2"] = np.nan

    df_v4.HS1 = df_v4.HS1.resample("H").interpolate(limit=12, method="nearest")
    ind_nan = df_v4.HS1.isnull()
    average_acc = df_v4.HS1.loc[:"1999"].diff().mean()
    HS_avg = np.arange(len(df_v4.HS1)) * average_acc

    df_v4.HS1.loc[ind_nan] = HS_avg[ind_nan]
    adj_list = df_v4.HS1.diff().loc[(df_v4.HS1.diff().abs() > 0.3)]
    for i in adj_list.index:
        df_v4.HS1.loc[i:] = df_v4.HS1.loc[i:] - adj_list.loc[i]
    df_v4.HS1.loc[ind_nan] = np.nan
    diff = df_v4.HS1.diff()
    diff.loc[diff.isnull()] = average_acc
    df_v4["HS1_adj"] = diff.cumsum()

    plt.figure()
    df_v4.HS1.diff().plot()
    df_v4.HS1.plot()
    (-df_v4.HW1).plot(label="original instrument height")
    df_v4.HS1.plot()
    df_v4.HS1_adj.plot(label="final adjusted HS")
    plt.title("HS1")

    df_v4.HS2 = df_v4.HS2.resample("H").interpolate(limit=12, method="nearest")
    ind_nan = df_v4.HS2.isnull()
    average_acc = df_v4.HS2.loc[:"1999"].diff().mean()
    HS_avg = np.arange(len(df_v4.HS2)) * average_acc

    df_v4.HS2.loc[ind_nan] = HS_avg[ind_nan]
    adj_list = df_v4.HS2.diff().loc[(df_v4.HS2.diff().abs() > 0.3)]
    for i in adj_list.index:
        df_v4.HS2.loc[i:] = df_v4.HS2.loc[i:] - adj_list.loc[i]
    df_v4.HS2.loc[ind_nan] = np.nan
    diff = df_v4.HS2.diff()
    diff.loc[diff.isnull()] = average_acc
    df_v4["HS2_adj"] = diff.cumsum()

    plt.figure()
    df_v4.HS2.diff().plot()
    df_v4.HS2.plot()
    (-df_v4.HW2).plot(label="original instrument height")
    df_v4.HS2.plot()
    df_v4.HS2_adj.plot(label="final adjusted HS")
    plt.title("HS2")
    return df_v4


def combine_hs_dpt(df, site):
    # smoothing and filtering pressure transducer data
    df["DepthPressureTransducer_Cor_adj(m)"] = hampel(
        df["DepthPressureTransducer_Cor(m)"].interpolate(limit=72)
    ).values
    df["SnowHeight_adj(m)"] = hampel(df["SnowHeight(m)"].interpolate(limit=72)).values
    df["SurfaceHeight_adj(m)"] = hampel(
        df["SurfaceHeight(m)"].interpolate(limit=72)
    ).values

    # defining ice ablation period
    smoothed_PT = (
        df["DepthPressureTransducer_Cor(m)"]
        .interpolate(limit=72)
        .rolling("7D", min_periods=1)
        .mean()
        .shift(-84, freq="h")
    )
    smoothed_PT = smoothed_PT.rolling("7D", min_periods=1).mean().shift(-84, freq="h")
    ind_ablation = np.logical_and(
        smoothed_PT.diff().values < -0.00035,
        np.isin(smoothed_PT.diff().index.month, [6, 7, 8, 9]),
    )
    ind_ablation = np.concatenate(
        (ind_ablation[2 * 84 :], ind_ablation[: 2 * 84])
    )  # no idea why the array is still shifted
    ind_accumulation = ~ind_ablation

    # adjusting Snow and Surface heights to the PT-derived height
    hs1 = df["SnowHeight_adj(m)"].interpolate(limit=24 * 14).copy()
    hs2 = df["SurfaceHeight_adj(m)"].interpolate(limit=24 * 14).copy()
    z = df["DepthPressureTransducer_Cor_adj(m)"].copy()

    from sklearn.linear_model import LinearRegression

    if np.any(~np.isnan(z)):
        Y = z.iloc[:].values.reshape(-1, 1)
        X = z.iloc[~np.isnan(Y)].index.astype(np.int64).values.reshape(-1, 1)
        Y = Y[~np.isnan(Y)]
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(X, Y)  # perform linear regression
        Y_pred = linear_regressor.predict(
            z.index.astype(np.int64).values.reshape(-1, 1)
        )
        plt.figure()
        plt.scatter(X, Y)
        plt.plot(z.index.astype(np.int64).values, Y_pred, color="red")
        plt.title("Removing intercept at " + site)
        plt.show()
        z = z - Y_pred[0]

    years = df.index.year.values
    ind_start = years.astype(int)
    ind_end = years.astype(int)
    for i, y in enumerate(np.unique(years)):
        # for each year
        ind_yr = years == y
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
            ind_abl_yr = np.logical_and(
                ind_yr, np.isin(df.index.month.values, [6, 7, 8])
            )
            ind_start[i] = np.argwhere(ind_abl_yr)[0][0]
            ind_end[i] = np.argwhere(ind_abl_yr)[-1]
            ind_ablation[ind_start[i] : ind_end[i]] = True
            ind_accumulation[ind_start[i] : ind_end[i]] = False
        else:
            # otherwise left as nan
            ind_start[i] = -999
            ind_end[i] = -999
            continue

    plt.figure()
    # plt.plot(df.index, ind_ablation*(-10))
    ((smoothed_PT - smoothed_PT.mean()) / 1000).plot()
    ((z - z.mean()) / 1000).plot()

    smoothed_PT.diff().plot()
    plt.axhline(-0.00035)
    for i, y in enumerate(np.unique(years)):
        plt.axvspan(
            df.index[ind_start[i]], df.index[ind_end[i]], color="orange", alpha=0.1
        )

    plt.figure()
    df["SnowHeight(m)"].plot(color="darkgray", label="")
    df["SnowHeight_adj(m)"].plot(label="SnowHeight(m)")
    df["SurfaceHeight(m)"].plot(color="darkgray", label="")
    df["SurfaceHeight_adj(m)"].plot(label="SurfaceHeight(m)")
    df["DepthPressureTransducer_Cor(m)"].plot(color="darkgray", label="")
    df["DepthPressureTransducer_Cor_adj(m)"].plot(
        label="DepthPressureTransducer_Cor(m)"
    )

    plt.legend()
    plt.title(site)
    for i, y in enumerate(np.unique(years)):
        plt.axvspan(
            df.index[ind_start[i]], df.index[ind_end[i]], color="orange", alpha=0.1
        )

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
        if np.any(~np.isnan(z.iloc[(ind_end[i] - 24 * 7) : (ind_end[i] + 24 * 7)])):

            # if it is not the first year and that no adjustment has been done
            if (i > 0 or z.first_valid_index().month >= 8) and flag == 0:
                # then we adjust the pressur transducer to SR2
                ind_first_nonan = z.index.get_loc(
                    z.iloc[ind_start[i] :].first_valid_index()
                )
                z = (
                    z
                    - np.nanmean(z.iloc[ind_first_nonan : (ind_first_nonan + 24 * 7)])
                    + np.nanmean(hs2.iloc[ind_first_nonan : (ind_first_nonan + 24 * 7)])
                )
                z.plot()
                flag = 1

            if i == 0:
                flag = 1

            if ~np.isnan(
                np.nanmean(hs1.iloc[(ind_end[i] - 24 * 7) : (ind_end[i] + 24 * 7)])
            ):
                # if hs1.first_valid_index().month>=8
                hs1.iloc[ind_end[i] :] = (
                    hs1.iloc[ind_end[i] :]
                    - np.nanmean(
                        hs1.iloc[(ind_end[i] - 24 * 7) : (ind_end[i] + 24 * 7)]
                    )
                    + np.nanmean(z.iloc[(ind_end[i] - 24 * 7) : (ind_end[i] + 24 * 7)])
                )
            else:
                tmp1 = hs1.iloc[ind_end[i] : ind_start[i + 1]].values
                tmp2 = hs2.iloc[ind_end[i] : ind_start[i + 1]].values
                ind = ~np.isnan(tmp1 + tmp2)

                hs1.iloc[ind_end[i] :] = (
                    hs1.iloc[ind_end[i] :]
                    - np.nanmean(tmp1[ind])
                    + np.nanmean(tmp2[ind])
                )

        # and adjust the end of ablation SR1 height to the SR2 height
        elif np.any(~np.isnan(hs2.iloc[ind_end[i] : (ind_end[i] + 24 * 7)])):

            # if it is not the first year and that no adjustment has been done
            if i > 0 and flag == 0:
                # then we adjust the pressur SR2 to transducer
                ind_first_nonan = hs2.index.get_loc(
                    hs2.iloc[ind_start[i] :].first_valid_index()
                )
                if np.any(
                    ~np.isnan(z.iloc[ind_first_nonan : (ind_first_nonan + 24 * 7)])
                ):
                    hs2 = (
                        hs2
                        - np.nanmean(
                            hs2.iloc[ind_first_nonan : (ind_first_nonan + 24 * 7)]
                        )
                        + np.nanmean(
                            z.iloc[ind_first_nonan : (ind_first_nonan + 24 * 7)]
                        )
                    )
                else:
                    hs2 = (
                        hs2
                        - np.nanmean(
                            hs2.iloc[ind_first_nonan : (ind_first_nonan + 24 * 7)]
                        )
                        + np.nanmean(
                            hs1.iloc[ind_first_nonan : (ind_first_nonan + 24 * 7)]
                        )
                    )
                flag = 1
            if i == 0:
                flag = 1
            hs1.iloc[ind_end[i] :] = (
                hs1.iloc[ind_end[i] :]
                - np.nanmean(hs1.iloc[ind_end[i] : (ind_end[i] + 24 * 7)])
                + np.nanmean(hs2.iloc[ind_end[i] : (ind_end[i] + 24 * 7)])
            )

        if np.any(~np.isnan(z.iloc[(ind_end[i] - 24 * 7) : (ind_end[i] + 24 * 7)])):
            hs2.iloc[ind_start[i] :] = (
                hs2.iloc[ind_start[i] :]
                - np.nanmean(hs2.iloc[(ind_end[i] - 24 * 7) : (ind_end[i] + 24 * 7)])
                + np.nanmean(z.iloc[(ind_end[i] - 24 * 7) : (ind_end[i] + 24 * 7)])
            )

        hs1.plot()
        hs2.plot()
        plt.axvline(hs1.index[ind_end[i]])

    df["SurfaceHeight1_adj(m)"] = hs1.interpolate(limit=7 * 24).values
    df["SurfaceHeight2_adj(m)"] = hs2.interpolate(limit=7 * 24).values
    df["DepthPressureTransducer_Cor_adj(m)"] = z.interpolate(limit=7 * 24).values

    # making a summary of the surface height
    df["SurfaceHeight_summary(m)"] = np.nan

    # in winter, both SR1 and SR2 are used
    df["SurfaceHeight_summary(m)"] = np.nanmean(
        df[["SurfaceHeight1_adj(m)", "SurfaceHeight2_adj(m)"]].values, axis=1
    )

    # in ablation season we use SR2 instead of the SR1&2 average
    data_update = df["SurfaceHeight2_adj(m)"].interpolate(limit=72).values
    ind_update = np.logical_and(ind_ablation, ~np.isnan(data_update))
    df.loc[ind_update, "SurfaceHeight_summary(m)"] = data_update[ind_update]

    # in ablation season we use pressure transducer over all other options
    data_update = df["DepthPressureTransducer_Cor_adj(m)"].interpolate(limit=72).values
    ind_update = np.logical_and(ind_ablation, ~np.isnan(data_update))
    df.loc[ind_update, "SurfaceHeight_summary(m)"] = data_update[ind_update]

    # plotting result
    f1 = plt.figure(figsize=(12, 8))
    df["DepthPressureTransducer_Cor_adj(m)"].plot(label="Pressure transducer")
    df["SurfaceHeight1_adj(m)"].plot(label="SonicRanger1")
    df["SurfaceHeight2_adj(m)"].plot(label="SonicRanger2")
    df["SurfaceHeight_summary(m)"].plot(
        label="Summary", linestyle="--", linewidth=2, color="tab:red"
    )

    plt.legend(prop={"size": 15})
    plt.xlabel("Year", size=20)
    plt.ylabel("Height (m)", size=20)
    plt.title(site, size=20)
    plt.grid()
    for i, y in enumerate(np.unique(years)):
        plt.axvspan(
            df.index[ind_start[i]], df.index[ind_end[i]], color="orange", alpha=0.1
        )
    f1.savefig(
        "figures/L1_data_treatment/" + site + "_surface_height.png",
        dpi=90,
        bbox_inches="tight",
    )
    Msg(" ")
    Msg(
        "![Surface height adjustement at "
        + site
        + "](../figures/L1_data_treatment/"
        + site
        + "_surface_height.png)"
    )
    Msg(" ")

    return df


def RH_water2ice(RH, T):
    # switch ONLY SUBFREEZING timesteps to with-regards-to-ice
    Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
    Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
    Rv = 461.5  # H2O Vapor Gaz constant (J/kg/K)
    ind = T < 0
    # ind = T == T
    TCoeff = 1 / 273.15 - 1 / (T + 273.15)
    Es_Water = 6.112 * np.exp(Lv / Rv * TCoeff)
    Es_Ice = 6.112 * np.exp(Ls / Rv * TCoeff)
    RH_out = RH.copy()
    RH_out[ind] = RH[ind] * Es_Water[ind] / Es_Ice[ind]
    return RH_out


def RH_ice2water(RH, T):
    # switch ALL timestep to with-regards-to-water
    RH = np.array(RH)
    Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
    Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
    Rv = 461.5  # H2O Vapor Gaz constant (J/kg/K)
    ind = T < 0
    TCoeff = 1 / 273.15 - 1 / (T + 273.15)
    Es_Water = 6.112 * np.exp(Lv / Rv * TCoeff)
    Es_Ice = 6.112 * np.exp(Ls / Rv * TCoeff)
    RH_out = RH.copy()

    # T_100 = 373.15
    # T_0 = 273.15
    # T = T +T_0
    # # GOFF-GRATCH 1945 equation
    #    # saturation vapour pressure above 0 C (hPa)
    # Es_Water = 10**(  -7.90298*(T_100/T - 1) + 5.02808 * np.log(T_100/T)
    #     - 1.3816E-7 * (10**(11.344*(1-T/T_100))-1)
    #     + 8.1328E-3*(10**(-3.49149*(T_100/T-1)) -1.) + np.log(1013.246) )
    # # saturation vapour pressure below 0 C (hPa)
    # Es_Ice = 10**(  -9.09718 * (T_0 / T - 1.) - 3.56654 * np.log(T_0 / T) +
    #              0.876793 * (1. - T / T_0) + np.log(6.1071)  )

    RH_out[ind] = RH[ind] / Es_Water[ind] * Es_Ice[ind]

    return RH_out


def RH_ice2water2(RH, T):
    # switch ALL timestep to with-regards-to-water
    RH = np.array(RH)
    # Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
    # Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
    # Rv = 461.5     # H2O Vapor Gaz constant (J/kg/K)
    ind = T == T  # T < 0
    # TCoeff = 1/273.15 - 1/(T+273.15)
    # Es_Water = 6.112*np.exp(Lv/Rv*TCoeff)
    # Es_Ice = 6.112*np.exp(Ls/Rv*TCoeff)
    RH_out = RH.copy()

    T_100 = 373.15
    T_0 = 273.15
    T = T + T_0
    # GOFF-GRATCH 1945 equation
    # saturation vapour pressure above 0 C (hPa)
    Es_Water = 10 ** (
        -7.90298 * (T_100 / T - 1)
        + 5.02808 * np.log10(T_100 / T)
        - 1.3816e-7 * (10 ** (11.344 * (1 - T / T_100)) - 1)
        + 8.1328e-3 * (10 ** (-3.49149 * (T_100 / T - 1)) - 1.0)
        + np.log10(1013.246)
    )
    # saturation vapour pressure below 0 C (hPa)
    Es_Ice = 10 ** (
        -9.09718 * (T_0 / T - 1.0)
        - 3.56654 * np.log10(T_0 / T)
        + 0.876793 * (1.0 - T / T_0)
        + np.log10(6.1071)
    )

    RH_out[ind] = RH[ind] / Es_Water[ind] * Es_Ice[ind]

    return RH_out


# def RH_ice2water3(RH, T):
#     # switch ALL timestep to with-regards-to-water
#     RH = np.array(RH)
#     # Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
#     # Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
#     # Rv = 461.5     # H2O Vapor Gaz constant (J/kg/K)
#     ind = T < 0
#     # TCoeff = 1/273.15 - 1/(T+273.15)
#     # Es_Water = 6.112*np.exp(Lv/Rv*TCoeff)
#     # Es_Ice = 6.112*np.exp(Ls/Rv*TCoeff)
#     RH_out = RH.copy()

#     T_100 = 373.15
#     T_0 = 273.15
#     T = T +T_0
#    # saturation vapour pressure above 0 C (hPa)
#     Es_Water = 10**(  10.79574*(1 - T_100/T) + 5.028 * np.log10(T / T_100)
#                     + 1.50475E-4 * (1 - 10**(-8.2969 * (T/T_100 - 1)))
#                     + 0.42873E-3*(10**(4.76955*(1 - T_100/T)) -1.) +  0.78614 + 2.0 )

#     Es_Ice = 10**( -9.09685 * (T_0 / T - 1.) - 3.56654 * np.log10(T_0 / T) +
#                   0.87682 * (1. - T / T_0) + 0.78614   )
#     RH_out[ind] = RH[ind] / Es_Water[ind]*Es_Ice[ind]

#     return RH_out


def RH2SpecHum(RH, T, pres):
    # Note: RH[T<0] needs to be with regards to ice

    Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
    Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
    Rv = 461.5  # H2O Vapor Gaz constant (J/kg/K)
    es = 0.622

    TCoeff = 1 / 273.15 - 1 / (T + 273.15)
    Es_Water = 6.112 * np.exp(Lv / Rv * TCoeff)
    Es_Ice = 6.112 * np.exp(Ls / Rv * TCoeff)

    es_all = Es_Water.copy()
    es_all[T < 0] = Es_Ice[T < 0]

    # specific humidity at saturation
    q_sat = es * es_all / (pres - (1 - es) * es_all)

    # specific humidity
    q = RH * q_sat / 100
    return q


def SpecHum2RH(q, T, pres):
    # Note: RH[T<0] will be with regards to ice

    Lv = 2.5001e6  # H2O Vaporization Latent Heat (J/kg)
    Ls = 2.8337e6  # H2O Sublimation Latent Heat (J/kg)
    Rv = 461.5  # H2O Vapor Gaz constant (J/kg/K)
    es = 0.622

    TCoeff = 1 / 273.15 - 1 / (T + 273.15)
    Es_Water = 6.112 * np.exp(Lv / Rv * TCoeff)
    Es_Ice = 6.112 * np.exp(Ls / Rv * TCoeff)

    es_all = Es_Water
    es_all[T < 0] = Es_Ice

    # specific humidity at saturation
    q_sat = es * es_all / (pres - (1 - es) * es_all)

    # relative humidity
    RH = q / q_sat * 100
    return RH

# -*- coding: utf-8 -*-

"""
tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import datetime
import pytz
import os
import warnings
import jaws_tools
import nead
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
        "DW2",
        "HS1",
        "HS2",
        "HS1",
        "HS2",
        "NR",
    ]

    try:
        index = promice_names.index(name_in)
        return gcnet_names[index]
    except:
        return None


def field_info(fields):
    tmp =pd.read_csv('metadata/L1_variable_list.csv', skipinitialspace=True)
    field_list = tmp.fields.tolist()
    units = tmp.units.tolist()
    display_description = tmp.display_description.tolist()
    database_fields = tmp.database_fields.tolist()
    database_fields_data_types = tmp.database_fields_data_types.tolist()

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

    flag_data = pd.read_csv("metadata/flags/" + site + ".csv", comment="#", skipinitialspace=True)

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
            + site.replace(" ", "")
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
                    elif flag == "NAN":
                        df.loc[df[var] == flag, var[:-3]].plot(
                            marker="o", linestyle="none", color="violet", label=flag
                        )
                    elif flag == "OOL":
                        df.loc[df[var] == flag, var[:-3]].plot(
                            marker="o", linestyle="none", color="red", label=flag
                        )
                    elif flag == "IWS":
                        df.loc[df[var] == flag, var[:-3]].plot(
                            marker="o", linestyle="none", color="cyan", label=flag
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
                    + site.replace(" ", "")
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
                df_out.loc[t0:t1, var] = (df_out.loc[t0:t1, var].values + val) % 360

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
                
            if func == "air_temp_sonic_anticorrection":
                # finding the available air temp measurements
                tmp = df_out.loc[t0:t1, "TA" + var[-1]]
                tmp2 = df_out.loc[t0:t1, ["TA" + str(i) for i in range(1, 5)]].mean(
                    axis=1
                )
                tmp.loc[tmp.isnull()] = tmp2.loc[tmp.isnull()]
                tmp = tmp.interpolate(method="nearest", fill_value="extrapolate")
                # plt.figure()
                # df_out.loc[t0:t1, var].plot(ax=plt.gca(), label='original')
                # (df_out.loc[t0:t1, var] * np.sqrt((tmp + 273.15) / 273.15)).plot(ax=plt.gca(), label='corrected')
                df_out.loc[t0:t1, var] = df_out.loc[t0:t1, var].values / np.sqrt(
                    (tmp.values + 273.15) / 273.15
                )
                # df_out.loc[t0:t1, var].plot(ax=plt.gca(), label='anticorrected')
                # plt.gca().legend()

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
                + site.replace(" ", "")
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
                + site.replace(" ", "")
                + "_adj_"
                + var
                + ".jpeg)"
            )
            Msg(" ")

    return df_out


def augment_data(df_in, latitude, longitude, elevation, site):
    # Interpolate small gaps in available variables
    # and add variables to the dataset:
    # Surface height HS
    # Sensible and Latent Heat Fluxes SHF & LHF
    # Solar azimuth and zenith angles
    # albedo
    
    # for debug:
    # df_in = df_v5.copy()
    df = df_in.copy()
    
    # Interpolation over gaps smaller than a week
    mask = df[["HW1", "HW2"]].copy()
    for i in ["HW1", "HW2"]:
        tmp = pd.DataFrame(df[i])
        tmp["new"] = (tmp.notnull() != tmp.shift().notnull()).cumsum()
        tmp["ones"] = 1
        mask[i] = (tmp.groupby("new")["ones"].transform("count") < 24 * 2) | df[
            i
        ].notnull()
    df[["HW1", "HW2"]] = df[["HW1", "HW2"]].interpolate().values
    df.loc[mask.HW1 == False, "HW1"] = np.nan
    df.loc[mask.HW2 == False, "HW2"] = np.nan


    def fill_gap_HW(df1, df2, var_target="HW1", var_sec="HW2", note=''):
        if var_target+'_org' not in df1.columns:
            df1[var_target+'_org'] = ''
        # Gap-filling HW using other sensor if available
        prev_no_nan = df1[var_target].notnull().shift(1).fillna(False)
        is_nan = df1[var_target].isnull()
        list_start_gaps = df1.index[(prev_no_nan & is_nan)]

        prev_nan = df1[var_target].isnull().shift(1).fillna(False)
        no_nan = df1[var_target].notnull()
        list_end_gaps = df1.index[(prev_nan & no_nan)]

        list_start_gaps = list_start_gaps[list_start_gaps < df2.index[-1]]
        list_start_gaps = list_start_gaps[list_start_gaps > df2.index[0]]
        list_end_gaps = list_end_gaps[list_end_gaps < df2.index[-1]]
        list_end_gaps = list_end_gaps[list_end_gaps > df2.index[0]]
        
        if list_end_gaps[-1] < list_start_gaps[-1]:
            list_end_gaps = np.append(list_end_gaps, min(df1.index[-1],df2.index[-1]))
        if list_end_gaps[0] < list_start_gaps[0]:
            list_start_gaps = np.append(max(df1.index[0],df2.index[0]), list_start_gaps)


        for start, end in zip(list_start_gaps, list_end_gaps):
            # we look at the month preceeding the gap
            # calculate the mean difference between the two heights during that time
            mean_diff = (
                df1.loc[(start - pd.Timedelta(days=30)) : start, var_target]
                - df2.loc[(start - pd.Timedelta(days=30)) : start, var_sec]
            ).mean()
            if np.isnan(mean_diff):
                mean_diff = df1.loc[:, var_target].mean() - df2.loc[:, var_sec].mean()

            # and use that difference to adjust the secondary height to the height
            # that is to be gap-filled
            df1.loc[start:end, var_target] = (
                df2.loc[start:end, var_sec].values + mean_diff
            )
            df1.loc[start:end, var_target+'_org'] = var_sec + note

        return df1[var_target].values
    df["HW1_org"] = 'HW1'
    df["HW2_org"] = 'HW2'
    df["HW1"] = fill_gap_HW(df, df, "HW1", "HW2")
    df["HW2"] = fill_gap_HW(df, df, "HW2", "HW1")
       
    # At swiss camp, using HW from tower to fill the gaps
    # if site == 'Swiss Camp':
    #     df2 = nead.read("L1/00-SwissCamp10m.csv").to_dataframe().reset_index(drop=True)
    #     df2['timestamp'] = pd.to_datetime(df2.timestamp)
    #     df2 = df2.set_index("timestamp").replace(-999, np.nan)
        
    #     df["HW1"] = fill_gap_HW(df, df2, "HW1", "HW1", note= ' tower')
    #     df["HW1"] = fill_gap_HW(df, df2, "HW1", "HW2", note= ' tower')
    #     df["HW2"] = fill_gap_HW(df, df2, "HW2", "HW2", note= ' tower')
    #     df["HW2"] = fill_gap_HW(df, df2, "HW2", "HW1", note= ' tower')
    if site == 'Swiss Camp 10m':
        df2 = nead.read("L1/01-SwissCamp.csv").to_dataframe().reset_index(drop=True)
        df2['timestamp'] = pd.to_datetime(df2.timestamp)
        df2 = df2.set_index("timestamp").replace(-999, np.nan)
        
        df["HW1"] = fill_gap_HW(df, df2, "HW1", "HW1", note= ' aws')
        df["HW1"] = fill_gap_HW(df, df2, "HW1", "HW2", note= ' aws')
        df["HW2"] = fill_gap_HW(df, df2, "HW2", "HW2", note= ' aws')
        df["HW2"] = fill_gap_HW(df, df2, "HW2", "HW1", note= ' aws')        

    fig,ax = plt.subplots(2,1, figsize=(15,8))
    for src in df.HW1_org.unique():
        df.HW1.loc[df.HW1_org == src].plot(ax=ax[0], label=src, marker="o", linestyle="None")
    for src in df.HW2_org.unique():
        df.HW2.loc[df.HW2_org == src].plot(ax=ax[1], label=src, marker="o", linestyle="None")
    ax[0].legend()
    ax[1].legend()
    fig.savefig("figures/L1_data_treatment/" + site + "_gap_filling_HW.png")

    df = df.drop(columns=['HW1_org','HW2_org'])
    # Creating surface height field
    if any(df.HW1.notnull()):
        ind1 = df.HW1.first_valid_index()
        df["HS1"] = df.HW1[ind1] - df.HW1
    if any(df.HW2.notnull()):
        ind2 = df.HW2.first_valid_index()
        df["HS2"] = df.HW2[ind2] - df.HW2

    # we then adjust and filter all surface height (could be replaced by an automated adjustment)
    df = adjust_data(df, site, ["HS1", "HS2"])

    # calculating SHF and LHF
    df["SHF"], df["LHF"] = jaws_tools.gradient_fluxes(df.copy())
    
    # interpolating variables at standard heights
    df["TA2m"] = extrapolate_temp(
        df, var=["TA1", "TA2"], target_height=2, max_diff=5
    )
    df["RH2m"] = extrapolate_temp(
        df, var=["RH1", "RH2"], target_height=2, max_diff=10
    )
    df["VW10m"] = extrapolate_temp(
        df, var=["VW1", "VW2"], target_height=10, max_diff=5
    )

    # Solar zenith and azimuth angles
    df["SZA"], df["SAA"] = sza_saa(df, longitude, latitude)
    
    # Albedo
    if 'OSWR' in df.columns:
        df['Alb'] = calcAlbedo(df.OSWR, df.ISWR, df.SZA)
    
    # Humidity with regard to ice and specific humidity
    T1 = df.TA1.copy()
    T1.loc[df.TA1.isnull()] = df.loc[df.TA1.isnull(), 'TA3']
    df['RH1_cor'] = correctHumidity(df.RH1, T1)
    T2 = df.TA2.copy()
    T2.loc[df.TA1.isnull()] = df.loc[df.TA2.isnull(), 'TA4']
    df['RH2_cor'] = correctHumidity(df.RH2, T2)

    df['SH1'] = calcHumid(T1, df.P, df.RH1_cor)  *1000
    df['SH2'] = calcHumid(T2, df.P, df.RH2_cor)  *1000
    df.loc[df['SH1']>40, 'SH1'] = np.nan
    df.loc[df['SH2']>40, 'SH2'] = np.nan
    return df


def calcHumid(T_h, p_h, RH_cor_h, T_0=273.15, T_100=373.15,
              es_0=6.1071, es_100=1013.246, eps=0.622):
    '''Calculate specific humidity'''                                                         
    # Saturation vapour pressure above 0 C (hPa)
    es_wtr = 10**(-7.90298 * (T_100 / (T_h + T_0) - 1) + 5.02808 * np.log10(T_100 / (T_h + T_0))
                  - 1.3816E-7 * (10**(11.344 * (1 - (T_h + T_0) / T_100)) - 1)
                  + 8.1328E-3 * (10**(-3.49149 * (T_100 / (T_h + T_0) -1)) - 1) + np.log10(es_100))

    # Saturation vapour pressure below 0 C (hPa)
    es_ice = 10**(-9.09718 * (T_0 / (T_h + T_0) - 1) - 3.56654
                  * np.log10(T_0 / (T_h + T_0)) + 0.876793
                  * (1 - (T_h + T_0) / T_0)
                  + np.log10(es_0)) 

    # Specific humidity at saturation (incorrect below melting point)
    q_sat = eps * es_wtr / (p_h - (1 - eps) * es_wtr) 
    
    # Replace saturation specific humidity values below melting point
    freezing = T_h < 0  
    q_sat[freezing] = eps * es_ice[freezing] / (p_h[freezing] - (1 - eps) * es_ice[freezing])
    
    # Convert to kg/kg
    return RH_cor_h * q_sat / 100 


def correctHumidity(rh, T, T_0=273.15, T_100=373.15, ews=1013.246, ei0=6.1071):
    '''Correct relative humidity using Groff & Gratch method
    Parameters
    ----------
    rh : xarray.DataArray
        Relative humidity
    T : xarray.DataArray
        Air temperature
    T_0 : int
        Steam point temperature
    T_100 : int
        Steam point temperature in K
    ews : int
        Saturation pressure (normal atmosphere) at steam point temperature
    ei0 : int
        DESCRIPTION
        
    Returns
    -------
    xarray.DataArray
        Corrected relative humidity
    '''                                            
    # Convert to hPa (Groff & Gratch)   
    e_s_wtr = 10**(-7.90298 * (T_100 / (T + T_0) - 1)
                   + 5.02808 * np.log10(T_100 / (T + T_0)) 
                   - 1.3816E-7 * (10**(11.344 * (1 - (T + T_0) / T_100)) - 1)
                   + 8.1328E-3 * (10**(-3.49149 * (T_100/(T + T_0) - 1)) -1)
                   + np.log10(ews))
    e_s_ice = 10**(-9.09718 * (T_0 / (T + T_0) - 1)
                   - 3.56654 * np.log10(T_0 / (T + T_0))
                   + 0.876793 * (1 - (T + T_0) / T_0)
                   + np.log10(ei0))
    
    # Define freezing point. Why > -100?  
    freezing = (T < 0) & (T > -100).values 

    # Set to Groff & Gratch values when freezing, otherwise just rh                         
    rh_cor = rh.where(~freezing, other = rh*(e_s_wtr / e_s_ice)) 
    return rh_cor  


def calcAlbedo(usr, dsr_cor, ZenithAngle_deg):
    '''Calculate surface albedo based on upwelling and downwelling shorwave 
    flux, the angle between the sun and sensor, and the sun zenith'''
    albedo = usr / dsr_cor    
    
    # NaN bad data
    OKalbedos = (ZenithAngle_deg < 70) & (albedo < 1) & (albedo > 0)    
    albedo[~OKalbedos] = np.nan             
    
    # Interpolate all. Note "use_coordinate=False" is used here to force 
    # comparison against the GDL code when that is run with *only* a TX file. 
    # Should eventually set to default (True) and interpolate based on time, 
    # not index.                                           
    # albedo = albedo.interpolate_na(dim='time', use_coordinate=False)           
    # albedo = albedo.ffill(dim='time').bfill(dim='time')                        #TODO remove this line and one above?
    return albedo


def sza_saa(df, longitude, latitude):
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
    return ZenithAngle_deg, DirectionSun_deg


def extrapolate_temp(dataframe, var=["TA1", "TA2"], target_height=2, max_diff=5):
    ht_low = dataframe["HW1"].copy()
    ht_high = dataframe["HW2"].copy()
    var_low = dataframe[var[0]].copy()
    var_high = dataframe[var[1]].copy()

    # making sure the level 1 is the lowest and 2 the highest
    ind = ht_high < ht_low
    ht_low.loc[ind] = dataframe["HW2"].values[ind]
    ht_high.loc[ind] = dataframe["HW1"].values[ind]
    var_low.loc[ind] = dataframe[var[1]].values[ind]
    var_high.loc[ind] = dataframe[var[0]].values[ind]

    msk = (
        var_low.notnull()
        & var_high.notnull()
        & ht_low.notnull()
        & ht_high.notnull()
        & ((var_low - var_high) != 0)
        & ((ht_low - ht_high) != 0)
    )
    surface_temp = ht_low * np.nan

    surface_temp.loc[msk] = var_low.loc[msk] - (
        ((var_high.loc[msk] - var_low.loc[msk]) / (ht_high.loc[msk] - ht_low.loc[msk]))
        * (target_height - ht_low.loc[msk])
    )
    diff_1 = (surface_temp - var_low).abs()
    diff_2 = (surface_temp - var_high).abs()
    surface_temp.loc[(diff_1 > max_diff) | (diff_2 > max_diff)] = np.nan
    return surface_temp

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
        "DW1",
        "DW2",
        "TA1",
        "TA1",
        "TA2",
        "TA3",
        "TA4",
        "P",
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
    df_lim = pd.read_csv("metadata/limits.csv", skipinitialspace=True)
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
    
    # Filtering DW for low or NaN values of VW
    msk = df_out.VW1.isnull() | df_out.VW1 < 0.5
    df_out.loc[msk, "DW1_qc"] = "IWS"
    msk = df_out.VW2.isnull() | df_out.VW2 < 0.5
    df_out.loc[msk, "DW2_qc"] = "IWS"
    
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

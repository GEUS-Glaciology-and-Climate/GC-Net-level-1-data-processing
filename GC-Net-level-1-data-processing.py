# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:00:14 2020

tip list:
    for plots in spyder command prompte
    %matplotlib inline
    for plots in a new window
    %matplotlib qt
@author: bav
"""
import os
import gc
from lib import PROMICE_toolbox as ptb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import os.path
import numpy as np
from lib import tocgen
from lib import liblogger
from os import path
import nead

class CustomError(Exception):
    pass

if not hasattr(nead, 'build_header_obj'):
    raise CustomError('Please install the latest version of pyNEAD. \nVisit https://github.com/GEUS-Glaciology-and-Climate/pyNEAD/')

try:
    os.mkdir("figures")
    os.mkdir("figures/L1_data_treatment")
    os.mkdir("out")
except:
    print("figures and output folders already exist")

open("out/Report.md", "w").close()
def Msg(txt):
    print(txt)
    with open("out/Report.md", "a") as _f:
        _f.write(txt + "\n")

path_to_L0 = "L0M/"
site_list = pd.read_csv("L1/GC-Net_location.csv", header=0, skipinitialspace=True)
# print(site_list)

# uncomment for use at specific sites
# All station names: 'Swiss Camp 10m', 'Swiss Camp', 'Crawford Point 1', 'NASA-U',
# 'GITS', 'Humboldt', 'Summit', 'Tunu-N', 'DYE-2', 'JAR1', 'Saddle',
# 'South Dome', 'NASA-E', 'CP2', 'NGRIP', 'NASA-SE', 'KAR', 'JAR2',
# 'KULU', 'Petermann ELA', 'NEEM', 'EastGRIP'
# site_list = site_list.loc[site_list.Name.values == 'Summit',:]
# site_list = site_list[17:]

# Swiss Camp 10m fills its HW gaps from the L1 file of Swiss Camp (PROMICE_toolbox.augment_data reads L1/hourly/SwissCamp.csv):
# Swiss Camp is therefore processed first, so that the 10 m tower always gets the heights of the same run.
_names = list(site_list.Name)
if "Swiss Camp 10m" in _names and "Swiss Camp" in _names:
    _names.remove("Swiss Camp 10m")
    _names.insert(_names.index("Swiss Camp") + 1, "Swiss Camp 10m")
    site_list = site_list.set_index("Name", drop=False).loc[_names].reset_index(drop=True)
# %
for site, ID in zip(site_list.Name, site_list.ID):
    # plt.close("all")
    Msg("# " + str(ID) + " " + site)
    L0dir = str(ID).zfill(2) + "-" + site
    filename = path_to_L0 + L0dir + ".csv"
    if path.exists(filename):
        ds = nead.read(filename)
        df = ds.to_dataframe()
        df = df.reset_index(drop=True)
        df.timestamp = pd.to_datetime(df.timestamp, utc=True)
        df = df.set_index("timestamp")
        ds_attrs = ds.attrs
    else:
        Msg("No logger file (L0M) for station " + str(ID) + " " + site + ": built from the C-level files only")
        df = pd.DataFrame(index=pd.DatetimeIndex([], tz="UTC", name="timestamp"))
        # metadata of the output files: the [METADATA] section of the station header, as in the L0M files
        import configparser
        cfg = configparser.ConfigParser()
        cfg.read("L0/L0_ini/" + L0dir + "_header.ini")
        ds_attrs = dict(cfg["METADATA"]) if cfg.has_section("METADATA") else {}

    # removing unneeded fields
    col_drop = [f for f in df.columns if '_min' in f] + \
        [f for f in df.columns if '_max' in f] + \
            [f for f in df.columns if '_stdev' in f]+ \
                [f for f in df.columns if '_std' in f]
    df = df.drop(columns=col_drop)

    if site == "Swiss Camp 10m":
        df["TA2"] = np.nan
        df["TA4"] = np.nan

    if len(df) > 0 and "HW1" not in df.columns:
        df.loc[df.HS1>900,"HS1"] = np.nan
        df["HW1"] = 2 + df["HS1"].max() - df["HS1"]
    if len(df) > 0 and ("HW2" not in df.columns) & ('HS2' in df.columns):
        df.loc[df.HS2>900,"HS2"] = np.nan
        df["HW2"] = 3.4 + df["HS2"].max() - df["HS2"]
    if len(df) > 0:
        df = df.resample("h").mean()

    # ---- Gap filling with the C-level files (legacy L1 data: Jason's file first, then the per-station file).
    # L0M holds the logger data only. The C-level data fill the hours/variables the logger lacks, until the missing
    # logger data are found. The values taken from the C-level files are tracked (mask) because they carry the C-level
    # conventions (RH wrt ice, corrected HW) that the adjustments below only apply to them.
    Msg("## Gap filling with the C-level files at " + site)
    sidecar = "L0M/provenance/" + L0dir + "_source_windows.csv"
    sw = pd.read_csv(sidecar) if path.exists(sidecar) else None
    logger_prov = liblogger.prov_from_windows(sw, df.index, list(df.columns)) if (sw is not None and len(df) > 0) else None
    df_logger = df.copy()   # kept as the true raw logger data for the diagnostic tables, before the HW/HS override below
    # first hour of CR1000 data (None if the station has none): the C-level heights are used only before it, and the C-level
    # values filling a gap after it must not get the HW sonic correction a second time (PROMICE_toolbox.FIRST_CR1000)
    # (CR1000 records stamped before 2000, e.g. the clock-reset block of Crawford Point 1 that a time_shift moves later, are no start)
    first_cr1000 = None
    if sw is not None and (sw.source_class == "CR1000").any():
        _starts = pd.to_datetime(sw.loc[sw.source_class == "CR1000", "start"], utc=True)
        _starts = _starts[_starts >= pd.Timestamp("2000-01-01", tz="UTC")]
        if len(_starts):
            first_cr1000 = _starts.min()

    # HW1, HW2, HS1, HS2: the existing L1 adjustments for these (air-temperature sonic correction, sensor swaps,
    # installation offsets) were built against the C-level convention for them, not the raw CR10X sonic-ranger reading.
    # Rather than re-derive that convention from the logger, CR10X-sourced hours of these four variables are dropped
    # here so the C-level file fills them below, exactly like any other gap; CR1000-sourced (and transmission-sourced)
    # hours are untouched.
    hw_hs_vars = [v for v in ("HW1", "HW2", "HS1", "HS2") if v in df.columns]
    if hw_hs_vars and sw is not None and len(df) > 0:
        cr10x_hw = liblogger.prov_from_windows(sw[sw.source_class == "CR10X"], df.index, hw_hs_vars).notna()
        n_drop = int(cr10x_hw.sum().sum())
        if n_drop:
            df[hw_hs_vars] = df[hw_hs_vars].mask(cr10x_hw)
            Msg("CR10X-sourced HW1/HW2/HS1/HS2 dropped (" + str(n_drop) + " values) to be filled from the C-level file instead")
    df, mask_c, prov_fill, c_all = liblogger.gapfill_from_c_level(df, L0dir, logger_prov=logger_prov, first_cr1000=first_cr1000)
    if c_all is None and len(df) == 0:
        Msg("Warning: no logger data and no C-level file for station " + str(ID) + " " + site)
        continue
    # RH: logger values are wrt water; the C-level values filled above are converted to wrt water where the C-level file
    # holds RH wrt ice (metadata/c_level_rh_convention.csv). From here on RH1/RH2 are wrt water everywhere.
    df = ptb.convert_c_level_rh_to_water(df, mask_c, site)
    if c_all is not None:
        n_c = int(mask_c.sum().sum())
        Msg("Values taken from the C-level files: " + str(n_c))
        try:
            if len(df_logger) > 0:
                liblogger.record_comparison(site, df_logger.select_dtypes("number"), c_all, sw)
            liblogger.record_fill_summary(site, mask_c, prov_fill)
            pv = [c for c in df.columns if c in prov_fill.columns]
            uniq = ~df.index.duplicated(keep="first")
            liblogger.plot_sources(site, df.loc[uniq, pv], prov_fill.loc[uniq, pv], c_all.reindex(columns=pv),
                                   "figures/L1_gapfill/" + L0dir + ".png")
        except Exception as e:
            Msg("Comparison / gap-fill plots failed for " + site + ": " + repr(e))

    Msg("## Interpolated values filter at " + site)
    df_lin = ptb.flag_linear_interp_runs(df.copy())

    Msg("## Manual flagging of data at " + site)
    df_out = ptb.flag_data(df_lin.copy(), site)

    Msg("## Adjusting data at " + site)
    # which hours come from CR10X logger files (raw RH wrt water) - see PROMICE_toolbox.SOURCE_CR10X
    ptb.SOURCE_CR10X = ptb.load_source_mask(L0dir, df.index, df.columns, "CR10X")
    # HW1/HW2/HS1/HS2 are never CR10X-sourced any more (dropped and re-filled from C-level above): the CR10X-only sonic
    # correction and installation-offset adjustments below must not fire for them
    if ptb.SOURCE_CR10X is not None:
        for hw_var in ("HW1", "HW2", "HS1", "HS2"):
            if hw_var in ptb.SOURCE_CR10X.columns:
                ptb.SOURCE_CR10X[hw_var] = False
    ptb.SOURCE_CLEVEL = mask_c.reindex(index=df.index, columns=df.columns).fillna(False).astype(bool)
    if sw is None and len(df_logger) > 0:
        # legacy L0M without provenance (LAR1-3, KULU, ...): its logger/C-level origin is unknown, so the legacy conversions
        # (ice_to_water of metadata/adjustments) apply to all its hours, as before the logger-first update
        ptb.SOURCE_CLEVEL.loc[:, :] = True
    ptb.FIRST_CR1000 = first_cr1000
    # we start by adjusting and filtering all variables except surface height
    df_v4 = ptb.adjust_data(df_out.copy(), site, skip_var=["HS1", "HS2"])
    # Applying standard filters again
    df_v4 = df_v4.resample("h").asfreq()
    df_v5 = ptb.filter_data(df_v4, site,
            site_list.loc[site_list.Name == site, "Latitude (°N)"].values[0],
            site_list.loc[site_list.Name == site, "Longitude (°E)"].values[0])

    Msg("## ROC filter at " + site)
    df_roc = ptb.roc_filter_dataframe(df_v5)

    ptb.plot_flagged_data(df_roc, df_out, site)
    df_v5b = ptb.remove_flagged_data(df_roc.copy())

    # correction of the net radiometer for windspeed
    if 'NR' in df_v5.columns:
        df_v5b = ptb.correct_net_rad(df_v5b,site)

    # interpolating short gaps and calculating added variables
    df_v5b = ptb.augment_data(
        df_v5b.copy(),
        site_list.loc[site_list.Name == site, "Latitude (°N)"].values[0],
        site_list.loc[site_list.Name == site, "Longitude (°E)"].values[0],
        site_list.loc[site_list.Name == site, "Elevation (wgs84 m)"].values[0],
        site,
    )

    if df_v5b[[v for v in df_v5b.columns if 'TS' in v]].notnull().any().any():
        df_v6 = ptb.therm_depth(df_v5b, site)
    else:
        df_v6= df_v5b.copy()

    # removing empty rows:
    useful_var_list = [
        "ISWR",  "OSWR", "NR", "TA1", "TA2", "TA3", "TA4",  "RH1", "RH2",
        "P","VW1","VW2"] + ["TS" + str(i) for i in range(1, 11)]
    ind_first = df_v6[
        [v for v in useful_var_list if v in df_v6.columns]
    ].first_valid_index()
    df_v6 = df_v6.loc[ind_first:, :]

    if len(df_v6) > 0:
        # get info related to the new fields
        (
            units,
            display_description,
            database_fields,
            database_fields_data_types,
        ) = ptb.field_info(df_v6.reset_index().columns)

        hourly_attrs = ds_attrs
        hourly_attrs['station_name'] = site
        hourly_attrs['geometry'] = 'POINTZ (%0.4f %0.4f %0.0f)'%(df_v6.longitude.mean(),
                                                                df_v6.latitude.mean(),
                                                                df_v6.elevation.mean())

        hourly_attrs['reference'] = 'Steffen, K.; Vandecrux, B.; Houtz, D.; Abdalati, W.; Bayou, N.; Box, J.E.; Colgan, W.T.; Espona Pernas, L.; Griessinger, N.; Haas-Artho, D.; Heilig, A.; Hubert, A.; Iosifescu Enescu, I.; Johnson-Amin, N.; Karlsson, N.B.; Kurup Buchholz, R.; McGrath, D.; Cullen, N.J.; Naderpour, R.; Molotch, N.P.; Pedersen, A.Ø.; Perren, B.; Philipps, T.; Plattner, G.-K.; Proksch, M.; Revheim, M.K.; Særrelse, M.; Schneebli, M.; Sampson, K.; Starkweather, S.; Steffen, S.; Stroeve, J.; Watler, B.; Winton, Ø.A.; Zwally, J.; Ahlstrøm, A., 2022, "GC-Net Level 1 historical automated weather station data", https://doi.org/10.22008/FK2/VVXGUT, GEUS Dataverse'
        hourly_attrs['doi'] = '10.22008/FK2/VVXGUT'
        hourly_attrs['dataset_description'] = 'Vandecrux, B., Box, J. E., Ahlstrøm, A. P., Andersen, S. B., Bayou, N., Colgan, W. T., Cullen, N. J., Fausto, R. S., Haas-Artho, D., Heilig, A., Houtz, D. A., How, P., Iosifescu Enescu, I., Karlsson, N. B., Kurup Buchholz, R., Mankoff, K. D., McGrath, D., Molotch, N. P., Perren, B., Revheim, M. K., Rutishauser, A., Sampson, K., Schneebeli, M., Starkweather, S., Steffen, S., Weber, J., Wright, P. J., Zwally, H. J., and Steffen, K.: The historical Greenland Climate Network (GC-Net) curated and augmented level-1 dataset, Earth Syst. Sci. Data, 15, 5467–5489, https://doi.org/10.5194/essd-15-5467-2023, 2023. '
        hourly_attrs['averaging'] = 'hourly'

        # build header object
        header_obj = nead.build_header_obj(
            df_v6.reset_index(),
            metadata=hourly_attrs,
            units=units,
            display_description=display_description,
            database_fields=database_fields,
            database_fields_data_types=database_fields_data_types,
        )


        # formatting and saving to file
        df_v6_formatted = df_v6.copy()
        for col in [c for c in df_v6_formatted.columns if c not in ['latitude','longitude', 'elevation','timestamp']]:
            df_v6_formatted[col] = df_v6_formatted[col].map(lambda x: \
                                              '' if np.isnan(x) \
                                                  else '0' if abs(x)<0.005 \
                                                  else '1' if abs(x-1)<0.005 \
                                                  else '%0.2f'%x)

        df_v6_formatted['elevation'] = df_v6_formatted['elevation'].map(lambda x: \
                                          '' if np.isnan(x) else '%0.2f'%x)
        for col in ['latitude','longitude']:
            df_v6_formatted[col] = df_v6_formatted[col].map(lambda x: \
                                              '' if np.isnan(x) else '%0.6f'%x)
        print('writing hourly values')
        nead.write(
            df_v6_formatted.reset_index(),
            header_obj,
            "L1/hourly/" + site.replace(" ", "") + ".csv",
        )

        # daily average
        print('calculating daily averages')
        df_v7 = ptb.daily_average(df_v6)

        daily_attrs = hourly_attrs
        daily_attrs['averaging'] = 'daily'

        # write ini file
        header_obj = nead.build_header_obj(
            df_v7.reset_index(),
            metadata=ds_attrs,
            units=units,
            display_description=display_description,
            database_fields=database_fields,
            database_fields_data_types=database_fields_data_types,
        )

        # formatting and saving to file
        for col in [c for c in df_v7.columns if c not in ['latitude','longitude', 'elevation','timestamp']]:
            df_v7[col] = df_v7[col].map(lambda x: \
                                              '' if np.isnan(x) \
                                                  else '0' if abs(x)<0.005 \
                                                  else '1' if abs(x-1)<0.005 \
                                                  else '%0.2f'%x)

        df_v7['elevation'] = df_v7['elevation'].map(lambda x: \
                                          '' if np.isnan(x) else '%0.2f'%x)
        for col in ['latitude','longitude']:
            df_v7[col] = df_v7[col].map(lambda x: '' if np.isnan(x) else '%0.6f'%x)
        print('writing daily averages')
        nead.write(
            df_v7.reset_index(),
            header_obj,
            "L1/daily/" + site.replace(" ", "") + "_daily.csv",
        )

    # memory: drop the figures and the large per-station objects before the next station. Without this every figure of
    # every station stays alive in pyplot (a few GB over the 22 stations) and the Spyder kernel keeps them after the run.
    plt.close("all")
    for _v in ("df", "ds", "mask_c", "prov_fill", "c_all", "df_v7", "hourly_attrs", "daily_attrs", "header_obj"):
        globals().pop(_v, None)
    gc.collect()

tocgen.processFile("out/Report.md", "out/report_with_toc.md")

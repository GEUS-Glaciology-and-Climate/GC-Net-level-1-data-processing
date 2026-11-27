GC-Net Level 1 automated weather station data

In Memory of Dr. Konrad (Koni) Steffen

Author: B. Vandecrux
Contact: bav@geus.dk
Last update: 2026-11-27 (2026 version of the processing, see "Status" below)

# Citation

Steffen, K.; Vandecrux, B.; Houtz, D.; Abdalati, W.; Bayou, N.; Box, J.; Colgan, L.; Espona Pernas, L.; Griessinger, N.; Haas-Artho, D.; Heilig, A.; Hubert, A.; Iosifescu Enescu, I.; Johnson-Amin, N.; Karlsson, N. B.; Kurup Buchholz, R.; McGrath, D.; Cullen, N.J.; Naderpour, R.; Molotch, N.P.; Pederson, A. Ø.; Perren, B.; Philipps, T.; Plattner, G.K.; Proksch, M.; Revheim, M. K.; Særrelse, M.; Schneebli, M.; Sampson, K.; Starkweather, S.; Steffen, S.; Stroeve, J.; Watler, B.; Winton, Ø. A.; Zwally, J.; Ahlstrøm, A., 2023, "GC-Net Level 1 automated weather station data", https://doi.org/10.22008/FK2/VVXGUT, GEUS Dataverse, V3

as described and processed by:

Vandecrux, B., Box, J. E., Ahlstrøm, A. P., Andersen, S. B., Bayou, N., Colgan, W. T., Cullen, N. J., Fausto, R. S., Haas-Artho, D., Heilig, A., Houtz, D. A., How, P., Iosifescu Enescu, I., Karlsson, N. B., Kurup Buchholz, R., Mankoff, K. D., McGrath, D., Molotch, N. P., Perren, B., Revheim, M. K., Rutishauser, A., Sampson, K., Schneebeli, M., Starkweather, S., Steffen, S., Weber, J., Wright, P. J., Zwally, H. J., and Steffen, K.: The historical Greenland Climate Network (GC-Net) curated and augmented Level 1 dataset, Earth Syst. Sci. Data, https://doi.org/10.5194/essd-15-5467-2023, 2023. 

# Description

The Greenland Climate Network (GC-Net) is a set of Automatic Weather Stations (AWS) set up and managed by the late Prof. Dr. Konrad (Koni) Steffen on the Greenland Ice Sheet (GrIS). This first station, "Swiss Camp" or the "ETH-CU" camp, was initiated in 1990 by A. Ohmura et al. (1991, 1992) with K. Steffen taking over the site from 1995 and expending the network from that year to 31 stations at 30 sites in Greenland (Steffen et al., 1996, 2001). The GC-Net was supported by multiple NASA, NOAA, and NSF grants throughout the years, and then supported by WSL in the later years. These data were previously hosted by the Cooperative Institute for Research in Environmental Sciences (CIRES) in Boulder, Colorado.

Provided in this dataset are the 25 two-level stations from 24 sites on the Greenland ice sheet and 3 experimental stations in Antarctica. The remaining 6 Greenland stations have a different design and will be added once quality checked. Although the GC-Net AWS transmitted their data near-real time through satellite communication, the present dataset is made from the datalogger files retrieved every 1-2 years during maintenance (Level 0). In the 2026 version these logger files are the primary source; the older "C-level" files (the L1 data of the previous releases) only fill the gaps where no logger file exists, and the transmissions (L0) are used after the last logger record.

Full dataset description publication will be forthcoming. The Geological Survey of Denmark and Greenland (GEUS) has undertaken the continuation of multiple GC-Net sites through the Programme for Monitoring of the Greenland Ice Sheet (PROMICE.dk).

The level 1 data is provided in NEAD format, which is a csv file with added metadata header. The format is documented at https://doi.org/10.16904/envidat.187 and a python package is available to read and write NEAD files: https://github.com/GEUS-Glaciology-and-Climate/pyNEAD .

The GC-Net stations measure:

    - Air temperature from four sensors at two heights above the surface 
    - Relative humidity at two heights above the surface
    - Wind speed and direction at two heights above the surface
    - Air pressure
    - Surface height from two sonic sounders
    - Incoming and outgoing shortwave radiation
    - Net radiation (long- and short-wave)*
	- Firn or ice temperatures at 10 levels below the surface

In the L1 dataset, these measurements are cleaned from sensor, station or logger malfunctions, adjusted and/or filtered when and where possible.

Additionally, the L1 dataset contains the following derived variables:

	- Surface height HS1, HS2, HS_combined (continuous: the steps of the sonic sounder heights at boom lifts and reinstallations are removed; HS_combined is the mean of HS1 and HS2 and is interpolated over gaps of 30 days at most)
	- Instrument heights HW1 and HW2 (heights of the two sonic sounders above the surface, with the steps of the boom lifts kept; they are not the heights of the temperature, humidity and wind sensors, which are 0.2 to 1.4 m from them)
	- Inter- or extrapolated temperature, relative humidity and wind speed at respectively 2, 2, and 10 m above the surface
	- Estimated depth of the subsurface temperature measurements (adjusted for snow accumulation, ice ablation and instrument replacement)
	- Interpolated firn or ice temperature at 10 m below the surface
	- Calculated solar an azimuth angles
	- Sensible and latent heat fluxes calculated after Steffen and Demaria (1996)
	- Inter- or extrapolated latitude and longitude based on multi-year GPS measurements (only possible at Swiss Camp, Crawford Point 1, NASA-U, GITS, Tunu-N, DYE-2, JAR1, NASA-E, NASA-SE and Petermann-ELA)

# Status of this folder

The processing described below (2026 version) is documented in release_note_2026.md at the root of the processing repository. The L1 files of this folder were generated with it (built 2026-11-24 to 2026-11-27). The sections "Calibration" and "Known limitations" describe their state.

# How the data are produced (2026 version)

    - L0: the raw datalogger files (CR10X, CR1000, older CR27 files) as retrieved in the field, and the transmissions received after the last logger record.
    - L0M: every logger file is read through its own description file (<file>.toml: columns, calibration factors, periods to ignore, year of the records), calibrated to physical units and stacked, one file per station. No filtering is done there and nothing from the C-level files is added. The file each value comes from is recorded (L0M/provenance).
    - L1: gaps of the logger record are filled with the C-level files (Jason's file, then the per-station file, never mixed value by value; heights only before the first CR1000 record). Then the adjustments of the measurement (sensor swaps, clock errors, instrument heights, a few calibration corrections: metadata/adjustments), the flags of known bad periods (metadata/flags) and the filters (limits, frozen values, spikes) are applied, the derived variables are calculated and the hourly and daily files are written (L1/hourly, L1/daily).
    - A raw file without a description file is not read. Corrections of C-level values are in metadata/c_level_corrections.csv.

# Time stamps, units, flags

    - UTC; the time stamp is the end of the averaging interval (timestamp_meaning = end in the header). A repeated time stamp in a cumulative logger download keeps the most recent file.
    - 30 clock corrections (a day, hours or longer) were made with the reanalysis CARRA (surface pressure for the day, shortwave radiation for the hour; adjustments with the function time_shift, at 10 stations). A residual error of up to a day remains possible where a logger run has no usable pressure or sunlight signal.
    - HW1 is meant to be the lower sonic sounder (at South Dome from 2006-07-20 and at Saddle 2003-2010 the two logger channels are exchanged to give this); periods with HW1 above HW2 that remain are listed in metadata/instrument_height_pair_anomalies.csv of the processing repository.
    - Relative humidity is given with respect to water everywhere and rejected above 105 %. C-level humidity with respect to ice is converted when it fills a gap. RH1/2_wrt_ice_or_water give the form of the raw value.
    - A variable ending in _adj_flag is 1 where an adjustment changed the value (heights, pressure, radiation). Daily values need 18 valid hours.
    - Limits that are enforced include TA3 and TA4 >= -39.5 degC (the probes stop at -39.8 degC), RH 20-105 %, a pressure window per station, and frozen-value filters.

# Calibration: what is documented and what is not

The complete list, station by station, is in metadata/calibration_overview.md of the processing repository (written by tools/calibration_overview.py from the description files and the adjustment tables). The reference tables are in metadata/calibration factors (shortwave factors SWin and SWref, net-radiometer factors, pressure offset, and the LI-COR factor 0.934 of the reflected-shortwave sensor, documented for 2014-2019).

Documented (equal to the tables): incoming shortwave (200 W/m2 per unit at most stations, 62 South Dome, 71.43 NASA-E), outgoing shortwave (the table value times 0.934: 186.8 at the 200-class stations, 71.918 Swiss Camp and NASA-U, 66.08 NASA-E, 67.985 South Dome), the net-radiometer factors and the pressure offset (+400 hPa written by the programs; +600 DYE-2, +300 NEEM), at Swiss Camp, Crawford Point 1, NASA-U, GITS, Humboldt, Summit, Tunu-N, DYE-2, JAR1, Saddle, South Dome, NASA-E, NASA-SE, Petermann ELA and NEEM for most of the logger files. The factor 0.934 is also applied to the years before 2014, where it is not documented (the previous release equals it in the later years). The net-radiometer factors of single files (and a few single-year shortwave factors) were fitted to the C-level overlap and differ from the tables.

Not documented, estimated from the data (each is an estimate of the order of 5-10 % in the radiation, not a sensor calibration; the evidence is in metadata/calibration_overview.md, section E):
    - NASA-U: incoming shortwave x1.15 from 2018-05-22 (new radiometers installed, scale not recorded); outgoing shortwave x2.762 (scale 198.64) from 2003 and a scale of 182 in 1997-99, without which the summer albedo is 0.30.
    - Petermann Glacier 2002-2006: 73.5 for both shortwave sensors (the logger scales and the C-level file gave values 2.3 times those of CARRA).
    - Crawford Point 1: incoming shortwave x1.139 (2005 to 2010-05-09) and x1.105 (after); Swiss Camp: outgoing shortwave x1.055 (1995-97) and x0.926 (from 2012-05-10). They keep the April-May albedo of dry snow at its value of the best documented years (Crawford Point 1 0.83 in 1995-2004, Swiss Camp 0.81 in 1998-2012; the dry-snow stations of the network are at 0.82-0.86 in spring). The albedo of these two stations is therefore a result of this choice and cannot be used to detect a trend.
    - Crawford Point 1 and Swiss Camp: the two shortwave channels are swapped from 2012 (not reported, found with the albedo); the 0.934 moves with the sensor.
    - LAR1 (Antarctica): outgoing shortwave x1.285 from 2011-11-15 (albedo 0.90 to 0.70 at a service with unchanged incoming radiation; no independent reference).
    - Stations without any table (Aurora, CP2, JAR2, JAR3, NGRIP, Petermann Glacier, KAR, Swiss Camp 10 m): the factors are those of the logger program headers or of the C-level files.
    - Pressure: Crawford Point 1 (1999-2010) and JAR3 (from 2002) read about half of the true amplitude (corrected by a fit to CARRA); Summit from 2016-05-22 (a CS106 sensor read with CS105 constants); NASA-U offsets (issue 46).
    - Independent checks used: CARRA surface shortwave radiation (not assimilated), CARRA surface pressure (assimilated: it dates but does not validate), neighbouring stations and the previous release.

# Known limitations

    - Some station-years remain inconsistent with the dry-snow albedo or with CARRA and are not corrected: Swiss Camp spring 2019, Crawford Point 1 summers after 2005 (albedo about 0.79 after the adjustment), NASA-U 1995-2001, Swiss Camp 10 m since 2014.
    - Humidity in 1999-2008 is 3-10 % higher than in the previous release at several stations (the C-level values carry a temperature-dependent offset that the logger values do not have).
    - The net radiation of LAR2 and LAR3 has the wrong sign.
    - HW1 and HW2 are derived from sonic sounder readings that sit on a separate boom, plus the station geometry and the maintenance shifts. The offset between the sonic reading and the anemometer height is not applied in the same way at all stations (e.g. at DYE-2 HW equals the sonic reading, the anemometers being about 0.5 m higher). The surface height is not affected.
    - In some periods HW1 is not the lower of the two levels or the distance between them is not that of the station (about 1.0-1.4 m): Crawford Point 1 2010-2012, NGRIP 2003, JAR1 2009-2010, JAR2 2005 and 2011, Petermann ELA 2013-2017, Swiss Camp 2002-2008 and 2021-2022. Where one height series is a copy of the other (JAR1 2002-03 and 2010, JAR2 2001-2005, Petermann ELA 2003 and 2007, Swiss Camp 2003, Petermann Glacier 2002-2006, KULU 1999-2000) it is removed.
    - HS_combined has gaps wherever both sonic sounders are missing for more than 30 days (the previous release interpolated over every gap).
    - Open questions are listed in section 8 of release_note_2026.md; the comparison with the previous release in its section 7.

Important links:

- The level 1 processing scripts and discussion page for Q&A and issue reporting (under "issues" tab) is available at: https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing

- The level 0 data (from which the L1 data was built from) is available at: https://www.doi.org/10.16904/envidat.1.

- The compilation of handheld GPS coordinates for each site and for multiple years is available here:  Vandecrux, B. and Box, J.E.: GC-Net AWS observed and estimated positions (Version v1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7729070, 2023c.

- The compilation of field pictures is available at: Box, J.E., Vandecrux, B., Houtz, D., Steffen, K.: GC-Net historical photo archive, https://geusgitlab.geus.dk/glaciology-and-climate/promice/historical_GC-Net_photos, 2023b

- The compilation of useful metadata (reports, field notes...) is available at: Vandecrux, B., Houtz, D., Box, J.E.: GC-Net historical metadata compilation [Data set]. Zenodo, https://doi.org/10.5281/zenodo.7829106, 2023b.

Acknowledgments
In addition to the support from several past NASA and NSF grants awarded to K. Steffen (grant nr. NAPW-2158, NAG51-1612, NAG5-10600, NAG5-10857, NNG06GB08G, OPP-9423530), financial support of the 2020 transition came from the DANCEA (Danish Cooperation for Environment in the Arctic) under the Danish Ministry of Energy, Buildings and Climate. The Danish Finance Law currently supports the GC-Net field and data activities. We acknowledge the key contributions from all the people that have participated in the GC-Net project, assisted Konrad Steffen through the years and contributed to the longevity of GC-Net. In particular, we acknowledge (in alphabetical order) the support from Robin Abbott, Waleed Abdalati, Todd Albert, Kate Daniels, Lucia Espona Pernas, Nena Griessinger, Alain Hubert, Russell Huff, Nighat Johnson-Amin, Mike MacFerrin, Molly McCallister, Reza Naderpour, Atsumu Ohmura, Allan Ø. Pedersen, Thomas, Philipps, Gian-Kasper Plattner, Kim Petersen, Martin Proksch, Christian Schneeberger, Christopher Shields, Martina Særrelse, Julienne Stroeve, Benjamin Walter, Øyvind A. Winton and many others.


References:

Ohmura, A., Steffen.K., Blatter, H., Greuell, W., Rotach.M., Konzelmann,T., Laternser.M., Abe-Ouchi, A. and Steiger, D. (1991) Energy and mass balance during the melt season at the equilibrium line altitude, Paakitsoq, Greenland ice sheet. ETH Greenland Expedition Prog. Report no. 1, Dept of Geography, Swiss Fed. Inst, of Technol., Zurich.

Ohmura, A., Steffen, K., Blatter, H., Greuell, W., Rotach.M., Konzelmann,T., Forrer, J., Abe-Ouchi, A., Steiger.D., Stober, M. and Niederbàumer, G. (1992) Energy and mass balance during the melt season at the equilibrium line altitude, Paakitsoq, Greenland ice sheet. ETH Greenland Expedition Prog. Report no. 2, Dept of Geography, Swiss Fed. Inst, of Technol., Zurich.

Steffen, K., & deMaria, T. (1996). Surface Energy Fluxes of Arctic Winter Sea Ice in Barrow Strait, Journal of Applied Meteorology and Climatology, 35(11), 2067-2079. Retrieved Feb 15, 2023, https://doi.org/10.1175/1520-0450(1996)035<2067:SEFOAW>2.0.CO;2

Steffen, K., Box, J.E. and Abdalati, W., 1996. Greenland climate network: GC-Net. US Army Cold Regions Reattach and Engineering (CRREL), CRREL Special Report, pp.98-103.

Steffen, K., and Box, J. (2001), Surface climatology of the Greenland Ice Sheet: Greenland Climate Network 1995–1999, J. Geophys. Res., 106( D24), 33951– 33964, doi:10.1029/2001JD900161. 

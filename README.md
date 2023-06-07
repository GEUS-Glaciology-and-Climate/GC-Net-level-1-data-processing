[![License: GPL v2](https://img.shields.io/badge/License-GPL_v2-blue.svg)](https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues-raw/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing)](https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing/issues)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing)](https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing/releases/)
[![](<https://img.shields.io/badge/Dataverse DOI-10.22008/FK2/VVXGUT-orange>)](https://doi.org/10.22008/FK2/VVXGUT)

# The GC-Net level 1 dataset and processing scripts

## In Memory of Dr. Konrad (Koni) Steffen

This repository contains scripts used to clean, adjust and interpolate GC-Net data.

- [Overview of the L0 data](out/L0_overview_toc.md)
- [Overview of the L1 data](out/L1_overview_toc.md)
- [Overview of the L1 data availability](out/L1_overview/data_availability.png)
- [Overview of the L1 air temperature](out/L1_air_temperature_overview_toc.md)
- Overview of the surface height data for the [accumulation sites](figures/L1_overview/HS_overview_accum.png) and for the [ablation sites](figures/L1_overview/HS_overview_abl.png)
- [Report of the data treatment](out/report_with_toc.md)
- [Air temperature diagnostic](out/L1_air_temperature_diagnostic_toc.md)
- [Instrument height assessment](out/L1_intrument_heights_toc.md)

## Dataset and processing overview
[![image](https://user-images.githubusercontent.com/35140661/211565684-4101ca83-4440-4610-b9a5-621eda120ed5.png)](https://docs.google.com/presentation/d/1p9Z7g7ZOYZ3aiXRJMUF1gz6hb4260d0f4XUG64YiP4Y/edit?usp=sharing)

## Usage

The last processing of the L1 dataset is available in the [L1 folder](L1).

The last stable release is available at:

Steffen, K.; Vandecrux, B.; Houtz, D.; Abdalati, W.; Bayou, N.; Box, J.; Colgan, L.; Espona Pernas, L.; Griessinger, N.; Haas-Artho, D.; Heilig, A.; Hubert, A.; Iosifescu Enescu, I.; Johnson-Amin, N.; Karlsson, N. B.; Kurup, R.; McGrath, D.; Naderpour, R.; Pederson, A. Ø.; Perren, B.; Philipps, T.; Plattner, G.K.; Proksch, M.; Revheim, M. K.; Særrelse, M.; Schneebli, M.; Sampson, K.; Starkweather, S.; Steffen, S.; Stroeve, J.; Watler, B.; Winton, Ø. A.; Zwally, J.; Ahlstrøm, A., 2023, "GC-Net Level 1 automated weather station data", https://doi.org/10.22008/FK2/VVXGUT, GEUS Dataverse, V2
When using the L0 data please cite:

When using the L1 data please additionally cite:

Vandecrux, B., Box, J. E., Ahlstrøm, A. P., Andersen, S. B., Bayou, N., Colgan, W. T., Cullen, N. J., Fausto, R. S., Haas-Artho, D., Heilig, A., Houtz, D. A., How, P., Iosifescu Enescu, I., Karlsson, N. B., Kurup Buchholz, R., Mankoff, K. D., McGrath, D., Molotch, N. P., Perren, B., Revheim, M. K., Rutishauser, A., Sampson, K., Schneebeli, M., Starkweather, S., Steffen, S., Weber, J., Wright, P. J., Zwally, H. J., and Steffen, K.: The historical Greenland Climate Network (GC-Net) curated and augmented Level 1 dataset, Earth Syst. Sci. Data Discuss. [preprint], https://doi.org/10.5194/essd-2023-147, in review, 2023. 

## Dataset decription

A complete description of the GC-Net history and instrumentation is available at https://doi.org/10.5194/essd-2023-147.

### Background
Starting with a single station in 1991, the Greenland Climate Network (commonly known as GC-Net) is a set of Automatic Weather Stations (AWS) set up and managed by the late Prof. Dr. Konrad (Koni) Steffen, and spanning the Greenland Ice Sheet (GrIS). This first station was "Swiss Camp" or the "ETH-CU" camp (GC-Net station #01) which was used as a field science and education site by Koni for years. The GC-Net was expanded with multiple NASA, NOAA, and NSF grants throughout the years, and then supported by WSL in the later years. These data (see "C-file" below) were previously hosted by the Cooperative Institute for Research in Environmental Sciences (CIRES) in Boulder, Colorado. 

### Overview 
Provided in this dataset are the 16 longest running stations in the network, which are spread over a significant area of the GrIS and the majority of the unique climatic zones. From the South Dome high point in the South, to the Western Jakobshavn ablation region in the west, to the Petermann glacier in the North across east of the Northeast Greenland Ice Stream to the east, GC-Net is the longest running climatological record of Greenland. 

### The standard GC-Net station consists of: 
* Air temperature measurements at 2 heights above the surface
* Relative humidity measurements at 2 heights above the surface
* Wind speed and direction measured at 2 heights above the surface
* Sonic distance sounder measurements for 2 snow height and distance of instruments to surface
* Incoming shortwave radiation measurement
* Reflected shortwave radiation measurement
* Net broadband radiation (long- and short-wave) measurement
* Air pressure measurement

Data have often been repatriated in near-real time using one of either the GOES geostationary satellite or the ARGOS polar orbiting satellite transmission system. The stations were visited typically every 1-2 years for maintenance and service, and to download full uncorrupted data directly from the dataloggers. GC-Net stations were visited by Twin Otter equipped with snow skids to land directly on the open-ice at the AWS locations, or by helicopter near the west coast. The AWSs operate on solar and battery power and occasionally lost power during the dark and cold winter months, particularly when the batteries were aging. 

### Dataset 
This dataset consists of 2 main data levels; Level 0 and Level 1. 
Level 0 is the raw data from the dataloggers, historical processing codes, satellite transmissions, and Koni’s personal data archive. Level 0 data (.zip) directories contain subdirectories: 

* “C file” - contains the historical processed datafile for each station.

* “Campbell logger files” - contains the raw csv datafiles from the stations’ Campbell Scientific dataloggers since the CR1000 era (~2007-2008 for most stations).

* “Photos” - contains photographs of the station when available marked by year.

Level 1 is the appended, calibrated, cleaned, and quality flagged data. The full processing scheme is open-source and publicly available.

The latest version of the data can also be pulled from this repository. Level 1 data is provided in the newly described csv-compatible NEAD format (https://www.envidat.ch/#/metadata/nead).

### Additional Details
Dataset description publication will be forthcoming. 
The Geological Survey of Denmark and Greenland (GEUS) has been imperative in the reprocessing and continuity mission of GC-Net. Multiple GC-Net stations have been replaced with updated and upgraded AWS hardware at the same coordinates by GEUS. This effort will ensure continuity of the GC-Net dataset into the future.  


## Data treatment overview

![image](https://user-images.githubusercontent.com/35140661/173344278-09b6a34e-cf0f-4f9c-af9a-5a109b51101a.png)

## Installation
If you want to use this code you will need (among others) the [pyNEAD](https://github.com/GEUS-PROMICE/pyNEAD) library.

```
pip install git+https://github.com/GEUS-PROMICE/pyNEAD.git

```

GC-Net Level 1 automated weather station data

In Memory of Dr. Konrad (Koni) Steffen

Contact: bav@geus.dk

# Citation

The data:

Steffen, K.; Vandecrux, B.; Houtz, D.; Abdalati, W.; Bayou, N.; Box, J.; Colgan, L.; Espona Pernas, L.; Griessinger, N.; Haas-Artho, D.; Heilig, A.; Hubert, A.; Iosifescu Enescu, I.; Johnson-Amin, N.; Karlsson, N. B.; Kurup, R.; McGrath, D.; Naderpour, R.; Pederson, A. Ø.; Perren, B.; Philipps, T.; Plattner, G.K.; Proksch, M.; Revheim, M. K.; Særrelse, M.; Schneebli, M.; Sampson, K.; Starkweather, S.; Steffen, S.; Stroeve, J.; Watler, B.; Winton, Ø. A.; Zwally, J.; Ahlstrøm, A., 2023, "GC-Net Level 1 automated weather station data", https://doi.org/10.22008/FK2/VVXGUT, GEUS Dataverse, V2

as processed by:

Vandecrux, B., Box, J., Houtz, D., & Revheim, M. K. The GC-Net level 1 dataset and processing scripts (Version 1) [Computer software]. https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing

# Description

The Greenland Climate Network (GC-Net) is a set of Automatic Weather Stations (AWS) set up and managed by the late Prof. Dr. Konrad (Koni) Steffen, and spanning the Greenland Ice Sheet (GrIS). This first station, "Swiss Camp" or the "ETH-CU" camp, was initiated in 1990 by A. Ohmura et al. (1991, 1992) with K. Steffen taking over the site from 1995 and expending the network to 29 sites in Greenland (Steffen et al., 1996, 2001) and 3 sites in Antarctica. The GC-Net was supported by multiple NASA, NOAA, and NSF grants throughout the years, and then supported by WSL in the later years. These data were previously hosted by the Cooperative Institute for Research in Environmental Sciences (CIRES) in Boulder, Colorado.

Provided in this dataset are the 25 two-level stations from 24 sites on the Greenland ice sheet and 3 in Antarctica. The remaining 5 stations of a different design will be added once quality checked. Although the GC-Net AWS transmitted their data near-real thourgh the ARGOES/GOES satellitestransmission system, the present dataset was made from uncorrupted datalogger files, retrieved every 1-2 years during maintenance.

Full dataset description publication will be forthcoming. The Geological Survey of Denmark and Greenland (GEUS) has been imperative in the reprocessing and continuity mission of GC-Net. Multiple GC-Net stations have been replaced with updated and upgraded AWS hardware at the same coordinates by GEUS. This effort will ensure continuity of the GC-Net dataset into the future.
(2020-07-01) 

The level 1 data is provided in the newly described csv-compatible NEAD format, which is a csv with added metadata header. The format is documented at https://doi.org/10.16904/envidat.187 and a python package is available to  read-write NEAD files: https://github.com/GEUS-Glaciology-and-Climate/pyNEAD .

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

	- Surface height (corrected from the shifts in sonic sounder height)
	- Instrument heights (derived from sonic sounder height and station geometry)
	- Inter- or extrapolated temperature, relative humidity and wind speed at respectively 2, 2, and 10 m above the surface
	- Estimated depth of the subsurface temperature measurements (adjusted for snow accumulation, ice ablation and instrument replacement)
	- Interpolated firn or ice temperature at 10 m below the surface
	- Calculated solar an azimuth angles
	- Sensible and latent heat fluxes calculated after Steffen and Demaria (1996)

Important links:

- The level 1 processing scripts and discussion page for Q&A and issue reporting (under "issues" tab) is available at:

Vandecrux, B., Box, J., Houtz, D., & Revheim, M. K. The GC-Net level 1 dataset and processing scripts (Version 1) [Computer software]. https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing

- The level 0 data (from which the L1 data was built from) is available at:

Steffen (†), K.; Houtz, D.; Vandecrux, B.; Abdalati, W.; Bayou, N.; Box, J.; Colgan, W.; Espona Pernas, L.; Griessinger, N.; Haas-Artho, D.; Heilig, A.; Hubert, A.; Iosifescu Enescu, I.; Johnson-Amin, N.; Karlsson, N. B.; Kurup, R.; McGrath, D.; Naderpour, R.; Pederson, A. Ø.; Perren, B.; Phillips, T.; Plattner, G.; Proksch, M.; Revheim, M. K.; Saettele, M.; Schneebeli, M.; Sampson, K.; Starkweather, S.; Steffen, S.; Stroeve, J.; Walter, B.; Winton, Ø. A.; Zwally, J. et al. Greenland Climate Network (GC-Net) Data. EnviDat 2020, https://www.doi.org/10.16904/envidat.1.

References:

Ohmura, A., Steffen.K., Blatter, H., Greuell, W., Rotach.M., Konzelmann,T., Laternser.M., Abe-Ouchi, A. and Steiger, D. (1991) Energy and mass balance during the melt season at the equilibrium line altitude, Paakitsoq, Greenland ice sheet. ETH Greenland Expedition Prog. Report no. 1, Dept of Geography, Swiss Fed. Inst, of Technol., Zurich.

Ohmura, A., Steffen, K., Blatter, H., Greuell, W., Rotach.M., Konzelmann,T., Forrer, J., Abe-Ouchi, A., Steiger.D., Stober, M. and Niederbàumer, G. (1992) Energy and mass balance during the melt season at the equilibrium line altitude, Paakitsoq, Greenland ice sheet. ETH Greenland Expedition Prog. Report no. 2, Dept of Geography, Swiss Fed. Inst, of Technol., Zurich.

Steffen, K., & deMaria, T. (1996). Surface Energy Fluxes of Arctic Winter Sea Ice in Barrow Strait, Journal of Applied Meteorology and Climatology, 35(11), 2067-2079. Retrieved Feb 15, 2023, https://doi.org/10.1175/1520-0450(1996)035<2067:SEFOAW>2.0.CO;2

Steffen, K., and Box, J. (2001), Surface climatology of the Greenland Ice Sheet: Greenland Climate Network 1995–1999, J. Geophys. Res., 106( D24), 33951– 33964, doi:10.1029/2001JD900161. 

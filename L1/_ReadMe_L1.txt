GC-Net Level 1 automated weather station data

In Memory of Dr. Konrad (Koni) Steffen

Author: B. Vandecrux
Contact: bav@geus.dk
Last update: 23-02-2023

# Citation

Steffen, K.; Vandecrux, B.; Houtz, D.; Abdalati, W.; Bayou, N.; Box, J.; Colgan, L.; Espona Pernas, L.; Griessinger, N.; Haas-Artho, D.; Heilig, A.; Hubert, A.; Iosifescu Enescu, I.; Johnson-Amin, N.; Karlsson, N. B.; Kurup Buchholz, R.; McGrath, D.; Cullen, N.J.; Naderpour, R.; Molotch, N.P.; Pederson, A. Ø.; Perren, B.; Philipps, T.; Plattner, G.K.; Proksch, M.; Revheim, M. K.; Særrelse, M.; Schneebli, M.; Sampson, K.; Starkweather, S.; Steffen, S.; Stroeve, J.; Watler, B.; Winton, Ø. A.; Zwally, J.; Ahlstrøm, A., 2023, "GC-Net Level 1 automated weather station data", https://doi.org/10.22008/FK2/VVXGUT, GEUS Dataverse, V3

as processed by:

Vandecrux, B., Box, J., Houtz, D., & Revheim, M. K. The GC-Net level 1 dataset and processing scripts (Version 1) [Computer software]. https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing

# Description

The Greenland Climate Network (GC-Net) is a set of Automatic Weather Stations (AWS) set up and managed by the late Prof. Dr. Konrad (Koni) Steffen on the Greenland Ice Sheet (GrIS). This first station, "Swiss Camp" or the "ETH-CU" camp, was initiated in 1990 by A. Ohmura et al. (1991, 1992) with K. Steffen taking over the site from 1995 and expending the network from that year to 31 stations at 30 sites in Greenland (Steffen et al., 1996, 2001). The GC-Net was supported by multiple NASA, NOAA, and NSF grants throughout the years, and then supported by WSL in the later years. These data were previously hosted by the Cooperative Institute for Research in Environmental Sciences (CIRES) in Boulder, Colorado.

Provided in this dataset are the 25 two-level stations from 24 sites on the Greenland ice sheet and 3 experimental stations in Antarctica. The remaining 6 Greenland stations have a different design and will be added once quality checked. Although the GC-Net AWS transmitted their data near-real time through satellite communication, the present dataset was made from uncorrupted datalogger files, retrieved every 1-2 years during maintenance.

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

	- Surface height (corrected from the shifts in sonic sounder height)
	- Instrument heights (derived from sonic sounder height and station geometry)
	- Inter- or extrapolated temperature, relative humidity and wind speed at respectively 2, 2, and 10 m above the surface
	- Estimated depth of the subsurface temperature measurements (adjusted for snow accumulation, ice ablation and instrument replacement)
	- Interpolated firn or ice temperature at 10 m below the surface
	- Calculated solar an azimuth angles
	- Sensible and latent heat fluxes calculated after Steffen and Demaria (1996)
	- Inter- or extrapolated latitude and longitude based on multi-year GPS measurements (only possible at Swiss Camp, Crawford Point 1, NASA-U, GITS, Tunu-N, DYE-2, JAR1, NASA-E, NASA-SE and Petermann-ELA)

Important links:

- The level 1 processing scripts and discussion page for Q&A and issue reporting (under "issues" tab) is available at: https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing

- The level 0 data (from which the L1 data was built from) is available at: https://www.doi.org/10.16904/envidat.1.

- The compilation of handheld GPS coordinates for each site and for multiple years is available here:  Vandecrux, B. and Box, J.E.: GC-Net AWS observed and estimated positions (Version v1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7729070, 2023c.

- The compilation of field pictures is available at: Box, J.E., Vandecrux, B., Houtz, D., Steffen, K.: GC-Net historical photo archive, https://geusgitlab.geus.dk/glaciology-and-climate/promice/historical_GC-Net_photos, 2023b

- The compilaiton of useful metadata (reports, field notes...) is available at: Vandecrux, B., Houtz, D., Box, J.E.: GC-Net historical metadata compilation [Data set]. Zenodo, https://doi.org/10.5281/zenodo.7728549, 2023b.

Acknowledgments
In addition to the support from several past NASA and NSF grants awarded to K. Steffen (grant nr. NAPW-2158, NAG51-1612, NAG5-10600, NAG5-10857, NNG06GB08G, OPP-9423530), financial support of the 2020 transition came from the DANCEA (Danish Cooperation for Environment in the Arctic) under the Danish Ministry of Energy, Buildings and Climate. The Danish Finance Law currently supports the GC-Net field and data activities. We acknowledge the key contributions from all the people that have participated in the GC-Net project, assisted Konrad Steffen through the years and contributed to the longevity of GC-Net. In particular, we acknowledge (in alphabetical order) the support from Robin Abbott, Waleed Abdalati, Todd Albert, Kate Daniels, Lucia Espona Pernas, Nena Griessinger, Alain Hubert, Russell Huff, Nighat Johnson-Amin, Mike MacFerrin, Molly McCallister, Reza Naderpour, Atsumu Ohmura, Allan Ø. Pedersen, Thomas, Philipps, Gian-Kasper Plattner, Kim Petersen, Martin Proksch, Christian Schneeberger, Christopher Shields, Martina Særrelse, Julienne Stroeve, Benjamin Walter, Øyvind A. Winton and many others.


References:

Ohmura, A., Steffen.K., Blatter, H., Greuell, W., Rotach.M., Konzelmann,T., Laternser.M., Abe-Ouchi, A. and Steiger, D. (1991) Energy and mass balance during the melt season at the equilibrium line altitude, Paakitsoq, Greenland ice sheet. ETH Greenland Expedition Prog. Report no. 1, Dept of Geography, Swiss Fed. Inst, of Technol., Zurich.

Ohmura, A., Steffen, K., Blatter, H., Greuell, W., Rotach.M., Konzelmann,T., Forrer, J., Abe-Ouchi, A., Steiger.D., Stober, M. and Niederbàumer, G. (1992) Energy and mass balance during the melt season at the equilibrium line altitude, Paakitsoq, Greenland ice sheet. ETH Greenland Expedition Prog. Report no. 2, Dept of Geography, Swiss Fed. Inst, of Technol., Zurich.

Steffen, K., & deMaria, T. (1996). Surface Energy Fluxes of Arctic Winter Sea Ice in Barrow Strait, Journal of Applied Meteorology and Climatology, 35(11), 2067-2079. Retrieved Feb 15, 2023, https://doi.org/10.1175/1520-0450(1996)035<2067:SEFOAW>2.0.CO;2

Steffen, K., Box, J.E. and Abdalati, W., 1996. Greenland climate network: GC-Net. US Army Cold Regions Reattach and Engineering (CRREL), CRREL Special Report, pp.98-103.

Steffen, K., and Box, J. (2001), Surface climatology of the Greenland Ice Sheet: Greenland Climate Network 1995–1999, J. Geophys. Res., 106( D24), 33951– 33964, doi:10.1029/2001JD900161. 

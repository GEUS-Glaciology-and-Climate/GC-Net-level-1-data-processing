* [6 Summit](#s1)
  * [Interpolated values filter at Summit](#s1-1)
  * [Manual flagging of data at Summit](#s1-2)
  * [Adjusting data at Summit](#s1-3)
  * [ROC filter at Summit](#s1-4)
# <a id='s1' />6 Summit
## <a id='s1-1' />Interpolated values filter at Summit
ISWR: 210 samples flagged
OSWR: 186 samples flagged
NR: 406 samples flagged
TA1: 3750 samples flagged
TA2: 3417 samples flagged
TA3: 1326 samples flagged
TA4: 1784 samples flagged
RH1: 2035 samples flagged
RH2: 2029 samples flagged
VW1: 9017 samples flagged
VW2: 8183 samples flagged
DW1: 808 samples flagged
DW2: 915 samples flagged
P: 5009 samples flagged
TA5: 19 samples flagged
TS1: 1452 samples flagged
TS2: 1034 samples flagged
TS3: 1075 samples flagged
TS4: 1063 samples flagged
TS5: 1010 samples flagged
TS6: 1075 samples flagged
TS7: 909 samples flagged
TS8: 950 samples flagged
TS9: 995 samples flagged
TS10: 1019 samples flagged
## <a id='s1-2' />Manual flagging of data at Summit
Flagging data:
|start time|end time|variable|
|-|-|-|
|1997-05-21 00:00:00+00:00|1998-07-01 00:00:00+00:00|TA3|
|2017-11-17 00:00:00+00:00|2018-02-23 00:00:00+00:00|HW1|
|2018-11-10 00:00:00+00:00|2019-06-09 00:00:00+00:00|HW1|
|2017-12-17 00:00:00+00:00|2018-02-19 00:00:00+00:00|HW2|
|2018-11-20 00:00:00+00:00|2019-04-09 00:00:00+00:00|HW2|
|1998-11-11 00:00:00+00:00|1999-04-01 00:00:00+00:00|HW1|
|1998-11-11 00:00:00+00:00|1999-04-01 00:00:00+00:00|HW2|
|2019-01-10 00:00:00+00:00|2025-01-01 00:00:00+00:00|DW2|
|2010-05-18 00:00:00+00:00|2025-01-01 00:00:00+00:00|TS1|
|2010-05-18 00:00:00+00:00|2025-01-01 00:00:00+00:00|TS2|
|2010-05-18 00:00:00+00:00|2025-01-01 00:00:00+00:00|TS3|
|2010-05-18 00:00:00+00:00|2025-01-01 00:00:00+00:00|TS4|
|2010-05-18 00:00:00+00:00|2025-01-01 00:00:00+00:00|TS5|
|2010-05-18 00:00:00+00:00|2025-01-01 00:00:00+00:00|TS6|
|2010-05-18 00:00:00+00:00|2025-01-01 00:00:00+00:00|TS7|
|2010-05-18 00:00:00+00:00|2025-01-01 00:00:00+00:00|TS8|
|2010-05-18 00:00:00+00:00|2025-01-01 00:00:00+00:00|TS9|
|2010-05-18 00:00:00+00:00|2025-01-01 00:00:00+00:00|TS10|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS1|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS2|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS3|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS4|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS5|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS6|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS7|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS8|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS9|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS10|
## <a id='s1-3' />Adjusting data at Summit

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2001-06-15 16:00:00+00:00|2003-12-13 17:00:00+00:00|HW1|add|0.78|0|
|2003-12-13 17:05:00+00:00|2005-05-04 19:00:00+00:00|HW1|add|0.37|0|
|2004-12-13 17:05:00+00:00|2005-07-04 19:00:00+00:00|HW1|min_filter|-4.0|0|
|2005-05-26 07:00:00+00:00|2008-09-13 01:05:00+00:00|HW1|add|0.72|0|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW1|hampel_filter|1.0|2876|
|2009-05-15 00:00:00+00:00|2022-11-05 01:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2022-11-05 01:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|13913|
|2009-05-15 00:00:00+00:00|2022-11-05 01:00:00+00:00|HW1|hampel_filter|2.0|8334|
|2009-05-19 19:00:00+00:00|2010-08-06 23:05:00+00:00|HW1|add|-0.39|0|
|2010-08-16 19:00:00+00:00|2022-11-05 01:00:00+00:00|HW1|add|-0.4|0|
|2001-06-15 16:00:00+00:00|2003-12-13 17:00:00+00:00|HW2|add|0.62|0|
|2003-12-13 17:05:00+00:00|2004-03-02 16:05:00+00:00|HW2|add|0.84|0|
|2004-08-19 17:05:00+00:00|2005-05-04 21:00:00+00:00|HW2|add|0.84|0|
|2005-05-26 07:00:00+00:00|2010-08-06 23:05:00+00:00|HW2|add|0.39|0|
|2005-10-08 15:00:00+00:00|2006-03-17 14:05:00+00:00|HW2|add|0.87|0|
|2007-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW2|hampel_filter|1.0|5736|
|2009-05-15 00:00:00+00:00|2022-11-05 01:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2022-11-05 01:00:00+00:00|HW2|biweekly_upper_range_filter|0.3|27986|
|2009-05-15 00:00:00+00:00|2022-11-05 01:00:00+00:00|HW2|hampel_filter|2.0|4306|
|2009-05-19 19:00:00+00:00|2010-08-06 23:05:00+00:00|HW2|add|-0.39|0|
|2010-08-16 19:00:00+00:00|2022-11-05 01:00:00+00:00|HW2|add|0.3|0|
|2009-05-19 00:00:00+00:00|2022-11-05 01:00:00+00:00|OSWR|multiply|0.91|0|
|2016-05-22 00:00:00+00:00|2022-11-05 01:00:00+00:00|P|add|-600.0|0|
|2016-05-22 00:00:00+00:00|2022-11-05 01:00:00+00:00|P|multiply|1.3043|0|
|2016-05-22 00:00:00+00:00|2022-11-05 01:00:00+00:00|P|add|500.0|0|
|2018-05-15 00:00:00+00:00|2022-11-05 01:00:00+00:00|RH1|swap_with_RH2|0.0|0|
|1996-01-01 00:00:00+00:00|2009-05-19 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1996-01-01 00:00:00+00:00|2009-05-19 00:00:00+00:00|RH2|ice_to_water|0.0|0|
## <a id='s1-4' />ROC filter at Summit
 
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_ISWR.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_OSWR.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_NR.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TA1.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TA2.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TA3.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TA4.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_RH1.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_RH2.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_VW1.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_VW2.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_DW1.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_DW2.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_P.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_HW1.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_HW2.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_V.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TA5.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TS1.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TS2.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TS3.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TS4.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TS5.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TS6.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TS7.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TS8.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TS9.jpeg)
![Adjusted and flagged data at Summit](figures/L1_data_treatment/Summit_TS10.jpeg)
 

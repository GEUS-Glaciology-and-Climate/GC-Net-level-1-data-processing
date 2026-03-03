# 0 Swiss Camp 10m
## Interpolated values filter at Swiss Camp 10m
ISWR: 3 samples flagged
OSWR: 3 samples flagged
NR: 4 samples flagged
TA1: 197 samples flagged
TA3: 7 samples flagged
RH1: 260 samples flagged
RH2: 245 samples flagged
VW1: 3 samples flagged
VW2: 10 samples flagged
DW1: 9 samples flagged
DW2: 35 samples flagged
P: 1013 samples flagged
## Manual flagging of data at Swiss Camp 10m
Flagging data:
|start time|end time|variable|
|-|-|-|
|1997-05-22 00:00:00+00:00|1998-05-22 00:00:00+00:00|OSWR|
|2001-06-03 00:00:00+00:00|2002-05-11 00:00:00+00:00|ISWR|
|2001-06-03 00:00:00+00:00|2002-05-11 00:00:00+00:00|OSWR|
|2001-06-03 00:00:00+00:00|2002-05-11 00:00:00+00:00|TA1|
|2001-06-03 00:00:00+00:00|2002-05-11 00:00:00+00:00|TA2|
|2001-06-03 00:00:00+00:00|2002-05-11 00:00:00+00:00|DW1|
|2001-06-03 00:00:00+00:00|2002-05-11 00:00:00+00:00|DW2|
|2011-01-01 00:00:00+00:00|2012-12-31 00:00:00+00:00|DW2|
|2001-06-03 00:00:00+00:00|2002-05-11 00:00:00+00:00|VW1|
|2001-06-03 00:00:00+00:00|2002-05-11 00:00:00+00:00|RH1|
|2001-06-03 00:00:00+00:00|2002-05-11 00:00:00+00:00|RH2|
|2005-02-04 00:00:00+00:00|2005-05-15 00:00:00+00:00|RH1|
|2016-05-01 00:00:00+00:00|2017-06-01 00:00:00+00:00|OSWR|
|2015-05-15 00:00:00+00:00|2016-05-15 00:00:00+00:00|TA3|
|2015-05-15 00:00:00+00:00|2016-05-15 00:00:00+00:00|TA1|
|2018-02-15 00:00:00+00:00|2018-05-05 00:00:00+00:00|P|
|2017-08-21 00:00:00+00:00|2018-05-05 00:00:00+00:00|HW2|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|TA1|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|TA2|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|TA3|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|TA4|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|RH1|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|RH2|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|VW1|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|VW2|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|DW1|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|DW2|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|ISWR|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|OSWR|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|NR|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|HW1|
|2012-07-11 00:00:00+00:00|2013-05-26 00:00:00+00:00|HW2|
## Adjusting data at Swiss Camp 10m
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-05-01 00:00:00+00:00|2002-01-01 00:00:00+00:00|DW1|rotate|-100.0|0|
|1998-05-01 00:00:00+00:00|2002-01-01 00:00:00+00:00|DW2|rotate|-100.0|0|
|2014-01-01 00:00:00+00:00|2020-11-03 21:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2014-01-01 00:00:00+00:00|2020-11-03 21:00:00+00:00|HW1|biweekly_upper_range_filter|0.5|2602|
|2014-01-01 00:00:00+00:00|2020-11-03 21:00:00+00:00|HW1|hampel_filter|2.0|3797|
|2014-01-01 00:00:00+00:00|2020-11-03 21:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2014-01-01 00:00:00+00:00|2020-11-03 21:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|8516|
|2014-01-01 00:00:00+00:00|2020-11-03 21:00:00+00:00|HW2|hampel_filter|2.0|2730|
|2014-05-09 21:00:00+00:00|2020-11-03 21:00:00+00:00|HW2|add|9.0|0|
|2014-01-01 00:00:00+00:00|2019-05-05 00:00:00+00:00|P|add|-96.5|0|
|1990-06-01 01:00:00+00:00|2005-01-01 00:00:00+00:00|RH1|swap_with_RH2|0.0|38279|
|2014-01-01 00:00:00+00:00|2020-11-03 21:00:00+00:00|TA1|swap_with_TA2|0.0|47821|
## ROC filter at Swiss Camp 10m
 
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_ISWR.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_OSWR.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_NR.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_TA1.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_TA3.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_RH1.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_RH2.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_VW1.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_VW2.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_DW1.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_DW2.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_P.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_HW1.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_HW2.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_V.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_TA2.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_HS2.jpeg)
 
Using metadata/interpolated positions/GC-Net_elevation_tie_points.csv for variable elevation
# 1 Swiss Camp
## Interpolated values filter at Swiss Camp
ISWR: 27 samples flagged
OSWR: 59 samples flagged
NR: 446 samples flagged
TA1: 2973 samples flagged
TA2: 3607 samples flagged
TA3: 1242 samples flagged
TA4: 1207 samples flagged
RH1: 1171 samples flagged
RH2: 1225 samples flagged
VW1: 6133 samples flagged
VW2: 5798 samples flagged
DW1: 983 samples flagged
DW2: 975 samples flagged
P: 2842 samples flagged
TA5: 2563 samples flagged
TS1: 58 samples flagged
TS2: 67 samples flagged
TS3: 78 samples flagged
TS4: 204 samples flagged
TS5: 232 samples flagged
TS6: 1044 samples flagged
TS7: 804 samples flagged
TS8: 1203 samples flagged
TS9: 739 samples flagged
TS10: 2531 samples flagged
IUVR: 99 samples flagged
ILWR: 24 samples flagged
Tsurf1: 34 samples flagged
Tsurf2: 18 samples flagged
## Manual flagging of data at Swiss Camp
Flagging data:
|start time|end time|variable|
|-|-|-|
|2015-06-01 00:00:00+00:00|2016-05-01 00:00:00+00:00|RH1|
|2009-07-01 00:00:00+00:00|2009-07-01 00:00:00+00:00|ISWR|
|2009-07-01 00:00:00+00:00|2009-07-01 00:00:00+00:00|OSWR|
|2011-02-15 00:00:00+00:00|2011-05-10 00:00:00+00:00|OSWR|
|2011-08-01 00:00:00+00:00|2012-05-10 00:00:00+00:00|OSWR|
|2011-02-15 00:00:00+00:00|2011-05-10 00:00:00+00:00|ISWR|
|2015-06-01 00:00:00+00:00|2016-05-01 00:00:00+00:00|VW1|
Warning: HS1 not found
Warning: HS1 not found
Warning: HS2 not found
Warning: HS2 not found
Warning: HS1 not found
|1995-01-01 00:00:00+00:00|1996-06-23 00:00:00+00:00|HW1|
|1998-06-03 12:00:00+00:00|1999-04-06 00:00:00+00:00|HW1|
|2004-05-28 00:00:00+00:00|2004-05-29 00:00:00+00:00|HW1|
|2011-08-14 00:00:00+00:00|2012-05-31 21:00:00+00:00|HW1|
|2017-05-17 00:00:00+00:00|2018-04-28 00:00:00+00:00|HW1|
|2011-08-14 00:00:00+00:00|2012-05-24 00:00:00+00:00|HW2|
|2012-05-12 00:00:00+00:00|2022-08-03 19:00:00+00:00|TS1|
|2012-05-12 00:00:00+00:00|2022-08-03 19:00:00+00:00|TS3|
|2014-05-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|TS2|
|2013-08-16 00:00:00+00:00|2014-09-12 00:00:00+00:00|TS4|
|2013-08-16 00:00:00+00:00|2014-09-12 00:00:00+00:00|TS5|
|2013-08-16 00:00:00+00:00|2014-09-12 00:00:00+00:00|TS9|
## Adjusting data at Swiss Camp
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1996-01-01 00:00:00+00:00|1996-08-01 00:00:00+00:00|HW1|air_temp_sonic_anticorrection|0.0|0|
|2009-01-01 00:00:00+00:00|2011-07-15 00:00:00+00:00|HW1|min_filter|1.0|7677|
|2009-05-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW1|add|-0.5|0|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW1|biweekly_upper_range_filter|0.5|5337|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW1|hampel_filter|2.0|706|
|1995-01-12 00:00:00+00:00|2000-01-01 00:00:00+00:00|HW2|max_filter|8.0|19148|
|1996-01-01 00:00:00+00:00|1996-08-01 00:00:00+00:00|HW2|air_temp_sonic_anticorrection|0.0|0|
|2009-01-01 00:00:00+00:00|2012-01-15 00:00:00+00:00|HW2|min_filter|1.0|2949|
|2009-05-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW2|add|0.3|0|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|12071|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW2|hampel_filter|2.0|3607|
|2018-03-12 00:00:00+00:00|2018-05-12 00:00:00+00:00|HW2|max_filter|0.77|430|
|2012-05-10 00:00:00+00:00|2022-08-03 19:00:00+00:00|ISWR|swap_with_OSWR|0.0|0|
|2009-05-07 00:00:00+00:00|2022-08-03 19:00:00+00:00|OSWR|multiply|0.934|0|
|2019-11-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|P|min_filter|856.0|5228|
|2005-05-09 00:00:00+00:00|2022-08-03 19:00:00+00:00|RH1|swap_with_RH2|0.0|0|
|1996-01-01 00:00:00+00:00|2011-01-01 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1996-01-01 00:00:00+00:00|2011-01-01 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS1|max_filter|-1.0|4|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS10|max_filter|-1.0|566|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS2|max_filter|-1.0|4|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS3|max_filter|-1.0|4|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS4|max_filter|-1.0|4|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS5|max_filter|-1.0|2|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS6|max_filter|-1.0|2|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS7|max_filter|-1.0|1|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS8|max_filter|-1.0|1|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS9|max_filter|-1.0|1|
## ROC filter at Swiss Camp
 
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_ISWR.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_OSWR.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_NR.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TA1.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TA2.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TA3.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TA4.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_RH1.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_RH2.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_VW1.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_VW2.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_DW1.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_DW2.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_P.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_HW1.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_HW2.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_V.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TA5.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TS1.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TS2.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TS3.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TS4.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TS5.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TS6.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TS7.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TS8.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TS9.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_TS10.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_IUVR.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_ILWR.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_Tsurf1.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_Tsurf2.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1999-01-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.75|0|
|2000-12-31 08:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.7|0|
|2001-05-17 17:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.3|0|
|2002-01-25 19:30:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|1.5|0|
|2003-01-24 01:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.6|0|
|2003-04-26 16:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|0.4|0|
|2004-01-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.5|0|
|2011-08-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-3.0|0|
|2014-05-08 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-2.0|0|
 
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2000-12-31 08:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-0.8|0|
|2001-05-17 17:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-0.3|0|
|2011-08-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-3.0|0|
|2014-05-08 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-2.0|0|
 
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_HS2.jpeg)
 
Using metadata/interpolated positions/Swiss Camp_position_interpolated.csv for variable latitude and longitude
Using metadata/interpolated positions/GC-Net_elevation_tie_points.csv for variable elevation
# 2 Crawford Point 1
## Interpolated values filter at Crawford Point 1
ISWR: 42 samples flagged
OSWR: 22 samples flagged
NR: 537 samples flagged
TA1: 2221 samples flagged
TA2: 1892 samples flagged
TA3: 1630 samples flagged
TA4: 1954 samples flagged
RH1: 849 samples flagged
RH2: 659 samples flagged
VW1: 6061 samples flagged
VW2: 5704 samples flagged
DW1: 758 samples flagged
DW2: 792 samples flagged
P: 6440 samples flagged
TA5: 222 samples flagged
TS1: 302 samples flagged
TS2: 234 samples flagged
TS3: 2799 samples flagged
TS4: 768 samples flagged
TS5: 572 samples flagged
TS6: 741 samples flagged
TS7: 2711 samples flagged
TS8: 551 samples flagged
TS9: 462 samples flagged
TS10: 386 samples flagged
## Manual flagging of data at Crawford Point 1
Flagging data:
|start time|end time|variable|
|-|-|-|
|1990-01-01 16:00:00+00:00|1997-01-01 00:00:00+00:00|RH1|
|1990-01-01 16:00:00+00:00|1997-01-01 00:00:00+00:00|RH2|
|1998-01-01 00:00:00+00:00|1998-05-31 00:00:00+00:00|ISWR|
|1998-01-01 00:00:00+00:00|1998-05-31 00:00:00+00:00|OSWR|
|2011-05-25 00:00:00+00:00|2012-11-01 00:00:00+00:00|P|
|2008-06-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|DW1|
|2008-06-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|DW2|
|1990-01-01 16:00:00+00:00|1992-01-01 00:00:00+00:00|DW1|
|1990-01-01 16:00:00+00:00|1992-01-01 00:00:00+00:00|DW2|
|1995-01-01 00:00:00+00:00|1996-06-12 00:00:00+00:00|VW1|
|1995-01-01 00:00:00+00:00|1996-06-12 00:00:00+00:00|VW2|
|2019-11-17 00:00:00+00:00|2020-03-26 22:00:00+00:00|VW1|
|2004-11-16 00:00:00+00:00|2005-05-04 00:00:00+00:00|RH1|
|2004-11-16 00:00:00+00:00|2005-05-04 00:00:00+00:00|RH2|
|2005-01-01 00:00:00+00:00|2007-05-10 00:00:00+00:00|TA1|
|2017-03-10 00:00:00+00:00|2017-05-22 00:00:00+00:00|TA3|
|2013-06-01 00:00:00+00:00|2015-07-01 00:00:00+00:00|HW2|
|2017-07-26 00:00:00+00:00|2019-05-11 18:00:00+00:00|HW1|
|2005-05-04 00:00:00+00:00|2005-05-04 02:00:00+00:00|HW2|
|2000-08-01 00:00:00+00:00|2000-08-10 00:00:00+00:00|TS1|
|2000-08-01 00:00:00+00:00|2000-08-10 00:00:00+00:00|TS2|
|2000-08-01 00:00:00+00:00|2000-08-10 00:00:00+00:00|TS3|
|2000-08-01 00:00:00+00:00|2000-08-10 00:00:00+00:00|TS4|
|2000-08-01 00:00:00+00:00|2000-08-10 00:00:00+00:00|TS5|
|2000-08-01 00:00:00+00:00|2000-08-10 00:00:00+00:00|TS6|
|2000-08-01 00:00:00+00:00|2000-08-10 00:00:00+00:00|TS7|
|2000-08-01 00:00:00+00:00|2000-08-10 00:00:00+00:00|TS8|
|2000-08-01 00:00:00+00:00|2000-08-10 00:00:00+00:00|TS9|
|2000-08-01 00:00:00+00:00|2000-08-10 00:00:00+00:00|TS10|
|2002-10-15 00:00:00+00:00|2002-11-05 00:00:00+00:00|TS4|
|2003-10-05 00:00:00+00:00|2003-11-30 00:00:00+00:00|TS4|
|2001-09-10 00:00:00+00:00|2001-12-01 00:00:00+00:00|TS8|
|2002-02-01 00:00:00+00:00|2002-07-20 00:00:00+00:00|TS8|
|2000-10-20 00:00:00+00:00|2000-11-10 00:00:00+00:00|TS8|
|2002-10-15 00:00:00+00:00|2002-11-05 00:00:00+00:00|TS8|
|2003-10-05 00:00:00+00:00|2004-06-30 00:00:00+00:00|TS8|
|1998-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TS1|
|1998-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TS2|
|1998-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TS3|
|1998-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TS4|
|1998-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TS5|
|1998-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TS6|
|1998-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TS7|
|1998-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TS8|
|1998-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TS9|
|1998-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TS10|
|2000-10-26 04:00:00+00:00|2000-11-08 00:00:00+00:00|TS3|
|2001-09-05 06:00:00+00:00|2002-08-14 00:00:00+00:00|TS3|
|2003-10-14 08:00:00+00:00|2004-04-21 00:00:00+00:00|TS3|
|2000-07-29 18:00:00+00:00|2000-08-10 00:00:00+00:00|TS1|
|2003-09-30 17:00:00+00:00|2003-12-13 00:00:00+00:00|TS7|
|2008-06-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|TS1|
|2008-06-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|TS2|
|2008-06-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|TS3|
|2008-06-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|TS4|
|2008-06-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|TS5|
|2008-06-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|TS6|
|2008-06-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|TS7|
|2008-06-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|TS8|
|2008-06-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|TS9|
|2008-06-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|TS10|
## Adjusting data at Crawford Point 1
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|DW1|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|DW1|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|DW1|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|DW1|time_shift|180552.0|6431|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|DW2|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|DW2|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|DW2|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|DW2|time_shift|180552.0|6431|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|HW1|time_shift|24.0|25|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|HW1|time_shift|24.0|24|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|HW1|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW1|time_shift|180552.0|6431|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW1|swap_with_HW2|0.0|-5857|
|2010-05-09 22:00:00+00:00|2010-08-07 00:00:00+00:00|HW1|swap_with_HW2|0.0|38|
|2011-05-02 14:00:00+00:00|2020-07-22 09:00:00+00:00|HW1|swap_with_HW2|0.0|5158|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2001-12-31 14:00:00+00:00|2002-12-31 14:00:00+00:00|HW1|add|-0.3|0|
|2002-09-24 13:00:00+00:00|2002-12-31 14:00:00+00:00|HW1|add|-0.94|0|
|2009-05-10 00:00:00+00:00|2020-07-22 09:00:00+00:00|HW1|hampel_filter|2.0|5199|
|2009-12-14 15:00:00+00:00|2010-05-09 22:00:00+00:00|HW1|add|-1.1|0|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW1|min_filter|0.1|8880|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW1|biweekly_upper_range_filter|0.5|2068|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|HW2|time_shift|24.0|25|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|HW2|time_shift|24.0|24|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|HW2|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW2|time_shift|180552.0|0|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|0|
|2002-12-31 14:00:00+00:00|2002-12-31 14:00:00+00:00|HW2|add|-1.0|0|
|2009-05-10 00:00:00+00:00|2020-07-22 09:00:00+00:00|HW2|hampel_filter|2.0|7126|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2010-05-09 22:00:00+00:00|2010-08-07 00:00:00+00:00|HW2|max_filter|3.9|10|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW2|min_filter|0.1|1535|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|12382|
|2017-05-10 00:00:00+00:00|2020-07-22 09:00:00+00:00|HW2|biweekly_upper_range_filter|0.2|1502|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|ISWR|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|ISWR|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|ISWR|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|ISWR|time_shift|180552.0|14|
|2012-01-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|ISWR|swap_with_OSWR|0.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|NR|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|NR|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|NR|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|NR|time_shift|180552.0|1769|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|OSWR|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|OSWR|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|OSWR|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|OSWR|time_shift|180552.0|22|
|2010-05-09 00:00:00+00:00|2020-07-22 09:00:00+00:00|OSWR|multiply|0.934|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|P|time_shift|24.0|25|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|P|time_shift|24.0|24|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|P|time_shift|24.0|1|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|P|time_shift|180552.0|6431|
|1999-01-01 00:00:00+00:00|2010-05-09 22:00:00+00:00|P|add|-12.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|RH1|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|RH1|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|RH1|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|RH1|time_shift|180552.0|6419|
|1996-01-01 00:00:00+00:00|2010-05-16 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|RH2|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|RH2|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|RH2|time_shift|24.0|4|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|RH2|time_shift|180552.0|6431|
|1996-01-01 00:00:00+00:00|2010-05-16 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TA1|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TA1|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TA1|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TA1|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TA2|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TA2|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TA2|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TA2|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TA3|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TA3|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TA3|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TA3|time_shift|180552.0|6429|
|1990-01-01 16:00:00+00:00|1999-01-01 00:00:00+00:00|TA3|swap_with_TA4|0.0|-6384|
|2006-01-01 00:00:00+00:00|2007-04-26 00:00:00+00:00|TA3|swap_with_TA4|0.0|3087|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TA4|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TA4|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TA4|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TA4|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TA5|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TA5|time_shift|24.0|0|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TA5|time_shift|24.0|0|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TA5|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS1|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS1|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS1|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS1|time_shift|180552.0|0|
|1990-01-01 16:00:00+00:00|2020-07-22 09:00:00+00:00|TS1|min_filter|-20.0|6189|
|1990-01-01 16:00:00+00:00|2020-07-22 09:00:00+00:00|TS1|max_filter|-15.0|5999|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS10|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS10|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS10|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS10|time_shift|180552.0|0|
|1990-01-01 16:00:00+00:00|2020-07-22 09:00:00+00:00|TS10|min_filter|-26.0|908|
|1990-01-01 16:00:00+00:00|2020-07-22 09:00:00+00:00|TS10|max_filter|-10.0|10572|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS2|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS2|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS2|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS2|time_shift|180552.0|0|
|1990-01-01 16:00:00+00:00|2005-01-01 00:00:00+00:00|TS2|min_filter|-20.0|66|
|1990-01-01 16:00:00+00:00|2005-01-01 00:00:00+00:00|TS2|max_filter|-15.0|562|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS3|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS3|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS3|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS3|time_shift|180552.0|0|
|1997-01-01 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS3|min_filter|-20.0|1606|
|1997-01-01 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS3|max_filter|-15.0|948|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS4|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS4|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS4|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS4|time_shift|180552.0|0|
|1997-01-01 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS4|min_filter|-20.0|89|
|1997-01-01 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS4|max_filter|-15.0|988|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS5|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS5|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS5|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS5|time_shift|180552.0|0|
|2000-03-01 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS5|min_filter|-20.0|72|
|2000-03-01 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS5|max_filter|-15.0|894|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS6|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS6|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS6|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS6|time_shift|180552.0|0|
|2000-03-01 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS6|min_filter|-20.0|73|
|2000-03-01 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS6|max_filter|-15.0|925|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS7|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS7|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS7|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS7|time_shift|180552.0|0|
|2000-03-01 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS7|min_filter|-20.0|1141|
|2000-03-01 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS7|max_filter|-15.0|3089|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS8|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS8|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS8|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS8|time_shift|180552.0|0|
|1990-01-01 16:00:00+00:00|2020-07-22 09:00:00+00:00|TS8|min_filter|-26.0|4939|
|1990-01-01 16:00:00+00:00|2020-07-22 09:00:00+00:00|TS8|max_filter|-10.0|5472|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS9|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS9|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS9|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS9|time_shift|180552.0|0|
|1990-01-01 16:00:00+00:00|2020-07-22 09:00:00+00:00|TS9|min_filter|-26.0|5663|
|1990-01-01 16:00:00+00:00|2020-07-22 09:00:00+00:00|TS9|max_filter|-10.0|11795|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|V|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|V|time_shift|24.0|0|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|V|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|V|time_shift|180552.0|6431|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|VW1|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|VW1|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|VW1|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|VW1|time_shift|180552.0|6431|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|VW2|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|VW2|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|VW2|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|VW2|time_shift|180552.0|6431|
## ROC filter at Crawford Point 1
 
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_ISWR.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_OSWR.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_NR.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TA1.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TA2.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TA3.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TA4.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_RH1.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_RH2.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_VW1.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_VW2.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_DW1.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_DW2.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_P.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_HW1.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_HW2.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_V.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TA5.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TS1.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TS2.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TS3.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TS4.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TS5.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TS6.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TS7.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TS8.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TS9.jpeg)
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1997-05-13 09:00:00+00:00|2020-07-22 09:00:00+00:00|HS1|add|2.5|0|
|1998-09-05 00:00:00+00:00|2020-07-22 09:00:00+00:00|HS1|add|3.0|0|
|2001-05-28 18:00:00+00:00|2020-07-22 09:00:00+00:00|HS1|add|2.0|0|
|2003-04-11 00:00:00+00:00|2020-07-22 09:00:00+00:00|HS1|add|2.8|0|
|2005-05-03 08:00:00+00:00|2020-07-22 09:00:00+00:00|HS1|add|3.0|0|
|2008-05-05 14:00:00+00:00|2020-07-22 09:00:00+00:00|HS1|add|2.7|0|
|2011-05-02 23:00:00+00:00|2020-07-22 09:00:00+00:00|HS1|add|2.8|0|
|2017-05-21 00:00:00+00:00|2020-07-22 09:00:00+00:00|HS1|add|2.0|0|
 
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1997-05-13 09:00:00+00:00|2020-07-22 09:00:00+00:00|HS2|add|2.5|0|
|1998-09-05 00:00:00+00:00|2020-07-22 09:00:00+00:00|HS2|add|3.0|0|
|2001-05-28 18:00:00+00:00|2020-07-22 09:00:00+00:00|HS2|add|2.0|0|
|2001-12-31 14:00:00+00:00|2020-07-22 09:00:00+00:00|HS2|add|1.0|0|
|2003-04-11 00:00:00+00:00|2020-07-22 09:00:00+00:00|HS2|add|1.5|0|
|2005-05-03 08:00:00+00:00|2020-07-22 09:00:00+00:00|HS2|add|3.6|0|
|2008-05-05 14:00:00+00:00|2020-07-22 09:00:00+00:00|HS2|add|3.0|0|
|2009-12-10 00:00:00+00:00|2020-07-22 09:00:00+00:00|HS2|add|0.3|0|
|2011-05-02 18:00:00+00:00|2020-07-22 09:00:00+00:00|HS2|add|2.8|0|
|2016-01-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|HS2|add|-0.7|0|
|2017-05-21 00:00:00+00:00|2020-07-22 09:00:00+00:00|HS2|add|2.2|0|
 
![Adjusted and flagged data at Crawford Point 1](figures/L1_data_treatment/CrawfordPoint1_HS2.jpeg)
 
Using metadata/interpolated positions/Crawford Point 1_position_interpolated.csv for variable latitude and longitude
# 13 CP2
## Interpolated values filter at CP2
ISWR: 6 samples flagged
OSWR: 7 samples flagged
NR: 55 samples flagged
TA1: 122 samples flagged
TA2: 115 samples flagged
TA3: 42 samples flagged
TA4: 76 samples flagged
RH1: 15 samples flagged
RH2: 20 samples flagged
VW1: 3 samples flagged
P: 403 samples flagged
HS1: 98 samples flagged
HS2: 103 samples flagged
TS1: 104 samples flagged
TS2: 46 samples flagged
TS3: 54 samples flagged
TS4: 23 samples flagged
TS5: 10 samples flagged
TS6: 25 samples flagged
TS7: 21 samples flagged
TS8: 27 samples flagged
TS9: 23 samples flagged
TS10: 74 samples flagged
## Manual flagging of data at CP2
Flagging data:
|start time|end time|variable|
|-|-|-|
|1999-02-07 00:00:00+00:00|1999-07-01 00:00:00+00:00|RH2|
|1997-08-12 00:00:00+00:00|1997-10-01 00:00:00+00:00|TS1|
|1997-08-12 00:00:00+00:00|1997-10-01 00:00:00+00:00|TS2|
|1997-08-12 00:00:00+00:00|1997-10-01 00:00:00+00:00|TS3|
|1997-08-12 00:00:00+00:00|1997-10-01 00:00:00+00:00|TS4|
|1997-08-12 00:00:00+00:00|1997-10-01 00:00:00+00:00|TS5|
|1997-08-12 00:00:00+00:00|1997-10-01 00:00:00+00:00|TS6|
|1997-08-12 00:00:00+00:00|1997-10-01 00:00:00+00:00|TS7|
|1997-08-12 00:00:00+00:00|1997-10-01 00:00:00+00:00|TS8|
|1997-08-12 00:00:00+00:00|1997-10-01 00:00:00+00:00|TS9|
## Adjusting data at CP2
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1997-01-01 00:00:00+00:00|2001-05-29 13:00:00+00:00|HW1|add|-4.0|0|
|1997-11-01 00:00:00+00:00|1998-04-01 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.2|203|
|1998-05-30 00:00:00+00:00|2001-05-29 13:00:00+00:00|HW1|add|1.0|0|
|1999-05-27 00:00:00+00:00|2001-05-29 13:00:00+00:00|HW1|add|1.0|0|
|2000-06-02 00:00:00+00:00|2001-05-29 13:00:00+00:00|HW1|add|1.7|0|
|1997-01-01 00:00:00+00:00|2001-05-29 13:00:00+00:00|HW2|add|-2.2|0|
|1998-01-01 00:00:00+00:00|1998-03-01 00:00:00+00:00|HW2|biweekly_upper_range_filter|0.1|125|
|1998-05-30 00:00:00+00:00|2001-05-29 13:00:00+00:00|HW2|add|0.5|0|
|1999-05-27 00:00:00+00:00|2001-05-29 13:00:00+00:00|HW2|add|1.0|0|
|2000-06-02 00:00:00+00:00|2001-05-29 13:00:00+00:00|HW2|add|1.7|0|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|1997-01-01 00:00:00+00:00|2001-05-29 13:00:00+00:00|TA1|swap_with_TA2|0.0|0|
## ROC filter at CP2
 
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_ISWR.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_OSWR.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_NR.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TA1.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TA2.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TA3.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TA4.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_RH1.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_RH2.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_VW1.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_VW2.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_DW1.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_DW2.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_P.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_HS1.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_HS2.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_V.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_HW1.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_HW2.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TS1.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TS2.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TS3.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TS4.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TS5.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TS6.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TS7.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TS8.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TS9.jpeg)
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-05-30 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS1|add|1.0|0|
|1999-05-27 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS1|add|1.0|0|
|2000-06-02 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS1|add|1.7|0|
 
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-05-30 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS2|add|1.0|0|
|1999-05-27 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS2|add|1.0|0|
|2000-06-02 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS2|add|1.7|0|
 
![Adjusted and flagged data at CP2](figures/L1_data_treatment/CP2_HS2.jpeg)
 
# 9 JAR1
## Interpolated values filter at JAR1
ISWR: 154 samples flagged
OSWR: 72 samples flagged
NR: 353 samples flagged
TA1: 4207 samples flagged
TA2: 3126 samples flagged
TA3: 1598 samples flagged
TA4: 1143 samples flagged
RH1: 1075 samples flagged
RH2: 1120 samples flagged
VW1: 4713 samples flagged
VW2: 4524 samples flagged
DW1: 805 samples flagged
DW2: 916 samples flagged
P: 4587 samples flagged
TA5: 476 samples flagged
TS1: 1288 samples flagged
TS2: 4387 samples flagged
TS3: 3101 samples flagged
TS4: 2964 samples flagged
TS5: 2929 samples flagged
TS6: 3259 samples flagged
TS7: 2577 samples flagged
TS8: 35 samples flagged
TS9: 1620 samples flagged
TS10: 2715 samples flagged
## Manual flagging of data at JAR1
Flagging data:
|start time|end time|variable|
|-|-|-|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|TA1|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|TA2|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|TA3|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|TA4|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|RH1|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|RH2|
|2010-10-01 00:00:00+00:00|2011-05-04 00:00:00+00:00|RH1|
|2010-10-01 00:00:00+00:00|2011-05-04 00:00:00+00:00|RH2|
|2010-10-01 00:00:00+00:00|2012-05-04 00:00:00+00:00|TA2|
|2010-10-01 00:00:00+00:00|2011-06-05 00:00:00+00:00|TA4|
|2010-10-01 00:00:00+00:00|2011-06-05 00:00:00+00:00|TA3|
|2013-10-01 00:00:00+00:00|2014-10-05 00:00:00+00:00|TA4|
|2005-05-08 00:00:00+00:00|2005-05-08 21:00:00+00:00|HW2|
|2011-09-06 00:00:00+00:00|2012-01-30 00:00:00+00:00|HW2|
|2012-08-01 00:00:00+00:00|2012-08-13 00:00:00+00:00|HW2|
|2015-08-24 00:00:00+00:00|2015-08-30 00:00:00+00:00|HW2|
|2011-05-01 00:00:00+00:00|2011-06-01 00:00:00+00:00|HW1|
|2011-09-09 00:00:00+00:00|2012-01-01 00:00:00+00:00|HW1|
|2013-07-01 00:00:00+00:00|2013-08-01 00:00:00+00:00|HW1|
|2011-08-16 00:00:00+00:00|2012-01-01 00:00:00+00:00|ISWR|
|2011-08-16 00:00:00+00:00|2012-01-01 00:00:00+00:00|OSWR|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|TA1|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|TA2|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|TA3|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|TA4|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|RH1|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|RH2|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|VW1|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|VW2|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|DW1|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|DW2|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|HW1|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|HW2|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|ISWR|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|OSWR|
|2010-07-19 00:00:00+00:00|2011-05-06 00:00:00+00:00|NR|
|1999-06-01 00:00:00+00:00|2001-06-01 00:00:00+00:00|TS1|
|1999-06-01 00:00:00+00:00|2001-06-01 00:00:00+00:00|TS2|
|1999-06-01 00:00:00+00:00|2001-06-01 00:00:00+00:00|TS3|
|1999-06-01 00:00:00+00:00|2001-06-01 00:00:00+00:00|TS4|
|1999-06-01 00:00:00+00:00|2001-06-01 00:00:00+00:00|TS5|
|1999-06-01 00:00:00+00:00|2001-06-01 00:00:00+00:00|TS6|
|1999-06-01 00:00:00+00:00|2001-06-01 00:00:00+00:00|TS7|
|1999-06-01 00:00:00+00:00|2001-06-01 00:00:00+00:00|TS8|
|1999-06-01 00:00:00+00:00|2001-06-01 00:00:00+00:00|TS9|
|1999-06-01 00:00:00+00:00|2001-06-01 00:00:00+00:00|TS10|
|2003-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS1|
|2003-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS2|
|2003-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS3|
|2003-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS4|
|2003-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS5|
|2003-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS6|
|2003-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS7|
|2003-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS8|
|2003-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS9|
|2003-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS10|
## Adjusting data at JAR1
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|DW1|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|DW1|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|DW2|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|DW2|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|HW1|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|HW1|time_shift|24.0|17|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW1|hampel_filter|2.0|3234|
|2009-08-14 00:00:00+00:00|2010-05-01 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|468|
|2010-06-11 00:00:00+00:00|2010-06-21 00:00:00+00:00|HW1|min_filter|2.21|12|
|2010-07-08 00:00:00+00:00|2010-07-19 00:00:00+00:00|HW1|min_filter|3.35|31|
|2018-10-01 00:00:00+00:00|2018-10-10 00:00:00+00:00|HW1|min_filter|2.17|16|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|HW2|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|HW2|time_shift|24.0|17|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|17052|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|hampel_filter|2.0|544|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|ISWR|time_shift|-745.0|554|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|ISWR|time_shift|24.0|16|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|NR|time_shift|-745.0|553|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|NR|time_shift|24.0|14|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|OSWR|time_shift|-745.0|553|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|OSWR|time_shift|24.0|17|
|2009-05-06 00:00:00+00:00|2019-09-08 01:00:00+00:00|OSWR|multiply|0.934|0|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|P|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|P|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|RH1|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|RH1|time_shift|24.0|1|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|RH2|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|RH2|time_shift|24.0|1|
|2012-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|RH2|swap_with_RH1|0.0|-1670|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA1|time_shift|-745.0|337|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA1|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA2|time_shift|-745.0|0|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA2|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA3|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA3|time_shift|24.0|1|
|2005-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|TA3|swap_with_TA4|0.0|-841|
|2018-02-01 00:00:00+00:00|2019-12-20 00:00:00+00:00|TA3|max_filter|9.0|215|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA4|time_shift|-745.0|745|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA4|time_shift|24.0|1|
|2013-02-01 00:00:00+00:00|2015-12-20 00:00:00+00:00|TA4|max_filter|9.0|3469|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA5|time_shift|-745.0|338|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA5|time_shift|24.0|0|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS1|time_shift|-745.0|211|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS1|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS10|time_shift|-745.0|23|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS10|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS2|time_shift|-745.0|231|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS2|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS3|time_shift|-745.0|4|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS3|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS4|time_shift|-745.0|110|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS4|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS5|time_shift|-745.0|123|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS5|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS6|time_shift|-745.0|19|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS6|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS7|time_shift|-745.0|34|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS7|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS8|time_shift|-745.0|13|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS8|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS9|time_shift|-745.0|60|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS9|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|V|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|V|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|VW1|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|VW1|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|VW2|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|VW2|time_shift|24.0|17|
## ROC filter at JAR1
 
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_ISWR.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_OSWR.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_NR.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TA1.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TA2.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TA3.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TA4.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_RH1.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_RH2.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_VW1.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_VW2.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_DW1.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_DW2.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_P.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_HW1.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_HW2.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_V.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TA5.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TS1.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TS2.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TS3.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TS4.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TS5.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TS6.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TS7.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TS8.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TS9.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_TS10.jpeg)
 
Using metadata/interpolated positions/JAR1_position_interpolated.csv for variable latitude and longitude
Using metadata/interpolated positions/GC-Net_elevation_tie_points.csv for variable elevation
Cannot download maintenance summary. Using local file.
# 17 JAR2
## Interpolated values filter at JAR2
ISWR: 50 samples flagged
OSWR: 71 samples flagged
NR: 238 samples flagged
TA1: 359 samples flagged
TA2: 344 samples flagged
TA3: 271 samples flagged
TA4: 266 samples flagged
RH1: 476 samples flagged
RH2: 567 samples flagged
VW1: 3101 samples flagged
VW2: 2808 samples flagged
DW1: 413 samples flagged
DW2: 406 samples flagged
P: 1467 samples flagged
TA5: 6 samples flagged
TS1: 313 samples flagged
TS2: 4076 samples flagged
TS3: 448 samples flagged
TS4: 529 samples flagged
TS5: 707 samples flagged
TS6: 777 samples flagged
TS7: 601 samples flagged
TS8: 1581 samples flagged
TS9: 1756 samples flagged
TS10: 805 samples flagged
## Manual flagging of data at JAR2
Flagging data:
|start time|end time|variable|
|-|-|-|
|2011-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|VW1|
|2011-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|DW1|
|2012-07-15 00:00:00+00:00|2012-07-17 00:00:00+00:00|HW2|
|2012-08-16 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|
|2002-05-07 00:00:00+00:00|2002-05-07 08:00:00+00:00|HW1|
|2002-05-07 00:00:00+00:00|2002-05-07 08:00:00+00:00|HW2|
|2004-05-01 00:00:00+00:00|2004-05-27 11:00:00+00:00|HW1|
|2004-05-01 00:00:00+00:00|2004-05-27 11:00:00+00:00|HW2|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|TA1|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|TA2|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|TA3|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|HW1|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|HW2|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|RH1|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|RH2|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|VW1|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|VW2|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|DW1|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|DW2|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|ISWR|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|OSWR|
|2010-07-01 00:00:00+00:00|2011-06-10 11:00:00+00:00|NR|
|2008-05-07 00:00:00+00:00|2011-06-10 11:00:00+00:00|TA4|
|2008-05-07 00:00:00+00:00|2011-06-10 11:00:00+00:00|TA3|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS1|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS2|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS3|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS4|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS5|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS6|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS7|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS8|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS9|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS10|
|2002-06-26 00:00:00+00:00|2003-05-06 00:00:00+00:00|TS1|
|2002-06-26 00:00:00+00:00|2003-05-06 00:00:00+00:00|TS2|
|2002-06-26 00:00:00+00:00|2003-05-06 00:00:00+00:00|TS3|
|2002-06-26 00:00:00+00:00|2003-05-06 00:00:00+00:00|TS4|
|2002-06-26 00:00:00+00:00|2003-05-06 00:00:00+00:00|TS5|
|2002-06-26 00:00:00+00:00|2003-05-06 00:00:00+00:00|TS6|
|2002-06-26 00:00:00+00:00|2003-05-06 00:00:00+00:00|TS7|
|2002-06-26 00:00:00+00:00|2003-05-06 00:00:00+00:00|TS8|
|2002-06-26 00:00:00+00:00|2003-05-06 00:00:00+00:00|TS9|
|2002-06-26 00:00:00+00:00|2003-05-06 00:00:00+00:00|TS10|
## Adjusting data at JAR2
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|DW1|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|DW1|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|DW2|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|DW2|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|time_shift|-749.0|2|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW1|time_shift|63.0|0|
|1999-04-19 00:00:00+00:00|2000-01-01 00:00:00+00:00|HW1|min_filter|0.5|10|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|max_filter|5.9|520|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|min_filter|1.05|4183|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|biweekly_upper_range_filter|0.7|792|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|time_shift|-749.0|2|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW2|time_shift|63.0|0|
|1999-04-19 00:00:00+00:00|2000-01-01 00:00:00+00:00|HW2|min_filter|0.5|10|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|min_filter|0.5|9992|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|max_filter|7.5|58|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|biweekly_upper_range_filter|0.7|3911|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|ISWR|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|ISWR|time_shift|63.0|0|
|2009-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|ISWR|multiply|0.5|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|NR|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|NR|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|OSWR|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|OSWR|time_shift|63.0|0|
|2009-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|OSWR|multiply|0.5|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|P|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|P|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|RH1|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|RH1|time_shift|63.0|0|
|2002-05-07 00:00:00+00:00|2013-06-16 08:00:00+00:00|RH1|swap_with_RH2|0.0|-20|
|1999-06-02 03:00:00+00:00|2013-06-16 08:00:00+00:00|RH1|ice_to_water|0.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|RH2|time_shift|-749.0|518|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|RH2|time_shift|63.0|0|
|1999-06-02 03:00:00+00:00|2013-06-16 08:00:00+00:00|RH2|ice_to_water|0.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TA1|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TA1|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TA2|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TA2|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TA3|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TA3|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TA4|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TA4|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TA5|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TA5|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS1|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS1|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS10|time_shift|-749.0|0|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS10|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS2|time_shift|-749.0|1|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS2|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS3|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS3|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS4|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS4|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS5|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS5|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS6|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS6|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS7|time_shift|-749.0|0|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS7|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS8|time_shift|-749.0|0|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS8|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS9|time_shift|-749.0|0|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS9|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|V|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|V|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|VW1|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|VW1|time_shift|63.0|0|
|2004-05-07 00:00:00+00:00|2005-05-14 00:00:00+00:00|VW1|swap_with_VW2|0.0|-459|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|VW2|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|VW2|time_shift|63.0|0|
## ROC filter at JAR2
 
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_ISWR.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_OSWR.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_NR.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TA1.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TA2.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TA3.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TA4.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_RH1.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_RH2.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_VW1.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_VW2.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_DW1.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_DW2.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_P.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_HW1.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_HW2.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_V.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TA5.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TS1.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TS2.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TS3.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TS4.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TS5.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TS6.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TS7.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TS8.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TS9.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_TS10.jpeg)
 
Using metadata/interpolated positions/GC-Net_elevation_tie_points.csv for variable elevation
Cannot download maintenance summary. Using local file.
# 19 JAR3
## Interpolated values filter at JAR3
ISWR: 9 samples flagged
NR: 35 samples flagged
TA1: 18 samples flagged
TA2: 15 samples flagged
TA3: 12 samples flagged
TA4: 32 samples flagged
RH1: 5 samples flagged
RH2: 7 samples flagged
VW1: 3 samples flagged
P: 1059 samples flagged
HS1: 46 samples flagged
## Manual flagging of data at JAR3
Flagging data:
|start time|end time|variable|
|-|-|-|
|2011-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|VW1|
|2011-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|DW1|
|2007-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|TS1|
|2007-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|TS2|
|2007-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|TS3|
|2007-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|TS4|
|2007-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|TS5|
|2007-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|TS6|
|2007-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|TS7|
|2007-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|TS8|
|2007-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|TS9|
|2007-01-01 00:00:00+00:00|2004-05-25 13:00:00+00:00|TS10|
## Adjusting data at JAR3
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2002-05-06 15:00:00+00:00|2004-05-25 13:00:00+00:00|P|add|70|0|
## ROC filter at JAR3
 
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_ISWR.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_OSWR.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_NR.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_TA1.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_TA2.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_TA3.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_TA4.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_RH1.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_RH2.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_VW1.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_VW2.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_DW1.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_DW2.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_P.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_HS1.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_V.jpeg)
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_HW1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at JAR3](figures/L1_data_treatment/JAR3_HS1.jpeg)
 
No valid data for HW2
Using metadata/interpolated positions/GC-Net_elevation_tie_points.csv for variable elevation
# 3 NASA-U
## Interpolated values filter at NASA-U
ISWR: 320 samples flagged
OSWR: 374 samples flagged
NR: 9937 samples flagged
TA1: 12596 samples flagged
TA2: 12115 samples flagged
TA3: 11712 samples flagged
TA4: 218 samples flagged
RH1: 1813 samples flagged
RH2: 621 samples flagged
VW1: 14637 samples flagged
VW2: 14587 samples flagged
DW1: 2713 samples flagged
DW2: 2746 samples flagged
P: 3304 samples flagged
TA5: 190 samples flagged
TS1: 926 samples flagged
TS2: 255 samples flagged
TS3: 10 samples flagged
TS4: 173 samples flagged
TS5: 172 samples flagged
TS7: 103 samples flagged
TS10: 97 samples flagged
## Manual flagging of data at NASA-U
Flagging data:
|start time|end time|variable|
|-|-|-|
|2002-01-06 19:00:00+00:00|2002-01-07 05:00:00+00:00|TA1|
|2017-12-11 00:00:00+00:00|2019-07-01 00:00:00+00:00|TA3|
|2011-01-01 00:00:00+00:00|2012-05-25 00:00:00+00:00|TA4|
|2011-01-01 00:00:00+00:00|2016-07-01 00:00:00+00:00|P|
|2017-08-01 00:00:00+00:00|2018-12-31 00:00:00+00:00|P|
|2011-01-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|RH2|
|2017-12-12 00:00:00+00:00|2018-05-23 00:00:00+00:00|RH2|
|2009-04-01 00:00:00+00:00|2009-04-24 21:00:00+00:00|HW1|
|2009-04-01 00:00:00+00:00|2009-04-25 01:00:00+00:00|HW2|
|2013-09-01 00:00:00+00:00|2014-05-21 00:00:00+00:00|HW1|
|2016-11-14 00:00:00+00:00|2018-07-01 00:00:00+00:00|HW1|
|2015-10-10 00:00:00+00:00|2016-02-14 00:00:00+00:00|HW2|
|2016-09-04 00:00:00+00:00|2017-05-02 00:00:00+00:00|HW2|
|2017-10-07 00:00:00+00:00|2018-05-19 00:00:00+00:00|HW2|
|2017-01-01 00:00:00+00:00|2017-04-09 00:00:00+00:00|ISWR|
|2022-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|DW1|
|2022-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|DW2|
|2010-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS1|
|2010-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS2|
|2010-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS3|
|2013-05-26 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS1|
|2013-05-26 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS2|
|2013-05-26 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS3|
|2013-05-26 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS4|
|2013-05-26 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS5|
|2013-05-26 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS6|
|2013-05-26 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS7|
|2013-05-26 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS8|
|2013-05-26 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS9|
|2013-05-26 00:00:00+00:00|2023-06-18 15:00:00+00:00|TS10|
|1995-01-01 00:00:00+00:00|1999-05-21 00:00:00+00:00|TS1|
|1995-01-01 00:00:00+00:00|1999-05-21 00:00:00+00:00|TS2|
|1995-01-01 00:00:00+00:00|1999-05-21 00:00:00+00:00|TS3|
|1995-01-01 00:00:00+00:00|1999-05-21 00:00:00+00:00|TS4|
|1995-01-01 00:00:00+00:00|1999-05-21 00:00:00+00:00|TS5|
|1995-01-01 00:00:00+00:00|1999-05-21 00:00:00+00:00|TS6|
|1995-01-01 00:00:00+00:00|1999-05-21 00:00:00+00:00|TS7|
|1995-01-01 00:00:00+00:00|1999-05-21 00:00:00+00:00|TS8|
|1995-01-01 00:00:00+00:00|1999-05-21 00:00:00+00:00|TS9|
|1995-01-01 00:00:00+00:00|1999-05-21 00:00:00+00:00|TS10|
|2006-04-26 00:00:00+00:00|2007-04-28 00:00:00+00:00|TS1|
|2006-04-26 00:00:00+00:00|2007-04-28 00:00:00+00:00|TS2|
|2006-04-26 00:00:00+00:00|2007-04-28 00:00:00+00:00|TS3|
|2006-04-26 00:00:00+00:00|2007-04-28 00:00:00+00:00|TS4|
|2006-04-26 00:00:00+00:00|2007-04-28 00:00:00+00:00|TS5|
|2006-04-26 00:00:00+00:00|2007-04-28 00:00:00+00:00|TS6|
|2006-04-26 00:00:00+00:00|2007-04-28 00:00:00+00:00|TS7|
|2006-04-26 00:00:00+00:00|2007-04-28 00:00:00+00:00|TS8|
|2006-04-26 00:00:00+00:00|2007-04-28 00:00:00+00:00|TS9|
|2006-04-26 00:00:00+00:00|2007-04-28 00:00:00+00:00|TS10|
|2002-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|NR|
|1995-05-31 01:00:00+00:00|1997-01-01 00:00:00+00:00|RH1|
|1995-05-31 01:00:00+00:00|1997-01-01 00:00:00+00:00|RH2|
|2022-09-24 00:00:00+00:00|2023-06-18 15:00:00+00:00|TA1|
|2022-09-24 00:00:00+00:00|2023-06-18 15:00:00+00:00|TA3|
|2022-09-24 00:00:00+00:00|2023-06-18 15:00:00+00:00|RH1|
|2022-09-24 00:00:00+00:00|2023-06-18 15:00:00+00:00|VW1|
|2022-09-24 00:00:00+00:00|2023-06-18 15:00:00+00:00|DW1|
|2022-09-24 00:00:00+00:00|2023-06-18 15:00:00+00:00|VW2|
|2022-09-24 00:00:00+00:00|2023-06-18 15:00:00+00:00|DW2|
## Adjusting data at NASA-U
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|DW1|time_shift|48.0|4|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|DW2|time_shift|48.0|4|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|HW1|time_shift|48.0|4|
|1990-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|HW1|add|-0.8|0|
|2001-05-31 21:00:00+00:00|2023-06-18 15:00:00+00:00|HW1|hampel_filter|3.0|11514|
|2007-02-12 00:00:00+00:00|2007-04-16 00:00:00+00:00|HW1|min_filter|2.4|164|
|2007-08-01 00:00:00+00:00|2007-12-16 00:00:00+00:00|HW1|min_filter|1.95|0|
|2008-02-01 00:00:00+00:00|2008-04-30 00:00:00+00:00|HW1|min_filter|1.66|794|
|2011-05-31 21:00:00+00:00|2023-06-18 15:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2011-05-31 21:00:00+00:00|2016-10-09 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|5067|
|2013-07-01 00:00:00+00:00|2014-07-01 00:00:00+00:00|HW1|min_filter|3.0|3751|
|2016-10-15 00:00:00+00:00|2016-11-15 00:00:00+00:00|HW1|min_filter|0.98|60|
|2016-10-15 00:00:00+00:00|2016-11-15 00:00:00+00:00|HW1|max_filter|1.07|106|
|2018-05-21 00:00:00+00:00|2023-06-18 15:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|4260|
|2021-10-15 00:00:00+00:00|2023-06-18 15:00:00+00:00|HW1|max_filter|1.5|11|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|HW2|time_shift|48.0|4|
|1990-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|HW2|add|-0.5|0|
|2001-05-31 21:00:00+00:00|2023-06-18 15:00:00+00:00|HW2|hampel_filter|3.0|14235|
|2007-02-12 00:00:00+00:00|2007-04-16 00:00:00+00:00|HW2|min_filter|3.2|86|
|2007-08-01 00:00:00+00:00|2007-12-16 00:00:00+00:00|HW2|min_filter|3.22|0|
|2008-02-01 00:00:00+00:00|2008-04-30 00:00:00+00:00|HW2|min_filter|3.0|807|
|2011-05-31 21:00:00+00:00|2023-06-18 15:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2011-05-31 21:00:00+00:00|2023-01-01 00:00:00+00:00|HW2|min_filter|1.0|9987|
|2011-05-31 21:00:00+00:00|2023-01-01 00:00:00+00:00|HW2|max_filter|5.1|30|
|2011-05-31 21:00:00+00:00|2023-06-18 15:00:00+00:00|HW2|biweekly_upper_range_filter|0.3|6875|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|ISWR|time_shift|48.0|4|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|NR|time_shift|48.0|4|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|OSWR|time_shift|48.0|4|
|2003-01-01 00:00:00+00:00|2018-05-22 00:00:00+00:00|OSWR|multiply|2.76205|0|
|2011-05-31 00:00:00+00:00|2023-06-18 15:00:00+00:00|OSWR|multiply|0.934|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|P|time_shift|48.0|0|
|1999-05-14 00:00:00+00:00|2000-01-01 00:00:00+00:00|P|add|-30.0|0|
|2000-01-01 00:00:00+00:00|2005-05-26 00:00:00+00:00|P|add|-15.0|0|
|2016-07-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|P|add|-40.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|RH1|time_shift|48.0|4|
|2012-05-09 00:00:00+00:00|2018-05-23 00:00:00+00:00|RH1|swap_with_RH2|0.0|-360|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|RH2|time_shift|48.0|0|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TA1|time_shift|48.0|4|
|2017-12-15 00:00:00+00:00|2018-02-16 00:00:00+00:00|TA1|min_filter|-56.6|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TA2|time_shift|48.0|4|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TA3|time_shift|48.0|4|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TA4|time_shift|48.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TA5|time_shift|48.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TS1|time_shift|48.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TS10|time_shift|48.0|4|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS10|max_filter|-22.6|1715|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS10|min_filter|-24.5|97|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TS2|time_shift|48.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TS3|time_shift|48.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TS4|time_shift|48.0|4|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS4|max_filter|-22.6|1690|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS4|min_filter|-24.5|247|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TS5|time_shift|48.0|4|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS5|max_filter|-22.6|1590|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS5|min_filter|-24.5|161|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TS6|time_shift|48.0|4|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS6|max_filter|-22.6|1591|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS6|min_filter|-24.5|8|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TS7|time_shift|48.0|4|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS7|max_filter|-22.6|1593|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS7|min_filter|-24.5|100|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TS8|time_shift|48.0|4|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS8|max_filter|-22.6|1677|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS8|min_filter|-24.5|25|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TS9|time_shift|48.0|4|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS9|max_filter|-22.6|1645|
|2007-01-01 00:00:00+00:00|2013-05-28 00:00:00+00:00|TS9|min_filter|-24.5|72|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|V|time_shift|48.0|4|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|VW1|time_shift|48.0|4|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|VW2|time_shift|48.0|4|
## ROC filter at NASA-U
 
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_ISWR.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_OSWR.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_NR.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TA1.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TA2.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TA3.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TA4.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_RH1.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_RH2.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_VW1.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_VW2.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_DW1.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_DW2.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_P.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_HW1.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_HW2.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_V.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TA5.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TS1.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TS2.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TS3.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TS4.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TS5.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TS6.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TS7.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TS8.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TS9.jpeg)
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1997-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|HS1|add|1.7|0|
|1999-05-13 16:00:00+00:00|2023-06-18 15:00:00+00:00|HS1|add|2.3|0|
|2003-06-02 15:00:00+00:00|2023-06-18 15:00:00+00:00|HS1|add|4.0|0|
|2005-05-25 21:00:00+00:00|2023-06-18 15:00:00+00:00|HS1|add|2.8|0|
|2009-04-20 16:00:00+00:00|2023-06-18 15:00:00+00:00|HS1|add|1.8|0|
|2011-05-31 22:00:00+00:00|2023-06-18 15:00:00+00:00|HS1|add|0.7|0|
|2013-05-25 22:00:00+00:00|2023-06-18 15:00:00+00:00|HS1|add|2.3|0|
|2018-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|HS1|add|2.7|0|
 
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1997-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|HS2|add|2.0|0|
|1999-05-13 16:00:00+00:00|2023-06-18 15:00:00+00:00|HS2|add|1.9|0|
|2003-06-02 15:00:00+00:00|2023-06-18 15:00:00+00:00|HS2|add|4.0|0|
|2005-05-25 21:00:00+00:00|2023-06-18 15:00:00+00:00|HS2|add|2.7|0|
|2009-04-20 16:00:00+00:00|2023-06-18 15:00:00+00:00|HS2|add|2.0|0|
|2011-05-31 22:00:00+00:00|2023-06-18 15:00:00+00:00|HS2|add|0.58|0|
|2013-06-04 00:00:00+00:00|2023-06-18 15:00:00+00:00|HS2|add|2.5|0|
|2018-01-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|HS2|add|2.5|0|
 
![Adjusted and flagged data at NASA-U](figures/L1_data_treatment/NASA-U_HS2.jpeg)
 
Using metadata/interpolated positions/NASA-U_position_interpolated.csv for variable latitude and longitude
Cannot download maintenance summary. Using local file.
# 4 GITS
## Interpolated values filter at GITS
ISWR: 259 samples flagged
OSWR: 325 samples flagged
NR: 2279 samples flagged
TA1: 6821 samples flagged
TA2: 3130 samples flagged
TA3: 6668 samples flagged
TA4: 3687 samples flagged
RH1: 2266 samples flagged
RH2: 916 samples flagged
VW1: 5519 samples flagged
VW2: 5238 samples flagged
DW1: 201 samples flagged
DW2: 1454 samples flagged
P: 2629 samples flagged
TS1: 30 samples flagged
TS7: 20 samples flagged
## Manual flagging of data at GITS
Flagging data:
|start time|end time|variable|
|-|-|-|
|1997-02-15 00:00:00+00:00|1997-05-18 00:00:00+00:00|HW1|
|2002-01-01 00:00:00+00:00|2002-01-24 08:00:00+00:00|HW1|
|2016-04-21 00:00:00+00:00|2016-04-25 00:00:00+00:00|HW1|
|2016-11-01 00:00:00+00:00|2018-01-01 00:00:00+00:00|HW1|
|1997-02-15 00:00:00+00:00|1997-05-18 00:00:00+00:00|HW2|
|2002-01-01 00:00:00+00:00|2002-01-23 00:00:00+00:00|HW2|
|2016-05-23 00:00:00+00:00|2016-04-25 00:00:00+00:00|HW2|
|2015-08-23 00:00:00+00:00|2016-04-06 00:00:00+00:00|HW2|
|2016-10-11 00:00:00+00:00|2018-05-15 00:00:00+00:00|HW2|
|2018-09-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW1|
|1999-01-01 00:00:00+00:00|2002-01-01 00:00:00+00:00|P|
|2011-05-25 00:00:00+00:00|2013-01-01 00:00:00+00:00|P|
|1995-06-07 13:00:00+00:00|2021-08-13 12:00:00+00:00|TS8|
|1995-06-07 13:00:00+00:00|1997-01-01 00:00:00+00:00|RH1|
|1995-06-07 13:00:00+00:00|1997-01-01 00:00:00+00:00|RH2|
|1990-01-01 00:00:00+00:00|1996-07-01 00:00:00+00:00|TA1|
|2006-06-28 00:00:00+00:00|2007-07-05 00:00:00+00:00|TA1|
|2006-06-28 00:00:00+00:00|2007-07-05 00:00:00+00:00|TA2|
|2006-06-28 00:00:00+00:00|2007-07-05 00:00:00+00:00|RH1|
|2013-09-04 00:00:00+00:00|2014-05-21 00:00:00+00:00|TA1|
|2010-01-01 00:00:00+00:00|2012-05-26 00:00:00+00:00|TA1|
|2010-01-01 00:00:00+00:00|2012-05-26 00:00:00+00:00|TA2|
|2010-01-01 00:00:00+00:00|2012-05-26 00:00:00+00:00|TA3|
|2014-04-15 00:00:00+00:00|2014-05-21 00:00:00+00:00|TA3|
|2010-01-01 00:00:00+00:00|2012-05-26 00:00:00+00:00|RH1|
|2020-08-23 00:00:00+00:00|2021-08-30 00:00:00+00:00|RH1|
|2007-01-01 00:00:00+00:00|2014-05-01 00:00:00+00:00|VW2|
|2007-01-01 00:00:00+00:00|2014-05-01 00:00:00+00:00|P|
|1995-01-01 00:00:00+00:00|1996-05-01 00:00:00+00:00|P|
|2016-11-22 00:00:00+00:00|2016-12-29 00:00:00+00:00|VW2|
|2016-11-22 00:00:00+00:00|2016-12-07 00:00:00+00:00|VW1|
|2016-11-22 00:00:00+00:00|2017-01-02 00:00:00+00:00|VW1|
|2012-01-01 00:00:00+00:00|2014-06-01 00:00:00+00:00|DW2|
|2014-01-01 00:00:00+00:00|2014-04-26 00:00:00+00:00|ISWR|
|2010-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS1|
|2010-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS2|
|2010-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS3|
|2010-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS4|
|2010-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS5|
|2010-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS6|
|2010-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS7|
|2010-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS8|
|2010-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS9|
|2010-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS10|
|2005-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS2|
|2005-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS3|
|2005-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TS4|
|2019-10-28 00:00:00+00:00|2021-08-13 12:00:00+00:00|DW2|
|2020-08-10 00:00:00+00:00|2021-08-13 12:00:00+00:00|ISWR|
|2020-08-10 00:00:00+00:00|2021-08-13 12:00:00+00:00|OSWR|
|2020-08-29 00:00:00+00:00|2021-08-13 12:00:00+00:00|TA1|
|2020-08-29 00:00:00+00:00|2021-08-13 12:00:00+00:00|TA2|
|2020-08-29 00:00:00+00:00|2021-08-13 12:00:00+00:00|TA3|
|2020-08-29 00:00:00+00:00|2021-08-13 12:00:00+00:00|RH2|
## Adjusting data at GITS
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|DW1|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|DW2|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|HW1|time_shift|520.0|520|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW1|swap_with_HW2|0.5|15891|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW1|biweekly_upper_range_filter|0.5|5688|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW1|hampel_filter|2.0|2284|
|2019-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW1|max_filter|2.6|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|HW2|time_shift|520.0|503|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW2|max_filter|4.8|496|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|21456|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW2|hampel_filter|2.0|2735|
|2016-05-21 00:00:00+00:00|2019-10-22 00:00:00+00:00|HW2|biweekly_upper_range_filter|0.2|1083|
|2016-05-21 00:00:00+00:00|2016-10-22 00:00:00+00:00|HW2|biweekly_upper_range_filter|0.1|255|
|2019-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW2|max_filter|2.6|1232|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|ISWR|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|NR|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|OSWR|time_shift|520.0|520|
|2012-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|OSWR|multiply|0.934|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|P|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|RH1|time_shift|520.0|520|
|1995-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|RH2|time_shift|520.0|520|
|1995-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TA1|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TA2|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TA3|time_shift|520.0|520|
|1990-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TA3|min_filter|-39.4|7184|
|2005-01-01 00:00:00+00:00|2008-01-01 00:00:00+00:00|TA3|add|-2.8|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TA4|time_shift|520.0|520|
|1990-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TA4|min_filter|-39.4|5789|
|2001-01-01 00:00:00+00:00|2008-01-01 00:00:00+00:00|TA4|add|-2.8|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TA5|time_shift|520.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TS1|time_shift|520.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TS10|time_shift|520.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TS2|time_shift|520.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TS3|time_shift|520.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TS4|time_shift|520.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TS5|time_shift|520.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TS6|time_shift|520.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TS7|time_shift|520.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TS8|time_shift|520.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TS9|time_shift|520.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|V|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|VW1|time_shift|520.0|520|
|1990-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|VW1|max_filter|28.0|3|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|VW2|time_shift|520.0|520|
|1990-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|VW2|max_filter|28.0|3|
## ROC filter at GITS
 
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_ISWR.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_OSWR.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_NR.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TA1.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TA2.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TA3.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TA4.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_RH1.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_RH2.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_VW1.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_VW2.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_DW1.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_DW2.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_P.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_HW1.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_HW2.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_V.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TA5.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TS1.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TS2.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TS3.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TS4.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TS5.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TS6.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TS7.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TS8.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TS9.jpeg)
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1996-05-07 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|0.8|0|
|1997-05-01 11:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|1.0|0|
|1999-05-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|4.5|0|
|2010-05-03 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|9.0|0|
|2014-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|1.25|0|
|2016-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|2.0|0|
 
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1996-05-07 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|0.2|0|
|1997-05-17 11:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|1.4|0|
|1997-05-17 23:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|-0.7|0|
|1999-05-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|4.5|0|
|2010-05-03 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|9.25|0|
|2014-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|2.25|0|
|2016-05-23 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|2.0|0|
 
![Adjusted and flagged data at GITS](figures/L1_data_treatment/GITS_HS2.jpeg)
 
Cannot download maintenance summary. Using local file.
# 5 Humboldt
## Interpolated values filter at Humboldt
ISWR: 148 samples flagged
OSWR: 204 samples flagged
NR: 4156 samples flagged
TA1: 6233 samples flagged
TA2: 6251 samples flagged
TA3: 2590 samples flagged
TA4: 7662 samples flagged
RH1: 499 samples flagged
RH2: 929 samples flagged
VW1: 10619 samples flagged
VW2: 10364 samples flagged
DW1: 534 samples flagged
DW2: 1826 samples flagged
P: 8062 samples flagged
TS1: 70 samples flagged
TS2: 470 samples flagged
TS3: 10 samples flagged
TS4: 10 samples flagged
TS7: 10 samples flagged
TS9: 11 samples flagged
TS10: 55 samples flagged
## Manual flagging of data at Humboldt
Flagging data:
|start time|end time|variable|
|-|-|-|
|1995-06-22 02:00:00+00:00|1997-01-01 00:00:00+00:00|RH1|
|1995-06-22 02:00:00+00:00|1997-01-01 00:00:00+00:00|RH2|
|1990-01-01 00:00:00+00:00|1996-07-01 00:00:00+00:00|TA1|
|1990-01-01 00:00:00+00:00|1996-07-01 00:00:00+00:00|RH1|
|1990-01-01 00:00:00+00:00|1996-07-01 00:00:00+00:00|RH2|
|2007-03-01 00:00:00+00:00|2007-05-04 00:00:00+00:00|TA3|
|2007-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW1|
|2007-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW2|
|2003-05-27 18:00:00+00:00|2003-05-28 14:00:00+00:00|HW2|
|2020-02-17 18:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|
|2019-01-01 00:00:00+00:00|2023-03-05 08:00:00+00:00|NR|
|2010-01-01 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS1|
|2010-01-01 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS2|
|2010-01-01 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS3|
|2010-01-01 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS4|
|2010-01-01 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS5|
|2010-01-01 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS6|
|2010-01-01 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS7|
|2010-01-01 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS8|
|2010-01-01 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS9|
|2010-01-01 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS10|
## Adjusting data at Humboldt
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|DW1|time_shift|2815.0|2815|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|DW1|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|DW1|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|DW1|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|DW1|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|DW1|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|DW1|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|DW1|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|DW1|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|DW1|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|DW2|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|DW2|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|DW2|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|DW2|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|DW2|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|DW2|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|DW2|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|DW2|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|DW2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|DW2|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|HW1|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|HW1|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|HW1|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|HW1|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|HW1|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|HW1|time_shift|5611.0|1270|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|HW1|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|HW1|time_shift|2198.0|840|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|HW1|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|HW1|time_shift|-24.0|25|
|2002-06-02 04:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|add|-0.5|0|
|2003-05-22 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|add|1.0|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|add|-1.8|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|11560|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|hampel_filter|2.0|2382|
|2023-01-01 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|add|-1.2|0|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|HW2|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|HW2|time_shift|2954.0|1936|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|HW2|time_shift|5604.0|3216|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|HW2|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|HW2|time_shift|2954.0|1045|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|HW2|time_shift|5611.0|1269|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|HW2|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|HW2|time_shift|2198.0|839|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|HW2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|HW2|time_shift|-24.0|25|
|2002-03-01 12:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|add|0.4|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|add|-1.0|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|biweekly_upper_range_filter|0.3|10463|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|hampel_filter|2.0|3776|
|2011-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|add|1.0|0|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|ISWR|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|ISWR|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|ISWR|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|ISWR|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|ISWR|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|ISWR|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|ISWR|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|ISWR|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|ISWR|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|ISWR|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|NR|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|NR|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|NR|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|NR|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|NR|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|NR|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|NR|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|NR|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|NR|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|NR|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|OSWR|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|OSWR|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|OSWR|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|OSWR|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|OSWR|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|OSWR|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|OSWR|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|OSWR|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|OSWR|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|OSWR|time_shift|-24.0|25|
|2011-06-01 00:00:00+00:00|2023-03-05 08:00:00+00:00|OSWR|multiply|0.93|0|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|P|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|P|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|P|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|P|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|P|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|P|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|P|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|P|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|P|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|P|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|RH1|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|RH1|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|RH1|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|RH1|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|RH1|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|RH1|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|RH1|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|RH1|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|RH1|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|RH1|time_shift|-24.0|25|
|1999-01-01 00:00:00+00:00|2023-03-05 08:00:00+00:00|RH1|swap_with_RH2|0.0|24306|
|1995-01-01 00:00:00+00:00|2012-08-19 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|RH2|time_shift|2815.0|0|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|RH2|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|RH2|time_shift|5604.0|2825|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|RH2|time_shift|2954.0|2872|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|RH2|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|RH2|time_shift|5611.0|1321|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|RH2|time_shift|2943.0|2929|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|RH2|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|RH2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|RH2|time_shift|-24.0|25|
|1995-01-01 00:00:00+00:00|2012-08-19 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TA1|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TA1|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TA1|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TA1|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TA1|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TA1|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TA1|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TA1|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TA1|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TA1|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TA2|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TA2|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TA2|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TA2|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TA2|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TA2|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TA2|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TA2|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TA2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TA2|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TA3|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TA3|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TA3|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TA3|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TA3|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TA3|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TA3|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TA3|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TA3|time_shift|-48.0|0|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TA3|time_shift|-24.0|0|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TA4|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TA4|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TA4|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TA4|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TA4|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TA4|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TA4|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TA4|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TA4|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TA4|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TS1|time_shift|2815.0|0|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TS1|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS1|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS1|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS1|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS1|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS1|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS1|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS1|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS1|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TS10|time_shift|2815.0|0|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TS10|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS10|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS10|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS10|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS10|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS10|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS10|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS10|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS10|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TS2|time_shift|2815.0|0|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TS2|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS2|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS2|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS2|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS2|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS2|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS2|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS2|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TS3|time_shift|2815.0|0|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TS3|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS3|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS3|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS3|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS3|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS3|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS3|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS3|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS3|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TS4|time_shift|2815.0|0|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TS4|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS4|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS4|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS4|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS4|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS4|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS4|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS4|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS4|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TS5|time_shift|2815.0|0|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TS5|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS5|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS5|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS5|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS5|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS5|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS5|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS5|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS5|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TS6|time_shift|2815.0|0|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TS6|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS6|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS6|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS6|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS6|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS6|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS6|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS6|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS6|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TS7|time_shift|2815.0|0|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TS7|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS7|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS7|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS7|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS7|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS7|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS7|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS7|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS7|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TS8|time_shift|2815.0|0|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TS8|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS8|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS8|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS8|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS8|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS8|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS8|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS8|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS8|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|TS9|time_shift|2815.0|0|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|TS9|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS9|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS9|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS9|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS9|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS9|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS9|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS9|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS9|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|V|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|V|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|V|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|V|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|V|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|V|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|V|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|V|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|V|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|V|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|VW1|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|VW1|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|VW1|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|VW1|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|VW1|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|VW1|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|VW1|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|VW1|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|VW1|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|VW1|time_shift|-24.0|25|
|2022-12-01 00:00:00+00:00|2023-06-16 00:00:00+00:00|VW2|time_shift|2815.0|351|
|2021-12-01 00:00:00+00:00|2022-02-23 06:00:00+00:00|VW2|time_shift|2954.0|1938|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|VW2|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|VW2|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|VW2|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|VW2|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|VW2|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|VW2|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|VW2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|VW2|time_shift|-24.0|25|
## ROC filter at Humboldt
 
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_ISWR.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_OSWR.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_NR.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TA1.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TA2.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TA3.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TA4.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_RH1.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_RH2.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_VW1.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_VW2.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_DW1.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_DW2.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_P.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_HW1.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_HW2.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_V.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TS1.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TS2.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TS3.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TS4.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TS5.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TS6.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TS7.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TS8.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TS9.jpeg)
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1999-05-04 18:00:00+00:00|2023-10-11 07:00:00+00:00|HS1|add|1.2|0|
|2003-05-22 00:00:00+00:00|2023-10-11 07:00:00+00:00|HS1|add|3.0|0|
|2010-03-01 00:00:00+00:00|2023-10-11 07:00:00+00:00|HS1|add|3.0|0|
|2015-05-20 00:00:00+00:00|2023-10-11 07:00:00+00:00|HS1|add|2.45|0|
 
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1999-05-04 18:00:00+00:00|2023-10-11 07:00:00+00:00|HS2|add|0.6|0|
|2003-05-22 00:00:00+00:00|2023-10-11 07:00:00+00:00|HS2|add|3.0|0|
|2010-03-01 00:00:00+00:00|2023-10-11 07:00:00+00:00|HS2|add|3.0|0|
|2011-02-25 00:00:00+00:00|2023-10-11 07:00:00+00:00|HS2|add|-1.0|0|
|2011-05-15 00:00:00+00:00|2023-10-11 07:00:00+00:00|HS2|add|1.0|0|
|2015-05-20 21:00:00+00:00|2023-10-11 07:00:00+00:00|HS2|add|2.45|0|
 
![Adjusted and flagged data at Humboldt](figures/L1_data_treatment/Humboldt_HS2.jpeg)
 
Using metadata/interpolated positions/Humboldt_position_interpolated.csv for variable latitude and longitude
Cannot download maintenance summary. Using local file.
# 6 Summit
## Interpolated values filter at Summit
ISWR: 207 samples flagged
OSWR: 186 samples flagged
NR: 406 samples flagged
TA1: 3750 samples flagged
TA2: 3417 samples flagged
TA3: 1326 samples flagged
TA4: 1784 samples flagged
RH1: 2035 samples flagged
RH2: 2035 samples flagged
VW1: 9026 samples flagged
VW2: 8195 samples flagged
DW1: 774 samples flagged
DW2: 888 samples flagged
P: 4710 samples flagged
TA5: 13 samples flagged
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
## Manual flagging of data at Summit
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
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS1|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS2|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS3|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS4|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS5|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS6|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS7|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS8|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS9|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS10|
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
## Adjusting data at Summit
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2001-06-15 16:00:00+00:00|2003-12-13 17:00:00+00:00|HW1|add|0.78|0|
|2003-12-13 17:05:00+00:00|2005-05-04 19:00:00+00:00|HW1|add|0.37|0|
|2004-12-13 17:05:00+00:00|2005-07-04 19:00:00+00:00|HW1|min_filter|-4.0|0|
|2005-05-26 07:00:00+00:00|2008-09-13 01:05:00+00:00|HW1|add|0.72|0|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW1|hampel_filter|1.0|2876|
|2009-05-15 00:00:00+00:00|2022-10-07 03:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2022-10-07 03:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|13009|
|2009-05-15 00:00:00+00:00|2022-10-07 03:00:00+00:00|HW1|hampel_filter|2.0|5776|
|2009-05-19 19:00:00+00:00|2010-08-06 23:05:00+00:00|HW1|add|-0.39|0|
|2010-08-16 19:00:00+00:00|2022-10-07 03:00:00+00:00|HW1|add|-0.4|0|
|2001-06-15 16:00:00+00:00|2003-12-13 17:00:00+00:00|HW2|add|0.62|0|
|2003-12-13 17:05:00+00:00|2004-03-02 16:05:00+00:00|HW2|add|0.84|0|
|2004-08-19 17:05:00+00:00|2005-05-04 21:00:00+00:00|HW2|add|0.84|0|
|2005-05-26 07:00:00+00:00|2010-08-06 23:05:00+00:00|HW2|add|0.39|0|
|2005-10-08 15:00:00+00:00|2006-03-17 14:05:00+00:00|HW2|add|0.87|0|
|2007-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW2|hampel_filter|1.0|5736|
|2009-05-15 00:00:00+00:00|2022-10-07 03:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2022-10-07 03:00:00+00:00|HW2|biweekly_upper_range_filter|0.3|18067|
|2009-05-15 00:00:00+00:00|2022-10-07 03:00:00+00:00|HW2|hampel_filter|2.0|4119|
|2009-05-19 19:00:00+00:00|2010-08-06 23:05:00+00:00|HW2|add|-0.39|0|
|2010-08-16 19:00:00+00:00|2022-10-07 03:00:00+00:00|HW2|add|0.3|0|
|2009-05-19 00:00:00+00:00|2022-10-07 03:00:00+00:00|OSWR|multiply|0.91|0|
|2016-05-22 00:00:00+00:00|2022-10-07 03:00:00+00:00|P|add|-61.0|0|
|2019-04-28 00:00:00+00:00|2022-10-07 03:00:00+00:00|P|add|38.0|0|
|2019-04-29 00:00:00+00:00|2022-10-07 03:00:00+00:00|P|add|21.0|0|
|2022-04-29 00:00:00+00:00|2022-10-07 03:00:00+00:00|P|add|-61.0|0|
|2018-05-15 00:00:00+00:00|2022-10-07 03:00:00+00:00|RH1|swap_with_RH2|0.0|7|
|1996-01-01 00:00:00+00:00|2009-05-19 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1996-01-01 00:00:00+00:00|2009-05-19 00:00:00+00:00|RH2|ice_to_water|0.0|0|
## ROC filter at Summit
 
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
 
Cannot download maintenance summary. Using local file.
# 7 Tunu-N
## Interpolated values filter at Tunu-N
ISWR: 115 samples flagged
OSWR: 110 samples flagged
NR: 1543 samples flagged
TA1: 3171 samples flagged
TA2: 3053 samples flagged
TA3: 1956 samples flagged
TA4: 2268 samples flagged
RH1: 480 samples flagged
RH2: 460 samples flagged
VW1: 8563 samples flagged
VW2: 8087 samples flagged
DW1: 1065 samples flagged
DW2: 1195 samples flagged
P: 5143 samples flagged
TS1: 562 samples flagged
TS2: 897 samples flagged
TS3: 150 samples flagged
TS4: 283 samples flagged
TS5: 186 samples flagged
TS6: 161 samples flagged
TS7: 374 samples flagged
TS8: 967 samples flagged
TS9: 734 samples flagged
TS10: 2437 samples flagged
## Manual flagging of data at Tunu-N
Flagging data:
|start time|end time|variable|
|-|-|-|
|2011-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|VW1|
|2011-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|TA1|
|2011-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|TA2|
|2011-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|TA3|
|2011-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|TA4|
|2014-01-01 00:00:00+00:00|2014-04-26 00:00:00+00:00|ISWR|
|2011-06-10 00:00:00+00:00|2013-05-23 00:00:00+00:00|HW1|
|2017-01-16 00:00:00+00:00|2017-01-30 00:00:00+00:00|HW1|
|2002-02-15 00:00:00+00:00|2002-02-16 00:00:00+00:00|HW2|
|2011-06-10 00:00:00+00:00|2013-05-23 00:00:00+00:00|HW2|
|2008-04-30 00:00:00+00:00|2008-05-01 00:00:00+00:00|HW2|
|2013-12-07 00:00:00+00:00|2013-12-08 00:00:00+00:00|HW2|
|2014-05-05 00:00:00+00:00|2014-05-19 00:00:00+00:00|HW2|
|2013-01-10 00:00:00+00:00|2023-06-20 13:00:00+00:00|DW2|
|2020-01-10 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|
|2020-01-10 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|
|2015-05-21 00:00:00+00:00|2023-06-20 13:00:00+00:00|NR|
|1996-05-16 18:00:00+00:00|1996-05-18 12:00:00+00:00|TS1|
|1996-05-16 18:00:00+00:00|1996-05-18 12:00:00+00:00|TS2|
|1996-05-16 18:00:00+00:00|1996-05-18 12:00:00+00:00|TS3|
|1996-05-16 18:00:00+00:00|1996-05-18 12:00:00+00:00|TS4|
|1996-05-16 18:00:00+00:00|1996-05-18 12:00:00+00:00|TS5|
|1996-05-16 18:00:00+00:00|1996-05-18 12:00:00+00:00|TS6|
|1996-05-16 18:00:00+00:00|1996-05-18 12:00:00+00:00|TS7|
|1996-05-16 18:00:00+00:00|1996-05-18 12:00:00+00:00|TS8|
|1996-05-16 18:00:00+00:00|1996-05-18 12:00:00+00:00|TS9|
|1996-05-16 18:00:00+00:00|1996-05-18 12:00:00+00:00|TS10|
|1996-05-16 18:00:00+00:00|1996-05-16 20:00:00+00:00|TA1|
|1996-05-16 18:00:00+00:00|1996-05-16 20:00:00+00:00|TA2|
|1996-05-16 18:00:00+00:00|1996-05-16 20:00:00+00:00|TA3|
|1996-05-16 18:00:00+00:00|1996-05-16 20:00:00+00:00|TA4|
|1996-05-16 18:00:00+00:00|1996-05-16 20:00:00+00:00|TA5|
## Adjusting data at Tunu-N
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2011-06-01 00:00:00+00:00|2012-06-01 00:00:00+00:00|DW1|rotate|90.0|0|
|2011-06-01 00:00:00+00:00|2012-06-01 00:00:00+00:00|DW2|rotate|90.0|0|
|1996-05-16 18:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|min_filter|0.05|37053|
|2002-02-15 00:00:00+00:00|2002-02-16 00:00:00+00:00|HW1|max_filter|1.8|4|
|2008-04-28 00:00:00+00:00|2008-05-12 00:00:00+00:00|HW1|min_filter|3.42|71|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|biweekly_upper_range_filter|0.2|9155|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|hampel_filter|2.0|3757|
|2013-01-01 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|add|-0.2|0|
|2017-01-01 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|min_filter|0.6|584|
|1996-05-16 18:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|min_filter|0.05|8682|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|biweekly_upper_range_filter|0.2|40663|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|hampel_filter|2.0|1656|
|2013-01-01 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|add|1.3|0|
|2015-05-22 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|add|-0.4|0|
|2017-01-01 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|max_filter|3.01|6374|
|2018-05-22 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|add|-0.3|0|
|2021-01-05 00:00:00+00:00|2022-09-09 00:00:00+00:00|P|grad_filter|5.0|0|
|1990-01-01 00:00:00+00:00|2012-01-01 00:00:00+00:00|RH1|swap_with_RH2|0.0|2656|
|1996-01-01 00:00:00+00:00|2011-01-01 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1996-01-01 00:00:00+00:00|2011-01-01 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|1996-05-16 18:00:00+00:00|2023-06-20 13:00:00+00:00|TS1|min_filter|-30.0|856|
|1996-05-16 18:00:00+00:00|2023-06-20 13:00:00+00:00|TS1|min_filter|-30.0|0|
|1996-05-16 18:00:00+00:00|2023-06-20 13:00:00+00:00|TS2|min_filter|-30.0|1456|
|1996-05-16 18:00:00+00:00|2023-06-20 13:00:00+00:00|TS3|min_filter|-30.0|482|
|2004-01-01 00:00:00+00:00|2023-06-20 13:00:00+00:00|TS7|min_filter|-32.0|0|
|2000-01-01 00:00:00+00:00|2023-06-20 13:00:00+00:00|TS8|min_filter|-34.0|287|
|2004-01-01 00:00:00+00:00|2023-06-20 13:00:00+00:00|TS9|min_filter|-34.0|45|
## ROC filter at Tunu-N
 
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_ISWR.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_OSWR.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_NR.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TA1.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TA2.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TA3.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TA4.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_RH1.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_RH2.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_VW1.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_VW2.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_DW1.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_DW2.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_P.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_HW1.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_HW2.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_V.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TS1.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TS2.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TS3.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TS4.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TS5.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TS6.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TS7.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TS8.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TS9.jpeg)
![Adjusted and flagged data at Tunu-N](figures/L1_data_treatment/Tunu-N_TS10.jpeg)
 
Using metadata/interpolated positions/Tunu-N_position_interpolated.csv for variable latitude and longitude
Cannot download maintenance summary. Using local file.
# 8 DYE-2
## Interpolated values filter at DYE-2
ISWR: 194 samples flagged
OSWR: 55 samples flagged
NR: 176 samples flagged
TA1: 142 samples flagged
TA2: 123 samples flagged
TA3: 398 samples flagged
TA4: 171 samples flagged
RH1: 762 samples flagged
RH2: 1045 samples flagged
VW1: 5570 samples flagged
VW2: 5018 samples flagged
DW1: 631 samples flagged
DW2: 642 samples flagged
P: 2918 samples flagged
TA5: 31 samples flagged
TS1: 274 samples flagged
TS2: 208 samples flagged
TS3: 110 samples flagged
TS4: 82 samples flagged
TS5: 43 samples flagged
TS6: 31 samples flagged
TS7: 10 samples flagged
TS8: 12 samples flagged
TS9: 999 samples flagged
TS10: 131 samples flagged
## Manual flagging of data at DYE-2
Flagging data:
|start time|end time|variable|
|-|-|-|
|2002-05-19 01:00:00+00:00|2003-05-09 20:00:00+00:00|HW1|
|2015-06-07 01:00:00+00:00|2018-05-07 00:00:00+00:00|HW1|
|2002-01-01 01:00:00+00:00|2003-05-09 20:00:00+00:00|HW2|
|2010-03-25 01:00:00+00:00|2014-05-23 00:00:00+00:00|HW2|
|2018-06-01 01:00:00+00:00|2019-05-20 00:00:00+00:00|HW2|
|2018-06-01 01:00:00+00:00|2019-05-20 00:00:00+00:00|HW2|
|2022-09-23 01:00:00+00:00|2023-06-14 12:00:00+00:00|HW2|
|1999-10-15 01:00:00+00:00|2000-05-15 00:00:00+00:00|TA3|
|2009-06-15 01:00:00+00:00|2010-05-02 00:00:00+00:00|TA3|
|2018-09-27 01:00:00+00:00|2018-10-05 00:00:00+00:00|TA3|
|2021-06-15 13:00:00+00:00|2023-06-14 12:00:00+00:00|TA3|
|2019-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|NR|
Warning: OSR not found
|2004-06-15 01:00:00+00:00|2004-08-25 00:00:00+00:00|ISWR|
|2011-05-26 09:00:00+00:00|2013-12-28 00:00:00+00:00|P|
|2010-05-21 07:00:02+00:00|2010-09-25 00:00:00+00:00|P|
|1996-09-14 22:00:00+00:00|1996-10-10 00:00:00+00:00|TA4|
|2009-05-19 21:00:00+00:00|2009-07-19 00:00:00+00:00|TA4|
|2009-09-09 12:00:00+00:00|2010-05-02 00:00:00+00:00|RH1|
|2010-02-09 12:00:00+00:00|2010-05-02 00:00:00+00:00|RH2|
|2012-11-06 22:00:00+00:00|2013-08-14 00:00:00+00:00|RH2|
|2013-10-27 07:59:57+00:00|2014-05-20 00:00:00+00:00|RH2|
|2013-06-13 01:00:00+00:00|2014-10-26 00:00:00+00:00|P|
|2002-01-14 10:00:00+00:00|2003-04-29 00:00:00+00:00|P|
|1999-04-19 21:00:00+00:00|1999-10-17 00:00:00+00:00|RH1|
|2012-02-11 04:59:00+00:00|2012-11-06 00:00:00+00:00|RH2|
|2012-05-07 18:00:00+00:00|2012-05-12 00:00:00+00:00|ISWR|
|2004-05-09 15:00:00+00:00|2005-06-10 00:00:00+00:00|ISWR|
|2004-05-09 15:00:00+00:00|2005-06-10 00:00:00+00:00|OSWR|
|2016-01-01 00:00:00+00:00|2018-01-01 00:00:00+00:00|VW2|
|2016-01-01 00:00:00+00:00|2018-01-01 00:00:00+00:00|RH2|
|2021-06-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|RH1|
|2010-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|RH2|
|2022-06-15 00:00:00+00:00|2023-06-14 12:00:00+00:00|P|
|2017-06-15 00:00:00+00:00|2023-06-14 12:00:00+00:00|VW2|
|2010-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TS1|
|2010-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TS2|
|2010-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TS3|
|2010-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TS4|
|2010-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TS5|
|2010-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TS6|
|2010-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TS7|
|2010-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TS8|
|2010-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TS9|
|2010-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TS10|
|2001-03-10 00:00:00+00:00|2001-04-20 00:00:00+00:00|TS5|
|1999-12-01 00:00:00+00:00|1999-12-10 00:00:00+00:00|TS9|
|2000-05-01 00:00:00+00:00|2001-04-17 00:00:00+00:00|TS9|
|2000-05-01 00:00:00+00:00|2001-04-17 00:00:00+00:00|TS10|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS1|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS2|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS3|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS4|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS5|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS6|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS7|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS8|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS9|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS10|
## Adjusting data at DYE-2
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1999-12-29 00:00:00+00:00|1999-12-31 00:00:00+00:00|HW1|min_filter|0.63|20|
|2001-06-04 00:00:00+00:00|2001-06-06 00:00:00+00:00|HW1|min_filter|1.45|1|
|2001-06-15 00:00:00+00:00|2002-05-20 12:00:00+00:00|HW1|add|-1.5|0|
|2009-05-16 00:00:00+00:00|2023-06-14 12:00:00+00:00|HW1|air_temp_sonic_correction|0.0|10|
|2009-05-16 00:00:00+00:00|2010-01-01 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.15|626|
|2009-05-16 00:00:00+00:00|2022-09-20 00:00:00+00:00|HW1|hampel_filter|2.0|8419|
|2010-01-01 00:00:00+00:00|2010-05-12 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|345|
|2010-05-10 00:00:00+00:00|2022-09-20 00:00:00+00:00|HW1|min_filter|1.4|26366|
|2010-05-12 00:00:00+00:00|2023-09-20 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|2196|
|1999-12-29 00:00:00+00:00|1999-12-31 00:00:00+00:00|HW2|min_filter|1.75|20|
|2001-06-04 00:00:00+00:00|2001-06-06 00:00:00+00:00|HW2|max_filter|2.7|4|
|2001-06-15 00:00:00+00:00|2002-05-20 12:00:00+00:00|HW2|add|-0.86|0|
|2003-05-10 00:00:00+00:00|2004-06-13 00:00:00+00:00|HW2|add|0.49|0|
|2009-05-16 00:00:00+00:00|2023-06-14 12:00:00+00:00|HW2|air_temp_sonic_correction|0.0|9|
|2009-05-16 00:00:00+00:00|2010-05-12 00:00:00+00:00|HW2|biweekly_upper_range_filter|0.2|443|
|2009-05-16 00:00:00+00:00|2020-09-20 00:00:00+00:00|HW2|hampel_filter|2.0|5701|
|2010-05-12 00:00:00+00:00|2023-09-20 00:00:00+00:00|HW2|biweekly_upper_range_filter|0.4|11468|
|2017-05-21 00:00:00+00:00|2022-09-20 00:00:00+00:00|HW2|min_filter|1.8|4550|
|2018-10-01 00:00:00+00:00|2022-12-31 00:00:00+00:00|HW2|max_filter|100.0|1|
|2009-05-16 00:00:00+00:00|2023-06-14 12:00:00+00:00|OSWR|multiply|0.934|0|
|1996-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1996-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|1990-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TA1|min_filter|-80.0|10|
|2019-10-01 00:00:00+00:00|2022-12-31 00:00:00+00:00|TA1|max_filter|4.0|0|
|2019-10-01 00:00:00+00:00|2022-12-31 00:00:00+00:00|TA2|max_filter|4.0|0|
|1990-01-01 00:00:00+00:00|2023-06-14 12:00:00+00:00|TS9|min_filter|-20.0|51355|
## ROC filter at DYE-2
 
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_ISWR.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_OSWR.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_NR.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TA1.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TA2.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TA3.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TA4.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_RH1.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_RH2.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_VW1.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_VW2.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_DW1.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_DW2.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_P.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_HW1.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_HW2.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_V.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TA5.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TS1.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TS2.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TS3.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TS4.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TS5.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TS6.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TS7.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TS8.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TS9.jpeg)
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-04-26 17:00:00+00:00|2023-06-14 12:00:00+00:00|HS1|add|1.24|0|
|2000-05-13 00:00:00+00:00|2023-06-14 12:00:00+00:00|HS1|add|2.4|0|
|2003-05-09 00:00:00+00:00|2023-06-14 12:00:00+00:00|HS1|add|4.0|0|
|2006-05-07 16:00:00+00:00|2023-06-14 12:00:00+00:00|HS1|add|2.5|0|
|2009-05-16 20:00:00+00:00|2023-06-14 12:00:00+00:00|HS1|add|0.5|0|
|2010-05-01 03:00:00+00:00|2023-06-14 12:00:00+00:00|HS1|add|2.6|0|
|2017-05-22 20:00:00+00:00|2023-06-14 12:00:00+00:00|HS1|add|2.3|0|
|2021-06-15 10:00:00+00:00|2023-06-14 12:00:00+00:00|HS1|add|2.1|0|
 
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-04-26 17:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|0.9|0|
|2000-05-13 00:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|2.45|0|
|2003-05-09 00:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|3.65|0|
|2006-05-07 16:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|2.5|0|
|2010-05-01 03:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|2.6|0|
|2017-05-22 20:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|2.5|0|
|2021-06-15 10:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|2.1|0|
 
![Adjusted and flagged data at DYE-2](figures/L1_data_treatment/DYE-2_HS2.jpeg)
 
Using metadata/interpolated positions/DYE-2_position_interpolated.csv for variable latitude and longitude
Cannot download maintenance summary. Using local file.
# 10 Saddle
## Interpolated values filter at Saddle
ISWR: 31 samples flagged
OSWR: 43 samples flagged
NR: 402 samples flagged
TA1: 598 samples flagged
TA2: 1702 samples flagged
TA3: 1231 samples flagged
TA4: 549 samples flagged
RH1: 821 samples flagged
RH2: 841 samples flagged
VW1: 5200 samples flagged
VW2: 4708 samples flagged
DW1: 752 samples flagged
DW2: 873 samples flagged
P: 3822 samples flagged
TA5: 24 samples flagged
TS1: 261 samples flagged
TS2: 220 samples flagged
TS3: 237 samples flagged
TS4: 62 samples flagged
TS5: 32 samples flagged
TS6: 20 samples flagged
TS7: 21 samples flagged
TS8: 10 samples flagged
TS9: 21 samples flagged
TS10: 96 samples flagged
## Manual flagging of data at Saddle
Flagging data:
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|RH1|
|2010-01-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|RH2|
|2010-01-01 00:00:00+00:00|2016-01-01 00:00:00+00:00|TA1|
|2010-01-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|RH2|
|2009-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|VW1|
|2009-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|VW2|
|2005-05-14 14:00:00+00:00|2005-05-26 16:00:00+00:00|HW2|
|2012-09-18 00:00:00+00:00|2013-05-19 00:00:00+00:00|HW2|
|2014-10-09 00:00:00+00:00|2016-05-15 00:00:00+00:00|HW1|
|2017-08-16 00:00:00+00:00|2018-05-26 00:00:00+00:00|HW1|
|2019-12-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW1|
|2005-05-14 00:00:00+00:00|2005-05-26 00:00:00+00:00|HW1|
|2010-04-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS1|
|2010-04-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS2|
|2010-04-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS3|
|2010-04-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS4|
|2010-04-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS5|
|2010-04-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS6|
|2010-04-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS7|
|2010-04-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS8|
|2010-04-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS9|
|2010-04-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS10|
|1999-01-01 00:00:00+00:00|2006-05-01 00:00:00+00:00|DW1|
|1999-01-01 00:00:00+00:00|2006-05-01 00:00:00+00:00|DW2|
|2007-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|DW1|
|2007-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|DW2|
|2021-06-14 00:00:00+00:00|2021-10-16 17:00:00+00:00|TA1|
|2021-06-14 00:00:00+00:00|2021-10-16 17:00:00+00:00|TA2|
|2021-06-14 00:00:00+00:00|2021-10-16 17:00:00+00:00|TA3|
|2021-06-14 00:00:00+00:00|2021-10-16 17:00:00+00:00|RH1|
|2021-06-14 00:00:00+00:00|2021-10-16 17:00:00+00:00|VW1|
|2021-06-14 00:00:00+00:00|2021-10-16 17:00:00+00:00|DW1|
|2004-01-03 00:00:00+00:00|2004-06-11 00:00:00+00:00|TA1|
|2004-01-03 00:00:00+00:00|2004-06-11 00:00:00+00:00|VW1|
|2004-01-03 00:00:00+00:00|2004-06-11 00:00:00+00:00|TA3|
|2004-01-03 00:00:00+00:00|2004-06-11 00:00:00+00:00|RH1|
## Adjusting data at Saddle
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2005-05-26 17:00:00+00:00|2007-05-27 17:00:00+00:00|HW1|add|-2.5|0|
|2009-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2019-09-03 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.5|19739|
|2009-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW1|hampel_filter|2.0|2427|
|2019-09-03 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW1|max_filter|1.4|3959|
|2019-09-03 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW1|min_filter|1.08|6963|
|2004-06-12 08:00:00+00:00|2004-10-14 13:00:00+00:00|HW2|add|2.5|0|
|2005-01-30 16:00:00+00:00|2005-03-28 15:00:00+00:00|HW2|add|2.5|0|
|2009-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|17172|
|2009-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW2|hampel_filter|2.0|1092|
|2019-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW2|min_filter|0.5|3215|
|2010-04-30 00:00:00+00:00|2021-10-16 17:00:00+00:00|OSWR|multiply|0.934|0|
|1996-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1996-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|1990-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TA1|swap_with_TA2|0.0|-8682|
|2000-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TA1|swap_with_TA2|0.0|-30509|
## ROC filter at Saddle
 
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_ISWR.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_OSWR.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_NR.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TA1.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TA2.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TA3.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TA4.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_RH1.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_RH2.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_VW1.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_VW2.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_DW1.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_DW2.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_P.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_HW1.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_HW2.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_V.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TA5.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TS1.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TS2.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TS3.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TS4.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TS5.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TS6.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TS7.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TS8.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TS9.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-04-17 14:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|0.4|0|
|1999-04-16 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|2.1|0|
|2001-06-05 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|2.6|0|
|2002-06-07 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|0.5|0|
|2004-06-12 13:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|2.5|0|
|2008-04-28 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|2.5|0|
|2010-01-07 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|4.0|0|
|2014-05-21 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|2.5|0|
|2018-04-24 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|1.5|0|
 
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1999-04-16 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|2.5|0|
|2001-06-05 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|2.5|0|
|2001-12-25 01:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|-1.0|0|
|2004-06-12 08:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|5.0|0|
|2010-01-07 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|4.0|0|
|2014-05-24 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|4.0|0|
|2018-03-01 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|2.0|0|
 
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_HS2.jpeg)
 
Cannot download maintenance summary. Using local file.
# 11 South Dome
## Interpolated values filter at South Dome
ISWR: 293 samples flagged
OSWR: 191 samples flagged
NR: 278 samples flagged
TA1: 3096 samples flagged
TA2: 678 samples flagged
TA3: 1505 samples flagged
TA4: 483 samples flagged
RH1: 1261 samples flagged
RH2: 685 samples flagged
VW1: 4044 samples flagged
VW2: 3703 samples flagged
DW1: 694 samples flagged
DW2: 565 samples flagged
P: 8046 samples flagged
TA5: 1983 samples flagged
TS1: 397 samples flagged
TS2: 105 samples flagged
TS3: 49 samples flagged
TS4: 485 samples flagged
TS5: 38 samples flagged
TS6: 164 samples flagged
TS7: 40 samples flagged
TS8: 11 samples flagged
TS9: 157 samples flagged
TS10: 112 samples flagged
## Manual flagging of data at South Dome
Flagging data:
|start time|end time|variable|
|-|-|-|
|2000-10-01 00:00:00+00:00|2013-05-21 00:00:00+00:00|P|
|1996-01-01 00:00:00+00:00|1999-06-01 00:00:00+00:00|TA4|
|2010-05-01 00:00:00+00:00|2011-06-01 00:00:00+00:00|TA4|
|2010-12-18 00:00:00+00:00|2011-06-01 00:00:00+00:00|TA1|
|2010-05-01 00:00:00+00:00|2011-06-01 00:00:00+00:00|TA2|
|2011-11-01 00:00:00+00:00|2012-03-12 00:00:00+00:00|HW1|
|2012-09-01 00:00:00+00:00|2014-05-12 00:00:00+00:00|HW1|
|2018-01-01 00:00:00+00:00|2018-05-12 00:00:00+00:00|HW1|
|1996-01-01 00:00:00+00:00|1999-06-01 00:00:00+00:00|RH2|
|2010-05-01 00:00:00+00:00|2011-06-01 00:00:00+00:00|RH2|
|2017-08-26 00:00:00+00:00|2021-06-21 16:00:00+00:00|HW1|
|2010-10-01 00:00:00+00:00|2010-12-01 00:00:00+00:00|HW1|
|2011-10-13 00:00:00+00:00|2012-10-01 00:00:00+00:00|HW1|
|2020-11-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TA1|
|2020-11-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TA3|
|2019-03-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|VW1|
|2019-03-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|DW1|
|2019-03-01 00:00:00+00:00|2019-05-15 00:00:00+00:00|TA3|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS1|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS2|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS3|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS4|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS5|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS6|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS7|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS8|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS9|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS10|
## Adjusting data at South Dome
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1995-05-26 20:00:00+00:00|2021-06-21 16:00:00+00:00|HW1|max_filter|20.0|1|
|1996-05-15 00:00:00+00:00|2021-06-21 16:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2021-06-21 16:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|58166|
|2009-05-15 00:00:00+00:00|2021-06-21 16:00:00+00:00|HW1|hampel_filter|2.0|1032|
|1995-05-26 20:00:00+00:00|2021-06-21 16:00:00+00:00|HW2|max_filter|20.0|1|
|1996-05-15 00:00:00+00:00|2021-06-21 16:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2021-06-21 16:00:00+00:00|HW2|biweekly_upper_range_filter|0.3|11549|
|2009-05-15 00:00:00+00:00|2021-06-21 16:00:00+00:00|HW2|hampel_filter|2.0|82|
|2009-05-15 00:00:00+00:00|2021-06-21 16:00:00+00:00|OSWR|multiply|0.934|0|
|1996-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1996-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|2007-06-13 16:00:00+00:00|2008-07-01 00:00:00+00:00|TS4|biweekly_upper_range_filter|1.3|1600|
## ROC filter at South Dome
 
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_ISWR.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_OSWR.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_NR.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TA1.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TA2.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TA3.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TA4.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_RH1.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_RH2.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_VW1.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_VW2.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_DW1.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_DW2.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_P.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_HW1.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_HW2.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_V.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TA5.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TS1.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TS2.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TS3.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TS4.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TS5.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TS6.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TS7.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TS8.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TS9.jpeg)
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-04-17 17:00:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|2.35|0|
|1999-04-22 21:30:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|1.55|0|
|2001-06-07 11:00:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|3.0|0|
|2005-05-26 20:00:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|6.0|0|
|2006-07-20 21:30:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|2.1|0|
|2007-04-23 01:00:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|3.4|0|
|2009-05-15 22:00:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|2.0|0|
|2011-05-28 18:00:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|3.0|0|
|2013-05-19 20:00:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|2.6|0|
|2015-05-25 20:00:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|2.5|0|
|2017-05-22 15:00:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|2.3|0|
|2019-05-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|HS1|add|2.0|0|
 
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-04-17 17:00:00+00:00|2021-06-21 16:00:00+00:00|HS2|add|2.4|0|
|1999-04-22 21:30:00+00:00|2021-06-21 16:00:00+00:00|HS2|add|1.55|0|
|2001-06-07 11:00:00+00:00|2021-06-21 16:00:00+00:00|HS2|add|3.0|0|
|2005-05-26 20:00:00+00:00|2021-06-21 16:00:00+00:00|HS2|add|6.0|0|
|2007-04-23 01:00:00+00:00|2021-06-21 16:00:00+00:00|HS2|add|3.4|0|
|2009-05-15 22:00:00+00:00|2021-06-21 16:00:00+00:00|HS2|add|1.5|0|
|2011-05-28 18:00:00+00:00|2021-06-21 16:00:00+00:00|HS2|add|3.0|0|
|2013-05-19 18:00:00+00:00|2021-06-21 16:00:00+00:00|HS2|add|3.0|0|
|2015-05-23 00:00:00+00:00|2021-06-21 16:00:00+00:00|HS2|add|3.0|0|
|2017-05-22 15:00:00+00:00|2021-06-21 16:00:00+00:00|HS2|add|2.3|0|
|2019-05-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|HS2|add|2.0|0|
 
![Adjusted and flagged data at South Dome](figures/L1_data_treatment/SouthDome_HS2.jpeg)
 
Cannot download maintenance summary. Using local file.
# 12 NASA-E
## Interpolated values filter at NASA-E
ISWR: 18 samples flagged
OSWR: 21 samples flagged
NR: 170 samples flagged
TA1: 823 samples flagged
TA2: 726 samples flagged
TA3: 50 samples flagged
TA4: 41 samples flagged
RH1: 140 samples flagged
RH2: 493 samples flagged
VW1: 4196 samples flagged
VW2: 3765 samples flagged
DW1: 922 samples flagged
DW2: 425 samples flagged
P: 4013 samples flagged
TA5: 72 samples flagged
TS1: 678 samples flagged
TS2: 415 samples flagged
TS3: 297 samples flagged
TS4: 407 samples flagged
TS5: 323 samples flagged
TS6: 383 samples flagged
TS7: 356 samples flagged
TS8: 337 samples flagged
TS9: 229 samples flagged
TS10: 302 samples flagged
## Manual flagging of data at NASA-E
Flagging data:
|start time|end time|variable|
|-|-|-|
|2012-02-01 00:00:00+00:00|2013-06-01 00:00:00+00:00|TA3|
|2012-02-01 00:00:00+00:00|2013-06-01 00:00:00+00:00|RH1|
|1998-04-12 00:00:00+00:00|1998-11-15 00:00:00+00:00|TA3|
|2001-06-07 00:00:00+00:00|2001-06-08 00:00:00+00:00|TA4|
|2015-09-29 00:00:00+00:00|2019-07-01 00:00:00+00:00|HW1|
|2016-08-29 00:00:00+00:00|2019-01-01 00:00:00+00:00|HW1|
|2011-06-05 00:00:00+00:00|2019-05-22 00:00:00+00:00|DW2|
|2013-03-14 00:00:00+00:00|2019-05-22 00:00:00+00:00|DW1|
|2013-03-14 00:00:00+00:00|2022-10-07 06:00:00+00:00|VW1|
|2012-12-05 00:00:00+00:00|2013-02-01 00:00:00+00:00|VW2|
|2019-05-22 00:00:00+00:00|2022-10-07 06:00:00+00:00|DW1|
|2011-06-05 00:00:00+00:00|2022-10-07 06:00:00+00:00|TS9|
|2011-06-05 00:00:00+00:00|2022-10-07 06:00:00+00:00|TS10|
## Adjusting data at NASA-E
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2019-05-22 00:00:00+00:00|2022-10-07 06:00:00+00:00|DW2|swap_with_DW1|0.0|1|
|2011-06-02 00:00:00+00:00|2022-10-07 06:00:00+00:00|HW1|swap_with_HW2|nan|-2108|
|2009-05-15 00:00:00+00:00|2022-10-07 06:00:00+00:00|HW1|hampel_filter|2.0|13735|
|2011-05-15 00:00:00+00:00|2019-05-15 00:00:00+00:00|HW1|min_filter|1.5|35174|
|2011-06-02 00:00:00+00:00|2022-10-07 06:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2011-06-02 00:00:00+00:00|2022-10-07 06:00:00+00:00|HW1|biweekly_upper_range_filter|0.2|14933|
|2011-06-02 00:00:00+00:00|2022-10-07 06:00:00+00:00|HW1|hampel_filter|2.0|19|
|2019-01-15 00:00:00+00:00|2019-09-15 00:00:00+00:00|HW1|max_filter|1.5|54|
|2009-05-15 00:00:00+00:00|2022-10-07 06:00:00+00:00|HW2|hampel_filter|2.0|11655|
|2011-06-02 00:00:00+00:00|2022-10-07 06:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2011-06-02 00:00:00+00:00|2022-10-07 06:00:00+00:00|HW2|biweekly_upper_range_filter|0.2|3669|
|2011-06-02 00:00:00+00:00|2022-10-07 06:00:00+00:00|HW2|hampel_filter|2.0|288|
|2014-01-15 00:00:00+00:00|2014-09-15 00:00:00+00:00|HW2|min_filter|1.5|33|
|2017-12-06 00:00:00+00:00|2018-03-25 00:00:00+00:00|HW2|add|2.5|0|
|2011-06-02 00:00:00+00:00|2022-10-07 06:00:00+00:00|OSWR|multiply|0.934|0|
|1996-01-01 00:00:00+00:00|2011-06-01 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1996-01-01 00:00:00+00:00|2011-06-01 00:00:00+00:00|RH2|ice_to_water|0.0|0|
## ROC filter at NASA-E
 
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_ISWR.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_OSWR.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_NR.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TA1.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TA2.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TA3.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TA4.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_RH1.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_RH2.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_VW1.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_VW2.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_DW1.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_DW2.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_P.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_HW1.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_HW2.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_V.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TA5.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TS1.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TS2.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TS3.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TS4.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TS5.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TS6.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TS7.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TS8.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TS9.jpeg)
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2001-06-08 16:00:00+00:00|2022-10-07 06:00:00+00:00|HS1|add|2.5|0|
|2006-05-03 17:00:00+00:00|2022-10-07 06:00:00+00:00|HS1|add|2.4|0|
|2009-05-09 00:00:00+00:00|2022-10-07 06:00:00+00:00|HS1|add|-1.0|0|
|2009-05-09 00:00:00+00:00|2010-04-29 00:00:00+00:00|HS1|add|-0.5|0|
|2015-05-26 03:00:00+00:00|2022-10-07 06:00:00+00:00|HS1|add|2.0|0|
|2021-07-01 00:00:00+00:00|2022-10-07 06:00:00+00:00|HS1|add|0.9|0|
 
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2001-06-08 16:00:00+00:00|2022-10-07 06:00:00+00:00|HS2|add|2.5|0|
|2006-05-03 18:00:00+00:00|2022-10-07 06:00:00+00:00|HS2|add|2.4|0|
|2009-05-09 00:00:00+00:00|2022-10-07 06:00:00+00:00|HS2|add|-1.6|0|
|2011-06-02 00:00:00+00:00|2022-10-07 06:00:00+00:00|HS2|add|0.7|0|
|2015-05-26 03:00:00+00:00|2022-10-07 06:00:00+00:00|HS2|add|2.5|0|
 
![Adjusted and flagged data at NASA-E](figures/L1_data_treatment/NASA-E_HS2.jpeg)
 
Using metadata/interpolated positions/NASA-E_position_interpolated.csv for variable latitude and longitude
Cannot download maintenance summary. Using local file.
# 15 NASA-SE
## Interpolated values filter at NASA-SE
ISWR: 979 samples flagged
OSWR: 482 samples flagged
NR: 35 samples flagged
TA1: 847 samples flagged
TA2: 137 samples flagged
TA3: 749 samples flagged
TA4: 124 samples flagged
RH1: 2475 samples flagged
RH2: 2358 samples flagged
VW1: 5060 samples flagged
VW2: 4357 samples flagged
DW1: 834 samples flagged
DW2: 748 samples flagged
P: 2852 samples flagged
TA5: 380 samples flagged
TS1: 435 samples flagged
TS2: 77 samples flagged
TS3: 13 samples flagged
TS4: 91 samples flagged
TS5: 225 samples flagged
TS6: 106 samples flagged
TS7: 167 samples flagged
TS8: 154 samples flagged
TS9: 109 samples flagged
TS10: 187 samples flagged
## Manual flagging of data at NASA-SE
Flagging data:
|start time|end time|variable|
|-|-|-|
|2012-01-08 00:00:00+00:00|2021-06-01 00:00:00+00:00|TA1|
|2012-01-08 00:00:00+00:00|2021-06-01 00:00:00+00:00|TA2|
|2018-02-15 00:00:00+00:00|2018-05-31 00:00:00+00:00|TA3|
|2009-01-01 00:00:00+00:00|2011-05-19 00:00:00+00:00|HW1|
|2015-07-01 00:00:00+00:00|2016-05-19 00:00:00+00:00|HW1|
|2011-05-29 00:00:00+00:00|2011-05-30 00:00:00+00:00|HW1|
|2011-01-01 00:00:00+00:00|2011-05-29 00:00:00+00:00|HW2|
|2011-11-07 00:00:00+00:00|2011-12-26 00:00:00+00:00|HW2|
|2012-04-01 00:00:00+00:00|2014-05-25 21:00:00+00:00|HW2|
|2016-01-15 00:00:00+00:00|2016-05-19 00:00:00+00:00|HW2|
|2017-08-25 00:00:00+00:00|2018-05-26 00:00:00+00:00|HW2|
|2009-11-01 00:00:00+00:00|2010-04-30 00:00:00+00:00|VW1|
|2019-01-01 00:00:00+00:00|2019-05-26 00:00:00+00:00|VW2|
|2017-11-01 00:00:00+00:00|2019-05-26 00:00:00+00:00|VW1|
|2017-11-01 00:00:00+00:00|2019-05-26 00:00:00+00:00|DW1|
|2010-05-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS1|
|2010-05-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS2|
|2010-05-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS3|
|2010-05-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS4|
|2010-05-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS5|
|2010-05-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS6|
|2010-05-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS7|
|2010-05-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS8|
|2010-05-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS9|
|2010-05-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS10|
## Adjusting data at NASA-SE
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2000-05-16 16:00:00+00:00|2003-05-10 14:00:00+00:00|HW1|add|3.0|0|
|2003-05-10 14:00:00+00:00|2005-05-27 09:00:00+00:00|HW1|add|3.0|0|
|2005-05-27 09:00:00+00:00|2009-05-27 09:00:00+00:00|HW1|add|-1.0|0|
|2009-05-15 00:00:00+00:00|2019-09-26 09:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2019-09-26 09:00:00+00:00|HW1|biweekly_upper_range_filter|0.5|20073|
|2009-05-15 00:00:00+00:00|2019-09-26 09:00:00+00:00|HW1|hampel_filter|2.0|4380|
|2010-04-30 00:00:00+00:00|2019-09-26 09:00:00+00:00|HW1|add|-0.8|0|
|2013-05-01 00:00:00+00:00|2013-07-01 00:00:00+00:00|HW1|min_filter|1.4|216|
|2000-05-16 16:00:00+00:00|2003-05-10 14:00:00+00:00|HW2|add|3.0|0|
|2003-05-10 14:00:00+00:00|2005-05-27 09:00:00+00:00|HW2|add|4.0|0|
|2005-05-27 09:00:00+00:00|2009-04-01 09:00:00+00:00|HW2|add|-1.0|0|
|2009-05-15 00:00:00+00:00|2019-09-26 09:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2019-09-26 09:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|15533|
|2009-05-15 00:00:00+00:00|2019-09-26 09:00:00+00:00|HW2|hampel_filter|2.0|2943|
|2010-04-30 00:00:00+00:00|2019-09-26 09:00:00+00:00|HW2|add|1.5|0|
|2009-04-26 00:00:00+00:00|2019-09-26 09:00:00+00:00|OSWR|multiply|0.934|0|
|2015-01-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|RH1|swap_with_RH2|0.0|0|
|1996-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1996-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|2009-01-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|VW1|swap_with_VW2|0.0|0|
## ROC filter at NASA-SE
 
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_ISWR.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_OSWR.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_NR.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TA1.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TA2.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TA3.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TA4.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_RH1.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_RH2.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_VW1.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_VW2.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_DW1.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_DW2.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_P.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_HW1.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_HW2.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_V.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TA5.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TS1.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TS2.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TS3.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TS4.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TS5.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TS6.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TS7.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TS8.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TS9.jpeg)
![Adjusted and flagged data at NASA-SE](figures/L1_data_treatment/NASA-SE_TS10.jpeg)
 
Using metadata/interpolated positions/NASA-SE_position_interpolated.csv for variable latitude and longitude
Cannot download maintenance summary. Using local file.
# 14 NGRIP
## Interpolated values filter at NGRIP
ISWR: 18 samples flagged
NR: 1399 samples flagged
TA1: 5502 samples flagged
TA2: 3 samples flagged
RH1: 528 samples flagged
RH2: 25 samples flagged
VW1: 31 samples flagged
VW2: 9 samples flagged
DW1: 6 samples flagged
DW2: 3 samples flagged
P: 520 samples flagged
HS1: 2238 samples flagged
HS2: 2844 samples flagged
TS1: 55 samples flagged
TS2: 37 samples flagged
TS3: 58 samples flagged
TS4: 77 samples flagged
TS5: 64 samples flagged
TS6: 32 samples flagged
TS7: 110 samples flagged
TS8: 68 samples flagged
TS9: 42 samples flagged
TS10: 56 samples flagged
## Manual flagging of data at NGRIP
Flagging data:
|start time|end time|variable|
|-|-|-|
|2005-09-01 00:00:00+00:00|2006-01-01 00:00:00+00:00|HS1|
|2005-09-01 00:00:00+00:00|2006-01-01 00:00:00+00:00|HS2|
|2008-01-01 00:00:00+00:00|2010-05-08 13:00:00+00:00|TA1|
|2008-01-01 00:00:00+00:00|2010-05-08 13:00:00+00:00|VW1|
|2008-01-01 00:00:00+00:00|2010-05-08 13:00:00+00:00|RH1|
|2005-11-20 12:00:00+00:00|2005-11-20 13:00:00+00:00|HW1|
|2010-01-27 00:00:00+00:00|2010-04-16 00:00:00+00:00|HW1|
|2010-01-27 00:00:00+00:00|2010-04-16 00:00:00+00:00|HW2|
|2002-10-01 00:00:00+00:00|2003-04-01 00:00:00+00:00|VW1|
|2002-10-01 00:00:00+00:00|2003-04-01 00:00:00+00:00|VW2|
|2002-10-01 00:00:00+00:00|2003-04-01 00:00:00+00:00|DW1|
|2002-10-01 00:00:00+00:00|2003-04-01 00:00:00+00:00|DW2|
## Adjusting data at NGRIP
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2001-07-01 00:00:00+00:00|2010-05-08 13:00:00+00:00|HW1|add|-1.5|0|
|2005-09-01 00:00:00+00:00|2006-01-01 00:00:00+00:00|HW1|add|0.3|0|
|2007-11-16 13:00:00+00:00|2008-04-02 15:00:00+00:00|HW1|add|-1.5|0|
|2009-08-12 19:00:00+00:00|2010-05-08 13:00:00+00:00|HW1|add|-1.5|0|
|2005-09-01 00:00:00+00:00|2006-01-01 00:00:00+00:00|HW2|add|0.3|0|
|2002-06-09 18:00:00+00:00|2006-05-15 00:00:00+00:00|RH1|swap_with_RH2|0.0|0|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH2|ice_to_water|0.0|0|
## ROC filter at NGRIP
 
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_ISWR.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_OSWR.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_NR.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TA1.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TA2.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_RH1.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_RH2.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_VW1.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_VW2.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_DW1.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_DW2.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_P.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_HS1.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_HS2.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_HW1.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_HW2.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TS1.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TS2.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TS3.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TS4.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TS5.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TS6.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TS7.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TS8.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TS9.jpeg)
![Adjusted and flagged data at NGRIP](figures/L1_data_treatment/NGRIP_TS10.jpeg)
 
Cannot download maintenance summary. Using local file.
# 23 NEEM
## Interpolated values filter at NEEM
ISWR: 12 samples flagged
NR: 114 samples flagged
TA1: 2010 samples flagged
TA2: 78 samples flagged
TA3: 1154 samples flagged
TA4: 112 samples flagged
RH1: 403 samples flagged
RH2: 107 samples flagged
VW1: 78 samples flagged
VW2: 47 samples flagged
DW1: 28 samples flagged
DW2: 134 samples flagged
P: 180 samples flagged
TA5: 289 samples flagged
## Manual flagging of data at NEEM
Flagging data:
|start time|end time|variable|
|-|-|-|
|2009-01-01 00:00:00+00:00|2017-01-01 00:00:00+00:00|P|
|2017-02-01 00:00:00+00:00|2018-05-01 00:00:00+00:00|RH1|
|2017-02-01 00:00:00+00:00|2018-05-01 00:00:00+00:00|RH2|
|2017-02-01 00:00:00+00:00|2018-05-09 00:00:00+00:00|TA3|
|2018-05-04 00:00:00+00:00|2018-05-24 00:00:00+00:00|TA4|
|2010-07-15 00:00:00+00:00|2010-12-01 00:00:00+00:00|HW1|
|2010-08-06 00:00:00+00:00|2012-06-18 00:00:00+00:00|HW1|
|2020-01-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|HW1|
|2006-10-04 14:00:00+00:00|2006-10-21 16:00:00+00:00|HW2|
|2010-07-15 00:00:00+00:00|2011-09-24 00:00:00+00:00|HW2|
|2013-02-05 00:00:00+00:00|2013-03-17 00:00:00+00:00|HW2|
|2017-12-26 00:00:00+00:00|2018-04-01 00:00:00+00:00|HW2|
|2019-01-01 00:00:00+00:00|2019-04-10 00:00:00+00:00|HW2|
|2007-06-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TS1|
|2007-06-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TS2|
|2007-06-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TS3|
|2007-06-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TS4|
|2007-06-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TS5|
|2007-06-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TS6|
|2007-06-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TS7|
|2007-06-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TS8|
|2007-06-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TS9|
|2007-06-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TS10|
|2011-01-01 00:00:00+00:00|2011-05-19 00:00:00+00:00|ISWR|
|2011-01-01 00:00:00+00:00|2011-05-19 00:00:00+00:00|OSWR|
|2014-01-01 00:00:00+00:00|2014-05-06 00:00:00+00:00|ISWR|
|2014-01-01 00:00:00+00:00|2014-05-06 00:00:00+00:00|OSWR|
|2016-01-01 00:00:00+00:00|2016-04-16 00:00:00+00:00|ISWR|
|2016-01-01 00:00:00+00:00|2016-04-16 00:00:00+00:00|OSWR|
|2011-06-08 00:00:00+00:00|2011-07-04 00:00:00+00:00|VW2|
|2011-11-05 00:00:00+00:00|2011-11-13 00:00:00+00:00|VW1|
|2011-11-05 00:00:00+00:00|2011-11-13 00:00:00+00:00|VW2|
|2011-11-21 00:00:00+00:00|2012-02-10 00:00:00+00:00|VW1|
|2011-11-21 00:00:00+00:00|2012-02-10 00:00:00+00:00|VW2|
|2017-01-01 00:00:00+00:00|2017-04-01 00:00:00+00:00|VW1|
|2017-01-01 00:00:00+00:00|2017-04-01 00:00:00+00:00|VW2|
|2018-01-01 00:00:00+00:00|2018-04-01 00:00:00+00:00|VW2|
|2022-01-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|RH2|
|2020-11-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TA1|
|2020-11-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|TA3|
|2020-11-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|RH1|
|2020-11-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|VW2|
|2020-11-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|DW2|
|2015-01-01 00:00:00+00:00|2018-05-01 00:00:00+00:00|TA4|
## Adjusting data at NEEM
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2022-04-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|DW1|rotate|-185.0|0|
|2009-05-30 23:00:00+00:00|2022-10-07 05:00:00+00:00|HW1|swap_with_HW2|nan|8|
|2009-05-15 00:00:00+00:00|2022-10-07 05:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2022-10-07 05:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|31041|
|2009-05-15 00:00:00+00:00|2022-10-07 05:00:00+00:00|HW1|min_filter|0.1|5797|
|2009-05-15 00:00:00+00:00|2022-10-07 05:00:00+00:00|HW1|hampel_filter|2.0|5643|
|2011-01-01 00:00:00+00:00|2011-07-01 00:00:00+00:00|HW1|max_filter|0.6|65|
|2013-01-01 00:00:00+00:00|2015-07-01 00:00:00+00:00|HW1|min_filter|0.5|105|
|2009-05-15 00:00:00+00:00|2022-10-07 05:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2022-10-07 05:00:00+00:00|HW2|biweekly_upper_range_filter|0.3|16989|
|2009-05-15 00:00:00+00:00|2022-10-07 05:00:00+00:00|HW2|hampel_filter|2.0|6258|
|2009-05-30 00:00:00+00:00|2022-10-07 05:00:00+00:00|OSWR|multiply|0.934|0|
|2009-05-01 00:00:00+00:00|2022-10-07 05:00:00+00:00|RH1|swap_with_RH2|0.0|-360|
|1996-01-01 00:00:00+00:00|2009-05-15 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1996-01-01 00:00:00+00:00|2009-05-15 00:00:00+00:00|RH2|ice_to_water|0.0|0|
## ROC filter at NEEM
 
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_ISWR.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_OSWR.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_NR.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TA1.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TA2.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TA3.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TA4.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_RH1.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_RH2.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_VW1.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_VW2.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_DW1.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_DW2.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_P.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_HW1.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_HW2.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_V.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TA5.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TS1.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TS2.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TS3.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TS4.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TS5.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TS6.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TS7.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TS8.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TS9.jpeg)
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2008-08-13 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS1|add|1.8|0|
|2009-05-30 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS1|add|-0.5|0|
|2011-07-06 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS1|add|3.0|0|
|2016-05-23 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS1|add|2.2|0|
 
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2008-08-13 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS2|add|1.8|0|
|2009-05-30 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS2|add|-0.5|0|
|2011-07-06 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS2|add|3.0|0|
|2016-05-23 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS2|add|2.5|0|
 
![Adjusted and flagged data at NEEM](figures/L1_data_treatment/NEEM_HS2.jpeg)
 
Using metadata/interpolated positions/NEEM_position_interpolated.csv for variable latitude and longitude
# 24 EastGRIP
## Interpolated values filter at EastGRIP
TA1: 1572 samples flagged
TA2: 6 samples flagged
TA3: 1134 samples flagged
RH1: 1237 samples flagged
RH2: 13 samples flagged
VW1: 12 samples flagged
VW2: 6 samples flagged
DW1: 6 samples flagged
P: 2305 samples flagged
TA5: 146 samples flagged
## Manual flagging of data at EastGRIP
Flagging data:
|start time|end time|variable|
|-|-|-|
|2021-11-11 00:00:00+00:00|2023-06-22 12:00:00+00:00|VW1|
|2021-11-11 00:00:00+00:00|2023-06-22 12:00:00+00:00|DW1|
|2022-04-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|TA1|
|2022-04-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|RH1|
|2022-04-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|TA3|
|2014-05-17 20:00:00+00:00|2014-05-17 21:00:00+00:00|HW2|
|2021-04-24 00:00:00+00:00|2023-06-22 12:00:00+00:00|HW2|
|2016-04-15 00:00:00+00:00|2016-05-15 00:00:00+00:00|HW1|
|2020-12-05 00:00:00+00:00|2023-06-22 12:00:00+00:00|HW1|
Warning: ISWR not found
Warning: OSWR not found
## Adjusting data at EastGRIP
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2014-01-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|DW1|multiply|-1.0|0|
|2014-01-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|DW1|rotate|20.0|0|
|2014-01-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|DW1|rotate|30.0|0|
|2019-05-22 00:00:00+00:00|2023-06-22 12:00:00+00:00|DW1|rotate|185.0|0|
|2014-01-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2014-01-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|16699|
|2014-01-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|HW1|hampel_filter|3.0|2394|
|2014-10-01 00:00:00+00:00|2015-06-01 00:00:00+00:00|HW1|max_filter|0.7|161|
|2014-10-01 00:00:00+00:00|2015-06-01 00:00:00+00:00|HW1|min_filter|0.5|799|
|2016-05-15 00:00:00+00:00|2016-06-25 00:00:00+00:00|HW1|max_filter|2.36|68|
|2016-05-15 00:00:00+00:00|2016-06-25 00:00:00+00:00|HW1|min_filter|2.2|63|
|2014-01-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2014-01-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|HW2|biweekly_upper_range_filter|0.4|7452|
|2014-01-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|HW2|hampel_filter|3.0|3159|
|2014-01-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|HW2|add|1.2|0|
|2016-04-01 00:00:00+00:00|2021-10-01 00:00:00+00:00|P|hampel_filter|10.0|920|
## ROC filter at EastGRIP
 
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_TA1.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_TA2.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_TA3.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_TA4.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_RH1.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_RH2.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_VW1.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_VW2.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_DW1.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_DW2.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_P.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_HW1.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_HW2.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_V.jpeg)
![Adjusted and flagged data at EastGRIP](figures/L1_data_treatment/EastGRIP_TA5.jpeg)
 
Using metadata/interpolated positions/EastGRIP_position_interpolated.csv for variable latitude and longitude
# 16 KAR
## Interpolated values filter at KAR
NR: 12 samples flagged
TA1: 6 samples flagged
TA2: 3 samples flagged
TA3: 3 samples flagged
RH1: 214 samples flagged
VW1: 2199 samples flagged
VW2: 2055 samples flagged
DW1: 310 samples flagged
DW2: 288 samples flagged
P: 225 samples flagged
HS1: 43 samples flagged
HS2: 51 samples flagged
TS4: 10 samples flagged
TS10: 57 samples flagged
## Manual flagging of data at KAR
Flagging data:
|start time|end time|variable|
|-|-|-|
|1999-05-17 17:00:00+00:00|2001-06-07 13:00:00+00:00|RH2|
|1999-05-17 17:00:00+00:00|2001-06-07 13:00:00+00:00|TA4|
## Adjusting data at KAR
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH1|ice_to_water|0|0|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH2|ice_to_water|0|0|
## ROC filter at KAR
 
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_ISWR.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_OSWR.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_NR.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TA1.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TA2.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TA3.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TA4.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_RH1.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_RH2.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_VW1.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_VW2.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_DW1.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_DW2.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_P.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_HS1.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_HS2.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_V.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_HW1.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_HW2.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TS1.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TS2.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TS3.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TS4.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TS5.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TS6.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TS7.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TS8.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TS9.jpeg)
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at KAR](figures/L1_data_treatment/KAR_HS2.jpeg)
 
Cannot download maintenance summary. Using local file.
# 18 KULU
## Interpolated values filter at KULU
ISWR: 73 samples flagged
OSWR: 61 samples flagged
NR: 123 samples flagged
TA1: 212 samples flagged
TA2: 207 samples flagged
TA3: 591 samples flagged
TA4: 510 samples flagged
RH1: 680 samples flagged
RH2: 451 samples flagged
VW1: 953 samples flagged
VW2: 995 samples flagged
DW1: 183 samples flagged
DW2: 134 samples flagged
P: 368 samples flagged
HS1: 9 samples flagged
## Manual flagging of data at KULU
Flagging data:
|start time|end time|variable|
|-|-|-|
|2000-05-01 00:00:00+00:00|2000-09-14 22:00:00+00:00|TA1|
|2000-05-01 00:00:00+00:00|2000-09-14 22:00:00+00:00|TA2|
|2000-05-01 00:00:00+00:00|2000-09-14 22:00:00+00:00|P|
|1999-09-28 00:00:00+00:00|2000-09-14 22:00:00+00:00|DW1|
|1999-09-28 00:00:00+00:00|2000-09-14 22:00:00+00:00|DW2|
|1999-09-30 00:00:00+00:00|1999-12-01 00:00:00+00:00|TA3|
|2000-03-28 00:00:00+00:00|2000-06-21 00:00:00+00:00|ISWR|
|2000-03-28 00:00:00+00:00|2000-06-21 00:00:00+00:00|OSWR|
|1999-10-01 00:00:00+00:00|2000-05-01 00:00:00+00:00|TA3|
|1999-10-01 00:00:00+00:00|2000-05-01 00:00:00+00:00|TA4|
## Adjusting data at KULU
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH1|ice_to_water|0|0|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH2|ice_to_water|0|0|
## ROC filter at KULU
 
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_ISWR.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_OSWR.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_NR.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_TA1.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_TA2.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_TA3.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_TA4.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_RH1.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_RH2.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_VW1.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_VW2.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_DW1.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_DW2.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_P.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_HS1.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_V.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_HW1.jpeg)
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_HW2.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at KULU](figures/L1_data_treatment/KULU_HS2.jpeg)
 
# 20 Aurora
## Interpolated values filter at Aurora
ISWR: 12 samples flagged
TA3: 24 samples flagged
RH1: 89 samples flagged
VW1: 942 samples flagged
VW2: 835 samples flagged
DW1: 120 samples flagged
DW2: 100 samples flagged
P: 31 samples flagged
HS1: 21 samples flagged
## Manual flagging of data at Aurora
Flagging data:
|start time|end time|variable|
|-|-|-|
|2000-06-24 14:00:00+00:00|2001-05-06 00:00:00+00:00|OSWR|
## Adjusting data at Aurora
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2000-06-24 14:00:00+00:00|2001-05-06 00:00:00+00:00|RH1|ice_to_water|0|0|
|2000-06-24 14:00:00+00:00|2001-05-06 00:00:00+00:00|RH2|ice_to_water|0|0|
|2000-06-24 14:00:00+00:00|2001-05-06 00:00:00+00:00|TA3|min_filter|-20|3711|
## ROC filter at Aurora
 
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_ISWR.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_OSWR.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_NR.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_TA1.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_TA3.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_RH1.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_VW1.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_VW2.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_DW1.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_DW2.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_P.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_HS1.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_V.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_HW1.jpeg)
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_HW2.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at Aurora](figures/L1_data_treatment/Aurora_HS2.jpeg)
 
# 21 Petermann Glacier
## Interpolated values filter at Petermann Glacier
ISWR: 34 samples flagged
OSWR: 34 samples flagged
NR: 91 samples flagged
TA1: 449 samples flagged
TA2: 434 samples flagged
TA3: 905 samples flagged
TA4: 997 samples flagged
RH1: 453 samples flagged
RH2: 556 samples flagged
VW1: 475 samples flagged
VW2: 521 samples flagged
DW1: 378 samples flagged
DW2: 298 samples flagged
P: 540 samples flagged
HS1: 54 samples flagged
HS2: 9 samples flagged
TS1: 379 samples flagged
TS2: 587 samples flagged
TS3: 739 samples flagged
TS4: 299 samples flagged
TS5: 960 samples flagged
TS6: 2200 samples flagged
TS7: 3659 samples flagged
TS8: 2641 samples flagged
TS9: 1023 samples flagged
TS10: 952 samples flagged
## Manual flagging of data at Petermann Glacier
Flagging data:
|start time|end time|variable|
|-|-|-|
|2005-06-19 00:00:00+00:00|2005-08-13 00:00:00+00:00|TA3|
|2005-06-19 00:00:00+00:00|2005-08-13 00:00:00+00:00|TA4|
|2002-08-31 00:00:00+00:00|2002-09-06 00:00:00+00:00|TS1|
|2002-08-31 00:00:00+00:00|2002-09-06 00:00:00+00:00|TS2|
|2002-08-31 00:00:00+00:00|2002-09-06 00:00:00+00:00|TS3|
|2002-08-31 00:00:00+00:00|2002-09-06 00:00:00+00:00|TS4|
|2002-08-31 00:00:00+00:00|2002-09-06 00:00:00+00:00|TS5|
|2002-08-31 00:00:00+00:00|2002-09-06 00:00:00+00:00|TS6|
|2002-08-31 00:00:00+00:00|2002-09-06 00:00:00+00:00|TS7|
|2002-08-31 00:00:00+00:00|2002-09-06 00:00:00+00:00|TS8|
|2002-08-31 00:00:00+00:00|2002-09-06 00:00:00+00:00|TS9|
|2002-08-31 00:00:00+00:00|2002-09-06 00:00:00+00:00|TS10|
## Adjusting data at Petermann Glacier
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH2|ice_to_water|0.0|0|
## ROC filter at Petermann Glacier
 
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_ISWR.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_OSWR.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_NR.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TA1.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TA2.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TA3.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TA4.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_RH1.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_RH2.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_VW1.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_VW2.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_DW1.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_DW2.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_P.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_HS1.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_HS2.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_V.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_HW1.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_HW2.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TS1.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TS2.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TS3.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TS4.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TS5.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TS6.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TS7.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TS8.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TS9.jpeg)
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_TS10.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2003-01-01 00:00:00+00:00|2006-05-01 11:00:00+00:00|HS1|add|-0.3|0|
 
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2003-01-01 00:00:00+00:00|2006-05-01 11:00:00+00:00|HS2|add|-0.3|0|
 
![Adjusted and flagged data at Petermann Glacier](figures/L1_data_treatment/PetermannGlacier_HS2.jpeg)
 
Cannot download maintenance summary. Using local file.
# 22 Petermann ELA
## Interpolated values filter at Petermann ELA
ISWR: 16 samples flagged
NR: 18 samples flagged
TA1: 413 samples flagged
TA2: 404 samples flagged
TA3: 67 samples flagged
TA4: 53 samples flagged
RH1: 71 samples flagged
RH2: 44 samples flagged
VW1: 6 samples flagged
DW1: 22 samples flagged
P: 1567 samples flagged
TS1: 548 samples flagged
TS2: 1826 samples flagged
TS3: 84 samples flagged
TS4: 27 samples flagged
TS5: 27 samples flagged
TS6: 42 samples flagged
TS7: 42 samples flagged
TS8: 42 samples flagged
TS9: 38 samples flagged
TS10: 27 samples flagged
## Manual flagging of data at Petermann ELA
Flagging data:
|start time|end time|variable|
|-|-|-|
|2003-01-01 00:00:00+00:00|2011-05-23 00:00:00+00:00|RH1|
|2003-01-01 00:00:00+00:00|2011-05-01 00:00:00+00:00|RH2|
|2011-01-01 00:00:00+00:00|2015-01-01 00:00:00+00:00|TA1|
|2011-01-01 00:00:00+00:00|2015-01-01 00:00:00+00:00|TA2|
|2010-01-01 00:00:00+00:00|2022-04-12 18:00:00+00:00|VW1|
|2011-06-01 00:00:00+00:00|2011-07-04 00:00:00+00:00|HW1|
|2011-06-01 00:00:00+00:00|2012-05-25 00:00:00+00:00|HW2|
## Adjusting data at Petermann ELA
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2007-03-01 00:00:00+00:00|2007-04-10 00:00:00+00:00|HW1|min_filter|2.26|10|
|2009-05-15 00:00:00+00:00|2022-04-12 18:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2011-09-01 00:00:00+00:00|2012-05-01 00:00:00+00:00|HW1|max_filter|0.81|129|
|2012-08-16 00:00:00+00:00|2014-05-01 00:00:00+00:00|HW1|min_filter|1.37|1903|
|2012-08-16 00:00:00+00:00|2013-05-26 00:00:00+00:00|HW1|max_filter|1.43|810|
|2013-01-01 00:00:00+00:00|2022-04-12 18:00:00+00:00|HW1|min_filter|1.0|10480|
|2014-01-01 00:00:00+00:00|2015-01-01 00:00:00+00:00|HW1|max_filter|2.17|21|
|2014-01-01 00:00:00+00:00|2015-01-01 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|849|
|2016-01-01 00:00:00+00:00|2022-04-12 18:00:00+00:00|HW1|biweekly_upper_range_filter|0.5|5|
|2016-01-01 00:00:00+00:00|2022-04-12 18:00:00+00:00|HW1|hampel_filter|2.0|1515|
|2007-03-01 00:00:00+00:00|2007-04-10 00:00:00+00:00|HW2|min_filter|2.26|21|
|2009-05-15 00:00:00+00:00|2022-04-12 18:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2012-08-16 00:00:00+00:00|2014-05-01 00:00:00+00:00|HW2|min_filter|1.55|92|
|2015-07-01 00:00:00+00:00|2016-01-01 00:00:00+00:00|HW2|min_filter|1.4|3|
|2016-01-01 00:00:00+00:00|2022-04-12 18:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|7096|
|2016-01-01 00:00:00+00:00|2019-01-01 00:00:00+00:00|HW2|max_filter|3.12|156|
|2016-01-01 00:00:00+00:00|2019-01-01 00:00:00+00:00|HW2|min_filter|2.4|928|
|2016-01-01 00:00:00+00:00|2022-04-12 18:00:00+00:00|HW2|hampel_filter|2.0|22|
|2003-05-23 07:00:00+00:00|2022-04-12 18:00:00+00:00|TA2|max_filter|11.0|10|
|2003-05-23 07:00:00+00:00|2022-04-12 18:00:00+00:00|TA3|max_filter|11.0|9|
|2003-05-23 07:00:00+00:00|2022-04-12 18:00:00+00:00|TA4|max_filter|11.0|9|
## ROC filter at Petermann ELA
 
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_ISWR.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_OSWR.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_NR.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TA1.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TA2.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TA3.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TA4.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_RH1.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_RH2.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_VW1.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_VW2.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_DW1.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_DW2.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_P.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_HW1.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_HW2.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_V.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TS1.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TS2.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TS3.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TS4.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TS5.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TS6.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TS7.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TS8.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TS9.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_TS10.jpeg)
 
Using metadata/interpolated positions/Petermann ELA_position_interpolated.csv for variable latitude and longitude
Cannot download maintenance summary. Using local file.
# 33 SMS-PET
## Interpolated values filter at SMS-PET
TA1: 3 samples flagged
ISWR: 268 samples flagged
OSWR: 384 samples flagged
NR: 57 samples flagged
## Manual flagging of data at SMS-PET
===============
No erroneous data listed for SMS-PET
===============
## Adjusting data at SMS-PET
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2002-06-02 02:00:00+00:00|2004-05-14 15:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2002-06-02 02:00:00+00:00|2004-05-14 15:00:00+00:00|HW1|min_filter|0.7|40|
|2002-07-15 00:00:00+00:00|2003-05-07 15:30:00+00:00|HW1|biweekly_upper_range_filter|0.4|40|
|2003-09-01 00:00:00+00:00|2004-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|96|
## ROC filter at SMS-PET
 
![Adjusted and flagged data at SMS-PET](figures/L1_data_treatment/SMS-PET_TA1.jpeg)
![Adjusted and flagged data at SMS-PET](figures/L1_data_treatment/SMS-PET_TA2.jpeg)
![Adjusted and flagged data at SMS-PET](figures/L1_data_treatment/SMS-PET_RH1.jpeg)
![Adjusted and flagged data at SMS-PET](figures/L1_data_treatment/SMS-PET_VW1.jpeg)
![Adjusted and flagged data at SMS-PET](figures/L1_data_treatment/SMS-PET_DW1.jpeg)
![Adjusted and flagged data at SMS-PET](figures/L1_data_treatment/SMS-PET_HW1.jpeg)
![Adjusted and flagged data at SMS-PET](figures/L1_data_treatment/SMS-PET_V.jpeg)
![Adjusted and flagged data at SMS-PET](figures/L1_data_treatment/SMS-PET_ISWR.jpeg)
![Adjusted and flagged data at SMS-PET](figures/L1_data_treatment/SMS-PET_OSWR.jpeg)
![Adjusted and flagged data at SMS-PET](figures/L1_data_treatment/SMS-PET_NR.jpeg)
 
HW2 not in dataframe
# 25 SMS1
## Interpolated values filter at SMS1
TA1: 19 samples flagged
RH1: 16 samples flagged
## Manual flagging of data at SMS1
Flagging data:
|start time|end time|variable|
|-|-|-|
|2004-05-27 17:30:00+00:00|2004-05-27 19:30:00+00:00|HW1|
## Adjusting data at SMS1
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2001-09-01 00:00:00+00:00|2002-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|175|
|2002-01-01 00:00:00+00:00|2006-01-15 03:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2002-01-01 00:00:00+00:00|2006-01-15 03:00:00+00:00|HW1|min_filter|0.9|211|
|2002-01-01 00:00:00+00:00|2006-01-15 03:00:00+00:00|HW1|max_filter|3.75|18|
|2002-09-01 00:00:00+00:00|2003-05-01 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|7|
|2003-08-01 00:00:00+00:00|2004-05-15 00:00:00+00:00|HW1|max_filter|3.4|95|
|2003-08-01 00:00:00+00:00|2004-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|294|
|2004-08-01 00:00:00+00:00|2005-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|1606|
|2005-09-01 00:00:00+00:00|2006-05-15 00:00:00+00:00|HW1|min_filter|2.9|290|
## ROC filter at SMS1
 
![Adjusted and flagged data at SMS1](figures/L1_data_treatment/SMS1_TA1.jpeg)
![Adjusted and flagged data at SMS1](figures/L1_data_treatment/SMS1_TA2.jpeg)
![Adjusted and flagged data at SMS1](figures/L1_data_treatment/SMS1_RH1.jpeg)
![Adjusted and flagged data at SMS1](figures/L1_data_treatment/SMS1_VW1.jpeg)
![Adjusted and flagged data at SMS1](figures/L1_data_treatment/SMS1_DW1.jpeg)
![Adjusted and flagged data at SMS1](figures/L1_data_treatment/SMS1_HW1.jpeg)
 
HW2 not in dataframe
# 26 SMS2
## Interpolated values filter at SMS2
TA1: 3 samples flagged
TA2: 11 samples flagged
RH1: 15 samples flagged
## Manual flagging of data at SMS2
===============
No erroneous data listed for SMS2
===============
## Adjusting data at SMS2
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2003-04-24 04:00:00+00:00|2006-05-10 15:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2003-04-24 04:00:00+00:00|2006-05-10 15:00:00+00:00|HW1|min_filter|0.1|6660|
|2003-04-24 04:00:00+00:00|2006-05-10 15:00:00+00:00|HW1|max_filter|5.0|0|
|2003-08-01 00:00:00+00:00|2004-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|447|
|2004-08-26 00:00:00+00:00|2005-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|240|
|2005-09-01 00:00:00+00:00|2006-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|404|
## ROC filter at SMS2
 
![Adjusted and flagged data at SMS2](figures/L1_data_treatment/SMS2_TA1.jpeg)
![Adjusted and flagged data at SMS2](figures/L1_data_treatment/SMS2_TA2.jpeg)
![Adjusted and flagged data at SMS2](figures/L1_data_treatment/SMS2_RH1.jpeg)
![Adjusted and flagged data at SMS2](figures/L1_data_treatment/SMS2_VW1.jpeg)
![Adjusted and flagged data at SMS2](figures/L1_data_treatment/SMS2_DW1.jpeg)
![Adjusted and flagged data at SMS2](figures/L1_data_treatment/SMS2_HW1.jpeg)
![Adjusted and flagged data at SMS2](figures/L1_data_treatment/SMS2_V.jpeg)
 
HW2 not in dataframe
# 27 SMS3
## Interpolated values filter at SMS3
TA1: 15 samples flagged
TA2: 9 samples flagged
RH1: 26 samples flagged
## Manual flagging of data at SMS3
===============
No erroneous data listed for SMS3
===============
## Adjusting data at SMS3
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2001-05-22 21:00:00+00:00|2006-05-10 15:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2001-05-22 21:00:00+00:00|2006-05-10 15:00:00+00:00|HW1|min_filter|0.5|5324|
|2001-09-01 00:00:00+00:00|2002-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|254|
|2002-07-15 00:00:00+00:00|2003-05-01 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|1342|
|2003-09-01 00:00:00+00:00|2004-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|186|
|2004-07-15 00:00:00+00:00|2005-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|189|
|2005-07-11 00:00:00+00:00|2005-07-16 00:00:00+00:00|HW1|min_filter|1.8|3|
|2005-09-01 00:00:00+00:00|2006-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|223|
## ROC filter at SMS3
 
![Adjusted and flagged data at SMS3](figures/L1_data_treatment/SMS3_TA1.jpeg)
![Adjusted and flagged data at SMS3](figures/L1_data_treatment/SMS3_TA2.jpeg)
![Adjusted and flagged data at SMS3](figures/L1_data_treatment/SMS3_RH1.jpeg)
![Adjusted and flagged data at SMS3](figures/L1_data_treatment/SMS3_VW1.jpeg)
![Adjusted and flagged data at SMS3](figures/L1_data_treatment/SMS3_DW1.jpeg)
![Adjusted and flagged data at SMS3](figures/L1_data_treatment/SMS3_HW1.jpeg)
![Adjusted and flagged data at SMS3](figures/L1_data_treatment/SMS3_V.jpeg)
 
HW2 not in dataframe
# 28 SMS4
## Interpolated values filter at SMS4
TA2: 3 samples flagged
RH1: 10 samples flagged
DW1: 3 samples flagged
## Manual flagging of data at SMS4
===============
No erroneous data listed for SMS4
===============
## Adjusting data at SMS4
No data to fix at SMS4
## ROC filter at SMS4
 
===============
No data to fix at SMS4
===============
HW2 not in dataframe
# 29 SMS5
## Interpolated values filter at SMS5
## Manual flagging of data at SMS5
===============
No erroneous data listed for SMS5
===============
## Adjusting data at SMS5
No data to fix at SMS5
## ROC filter at SMS5
 
===============
No data to fix at SMS5
===============
HW2 not in dataframe
# 30 LAR1
## Interpolated values filter at LAR1
ISWR: 36 samples flagged
OSWR: 36 samples flagged
NR: 115 samples flagged
TA1: 2439 samples flagged
TA2: 2392 samples flagged
TA3: 2116 samples flagged
TA4: 2154 samples flagged
RH1: 968 samples flagged
RH2: 1098 samples flagged
VW2: 6 samples flagged
P: 590 samples flagged
HS1: 109 samples flagged
HS2: 155 samples flagged
TA5: 67 samples flagged
## Manual flagging of data at LAR1
Flagging data:
|start time|end time|variable|
|-|-|-|
## Adjusting data at LAR1
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2008-12-23 00:00:00+00:00|2012-12-25 23:00:00+00:00|ISWR|multiply|2.688|0|
|2008-12-23 00:00:00+00:00|2012-12-25 23:00:00+00:00|OSWR|multiply|2.2756|0|
|2008-12-23 00:00:00+00:00|2012-12-25 23:00:00+00:00|RH1|ice_to_water|0.0|0|
|2008-12-23 00:00:00+00:00|2012-12-25 23:00:00+00:00|RH2|ice_to_water|0.0|0|
## ROC filter at LAR1
 
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_ISWR.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_OSWR.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_NR.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_TA1.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_TA2.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_TA3.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_TA4.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_RH1.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_RH2.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_VW1.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_VW2.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_DW1.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_DW2.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_P.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_HS1.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_HS2.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_V.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_TA5.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_HW1.jpeg)
![Adjusted and flagged data at LAR1](figures/L1_data_treatment/LAR1_HW2.jpeg)
 
# 31 LAR2
## Interpolated values filter at LAR2
ISWR: 15 samples flagged
OSWR: 15 samples flagged
NR: 68 samples flagged
TA1: 1239 samples flagged
TA2: 1250 samples flagged
TA3: 1209 samples flagged
TA4: 1219 samples flagged
RH1: 671 samples flagged
RH2: 545 samples flagged
P: 465 samples flagged
HS1: 66 samples flagged
HS2: 82 samples flagged
TA5: 9 samples flagged
## Manual flagging of data at LAR2
===============
No erroneous data listed for LAR2
===============
## Adjusting data at LAR2
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2008-12-22 20:00:00+00:00|2011-11-15 13:00:00+00:00|ISWR|multiply|2.68|0|
|2008-12-22 20:00:00+00:00|2011-11-15 13:00:00+00:00|OSWR|multiply|2.88|0|
|2008-12-22 20:00:00+00:00|2011-11-15 13:00:00+00:00|RH1|ice_to_water|0.0|0|
|2008-12-22 20:00:00+00:00|2011-11-15 13:00:00+00:00|RH2|ice_to_water|0.0|0|
## ROC filter at LAR2
 
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_ISWR.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_OSWR.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_NR.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_TA1.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_TA2.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_TA3.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_TA4.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_RH1.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_RH2.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_VW1.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_VW2.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_DW1.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_DW2.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_P.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_HS1.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_HS2.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_V.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_TA5.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_HW1.jpeg)
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_HW2.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at LAR2](figures/L1_data_treatment/LAR2_HS2.jpeg)
 
# 32 LAR3
## Interpolated values filter at LAR3
ISWR: 267 samples flagged
OSWR: 326 samples flagged
NR: 37 samples flagged
TA1: 966 samples flagged
TA2: 948 samples flagged
TA3: 986 samples flagged
TA4: 585 samples flagged
RH1: 513 samples flagged
RH2: 355 samples flagged
VW1: 3 samples flagged
P: 324 samples flagged
HS1: 400 samples flagged
HS2: 535 samples flagged
TA5: 6 samples flagged
## Manual flagging of data at LAR3
Flagging data:
|start time|end time|variable|
|-|-|-|
|2009-08-10 14:00:00+00:00|2011-11-08 14:00:00+00:00|RH2|
|2009-08-10 14:00:00+00:00|2009-08-10 16:00:00+00:00|HW1|
## Adjusting data at LAR3
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2009-08-10 14:00:00+00:00|2011-11-08 14:00:00+00:00|RH1|ice_to_water|0|0|
|2009-08-10 14:00:00+00:00|2011-11-08 14:00:00+00:00|RH2|ice_to_water|0|0|
## ROC filter at LAR3
 
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_ISWR.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_OSWR.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_NR.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_TA1.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_TA2.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_TA3.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_TA4.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_RH1.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_RH2.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_VW1.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_VW2.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_DW1.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_DW2.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_P.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_HS1.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_HS2.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_V.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_TA5.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_HW1.jpeg)
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_HW2.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_HS1.jpeg)
 
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at LAR3](figures/L1_data_treatment/LAR3_HS2.jpeg)
 

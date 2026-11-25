* [1 Swiss Camp](#s1)
  * [Gap filling with the C-level files at Swiss Camp](#s1-1)
  * [Interpolated values filter at Swiss Camp](#s1-2)
  * [Manual flagging of data at Swiss Camp](#s1-3)
  * [Adjusting data at Swiss Camp](#s1-4)
  * [ROC filter at Swiss Camp](#s1-5)
* [0 Swiss Camp 10m](#s2)
  * [Gap filling with the C-level files at Swiss Camp 10m](#s2-1)
  * [Interpolated values filter at Swiss Camp 10m](#s2-2)
  * [Manual flagging of data at Swiss Camp 10m](#s2-3)
  * [Adjusting data at Swiss Camp 10m](#s2-4)
  * [ROC filter at Swiss Camp 10m](#s2-5)
* [9 JAR1](#s3)
  * [Gap filling with the C-level files at JAR1](#s3-1)
  * [Interpolated values filter at JAR1](#s3-2)
  * [Manual flagging of data at JAR1](#s3-3)
  * [Adjusting data at JAR1](#s3-4)
  * [ROC filter at JAR1](#s3-5)
* [17 JAR2](#s4)
  * [Gap filling with the C-level files at JAR2](#s4-1)
  * [Interpolated values filter at JAR2](#s4-2)
  * [Manual flagging of data at JAR2](#s4-3)
  * [Adjusting data at JAR2](#s4-4)
  * [ROC filter at JAR2](#s4-5)
* [10 Saddle](#s5)
  * [Gap filling with the C-level files at Saddle](#s5-1)
  * [Interpolated values filter at Saddle](#s5-2)
  * [Manual flagging of data at Saddle](#s5-3)
  * [Adjusting data at Saddle](#s5-4)
  * [ROC filter at Saddle](#s5-5)
* [22 Petermann ELA](#s6)
  * [Gap filling with the C-level files at Petermann ELA](#s6-1)
  * [Interpolated values filter at Petermann ELA](#s6-2)
  * [Manual flagging of data at Petermann ELA](#s6-3)
  * [Adjusting data at Petermann ELA](#s6-4)
  * [ROC filter at Petermann ELA](#s6-5)
# <a id='s1' />1 Swiss Camp
## <a id='s1-1' />Gap filling with the C-level files at Swiss Camp
CR10X-sourced HW1/HW2/HS1/HS2 dropped (121483 values) to be filled from the C-level file instead
RH1: 33100 hours taken from the C-level file converted from RH wrt ice to RH wrt water
RH2: 32946 hours taken from the C-level file converted from RH wrt ice to RH wrt water
Values taken from the C-level files: 886198
## <a id='s1-2' />Interpolated values filter at Swiss Camp
ISWR: 16 samples flagged
OSWR: 45 samples flagged
NR: 194 samples flagged
TA1: 3018 samples flagged
TA2: 3652 samples flagged
TA3: 1309 samples flagged
TA4: 1286 samples flagged
RH1: 975 samples flagged
RH2: 977 samples flagged
VW1: 2553 samples flagged
VW2: 1498 samples flagged
DW1: 164 samples flagged
DW2: 262 samples flagged
P: 2665 samples flagged
TA5: 3840 samples flagged
TS1: 41 samples flagged
TS2: 49 samples flagged
TS3: 59 samples flagged
TS4: 708 samples flagged
TS5: 4372 samples flagged
TS6: 2268 samples flagged
TS7: 4846 samples flagged
TS8: 1193 samples flagged
TS9: 4043 samples flagged
TS10: 2372 samples flagged
IUVR: 99 samples flagged
ILWR: 24 samples flagged
Tsurf1: 34 samples flagged
Tsurf2: 18 samples flagged
HS1: 80 samples flagged
HS2: 99 samples flagged
## <a id='s1-3' />Manual flagging of data at Swiss Camp
Flagging data:
|start time|end time|variable|
|-|-|-|
|2003-09-01 00:00:00+00:00|2004-07-01 00:00:00+00:00|TA1|
|2003-09-01 00:00:00+00:00|2004-07-01 00:00:00+00:00|TA2|
|2003-09-01 00:00:00+00:00|2004-07-01 00:00:00+00:00|TA3|
|2003-09-01 00:00:00+00:00|2004-07-01 00:00:00+00:00|TA4|
|2015-06-01 00:00:00+00:00|2016-05-01 00:00:00+00:00|RH1|
|2009-07-01 00:00:00+00:00|2009-07-01 00:00:00+00:00|ISWR|
|2009-07-01 00:00:00+00:00|2009-07-01 00:00:00+00:00|OSWR|
|2011-02-15 00:00:00+00:00|2011-05-10 00:00:00+00:00|OSWR|
|2011-08-01 00:00:00+00:00|2012-05-10 00:00:00+00:00|OSWR|
|2011-02-15 00:00:00+00:00|2011-05-10 00:00:00+00:00|ISWR|
|2015-06-01 00:00:00+00:00|2016-05-01 00:00:00+00:00|VW1|
|2011-02-15 00:00:00+00:00|2011-05-10 00:00:00+00:00|HS1|
|2011-08-01 00:00:00+00:00|2012-05-10 00:00:00+00:00|HS1|
|2011-02-15 00:00:00+00:00|2011-05-10 00:00:00+00:00|HS2|
|2011-08-01 00:00:00+00:00|2012-05-10 00:00:00+00:00|HS2|
|2017-05-15 00:00:00+00:00|2018-05-01 00:00:00+00:00|HS1|
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
|2003-08-21 22:00:00+00:00|2003-08-22 21:00:00+00:00|DW1|
|2003-09-27 04:00:00+00:00|2004-03-14 18:00:00+00:00|DW1|
|2004-03-15 01:00:00+00:00|2004-03-16 23:00:00+00:00|DW1|
|2004-03-20 01:00:00+00:00|2004-03-22 11:00:00+00:00|DW1|
|2011-02-11 16:00:00+00:00|2011-05-15 20:00:00+00:00|DW1|
|2011-07-26 13:00:00+00:00|2012-05-05 23:00:00+00:00|DW1|
|2012-05-06 01:00:00+00:00|2012-05-11 21:00:00+00:00|DW1|
|2003-09-23 06:00:00+00:00|2003-11-12 10:00:00+00:00|DW2|
|2003-11-15 13:00:00+00:00|2003-11-22 09:00:00+00:00|DW2|
|2003-11-28 22:00:00+00:00|2003-12-02 23:00:00+00:00|DW2|
|2003-12-04 09:00:00+00:00|2003-12-07 07:00:00+00:00|DW2|
|2003-12-11 00:00:00+00:00|2004-01-15 17:00:00+00:00|DW2|
|2004-01-15 19:00:00+00:00|2004-03-14 18:00:00+00:00|DW2|
|2004-03-15 02:00:00+00:00|2004-03-16 23:00:00+00:00|DW2|
|2004-03-20 02:00:00+00:00|2004-03-22 11:00:00+00:00|DW2|
|2011-02-11 15:00:00+00:00|2011-05-15 20:00:00+00:00|DW2|
|2011-07-26 18:00:00+00:00|2012-05-05 23:00:00+00:00|DW2|
|2012-05-06 01:00:00+00:00|2012-05-11 19:00:00+00:00|DW2|
|2003-09-22 02:00:00+00:00|2004-03-14 23:00:00+00:00|HW1|
|2004-03-15 01:00:00+00:00|2004-03-16 23:00:00+00:00|HW1|
|2004-05-31 21:00:00+00:00|2004-06-06 02:00:00+00:00|HW1|
|2005-05-04 22:00:00+00:00|2005-05-13 13:00:00+00:00|HW1|
|2007-05-17 22:00:00+00:00|2007-06-01 14:00:00+00:00|HW1|
|2011-03-26 19:00:00+00:00|2011-04-12 02:00:00+00:00|HW1|
|2011-04-27 15:00:00+00:00|2011-05-17 12:00:00+00:00|HW1|
|2017-09-03 22:00:00+00:00|2017-09-05 00:00:00+00:00|HW1|
|2017-11-07 17:00:00+00:00|2017-11-11 00:00:00+00:00|HW1|
|2017-11-20 20:00:00+00:00|2017-11-22 01:00:00+00:00|HW1|
|2017-11-22 06:00:00+00:00|2017-11-24 04:00:00+00:00|HW1|
|2017-12-19 07:00:00+00:00|2017-12-27 08:00:00+00:00|HW1|
|2017-12-28 05:00:00+00:00|2017-12-31 14:00:00+00:00|HW1|
|2018-01-01 17:00:00+00:00|2018-01-05 15:00:00+00:00|HW1|
|2018-01-12 09:00:00+00:00|2018-01-15 11:00:00+00:00|HW1|
|2018-01-16 19:00:00+00:00|2018-01-17 21:00:00+00:00|HW1|
|2018-01-18 05:00:00+00:00|2018-01-25 19:00:00+00:00|HW1|
|2018-01-27 17:00:00+00:00|2018-01-29 01:00:00+00:00|HW1|
|2018-02-01 20:00:00+00:00|2018-02-02 20:00:00+00:00|HW1|
|2018-02-08 13:00:00+00:00|2018-02-11 22:00:00+00:00|HW1|
|2018-02-12 07:00:00+00:00|2018-02-13 13:00:00+00:00|HW1|
|2018-02-15 06:00:00+00:00|2018-02-16 19:00:00+00:00|HW1|
|2018-02-19 22:00:00+00:00|2018-02-20 21:00:00+00:00|HW1|
|2018-02-21 12:00:00+00:00|2018-02-22 19:00:00+00:00|HW1|
|2018-02-22 22:00:00+00:00|2018-02-24 03:00:00+00:00|HW1|
|2018-03-05 01:00:00+00:00|2018-03-07 03:00:00+00:00|HW1|
|2018-03-09 01:00:00+00:00|2018-03-10 13:00:00+00:00|HW1|
|2003-09-22 02:00:00+00:00|2004-03-14 23:00:00+00:00|HW2|
|2004-03-15 01:00:00+00:00|2004-03-16 23:00:00+00:00|HW2|
|2004-03-20 01:00:00+00:00|2004-03-22 11:00:00+00:00|HW2|
|2011-02-20 20:00:00+00:00|2011-02-23 12:00:00+00:00|HW2|
|2011-02-28 18:00:00+00:00|2011-03-01 21:00:00+00:00|HW2|
|2011-03-06 01:00:00+00:00|2011-03-08 21:00:00+00:00|HW2|
|2011-03-11 14:00:00+00:00|2011-03-12 13:00:00+00:00|HW2|
|2011-03-18 02:00:00+00:00|2011-03-19 14:00:00+00:00|HW2|
|2011-04-13 22:00:00+00:00|2011-04-15 03:00:00+00:00|HW2|
|2012-05-13 21:00:00+00:00|2012-05-28 11:00:00+00:00|HW2|
|1998-05-22 04:00:00+00:00|1998-06-03 12:00:00+00:00|ISWR|
|2003-09-24 18:00:00+00:00|2004-03-14 23:00:00+00:00|ISWR|
|2004-03-15 01:00:00+00:00|2004-03-16 23:00:00+00:00|ISWR|
|2004-03-15 01:00:00+00:00|2004-03-16 23:00:00+00:00|NR|
|2004-03-15 01:00:00+00:00|2004-03-16 23:00:00+00:00|OSWR|
|1999-04-05 20:00:00+00:00|1999-04-08 19:00:00+00:00|P|
|2007-05-17 22:00:00+00:00|2007-06-01 14:00:00+00:00|P|
|2007-07-18 07:00:00+00:00|2007-07-21 08:00:00+00:00|P|
|2009-05-07 21:00:00+00:00|2009-05-14 02:00:00+00:00|P|
|2004-03-20 01:00:00+00:00|2004-03-22 11:00:00+00:00|RH1|
|2007-07-18 19:00:00+00:00|2007-07-20 16:00:00+00:00|RH1|
|2003-09-23 19:00:00+00:00|2004-03-14 23:00:00+00:00|RH2|
|2004-03-20 01:00:00+00:00|2004-03-21 23:00:00+00:00|RH2|
|2007-07-18 19:00:00+00:00|2007-07-20 14:00:00+00:00|RH2|
|2007-07-18 19:00:00+00:00|2007-07-20 16:00:00+00:00|TA3|
|2007-07-18 19:00:00+00:00|2007-07-20 16:00:00+00:00|TA4|
|2007-07-18 07:00:00+00:00|2007-07-21 08:00:00+00:00|V|
|2012-11-30 07:00:00+00:00|2012-12-02 18:00:00+00:00|V|
|2012-12-07 16:00:00+00:00|2012-12-08 21:00:00+00:00|V|
|2013-01-03 12:00:00+00:00|2013-01-04 14:00:00+00:00|V|
|2003-09-27 04:00:00+00:00|2004-03-14 23:00:00+00:00|VW1|
|2004-03-15 01:00:00+00:00|2004-03-16 23:00:00+00:00|VW1|
|2004-03-20 01:00:00+00:00|2004-03-22 11:00:00+00:00|VW1|
|2011-02-11 16:00:00+00:00|2011-05-15 20:00:00+00:00|VW1|
|2011-05-16 00:00:00+00:00|2011-05-17 16:00:00+00:00|VW1|
|2011-08-29 10:00:00+00:00|2012-05-05 23:00:00+00:00|VW1|
|2012-05-06 01:00:00+00:00|2012-05-11 21:00:00+00:00|VW1|
|2016-04-12 11:00:00+00:00|2016-05-09 12:00:00+00:00|VW1|
Warning: VW1_max not found
Warning: VW1_stdev not found
|2003-09-25 06:00:00+00:00|2004-03-14 23:00:00+00:00|VW2|
|2004-03-15 01:00:00+00:00|2004-03-16 23:00:00+00:00|VW2|
|2004-03-20 01:00:00+00:00|2004-03-22 11:00:00+00:00|VW2|
|2011-08-30 19:00:00+00:00|2012-05-05 23:00:00+00:00|VW2|
|2012-05-06 01:00:00+00:00|2012-05-11 19:00:00+00:00|VW2|
|2003-04-27 00:00:00+00:00|2003-09-21 00:00:00+00:00|HW2|
## <a id='s1-4' />Adjusting data at Swiss Camp

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1996-01-01 00:00:00+00:00|1996-08-01 00:00:00+00:00|HW1|air_temp_sonic_anticorrection|0.0|0|
|2009-01-01 00:00:00+00:00|2011-07-15 00:00:00+00:00|HW1|min_filter|1.0|7677|
|2009-05-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW1|add|-0.5|0|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW1|biweekly_upper_range_filter|0.5|5337|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW1|hampel_filter|2.0|706|
|2012-06-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW1|add|1.04|0|
|1995-01-12 00:00:00+00:00|2000-01-01 00:00:00+00:00|HW2|max_filter|8.0|19148|
|1996-01-01 00:00:00+00:00|1996-08-01 00:00:00+00:00|HW2|air_temp_sonic_anticorrection|0.0|0|
|2002-01-25 20:00:00+00:00|2022-08-03 19:00:00+00:00|HW2|add|-0.35|0|
|2009-01-01 00:00:00+00:00|2012-01-15 00:00:00+00:00|HW2|min_filter|1.0|3019|
|2009-05-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW2|add|0.3|0|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|11987|
|2009-05-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW2|hampel_filter|2.0|3567|
|2011-01-13 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW2|add|0.31|0|
|2012-06-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HW2|add|1.35|0|
|2018-03-12 00:00:00+00:00|2018-05-12 00:00:00+00:00|HW2|max_filter|0.77|412|
|2012-05-10 00:00:00+00:00|2022-08-03 19:00:00+00:00|ISWR|swap_with_OSWR|0.0|0|
|1995-01-01 00:00:00+00:00|1997-12-31 23:00:00+00:00|OSWR|multiply|1.055|0|
|2012-05-10 00:00:00+00:00|2022-08-03 19:00:00+00:00|OSWR|multiply|0.926|0|
|2019-11-15 00:00:00+00:00|2022-08-03 19:00:00+00:00|P|min_filter|856.0|5228|
|2005-05-09 00:00:00+00:00|2022-08-03 19:00:00+00:00|RH1|swap_with_RH2|0.0|-5|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS1|max_filter|-1.0|10|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS10|max_filter|-1.0|568|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS2|max_filter|-1.0|10|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS3|max_filter|-1.0|9|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS4|max_filter|-1.0|9|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS5|max_filter|-1.0|6|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS6|max_filter|-1.0|6|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS7|max_filter|-1.0|5|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS8|max_filter|-1.0|3|
|1997-05-18 00:00:00+00:00|1999-06-18 00:00:00+00:00|TS9|max_filter|-1.0|3|
## <a id='s1-5' />ROC filter at Swiss Camp
 
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
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_HS1.jpeg)
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_HS2.jpeg)
 

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1999-01-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.75|0|
|2000-12-31 08:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.7|0|
|2001-05-17 17:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.3|0|
|2002-01-25 19:30:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|1.5|0|
|2003-01-24 01:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.6|0|
|2003-04-26 16:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|0.4|0|
|2004-01-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.5|0|
|2009-05-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.8|0|
|2009-05-07 21:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|0.57|0|
|2010-12-10 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.48|0|
|2011-08-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-3.0|0|
|2012-06-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|1.04|0|
|2013-08-14 13:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-0.27|0|
|2014-05-08 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS1|add|-2.0|0|
 
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_HS1.jpeg)
 

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2000-12-31 08:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-0.8|0|
|2001-05-17 17:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-0.3|0|
|2003-04-26 16:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-0.45|0|
|2008-10-30 05:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-0.3|0|
|2011-08-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-3.0|0|
|2012-06-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|1.35|0|
|2013-08-13 22:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|0.24|0|
|2014-05-08 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-2.0|0|
|2017-11-17 03:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-0.68|0|
|2019-04-19 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-0.79|0|
|2021-12-10 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-0.95|0|
 
![Adjusted and flagged data at Swiss Camp](figures/L1_data_treatment/SwissCamp_HS2.jpeg)
 
Using metadata/interpolated positions/Swiss Camp_position_interpolated.csv for variable latitude and longitude
Using metadata/interpolated positions/GC-Net_elevation_tie_points.csv for variable elevation
# <a id='s2' />0 Swiss Camp 10m
## <a id='s2-1' />Gap filling with the C-level files at Swiss Camp 10m
## <a id='s2-2' />Interpolated values filter at Swiss Camp 10m
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
## <a id='s2-3' />Manual flagging of data at Swiss Camp 10m
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
## <a id='s2-4' />Adjusting data at Swiss Camp 10m

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
## <a id='s2-5' />ROC filter at Swiss Camp 10m
 
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
|2017-10-29 09:00:00+00:00|2020-11-03 21:00:00+00:00|HS1|add|-0.68|0|
 
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_HS1.jpeg)
 

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
 
![Adjusted and flagged data at Swiss Camp 10m](figures/L1_data_treatment/SwissCamp10m_HS2.jpeg)
 
Using metadata/interpolated positions/Swiss Camp 10m_position_interpolated.csv for variable latitude and longitude
Using metadata/interpolated positions/GC-Net_elevation_tie_points.csv for variable elevation
# <a id='s3' />9 JAR1
## <a id='s3-1' />Gap filling with the C-level files at JAR1
CR10X-sourced HW1/HW2/HS1/HS2 dropped (175800 values) to be filled from the C-level file instead
RH1: 1617 hours taken from the C-level file converted from RH wrt ice to RH wrt water
RH2: 1609 hours taken from the C-level file converted from RH wrt ice to RH wrt water
Values taken from the C-level files: 661766
## <a id='s3-2' />Interpolated values filter at JAR1
ISWR: 15 samples flagged
OSWR: 13 samples flagged
NR: 85 samples flagged
TA1: 5338 samples flagged
TA2: 3295 samples flagged
TA3: 2924 samples flagged
TA4: 2331 samples flagged
RH1: 1995 samples flagged
RH2: 1508 samples flagged
VW1: 1033 samples flagged
VW2: 971 samples flagged
DW1: 225 samples flagged
DW2: 222 samples flagged
P: 4573 samples flagged
TA5: 476 samples flagged
TS1: 6500 samples flagged
TS2: 12037 samples flagged
TS3: 10198 samples flagged
TS4: 12454 samples flagged
TS5: 10342 samples flagged
TS6: 12086 samples flagged
TS7: 5488 samples flagged
TS8: 6248 samples flagged
TS9: 8555 samples flagged
TS10: 9265 samples flagged
HS1: 307 samples flagged
HS2: 586 samples flagged
## <a id='s3-3' />Manual flagging of data at JAR1
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
|2007-09-27 12:00:00+00:00|2007-09-28 12:00:00+00:00|DW1|
|2007-09-27 13:00:00+00:00|2007-09-28 15:00:00+00:00|DW2|
|2011-03-30 18:00:00+00:00|2011-03-31 17:00:00+00:00|DW2|
|2011-04-16 12:00:00+00:00|2011-04-18 02:00:00+00:00|DW2|
|2008-02-01 10:00:00+00:00|2008-05-08 19:00:00+00:00|HW1|
|2012-05-09 18:00:00+00:00|2012-05-10 18:00:00+00:00|HW1|
|2013-05-11 17:00:00+00:00|2013-10-08 14:00:00+00:00|HW1|
|2013-10-08 17:00:00+00:00|2014-05-06 17:00:00+00:00|HW1|
|2010-07-27 03:00:00+00:00|2011-05-08 16:00:00+00:00|HW2|
|2013-05-11 17:00:00+00:00|2013-10-08 14:00:00+00:00|HW2|
|2013-10-08 16:00:00+00:00|2014-05-06 20:00:00+00:00|HW2|
|2007-09-11 19:00:00+00:00|2008-05-08 15:00:00+00:00|ISWR|
|2007-09-07 19:00:00+00:00|2008-05-08 15:00:00+00:00|OSWR|
|2009-05-06 13:00:00+00:00|2009-05-13 19:00:00+00:00|P|
|2016-05-15 16:00:00+00:00|2017-01-12 14:00:00+00:00|P|
|2015-05-07 17:00:00+00:00|2015-08-28 02:00:00+00:00|RH1|
|2013-06-06 13:00:00+00:00|2013-09-10 07:00:00+00:00|RH2|
|2013-09-12 06:00:00+00:00|2013-09-14 04:00:00+00:00|RH2|
|2013-09-15 02:00:00+00:00|2013-09-16 06:00:00+00:00|RH2|
|2015-05-07 18:00:00+00:00|2015-08-28 02:00:00+00:00|RH2|
|2015-10-04 12:00:00+00:00|2016-04-10 08:00:00+00:00|RH2|
|2019-04-06 12:00:00+00:00|2019-04-08 01:00:00+00:00|TA3|
|2005-01-28 07:00:00+00:00|2005-05-06 17:00:00+00:00|TA4|
|2013-06-06 13:00:00+00:00|2013-09-16 06:00:00+00:00|TA4|
|2014-07-11 03:00:00+00:00|2014-07-15 00:00:00+00:00|TA4|
|2014-07-27 07:00:00+00:00|2014-08-01 21:00:00+00:00|TA4|
|2007-09-27 12:00:00+00:00|2007-09-28 12:00:00+00:00|VW1|
|2007-09-27 13:00:00+00:00|2007-09-28 15:00:00+00:00|VW2|
|2013-05-11 19:00:00+00:00|2013-05-14 20:00:00+00:00|VW2|
|2003-12-01 00:00:00+00:00|2005-05-08 00:00:00+00:00|RH1|
|2003-12-01 00:00:00+00:00|2005-05-08 00:00:00+00:00|TA3|
|2010-02-27 00:00:00+00:00|2010-04-14 00:00:00+00:00|HW2|
|2002-09-18 00:00:00+00:00|2003-04-30 00:00:00+00:00|HW1|
## <a id='s3-4' />Adjusting data at JAR1

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|DW1|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|DW1|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|DW2|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|DW2|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|HW1|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|HW1|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|HW2|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|HW2|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|ISWR|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|ISWR|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|NR|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|NR|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|OSWR|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|OSWR|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|P|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|P|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|RH1|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|RH1|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|RH2|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|RH2|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA1|time_shift|-745.0|337|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA1|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA2|time_shift|-745.0|0|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA2|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA3|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA3|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA4|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA4|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA5|time_shift|-745.0|338|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA5|time_shift|24.0|0|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS1|time_shift|-745.0|211|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS1|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS10|time_shift|-745.0|23|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS10|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS2|time_shift|-745.0|231|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS2|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS3|time_shift|-745.0|4|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS3|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS4|time_shift|-745.0|110|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS4|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS5|time_shift|-745.0|123|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS5|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS6|time_shift|-745.0|19|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS6|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS7|time_shift|-745.0|34|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS7|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS8|time_shift|-745.0|13|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS8|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TS9|time_shift|-745.0|60|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TS9|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|V|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|V|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|VW1|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|VW1|time_shift|24.0|18|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|VW2|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|VW2|time_shift|24.0|18|

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2005-01-27 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW1|add|0.31|0|
|2005-03-28 08:00:00+00:00|2019-09-08 01:00:00+00:00|HW1|add|0.23|0|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW1|hampel_filter|2.0|3596|
|2009-08-14 00:00:00+00:00|2010-05-01 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|487|
|2009-12-19 08:00:00+00:00|2019-09-08 01:00:00+00:00|HW1|add|-0.25|0|
|2010-06-11 00:00:00+00:00|2010-06-21 00:00:00+00:00|HW1|min_filter|2.21|3|
|2010-07-08 00:00:00+00:00|2010-07-19 00:00:00+00:00|HW1|min_filter|3.35|26|
|2018-10-01 00:00:00+00:00|2018-10-10 00:00:00+00:00|HW1|min_filter|2.17|5|
|2005-01-31 20:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|add|0.2|0|
|2006-12-22 10:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|add|0.28|0|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|17035|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|hampel_filter|2.0|1176|
|2016-02-26 21:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|add|0.3|0|
|2016-03-15 07:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|add|0.35|0|
|2016-03-20 06:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|add|-0.29|0|
|2017-01-13 00:00:00+00:00|2019-09-08 01:00:00+00:00|P|add|400.0|0|
|2012-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|RH2|swap_with_RH1|0.0|-1678|
|2005-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|TA3|swap_with_TA4|0.0|0|
|2018-02-01 00:00:00+00:00|2019-12-20 00:00:00+00:00|TA3|max_filter|9.0|248|
|2013-02-01 00:00:00+00:00|2015-12-20 00:00:00+00:00|TA4|max_filter|9.0|3469|
## <a id='s3-5' />ROC filter at JAR1
 
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
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_HS1.jpeg)
![Adjusted and flagged data at JAR1](figures/L1_data_treatment/JAR1_HS2.jpeg)
 

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2006-05-13 23:00:00+00:00|2019-09-08 01:00:00+00:00|HS1|add|0.55|0|
|2012-05-13 16:00:00+00:00|2019-09-08 01:00:00+00:00|HS1|add|0.62|0|
|2012-07-28 17:00:00+00:00|2019-09-08 01:00:00+00:00|HS1|add|0.28|0|
|2015-11-24 12:00:00+00:00|2019-09-08 01:00:00+00:00|HS1|add|-0.45|0|

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2005-08-06 17:00:00+00:00|2019-09-08 01:00:00+00:00|HS2|add|-0.39|0|
|2008-07-08 00:00:00+00:00|2019-09-08 01:00:00+00:00|HS2|add|0.25|0|
|2009-07-20 16:00:00+00:00|2019-09-08 01:00:00+00:00|HS2|add|-0.49|0|
|2010-04-26 09:00:00+00:00|2019-09-08 01:00:00+00:00|HS2|add|-0.27|0|
|2015-08-08 14:00:00+00:00|2019-09-08 01:00:00+00:00|HS2|add|-0.26|0|
|2015-10-13 20:00:00+00:00|2019-09-08 01:00:00+00:00|HS2|add|0.41|0|
|2016-04-05 02:00:00+00:00|2019-09-08 01:00:00+00:00|HS2|add|-0.29|0|
|2016-04-08 18:00:00+00:00|2019-09-08 01:00:00+00:00|HS2|add|0.27|0|
Using metadata/interpolated positions/JAR1_position_interpolated.csv for variable latitude and longitude
Using metadata/interpolated positions/GC-Net_elevation_tie_points.csv for variable elevation
# <a id='s4' />17 JAR2
## <a id='s4-1' />Gap filling with the C-level files at JAR2
CR10X-sourced HW1/HW2/HS1/HS2 dropped (81121 values) to be filled from the C-level file instead
RH1: 12650 hours taken from the C-level file converted from RH wrt ice to RH wrt water
RH2: 12633 hours taken from the C-level file converted from RH wrt ice to RH wrt water
Values taken from the C-level files: 487479
## <a id='s4-2' />Interpolated values filter at JAR2
ISWR: 24 samples flagged
OSWR: 20 samples flagged
NR: 144 samples flagged
TA1: 525 samples flagged
TA2: 1197 samples flagged
TA3: 281 samples flagged
TA4: 270 samples flagged
RH1: 184 samples flagged
RH2: 191 samples flagged
VW1: 3 samples flagged
VW2: 10 samples flagged
DW1: 3 samples flagged
DW2: 52 samples flagged
P: 1331 samples flagged
TA5: 6 samples flagged
TS1: 158 samples flagged
TS2: 3831 samples flagged
TS3: 373 samples flagged
TS4: 428 samples flagged
TS5: 568 samples flagged
TS6: 694 samples flagged
TS7: 403 samples flagged
TS8: 1691 samples flagged
TS9: 1613 samples flagged
TS10: 663 samples flagged
HS1: 411 samples flagged
HS2: 161 samples flagged
## <a id='s4-3' />Manual flagging of data at JAR2
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
|2012-09-20 15:00:00+00:00|2012-09-23 14:00:00+00:00|DW1|
|2012-10-12 21:00:00+00:00|2012-10-19 05:00:00+00:00|DW1|
|2012-10-19 08:00:00+00:00|2012-10-24 14:00:00+00:00|DW1|
|2012-10-27 19:00:00+00:00|2012-11-05 20:00:00+00:00|DW1|
|2012-11-07 13:00:00+00:00|2012-11-13 03:00:00+00:00|DW1|
|2012-11-18 15:00:00+00:00|2012-11-25 09:00:00+00:00|DW1|
|2013-04-13 12:00:00+00:00|2013-04-18 00:00:00+00:00|DW1|
|2013-04-25 16:00:00+00:00|2013-04-26 22:00:00+00:00|DW1|
|2013-04-27 17:00:00+00:00|2013-04-29 04:00:00+00:00|DW1|
|2013-05-20 03:00:00+00:00|2013-05-21 22:00:00+00:00|DW1|
|2010-08-23 17:00:00+00:00|2010-10-24 05:00:00+00:00|DW2|
|2012-09-09 18:00:00+00:00|2012-09-14 14:00:00+00:00|DW2|
|2012-10-06 11:00:00+00:00|2012-10-11 21:00:00+00:00|DW2|
|2012-10-13 17:00:00+00:00|2012-10-15 16:00:00+00:00|DW2|
|2012-10-28 05:00:00+00:00|2012-11-03 17:00:00+00:00|DW2|
|2012-11-03 20:00:00+00:00|2012-11-05 20:00:00+00:00|DW2|
|2012-11-07 13:00:00+00:00|2012-11-17 08:00:00+00:00|DW2|
|2012-11-18 15:00:00+00:00|2012-11-25 09:00:00+00:00|DW2|
|2013-04-13 12:00:00+00:00|2013-04-18 19:00:00+00:00|DW2|
|2013-04-19 03:00:00+00:00|2013-05-06 22:00:00+00:00|DW2|
|2003-07-31 00:00:00+00:00|2004-05-24 21:00:00+00:00|HW1|
|2004-05-25 01:00:00+00:00|2004-05-26 01:00:00+00:00|HW1|
|2010-05-14 12:00:00+00:00|2010-10-24 05:00:00+00:00|HW1|
|2003-07-31 00:00:00+00:00|2004-05-24 21:00:00+00:00|HW2|
|2004-05-25 01:00:00+00:00|2004-05-26 01:00:00+00:00|HW2|
|2010-05-14 12:00:00+00:00|2010-10-24 05:00:00+00:00|HW2|
|2012-10-06 11:00:00+00:00|2012-10-24 14:00:00+00:00|ISWR|
|2012-11-07 12:00:00+00:00|2012-11-17 08:00:00+00:00|ISWR|
|2012-11-18 14:00:00+00:00|2012-11-25 09:00:00+00:00|ISWR|
|2013-04-13 11:00:00+00:00|2013-06-13 08:00:00+00:00|ISWR|
|2000-05-27 01:00:00+00:00|2000-12-31 23:00:00+00:00|P|
|2001-01-01 01:00:00+00:00|2001-05-19 18:00:00+00:00|P|
|2001-05-21 13:00:00+00:00|2001-05-22 12:00:00+00:00|P|
|2009-05-12 03:00:00+00:00|2009-11-04 00:00:00+00:00|P|
|2010-04-20 10:00:00+00:00|2010-10-24 05:00:00+00:00|P|
|2011-06-10 20:00:00+00:00|2011-07-13 06:00:00+00:00|P|
|2009-05-12 03:00:00+00:00|2009-11-04 00:00:00+00:00|RH1|
|2010-04-20 10:00:00+00:00|2010-10-24 05:00:00+00:00|RH1|
|2009-05-12 03:00:00+00:00|2009-11-04 00:00:00+00:00|RH2|
|2010-04-20 10:00:00+00:00|2010-10-24 05:00:00+00:00|RH2|
|2009-05-12 03:00:00+00:00|2009-11-04 00:00:00+00:00|TA3|
|2010-04-20 10:00:00+00:00|2010-10-24 05:00:00+00:00|TA3|
|2009-05-12 03:00:00+00:00|2009-11-04 00:00:00+00:00|TA4|
|2010-04-20 10:00:00+00:00|2010-10-24 05:00:00+00:00|TA4|
|2007-12-05 01:00:00+00:00|2007-12-07 02:00:00+00:00|V|
|2011-06-12 03:00:00+00:00|2011-06-13 18:00:00+00:00|VW1|
|2011-06-13 20:00:00+00:00|2011-06-15 10:00:00+00:00|VW1|
|2012-09-05 17:00:00+00:00|2012-09-09 14:00:00+00:00|VW2|
|2012-09-09 18:00:00+00:00|2012-09-14 14:00:00+00:00|VW2|
|2012-09-15 00:00:00+00:00|2012-09-15 23:00:00+00:00|VW2|
|2012-09-19 10:00:00+00:00|2012-09-22 13:00:00+00:00|VW2|
|2012-10-06 11:00:00+00:00|2012-10-11 21:00:00+00:00|VW2|
|2012-10-28 05:00:00+00:00|2012-11-03 17:00:00+00:00|VW2|
|2012-11-07 13:00:00+00:00|2012-11-17 08:00:00+00:00|VW2|
|2001-08-30 00:00:00+00:00|2003-07-31 00:00:00+00:00|HW2|
|2004-05-27 00:00:00+00:00|2005-03-31 00:00:00+00:00|HW2|
## <a id='s4-4' />Adjusting data at JAR2

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|DW1|time_shift|-749.0|442|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|DW1|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|DW1|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|DW1|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|DW2|time_shift|-749.0|446|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|DW2|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|DW2|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|DW2|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|time_shift|-749.0|2|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW1|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|HW1|time_shift|67.0|68|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|HW1|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|time_shift|-749.0|2|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW2|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|HW2|time_shift|67.0|68|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|HW2|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|ISWR|time_shift|-749.0|517|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|ISWR|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|ISWR|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|ISWR|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|NR|time_shift|-749.0|517|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|NR|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|NR|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|NR|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|OSWR|time_shift|-749.0|517|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|OSWR|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|OSWR|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|OSWR|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|P|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|P|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|P|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|P|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|RH1|time_shift|-749.0|517|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|RH1|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|RH1|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|RH1|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|RH2|time_shift|-749.0|517|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|RH2|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|RH2|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|RH2|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TA1|time_shift|-749.0|517|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TA1|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TA1|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TA1|time_shift|24.0|24|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TA2|time_shift|-749.0|517|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TA2|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TA2|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TA2|time_shift|24.0|24|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TA3|time_shift|-749.0|517|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TA3|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TA3|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TA3|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TA4|time_shift|-749.0|517|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TA4|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TA4|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TA4|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TA5|time_shift|-749.0|445|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TA5|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TA5|time_shift|67.0|0|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TA5|time_shift|24.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS1|time_shift|-749.0|27|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS1|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TS1|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TS1|time_shift|24.0|24|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS10|time_shift|-749.0|0|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS10|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TS10|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TS10|time_shift|24.0|24|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS2|time_shift|-749.0|1|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS2|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TS2|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TS2|time_shift|24.0|24|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS3|time_shift|-749.0|27|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS3|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TS3|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TS3|time_shift|24.0|24|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS4|time_shift|-749.0|33|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS4|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TS4|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TS4|time_shift|24.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS5|time_shift|-749.0|27|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS5|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TS5|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TS5|time_shift|24.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS6|time_shift|-749.0|27|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS6|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TS6|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TS6|time_shift|24.0|24|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS7|time_shift|-749.0|0|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS7|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TS7|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TS7|time_shift|24.0|24|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS8|time_shift|-749.0|246|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS8|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TS8|time_shift|67.0|0|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TS8|time_shift|24.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|TS9|time_shift|-749.0|514|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|TS9|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|TS9|time_shift|67.0|0|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|TS9|time_shift|24.0|24|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|V|time_shift|-749.0|445|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|V|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|V|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|V|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|VW1|time_shift|-749.0|445|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|VW1|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|VW1|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|VW1|time_shift|24.0|25|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|VW2|time_shift|-749.0|445|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|VW2|time_shift|63.0|0|
|2006-01-29 00:00:00+00:00|2006-04-29 00:00:00+00:00|VW2|time_shift|67.0|67|
|1999-06-02 03:00:00+00:00|2000-05-26 20:00:00+00:00|VW2|time_shift|24.0|25|

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1999-04-19 00:00:00+00:00|2000-01-01 00:00:00+00:00|HW1|min_filter|0.5|9|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|max_filter|5.9|520|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|min_filter|1.05|4183|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|biweekly_upper_range_filter|0.7|792|
|1999-04-19 00:00:00+00:00|2000-01-01 00:00:00+00:00|HW2|min_filter|0.5|9|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|min_filter|0.5|9992|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|max_filter|7.5|58|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|biweekly_upper_range_filter|0.7|3911|
|2002-05-07 00:00:00+00:00|2013-06-16 08:00:00+00:00|RH1|swap_with_RH2|0.0|-3|
|2004-05-07 00:00:00+00:00|2005-05-14 00:00:00+00:00|VW1|swap_with_VW2|0.0|-4|
## <a id='s4-5' />ROC filter at JAR2
 
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
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_HS1.jpeg)
![Adjusted and flagged data at JAR2](figures/L1_data_treatment/JAR2_HS2.jpeg)
 

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2011-10-31 18:00:00+00:00|2013-06-16 08:00:00+00:00|HS2|add|0.25|0|
|2012-07-13 18:00:00+00:00|2013-06-16 08:00:00+00:00|HS2|add|0.26|0|
Using metadata/interpolated positions/GC-Net_elevation_tie_points.csv for variable elevation
# <a id='s5' />10 Saddle
## <a id='s5-1' />Gap filling with the C-level files at Saddle
CR10X-sourced HW1/HW2/HS1/HS2 dropped (184768 values) to be filled from the C-level file instead
RH1: 8684 hours taken from the C-level file converted from RH wrt ice to RH wrt water
RH2: 8683 hours taken from the C-level file converted from RH wrt ice to RH wrt water
Values taken from the C-level files: 536107
## <a id='s5-2' />Interpolated values filter at Saddle
ISWR: 3 samples flagged
NR: 50 samples flagged
TA1: 4643 samples flagged
TA2: 1144 samples flagged
TA3: 727 samples flagged
TA4: 49 samples flagged
RH1: 429 samples flagged
RH2: 196 samples flagged
VW1: 45 samples flagged
VW2: 30 samples flagged
DW1: 313 samples flagged
DW2: 320 samples flagged
P: 3611 samples flagged
TA5: 24 samples flagged
TS1: 11559 samples flagged
TS2: 3706 samples flagged
TS3: 4144 samples flagged
TS4: 8038 samples flagged
TS5: 11077 samples flagged
TS6: 7942 samples flagged
TS7: 8878 samples flagged
TS8: 8139 samples flagged
TS9: 12781 samples flagged
TS10: 15954 samples flagged
HS1: 196 samples flagged
HS2: 233 samples flagged
## <a id='s5-3' />Manual flagging of data at Saddle
Flagging data:
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|RH1|
|2010-01-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|RH2|
|2010-01-01 00:00:00+00:00|2016-01-01 00:00:00+00:00|TA1|
|2010-01-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|RH2|
|2009-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|VW1|
|2009-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|VW2|
|2005-05-14 14:00:00+00:00|2005-05-26 16:00:00+00:00|HW1|
|2012-09-18 00:00:00+00:00|2013-05-19 00:00:00+00:00|HW2|
|2014-10-09 00:00:00+00:00|2016-05-15 00:00:00+00:00|HW1|
|2017-08-16 00:00:00+00:00|2018-05-26 00:00:00+00:00|HW1|
|2019-12-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW1|
|2005-05-14 00:00:00+00:00|2005-05-26 00:00:00+00:00|HW2|
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
|1998-01-07 06:00:00+00:00|1998-01-09 02:00:00+00:00|DW1|
|1998-01-13 17:00:00+00:00|1998-01-15 20:00:00+00:00|DW1|
|1998-01-29 09:00:00+00:00|1998-02-01 15:00:00+00:00|DW1|
|1998-02-24 06:00:00+00:00|1998-02-25 09:00:00+00:00|DW1|
|1998-12-09 00:00:00+00:00|1998-12-10 07:00:00+00:00|DW1|
|1998-12-18 05:00:00+00:00|1998-12-19 07:00:00+00:00|DW1|
|1999-01-10 08:00:00+00:00|1999-01-17 12:00:00+00:00|DW1|
|1999-01-19 16:00:00+00:00|1999-01-20 15:00:00+00:00|DW1|
|1999-01-23 01:00:00+00:00|1999-01-24 04:00:00+00:00|DW1|
|2003-11-12 18:00:00+00:00|2003-11-16 14:00:00+00:00|DW1|
|2003-11-27 17:00:00+00:00|2003-11-30 16:00:00+00:00|DW1|
|2003-12-06 04:00:00+00:00|2004-01-18 05:00:00+00:00|DW1|
|2004-01-18 10:00:00+00:00|2004-02-16 11:00:00+00:00|DW1|
|2004-03-12 10:00:00+00:00|2004-03-22 19:00:00+00:00|DW1|
|2004-03-28 21:00:00+00:00|2004-04-14 09:00:00+00:00|DW1|
|2004-05-05 19:00:00+00:00|2004-05-09 13:00:00+00:00|DW1|
|2004-05-11 07:00:00+00:00|2004-05-13 16:00:00+00:00|DW1|
|2004-05-13 19:00:00+00:00|2004-05-17 02:00:00+00:00|DW1|
|2004-05-18 19:00:00+00:00|2004-05-28 17:00:00+00:00|DW1|
|2004-05-28 19:00:00+00:00|2004-06-11 19:00:00+00:00|DW1|
|2008-12-06 18:00:00+00:00|2008-12-08 18:00:00+00:00|DW1|
|2008-12-16 12:00:00+00:00|2008-12-17 18:00:00+00:00|DW1|
|2008-12-17 20:00:00+00:00|2008-12-20 13:00:00+00:00|DW1|
|2008-12-24 13:00:00+00:00|2008-12-26 04:00:00+00:00|DW1|
|2009-01-03 00:00:00+00:00|2009-01-06 03:00:00+00:00|DW1|
|2009-01-09 21:00:00+00:00|2009-01-13 02:00:00+00:00|DW1|
|2009-01-13 05:00:00+00:00|2009-01-20 16:00:00+00:00|DW1|
|2010-09-26 19:00:00+00:00|2010-09-30 09:00:00+00:00|DW1|
|2011-01-27 01:00:00+00:00|2011-01-28 02:00:00+00:00|DW1|
|2011-02-24 05:00:00+00:00|2011-02-25 14:00:00+00:00|DW1|
|2012-01-20 13:00:00+00:00|2012-01-22 12:00:00+00:00|DW1|
|2012-01-24 18:00:00+00:00|2012-01-26 14:00:00+00:00|DW1|
|2012-10-30 19:00:00+00:00|2012-11-01 18:00:00+00:00|DW1|
|2012-12-27 10:00:00+00:00|2013-01-01 03:00:00+00:00|DW1|
|2013-02-07 07:00:00+00:00|2013-02-09 12:00:00+00:00|DW1|
|2013-09-26 17:00:00+00:00|2013-09-27 22:00:00+00:00|DW1|
|2013-12-14 11:00:00+00:00|2013-12-18 18:00:00+00:00|DW1|
|2013-12-20 08:00:00+00:00|2013-12-22 04:00:00+00:00|DW1|
|2014-01-31 07:00:00+00:00|2014-02-01 07:00:00+00:00|DW1|
|2017-12-04 22:00:00+00:00|2017-12-06 03:00:00+00:00|DW1|
|2017-12-19 11:00:00+00:00|2017-12-20 12:00:00+00:00|DW1|
|2018-01-22 18:00:00+00:00|2018-01-25 14:00:00+00:00|DW1|
|2018-02-08 15:00:00+00:00|2018-02-10 03:00:00+00:00|DW1|
|1999-01-10 08:00:00+00:00|1999-01-12 03:00:00+00:00|DW2|
|1999-01-27 12:00:00+00:00|1999-01-28 11:00:00+00:00|DW2|
|2004-01-04 01:00:00+00:00|2004-01-07 01:00:00+00:00|DW2|
|2004-01-16 15:00:00+00:00|2004-01-17 18:00:00+00:00|DW2|
|2004-02-11 06:00:00+00:00|2004-02-12 20:00:00+00:00|DW2|
|2004-03-19 01:00:00+00:00|2004-03-22 12:00:00+00:00|DW2|
|2008-11-03 23:00:00+00:00|2008-11-06 02:00:00+00:00|DW2|
|2008-11-12 11:00:00+00:00|2008-11-13 12:00:00+00:00|DW2|
|2008-12-07 04:00:00+00:00|2008-12-08 17:00:00+00:00|DW2|
|2008-12-27 23:00:00+00:00|2008-12-30 00:00:00+00:00|DW2|
|2009-01-09 21:00:00+00:00|2009-01-20 16:00:00+00:00|DW2|
|2009-01-29 17:00:00+00:00|2009-01-31 02:00:00+00:00|DW2|
|2009-01-31 04:00:00+00:00|2009-02-02 11:00:00+00:00|DW2|
|2009-02-09 15:00:00+00:00|2009-02-10 19:00:00+00:00|DW2|
|2009-02-19 01:00:00+00:00|2009-03-01 06:00:00+00:00|DW2|
|2009-03-03 04:00:00+00:00|2009-03-05 17:00:00+00:00|DW2|
|2011-01-01 18:00:00+00:00|2011-01-03 03:00:00+00:00|DW2|
|2011-02-28 13:00:00+00:00|2011-03-02 10:00:00+00:00|DW2|
|2012-03-27 09:00:00+00:00|2012-03-29 03:00:00+00:00|DW2|
|2012-12-07 04:00:00+00:00|2012-12-08 05:00:00+00:00|DW2|
|2012-12-15 05:00:00+00:00|2012-12-20 08:00:00+00:00|DW2|
|2013-01-12 01:00:00+00:00|2013-01-13 20:00:00+00:00|DW2|
|2013-02-16 01:00:00+00:00|2013-02-18 11:00:00+00:00|DW2|
|2013-11-27 12:00:00+00:00|2013-11-28 21:00:00+00:00|DW2|
|2013-12-01 12:00:00+00:00|2013-12-03 11:00:00+00:00|DW2|
|2013-12-20 09:00:00+00:00|2013-12-22 09:00:00+00:00|DW2|
|2014-02-11 04:00:00+00:00|2014-02-14 11:00:00+00:00|DW2|
|2014-02-23 17:00:00+00:00|2014-02-25 23:00:00+00:00|DW2|
|2014-03-11 22:00:00+00:00|2014-03-14 19:00:00+00:00|DW2|
|2018-01-27 14:00:00+00:00|2018-01-29 17:00:00+00:00|DW2|
|2018-03-01 11:00:00+00:00|2018-03-04 09:00:00+00:00|DW2|
|2008-04-18 15:00:00+00:00|2008-05-03 18:00:00+00:00|HW2|
|2016-03-10 04:00:00+00:00|2016-03-17 02:00:00+00:00|HW1|
|2016-03-23 20:00:00+00:00|2016-03-30 22:00:00+00:00|HW1|
|2016-04-08 09:00:00+00:00|2016-05-20 17:00:00+00:00|HW1|
|2012-07-28 11:00:00+00:00|2012-07-29 17:00:00+00:00|HW2|
|2012-11-11 04:00:00+00:00|2012-11-22 02:00:00+00:00|HW2|
|2012-11-23 14:00:00+00:00|2012-11-26 10:00:00+00:00|HW2|
|2012-12-02 05:00:00+00:00|2012-12-06 08:00:00+00:00|HW2|
|2012-12-06 13:00:00+00:00|2012-12-07 21:00:00+00:00|HW2|
|2012-12-12 17:00:00+00:00|2012-12-25 20:00:00+00:00|HW2|
|2012-12-25 22:00:00+00:00|2012-12-27 21:00:00+00:00|HW2|
|2013-01-01 09:00:00+00:00|2013-01-07 12:00:00+00:00|HW2|
|2013-01-10 15:00:00+00:00|2013-01-13 04:00:00+00:00|HW2|
|2013-01-13 16:00:00+00:00|2013-01-19 04:00:00+00:00|HW2|
|2013-01-24 20:00:00+00:00|2013-02-01 12:00:00+00:00|HW2|
|2013-02-02 07:00:00+00:00|2013-02-05 17:00:00+00:00|HW2|
|2013-02-06 20:00:00+00:00|2013-02-09 15:00:00+00:00|HW2|
|2013-02-09 17:00:00+00:00|2013-02-14 07:00:00+00:00|HW2|
|2013-02-15 13:00:00+00:00|2013-03-02 20:00:00+00:00|HW2|
|2013-03-07 05:00:00+00:00|2013-03-09 04:00:00+00:00|HW2|
|2013-03-11 22:00:00+00:00|2013-04-06 01:00:00+00:00|HW2|
|2013-04-06 15:00:00+00:00|2013-04-19 01:00:00+00:00|HW2|
|2013-04-19 16:00:00+00:00|2013-04-21 09:00:00+00:00|HW2|
|2013-04-21 15:00:00+00:00|2013-04-27 12:00:00+00:00|HW2|
|2013-04-27 19:00:00+00:00|2013-05-02 18:00:00+00:00|HW2|
|2013-05-04 05:00:00+00:00|2013-05-05 19:00:00+00:00|HW2|
|2013-05-09 19:00:00+00:00|2013-05-11 19:00:00+00:00|HW2|
|1997-10-07 16:00:00+00:00|1997-10-11 16:00:00+00:00|VW1|
|1998-01-13 17:00:00+00:00|1998-01-15 20:00:00+00:00|VW1|
|1998-03-02 16:00:00+00:00|1998-03-10 14:00:00+00:00|VW1|
|1998-12-11 20:00:00+00:00|1998-12-13 05:00:00+00:00|VW1|
|1998-12-18 05:00:00+00:00|1998-12-19 11:00:00+00:00|VW1|
|1999-01-16 00:00:00+00:00|1999-01-17 11:00:00+00:00|VW1|
|2000-11-27 17:00:00+00:00|2000-12-01 03:00:00+00:00|VW1|
|2000-12-02 02:00:00+00:00|2000-12-03 07:00:00+00:00|VW1|
|2002-02-03 05:00:00+00:00|2002-02-04 18:00:00+00:00|VW1|
|2002-02-04 22:00:00+00:00|2002-02-06 15:00:00+00:00|VW1|
|2003-10-02 17:00:00+00:00|2003-10-03 23:00:00+00:00|VW1|
|2003-11-13 05:00:00+00:00|2003-11-15 12:00:00+00:00|VW1|
|2003-11-15 15:00:00+00:00|2003-11-17 22:00:00+00:00|VW1|
|2003-11-18 19:00:00+00:00|2003-11-21 05:00:00+00:00|VW1|
|2003-12-01 17:00:00+00:00|2003-12-04 22:00:00+00:00|VW1|
|2003-12-06 04:00:00+00:00|2003-12-13 08:00:00+00:00|VW1|
|2003-12-13 10:00:00+00:00|2003-12-19 09:00:00+00:00|VW1|
|2003-12-19 12:00:00+00:00|2004-01-17 21:00:00+00:00|VW1|
|2004-01-18 00:00:00+00:00|2004-01-27 01:00:00+00:00|VW1|
|2004-01-27 03:00:00+00:00|2004-02-14 18:00:00+00:00|VW1|
|2004-02-14 21:00:00+00:00|2004-02-18 05:00:00+00:00|VW1|
|2004-02-18 07:00:00+00:00|2004-02-21 22:00:00+00:00|VW1|
|2004-02-23 11:00:00+00:00|2004-02-24 21:00:00+00:00|VW1|
|2004-02-24 23:00:00+00:00|2004-02-27 07:00:00+00:00|VW1|
|2004-02-27 09:00:00+00:00|2004-03-02 08:00:00+00:00|VW1|
|2004-03-03 13:00:00+00:00|2004-03-05 20:00:00+00:00|VW1|
|2004-03-05 22:00:00+00:00|2004-03-07 09:00:00+00:00|VW1|
|2004-03-07 12:00:00+00:00|2004-03-10 18:00:00+00:00|VW1|
|2004-03-10 20:00:00+00:00|2004-03-22 22:00:00+00:00|VW1|
|2004-03-23 14:00:00+00:00|2004-03-25 03:00:00+00:00|VW1|
|2004-03-25 05:00:00+00:00|2004-04-20 13:00:00+00:00|VW1|
|2004-04-20 15:00:00+00:00|2004-04-28 13:00:00+00:00|VW1|
|2004-04-28 15:00:00+00:00|2004-05-02 23:00:00+00:00|VW1|
|2004-05-03 02:00:00+00:00|2004-05-09 17:00:00+00:00|VW1|
|2004-05-10 13:00:00+00:00|2004-05-18 00:00:00+00:00|VW1|
|2004-05-18 02:00:00+00:00|2004-06-06 21:00:00+00:00|VW1|
|2004-06-06 23:00:00+00:00|2004-06-11 19:00:00+00:00|VW1|
|2008-01-12 01:00:00+00:00|2008-01-13 12:00:00+00:00|VW1|
|2008-01-15 10:00:00+00:00|2008-01-18 23:00:00+00:00|VW1|
|2008-02-02 15:00:00+00:00|2008-02-07 16:00:00+00:00|VW1|
|2008-02-20 04:00:00+00:00|2008-02-24 13:00:00+00:00|VW1|
|2008-02-27 07:00:00+00:00|2008-03-01 16:00:00+00:00|VW1|
|2008-03-02 23:00:00+00:00|2008-03-04 00:00:00+00:00|VW1|
|2008-03-06 14:00:00+00:00|2008-03-09 13:00:00+00:00|VW1|
|2008-03-19 19:00:00+00:00|2008-03-21 09:00:00+00:00|VW1|
|2008-12-07 04:00:00+00:00|2008-12-08 17:00:00+00:00|VW1|
|2009-01-04 09:00:00+00:00|2009-01-06 03:00:00+00:00|VW1|
|2009-01-09 21:00:00+00:00|2009-01-13 02:00:00+00:00|VW1|
|2009-01-13 05:00:00+00:00|2009-01-20 16:00:00+00:00|VW1|
|2009-01-28 12:00:00+00:00|2009-02-02 12:00:00+00:00|VW1|
|2009-02-13 10:00:00+00:00|2009-03-01 06:00:00+00:00|VW1|
|2009-03-05 20:00:00+00:00|2009-03-17 17:00:00+00:00|VW1|
|2009-04-21 19:00:00+00:00|2009-04-23 16:00:00+00:00|VW1|
|2011-02-24 05:00:00+00:00|2011-02-25 14:00:00+00:00|VW1|
|2011-02-28 16:00:00+00:00|2011-03-02 10:00:00+00:00|VW1|
|2012-01-20 18:00:00+00:00|2012-01-22 04:00:00+00:00|VW1|
|2012-02-24 21:00:00+00:00|2012-03-04 00:00:00+00:00|VW1|
|2012-03-14 11:00:00+00:00|2012-03-18 04:00:00+00:00|VW1|
|2012-10-30 19:00:00+00:00|2012-11-01 18:00:00+00:00|VW1|
|2012-12-15 15:00:00+00:00|2012-12-17 10:00:00+00:00|VW1|
|2012-12-27 10:00:00+00:00|2013-01-01 03:00:00+00:00|VW1|
|2013-01-12 00:00:00+00:00|2013-01-14 01:00:00+00:00|VW1|
|2013-01-28 13:00:00+00:00|2013-01-31 13:00:00+00:00|VW1|
|2013-02-02 22:00:00+00:00|2013-02-05 14:00:00+00:00|VW1|
|2013-02-16 01:00:00+00:00|2013-02-18 15:00:00+00:00|VW1|
|2013-02-19 16:00:00+00:00|2013-02-21 06:00:00+00:00|VW1|
|2013-02-27 00:00:00+00:00|2013-03-01 11:00:00+00:00|VW1|
|2013-03-01 15:00:00+00:00|2013-03-08 23:00:00+00:00|VW1|
|2013-03-13 18:00:00+00:00|2013-03-15 10:00:00+00:00|VW1|
|2013-03-16 19:00:00+00:00|2013-03-18 14:00:00+00:00|VW1|
|2013-04-30 15:00:00+00:00|2013-05-01 16:00:00+00:00|VW1|
|2013-09-26 17:00:00+00:00|2013-09-27 22:00:00+00:00|VW1|
|2013-12-01 12:00:00+00:00|2013-12-03 11:00:00+00:00|VW1|
|2013-12-08 20:00:00+00:00|2013-12-11 00:00:00+00:00|VW1|
|2013-12-14 11:00:00+00:00|2013-12-18 18:00:00+00:00|VW1|
|2014-01-16 11:00:00+00:00|2014-01-19 12:00:00+00:00|VW1|
|2014-01-22 14:00:00+00:00|2014-01-24 00:00:00+00:00|VW1|
|2014-01-24 17:00:00+00:00|2014-01-27 11:00:00+00:00|VW1|
|2014-01-31 07:00:00+00:00|2014-02-01 07:00:00+00:00|VW1|
|2014-02-03 05:00:00+00:00|2014-02-06 09:00:00+00:00|VW1|
|2014-02-08 18:00:00+00:00|2014-02-10 17:00:00+00:00|VW1|
|2014-02-10 19:00:00+00:00|2014-02-15 08:00:00+00:00|VW1|
|2014-02-20 06:00:00+00:00|2014-02-23 01:00:00+00:00|VW1|
|2014-02-23 17:00:00+00:00|2014-02-25 23:00:00+00:00|VW1|
|2014-05-18 19:00:00+00:00|2014-05-20 02:00:00+00:00|VW1|
|2014-05-23 15:00:00+00:00|2014-05-24 14:00:00+00:00|VW1|
|2014-12-28 18:00:00+00:00|2015-01-17 23:00:00+00:00|VW1|
|2015-02-11 02:00:00+00:00|2015-03-03 16:00:00+00:00|VW1|
|2016-04-29 00:00:00+00:00|2016-05-20 17:00:00+00:00|VW1|
|2017-11-30 07:00:00+00:00|2017-12-02 00:00:00+00:00|VW1|
|2017-12-07 18:00:00+00:00|2017-12-09 13:00:00+00:00|VW1|
|2017-12-31 00:00:00+00:00|2018-01-01 12:00:00+00:00|VW1|
|2018-01-10 16:00:00+00:00|2018-01-11 20:00:00+00:00|VW1|
|2018-01-12 17:00:00+00:00|2018-01-17 01:00:00+00:00|VW1|
|2018-01-17 16:00:00+00:00|2018-01-20 15:00:00+00:00|VW1|
|2018-01-21 01:00:00+00:00|2018-01-22 01:00:00+00:00|VW1|
|2018-01-23 18:00:00+00:00|2018-01-25 10:00:00+00:00|VW1|
|2018-01-25 14:00:00+00:00|2018-01-26 22:00:00+00:00|VW1|
|2018-01-27 14:00:00+00:00|2018-01-30 04:00:00+00:00|VW1|
|2018-02-03 22:00:00+00:00|2018-02-05 22:00:00+00:00|VW1|
|2018-02-06 07:00:00+00:00|2018-02-08 19:00:00+00:00|VW1|
|2018-02-12 09:00:00+00:00|2018-02-13 15:00:00+00:00|VW1|
|2018-02-14 18:00:00+00:00|2018-02-17 09:00:00+00:00|VW1|
|2018-02-18 03:00:00+00:00|2018-02-25 03:00:00+00:00|VW1|
|2018-02-26 03:00:00+00:00|2018-02-27 08:00:00+00:00|VW1|
Warning: VW1_max not found
Warning: VW1_max not found
Warning: VW1_max not found
Warning: VW1_max not found
Warning: VW1_max not found
Warning: VW1_max not found
Warning: VW1_max not found
Warning: VW1_max not found
Warning: VW1_max not found
|1999-01-13 20:00:00+00:00|1999-01-14 19:00:00+00:00|VW2|
|1999-01-16 00:00:00+00:00|1999-01-17 11:00:00+00:00|VW2|
|1999-02-24 00:00:00+00:00|1999-02-25 02:00:00+00:00|VW2|
|2003-11-18 22:00:00+00:00|2003-11-20 22:00:00+00:00|VW2|
|2004-01-04 01:00:00+00:00|2004-01-07 01:00:00+00:00|VW2|
|2004-01-10 01:00:00+00:00|2004-01-12 06:00:00+00:00|VW2|
|2004-01-12 14:00:00+00:00|2004-01-14 07:00:00+00:00|VW2|
|2004-01-14 20:00:00+00:00|2004-01-16 08:00:00+00:00|VW2|
|2004-01-16 15:00:00+00:00|2004-01-17 18:00:00+00:00|VW2|
|2004-03-03 11:00:00+00:00|2004-03-05 18:00:00+00:00|VW2|
|2004-03-07 20:00:00+00:00|2004-03-09 16:00:00+00:00|VW2|
|2004-03-29 15:00:00+00:00|2004-04-04 18:00:00+00:00|VW2|
|2007-03-24 19:00:00+00:00|2007-03-25 22:00:00+00:00|VW2|
|2007-12-28 08:00:00+00:00|2007-12-30 00:00:00+00:00|VW2|
|2008-01-15 10:00:00+00:00|2008-01-17 23:00:00+00:00|VW2|
|2008-01-18 01:00:00+00:00|2008-01-19 08:00:00+00:00|VW2|
|2008-01-25 15:00:00+00:00|2008-01-27 04:00:00+00:00|VW2|
|2008-01-27 08:00:00+00:00|2008-01-30 02:00:00+00:00|VW2|
|2008-01-30 04:00:00+00:00|2008-02-08 20:00:00+00:00|VW2|
|2008-02-08 22:00:00+00:00|2008-02-12 16:00:00+00:00|VW2|
|2008-02-13 21:00:00+00:00|2008-02-19 00:00:00+00:00|VW2|
|2008-02-19 07:00:00+00:00|2008-02-24 15:00:00+00:00|VW2|
|2008-02-26 22:00:00+00:00|2008-03-01 17:00:00+00:00|VW2|
|2008-03-02 01:00:00+00:00|2008-03-03 23:00:00+00:00|VW2|
|2008-03-06 05:00:00+00:00|2008-03-10 02:00:00+00:00|VW2|
|2008-03-10 17:00:00+00:00|2008-03-11 16:00:00+00:00|VW2|
|2008-03-17 08:00:00+00:00|2008-03-18 09:00:00+00:00|VW2|
|2008-03-18 14:00:00+00:00|2008-03-20 15:00:00+00:00|VW2|
|2008-03-28 09:00:00+00:00|2008-03-29 15:00:00+00:00|VW2|
|2008-03-29 17:00:00+00:00|2008-04-04 07:00:00+00:00|VW2|
|2009-01-04 09:00:00+00:00|2009-01-05 22:00:00+00:00|VW2|
|2009-01-06 09:00:00+00:00|2009-01-08 19:00:00+00:00|VW2|
|2009-01-09 21:00:00+00:00|2009-01-13 02:00:00+00:00|VW2|
|2009-01-13 04:00:00+00:00|2009-01-21 08:00:00+00:00|VW2|
|2009-01-27 00:00:00+00:00|2009-01-28 10:00:00+00:00|VW2|
|2009-01-29 17:00:00+00:00|2009-01-31 02:00:00+00:00|VW2|
|2009-01-31 04:00:00+00:00|2009-02-02 11:00:00+00:00|VW2|
|2009-02-03 11:00:00+00:00|2009-02-04 15:00:00+00:00|VW2|
|2009-02-08 05:00:00+00:00|2009-02-09 07:00:00+00:00|VW2|
|2009-02-09 15:00:00+00:00|2009-02-10 15:00:00+00:00|VW2|
|2009-02-10 17:00:00+00:00|2009-02-12 14:00:00+00:00|VW2|
|2009-02-13 10:00:00+00:00|2009-02-18 05:00:00+00:00|VW2|
|2009-02-19 01:00:00+00:00|2009-03-01 06:00:00+00:00|VW2|
|2009-03-03 04:00:00+00:00|2009-03-05 17:00:00+00:00|VW2|
|2009-03-06 16:00:00+00:00|2009-03-17 17:00:00+00:00|VW2|
|2009-03-21 12:00:00+00:00|2009-03-22 16:00:00+00:00|VW2|
|2009-03-24 11:00:00+00:00|2009-03-27 14:00:00+00:00|VW2|
|2009-03-28 13:00:00+00:00|2009-04-15 05:00:00+00:00|VW2|
|2011-02-23 23:00:00+00:00|2011-02-25 14:00:00+00:00|VW2|
|2011-02-28 16:00:00+00:00|2011-03-02 10:00:00+00:00|VW2|
|2012-02-22 12:00:00+00:00|2012-02-23 20:00:00+00:00|VW2|
|2012-02-25 09:00:00+00:00|2012-03-04 00:00:00+00:00|VW2|
|2012-03-14 11:00:00+00:00|2012-03-17 18:00:00+00:00|VW2|
|2012-03-21 16:00:00+00:00|2012-03-23 00:00:00+00:00|VW2|
|2012-12-15 05:00:00+00:00|2012-12-20 08:00:00+00:00|VW2|
|2013-01-29 05:00:00+00:00|2013-01-30 07:00:00+00:00|VW2|
|2013-02-19 13:00:00+00:00|2013-02-23 02:00:00+00:00|VW2|
|2013-02-27 00:00:00+00:00|2013-03-09 01:00:00+00:00|VW2|
|2013-03-13 18:00:00+00:00|2013-03-18 11:00:00+00:00|VW2|
|2014-01-17 08:00:00+00:00|2014-01-19 10:00:00+00:00|VW2|
|2014-01-24 21:00:00+00:00|2014-01-27 10:00:00+00:00|VW2|
|2014-02-03 06:00:00+00:00|2014-02-05 23:00:00+00:00|VW2|
|2014-02-09 07:00:00+00:00|2014-02-10 09:00:00+00:00|VW2|
|2014-02-11 04:00:00+00:00|2014-02-14 11:00:00+00:00|VW2|
|2014-03-02 02:00:00+00:00|2014-03-04 03:00:00+00:00|VW2|
|2014-03-05 09:00:00+00:00|2014-03-08 14:00:00+00:00|VW2|
|2014-03-10 15:00:00+00:00|2014-03-11 20:00:00+00:00|VW2|
|2014-03-11 22:00:00+00:00|2014-03-14 19:00:00+00:00|VW2|
|2014-03-19 03:00:00+00:00|2014-03-23 06:00:00+00:00|VW2|
|2014-03-24 14:00:00+00:00|2014-03-25 23:00:00+00:00|VW2|
|2014-04-02 14:00:00+00:00|2014-04-08 12:00:00+00:00|VW2|
## <a id='s5-4' />Adjusting data at Saddle

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2001-12-25 01:00:00+00:00|2021-10-16 17:00:00+00:00|HW1|add|0.38|0|
|2004-10-14 13:00:00+00:00|2005-01-30 16:00:00+00:00|HW1|add|-2.6|0|
|2005-03-28 16:00:00+00:00|2005-05-14 13:00:00+00:00|HW1|add|-2.6|0|
|2009-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2019-09-03 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.5|19710|
|2009-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW1|hampel_filter|2.0|2406|
|2019-09-03 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW1|max_filter|1.4|7686|
|2019-09-03 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW1|min_filter|1.08|3868|
|2003-12-11 11:00:00+00:00|2021-10-16 17:00:00+00:00|HW2|add|0.25|0|
|2007-05-27 15:00:00+00:00|2008-05-03 18:00:00+00:00|HW2|add|2.6|0|
|2009-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|17195|
|2009-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW2|hampel_filter|2.0|1020|
|2019-05-15 00:00:00+00:00|2021-10-16 17:00:00+00:00|HW2|min_filter|0.5|3214|
|1990-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TA1|swap_with_TA2|0.0|-34|
|2000-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TA1|swap_with_TA2|0.0|-25250|
## <a id='s5-5' />ROC filter at Saddle
 
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
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_HS1.jpeg)
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_HS2.jpeg)
 

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-04-17 14:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|0.4|0|
|1999-04-16 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|2.1|0|
|2001-06-05 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|2.6|0|
|2002-06-07 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|0.5|0|
|2004-06-12 09:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|2.77|0|
|2005-05-26 20:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|2.29|0|
|2010-01-07 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|4.0|0|
|2014-05-21 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|2.5|0|
|2018-04-24 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS1|add|1.5|0|
 
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_HS1.jpeg)
 

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1999-04-16 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|2.5|0|
|2001-06-05 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|2.5|0|
|2001-12-25 01:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|-1.0|0|
|2004-06-12 13:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|2.65|0|
|2005-05-26 20:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|2.61|0|
|2010-01-07 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|4.0|0|
|2014-05-24 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|4.0|0|
|2018-03-01 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|2.0|0|
 
![Adjusted and flagged data at Saddle](figures/L1_data_treatment/Saddle_HS2.jpeg)
 
# <a id='s6' />22 Petermann ELA
## <a id='s6-1' />Gap filling with the C-level files at Petermann ELA
CR10X-sourced HW1/HW2/HS1/HS2 dropped (8151 values) to be filled from the C-level file instead
RH1: 2 hours taken from the C-level file converted from RH wrt ice to RH wrt water
RH2: 2 hours taken from the C-level file converted from RH wrt ice to RH wrt water
Values taken from the C-level files: 191173
## <a id='s6-2' />Interpolated values filter at Petermann ELA
ISWR: 16 samples flagged
NR: 15 samples flagged
TA1: 562 samples flagged
TA2: 554 samples flagged
TA3: 763 samples flagged
TA4: 775 samples flagged
RH1: 632 samples flagged
RH2: 632 samples flagged
VW1: 3 samples flagged
DW1: 22 samples flagged
P: 1666 samples flagged
TS1: 547 samples flagged
TS2: 1810 samples flagged
TS3: 84 samples flagged
TS4: 27 samples flagged
TS5: 27 samples flagged
TS6: 42 samples flagged
TS7: 42 samples flagged
TS8: 42 samples flagged
TS9: 38 samples flagged
TS10: 27 samples flagged
HS2: 11 samples flagged
## <a id='s6-3' />Manual flagging of data at Petermann ELA
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
|2012-12-07 14:00:00+00:00|2012-12-08 19:00:00+00:00|DW1|
|2012-12-23 12:00:00+00:00|2012-12-24 17:00:00+00:00|DW1|
|2013-01-07 22:00:00+00:00|2013-01-09 04:00:00+00:00|DW1|
|2013-12-09 16:00:00+00:00|2013-12-10 16:00:00+00:00|DW1|
|2013-12-10 18:00:00+00:00|2013-12-12 01:00:00+00:00|DW1|
|2013-12-27 01:00:00+00:00|2014-01-01 05:00:00+00:00|DW1|
|2014-01-21 14:00:00+00:00|2014-01-22 13:00:00+00:00|DW1|
|2014-02-05 19:00:00+00:00|2014-02-13 14:00:00+00:00|DW1|
|2014-02-19 12:00:00+00:00|2014-02-20 12:00:00+00:00|DW1|
|2014-02-21 17:00:00+00:00|2014-02-22 21:00:00+00:00|DW1|
|2014-02-26 22:00:00+00:00|2014-03-02 22:00:00+00:00|DW1|
|2014-03-08 05:00:00+00:00|2014-03-09 04:00:00+00:00|DW1|
|2014-03-16 08:00:00+00:00|2014-03-17 07:00:00+00:00|DW1|
|2014-03-20 09:00:00+00:00|2014-03-29 15:00:00+00:00|DW1|
|2014-04-01 04:00:00+00:00|2014-04-02 13:00:00+00:00|DW1|
|2014-04-03 09:00:00+00:00|2014-04-04 19:00:00+00:00|DW1|
|2014-04-12 08:00:00+00:00|2014-04-13 15:00:00+00:00|DW1|
|2014-04-16 10:00:00+00:00|2014-04-19 17:00:00+00:00|DW1|
|2014-10-19 11:00:00+00:00|2015-01-05 19:00:00+00:00|HW1|
|2015-03-23 13:00:00+00:00|2015-03-24 21:00:00+00:00|HW1|
|2015-03-25 08:00:00+00:00|2015-05-20 20:00:00+00:00|HW1|
|2015-05-20 22:00:00+00:00|2015-06-10 07:00:00+00:00|HW1|
|2015-06-11 03:00:00+00:00|2015-11-30 20:00:00+00:00|HW1|
|2016-03-11 04:00:00+00:00|2016-03-12 12:00:00+00:00|HW1|
|2016-03-12 18:00:00+00:00|2016-05-26 13:00:00+00:00|HW1|
|2011-06-02 00:00:00+00:00|2011-06-07 13:00:00+00:00|HW2|
|2011-06-07 15:00:00+00:00|2011-06-12 20:00:00+00:00|HW2|
|2011-06-13 00:00:00+00:00|2011-06-14 18:00:00+00:00|HW2|
|2011-06-14 21:00:00+00:00|2011-06-25 16:00:00+00:00|HW2|
|2011-06-25 22:00:00+00:00|2011-07-05 14:00:00+00:00|HW2|
|2011-07-10 07:00:00+00:00|2011-07-17 13:00:00+00:00|HW2|
|2011-08-15 09:00:00+00:00|2011-08-17 19:00:00+00:00|HW2|
|2011-08-18 13:00:00+00:00|2011-10-20 01:00:00+00:00|HW2|
|2012-03-18 04:00:00+00:00|2012-03-31 18:00:00+00:00|HW2|
|2012-03-31 20:00:00+00:00|2012-04-12 15:00:00+00:00|HW2|
|2012-04-12 23:00:00+00:00|2012-04-15 13:00:00+00:00|HW2|
|2012-04-16 11:00:00+00:00|2012-05-02 07:00:00+00:00|HW2|
|2012-05-02 10:00:00+00:00|2012-05-25 12:00:00+00:00|HW2|
|2018-03-08 13:00:00+00:00|2018-03-10 02:00:00+00:00|HW2|
|2018-03-13 12:00:00+00:00|2018-03-25 13:00:00+00:00|HW2|
|2018-04-20 06:00:00+00:00|2018-04-30 05:00:00+00:00|HW2|
|2018-05-02 10:00:00+00:00|2018-05-06 05:00:00+00:00|HW2|
|2018-05-06 08:00:00+00:00|2018-05-08 01:00:00+00:00|HW2|
|2018-05-10 12:00:00+00:00|2018-05-14 18:00:00+00:00|HW2|
|2018-05-14 20:00:00+00:00|2018-05-24 13:00:00+00:00|HW2|
|2015-11-29 05:00:00+00:00|2015-11-30 20:00:00+00:00|OSWR|
|2011-06-02 00:00:00+00:00|2011-10-22 02:00:00+00:00|P|
|2012-03-15 13:00:00+00:00|2012-03-17 20:00:00+00:00|P|
|2012-03-18 04:00:00+00:00|2012-05-25 12:00:00+00:00|P|
|2003-05-25 00:00:00+00:00|2003-07-09 00:00:00+00:00|HW2|
|2007-03-24 00:00:00+00:00|2007-04-11 00:00:00+00:00|HW2|
|2003-08-06 00:00:00+00:00|2003-09-10 00:00:00+00:00|HW2|
## <a id='s6-4' />Adjusting data at Petermann ELA

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|DW1|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|DW2|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|HW1|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|HW2|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|ISWR|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|NR|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|OSWR|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|P|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|RH1|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|RH2|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TA1|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TA2|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TA3|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TA4|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TA5|time_shift|-112.0|0|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TS1|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TS10|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TS2|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TS3|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TS4|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TS5|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TS6|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TS7|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TS8|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|TS9|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|V|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|VW1|time_shift|-112.0|1|
|2005-04-09 00:00:00+00:00|2005-10-16 00:00:00+00:00|VW2|time_shift|-112.0|1|

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2007-03-01 00:00:00+00:00|2007-04-10 00:00:00+00:00|HW1|min_filter|2.26|10|
|2009-05-15 00:00:00+00:00|2022-04-12 18:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2011-09-01 00:00:00+00:00|2012-05-01 00:00:00+00:00|HW1|max_filter|0.81|129|
|2012-08-16 00:00:00+00:00|2014-05-01 00:00:00+00:00|HW1|min_filter|1.37|1901|
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
## <a id='s6-5' />ROC filter at Petermann ELA
 
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
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_HS1.jpeg)
![Adjusted and flagged data at Petermann ELA](figures/L1_data_treatment/PetermannELA_HS2.jpeg)
 

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2013-05-26 22:00:00+00:00|2022-04-12 18:00:00+00:00|HS1|add|0.25|0|

|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
Using metadata/interpolated positions/Petermann ELA_position_interpolated.csv for variable latitude and longitude

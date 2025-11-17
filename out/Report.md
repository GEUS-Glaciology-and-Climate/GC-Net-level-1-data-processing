# 0 Swiss Camp 10m
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
|2014-01-01 00:00:00+00:00|2020-11-03 21:00:00+00:00|TA1|swap_with_TA2|0.0|0|
 
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
 
# 1 Swiss Camp
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
 
# 2 Crawford Point 1
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
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW1|swap_with_HW2|0.0|574|
|2010-05-09 22:00:00+00:00|2010-08-07 00:00:00+00:00|HW1|swap_with_HW2|0.0|38|
|2011-05-02 14:00:00+00:00|2020-07-22 09:00:00+00:00|HW1|swap_with_HW2|0.0|5157|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2001-12-31 14:00:00+00:00|2002-12-31 14:00:00+00:00|HW1|add|-0.3|0|
|2002-09-24 13:00:00+00:00|2002-12-31 14:00:00+00:00|HW1|add|-0.94|0|
|2009-05-10 00:00:00+00:00|2020-07-22 09:00:00+00:00|HW1|hampel_filter|2.0|4333|
|2009-12-14 15:00:00+00:00|2010-05-09 22:00:00+00:00|HW1|add|-1.1|0|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW1|min_filter|0.1|8873|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW1|biweekly_upper_range_filter|0.5|1363|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|HW1|time_shift|24.0|25|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|HW1|time_shift|24.0|24|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|HW1|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW1|time_shift|180552.0|5857|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|809|
|2002-12-31 14:00:00+00:00|2002-12-31 14:00:00+00:00|HW2|add|-1.0|0|
|2009-05-10 00:00:00+00:00|2020-07-22 09:00:00+00:00|HW2|hampel_filter|2.0|7126|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2010-05-09 22:00:00+00:00|2010-08-07 00:00:00+00:00|HW2|max_filter|3.9|10|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW2|min_filter|0.1|1535|
|2010-05-09 22:00:00+00:00|2020-07-22 09:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|12382|
|2017-05-10 00:00:00+00:00|2020-07-22 09:00:00+00:00|HW2|biweekly_upper_range_filter|0.2|1502|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|HW2|time_shift|24.0|25|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|HW2|time_shift|24.0|24|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|HW2|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|HW2|time_shift|180552.0|5622|
|2012-01-01 00:00:00+00:00|2020-07-22 09:00:00+00:00|ISWR|swap_with_OSWR|0.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|ISWR|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|ISWR|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|ISWR|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|ISWR|time_shift|180552.0|14|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|NR|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|NR|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|NR|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|NR|time_shift|180552.0|1769|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|OSWR|time_shift|24.0|19|
|2010-05-09 00:00:00+00:00|2020-07-22 09:00:00+00:00|OSWR|multiply|0.934|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|OSWR|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|OSWR|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|OSWR|time_shift|180552.0|22|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|P|time_shift|24.0|25|
|1999-01-01 00:00:00+00:00|2010-05-09 22:00:00+00:00|P|add|-12.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|P|time_shift|24.0|24|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|P|time_shift|24.0|1|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|P|time_shift|180552.0|6431|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|RH1|time_shift|24.0|19|
|1996-01-01 00:00:00+00:00|2010-05-16 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|RH1|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|RH1|time_shift|24.0|7|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|RH1|time_shift|180552.0|6419|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|RH2|time_shift|24.0|19|
|1996-01-01 00:00:00+00:00|2010-05-16 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|RH2|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|RH2|time_shift|24.0|4|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|RH2|time_shift|180552.0|6431|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TA1|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TA1|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TA1|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TA1|time_shift|180552.0|6431|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TA2|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TA2|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TA2|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TA2|time_shift|180552.0|6431|
|1990-01-01 16:00:00+00:00|1999-01-01 00:00:00+00:00|TA3|swap_with_TA4|0.0|45|
|2006-01-01 00:00:00+00:00|2007-04-26 00:00:00+00:00|TA3|swap_with_TA4|0.0|3087|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TA3|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TA3|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TA3|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TA3|time_shift|180552.0|6431|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TA4|time_shift|24.0|19|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TA4|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TA4|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TA4|time_shift|180552.0|6429|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TA5|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TA5|time_shift|24.0|0|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TA5|time_shift|24.0|0|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TA5|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS1|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS1|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS1|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS1|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS10|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS10|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS10|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS10|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS2|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS2|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS2|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS2|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS3|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS3|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS3|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS3|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS4|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS4|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS4|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS4|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS5|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS5|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS5|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS5|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS6|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS6|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS6|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS6|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS7|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS7|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS7|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS7|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS8|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS8|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS8|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS8|time_shift|180552.0|0|
|2008-06-12 00:00:00+00:00|2009-04-27 00:00:00+00:00|TS9|time_shift|24.0|0|
|2003-04-19 14:00:00+00:00|2004-06-09 00:00:00+00:00|TS9|time_shift|24.0|25|
|1999-08-09 00:00:00+00:00|2000-06-04 06:00:00+00:00|TS9|time_shift|24.0|25|
|1990-01-01 16:00:00+00:00|1990-09-26 14:00:00+00:00|TS9|time_shift|180552.0|0|
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
 
# 13 CP2
## Manual flagging of data at CP2
Flagging data:
|start time|end time|variable|
|-|-|-|
|1999-02-07 00:00:00+00:00|1999-07-01 00:00:00+00:00|RH2|
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
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW1|hampel_filter|2.0|3173|
|2009-08-14 00:00:00+00:00|2010-05-01 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|468|
|2010-06-11 00:00:00+00:00|2010-06-21 00:00:00+00:00|HW1|min_filter|2.21|12|
|2010-07-08 00:00:00+00:00|2010-07-19 00:00:00+00:00|HW1|min_filter|3.35|31|
|2018-10-01 00:00:00+00:00|2018-10-10 00:00:00+00:00|HW1|min_filter|2.17|16|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|HW1|time_shift|-745.0|553|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|HW1|time_shift|24.0|17|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|16888|
|2009-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|HW2|hampel_filter|2.0|533|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|HW2|time_shift|-745.0|518|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|HW2|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|ISWR|time_shift|-745.0|554|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|ISWR|time_shift|24.0|16|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|NR|time_shift|-745.0|553|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|NR|time_shift|24.0|14|
|2009-05-06 00:00:00+00:00|2019-09-08 01:00:00+00:00|OSWR|multiply|0.934|0|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|OSWR|time_shift|-745.0|553|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|OSWR|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|P|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|P|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|RH1|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|RH1|time_shift|24.0|1|
|2012-05-15 00:00:00+00:00|2019-09-08 01:00:00+00:00|RH2|swap_with_RH1|0.0|-1670|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|RH2|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|RH2|time_shift|24.0|1|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA1|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA1|time_shift|24.0|17|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA2|time_shift|-745.0|555|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA2|time_shift|24.0|17|
|2005-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|TA3|swap_with_TA4|0.0|-654|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA3|time_shift|-745.0|555|
|2018-02-01 00:00:00+00:00|2019-12-20 00:00:00+00:00|TA3|max_filter|9.0|215|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA3|time_shift|24.0|1|
|2011-06-01 00:00:00+00:00|2012-05-09 00:00:00+00:00|TA4|time_shift|-745.0|555|
|2013-02-01 00:00:00+00:00|2015-12-20 00:00:00+00:00|TA4|max_filter|9.0|3469|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|TA4|time_shift|24.0|1|
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
 
# 17 JAR2
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
|1999-04-19 00:00:00+00:00|2000-01-01 00:00:00+00:00|HW1|min_filter|0.5|10|
|2007-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|max_filter|5.9|520|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|min_filter|1.05|4183|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|biweekly_upper_range_filter|0.7|732|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW1|time_shift|-749.0|1|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW1|time_shift|63.0|0|
|1999-04-19 00:00:00+00:00|2000-01-01 00:00:00+00:00|HW2|min_filter|0.5|10|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|min_filter|0.5|9993|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|max_filter|7.5|58|
|2008-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|biweekly_upper_range_filter|0.7|3917|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|HW2|time_shift|-749.0|1|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW2|time_shift|63.0|0|
|2009-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|ISWR|multiply|0.5|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|ISWR|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|ISWR|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|NR|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|NR|time_shift|63.0|0|
|2009-01-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|OSWR|multiply|0.5|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|OSWR|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|OSWR|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|P|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|P|time_shift|63.0|0|
|2002-05-07 00:00:00+00:00|2013-06-16 08:00:00+00:00|RH1|swap_with_RH2|0.0|-19|
|1999-06-02 03:00:00+00:00|2013-06-16 08:00:00+00:00|RH1|ice_to_water|0.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|RH1|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|RH1|time_shift|63.0|0|
|1999-06-02 03:00:00+00:00|2013-06-16 08:00:00+00:00|RH2|ice_to_water|0.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|RH2|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|RH2|time_shift|63.0|0|
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
|2004-05-07 00:00:00+00:00|2005-05-14 00:00:00+00:00|VW1|swap_with_VW2|0.0|-459|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|VW1|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|VW1|time_shift|63.0|0|
|2011-05-01 00:00:00+00:00|2013-06-16 08:00:00+00:00|VW2|time_shift|-749.0|3|
|2008-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|VW2|time_shift|63.0|0|
 
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
 

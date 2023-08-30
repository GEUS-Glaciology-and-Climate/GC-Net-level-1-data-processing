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
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_ISWR.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_OSWR.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_NR.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_TA1.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_TA3.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_RH1.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_RH2.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_VW1.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_VW2.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_DW1.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_DW2.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_P.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_HW1.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_HW2.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_V.jpeg)
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_TA2.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at Swiss Camp 10m](../figures/L1_data_treatment/SwissCamp10m_HS2.jpeg)
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
|2003-09-21 00:00:00+00:00|2004-05-01 00:00:00+00:00|TA1|
|2003-09-21 00:00:00+00:00|2004-05-01 00:00:00+00:00|TA2|
|2003-09-21 00:00:00+00:00|2004-05-01 00:00:00+00:00|TA3|
|2003-09-21 00:00:00+00:00|2004-05-01 00:00:00+00:00|TA4|
|2020-09-21 00:00:00+00:00|2022-08-03 19:00:00+00:00|TA4|
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
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_ISWR.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_OSWR.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_NR.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TA1.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TA2.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TA3.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TA4.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_RH1.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_RH2.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_VW1.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_VW2.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_DW1.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_DW2.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_P.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_HW1.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_HW2.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_V.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TA5.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TS1.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TS2.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TS3.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TS4.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TS5.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TS6.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TS7.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TS8.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TS9.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_TS10.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_IUVR.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_ILWR.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_Tsurf1.jpeg)
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_Tsurf2.jpeg)
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
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2000-12-31 08:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-0.8|0|
|2001-05-17 17:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-0.3|0|
|2011-08-01 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-3.0|0|
|2014-05-08 00:00:00+00:00|2022-08-03 19:00:00+00:00|HS2|add|-2.0|0|
![Adjusted and flagged data at Swiss Camp](../figures/L1_data_treatment/SwissCamp_HS2.jpeg)
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
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_ISWR.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_OSWR.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_NR.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TA1.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TA2.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TA3.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TA4.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_RH1.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_RH2.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_VW1.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_VW2.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_DW1.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_DW2.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_P.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_HW1.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_HW2.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_V.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TA5.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TS1.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TS2.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TS3.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TS4.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TS5.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TS6.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TS7.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TS8.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TS9.jpeg)
![Adjusted and flagged data at JAR1](../figures/L1_data_treatment/JAR1_TS10.jpeg)
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
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_ISWR.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_OSWR.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_NR.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TA1.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TA2.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TA3.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TA4.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_RH1.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_RH2.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_VW1.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_VW2.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_DW1.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_DW2.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_P.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_HW1.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_HW2.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_V.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TA5.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TS1.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TS2.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TS3.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TS4.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TS5.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TS6.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TS7.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TS8.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TS9.jpeg)
![Adjusted and flagged data at JAR2](../figures/L1_data_treatment/JAR2_TS10.jpeg)
# 19 JAR3
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
|2002-05-06 15:00:00+00:00|2004-05-25 13:00:00+00:00|P|add|70.0|0|
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_ISWR.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_OSWR.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_NR.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_TA1.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_TA2.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_TA3.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_TA4.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_RH1.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_RH2.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_VW1.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_VW2.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_DW1.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_DW2.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_P.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_HS1.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_V.jpeg)
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_HW1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at JAR3](../figures/L1_data_treatment/JAR3_HS1.jpeg)
# 2 Crawford Point 1
## Manual flagging of data at Crawford Point 1
Flagging data:
|start time|end time|variable|
|-|-|-|
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
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_ISWR.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_OSWR.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_NR.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TA1.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TA2.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TA3.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TA4.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_RH1.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_RH2.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_VW1.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_VW2.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_DW1.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_DW2.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_P.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_HW1.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_HW2.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_V.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TA5.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TS1.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TS2.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TS3.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TS4.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TS5.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TS6.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TS7.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TS8.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TS9.jpeg)
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_TS10.jpeg)
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
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_HS1.jpeg)
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
![Adjusted and flagged data at Crawford Point 1](../figures/L1_data_treatment/CrawfordPoint1_HS2.jpeg)
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
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_ISWR.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_OSWR.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_NR.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TA1.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TA2.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TA3.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TA4.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_RH1.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_RH2.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_VW1.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_VW2.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_DW1.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_DW2.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_P.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_HS1.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_HS2.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_V.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_HW1.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_HW2.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TS1.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TS2.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TS3.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TS4.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TS5.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TS6.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TS7.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TS8.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TS9.jpeg)
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_TS10.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-05-30 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS1|add|1.0|0|
|1999-05-27 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS1|add|1.0|0|
|2000-06-02 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS1|add|1.7|0|
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-05-30 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS2|add|1.0|0|
|1999-05-27 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS2|add|1.0|0|
|2000-06-02 00:00:00+00:00|2001-05-29 13:00:00+00:00|HS2|add|1.7|0|
![Adjusted and flagged data at CP2](../figures/L1_data_treatment/CP2_HS2.jpeg)
# 3 NASA-U
## Manual flagging of data at NASA-U
Flagging data:
|start time|end time|variable|
|-|-|-|
|2002-01-06 19:00:00+00:00|2002-01-07 05:00:00+00:00|TA1|
|2017-12-11 00:00:00+00:00|2019-07-01 00:00:00+00:00|TA3|
|2011-01-01 00:00:00+00:00|2012-05-25 00:00:00+00:00|TA4|
|2011-01-01 00:00:00+00:00|2016-07-01 00:00:00+00:00|P|
|2017-08-01 00:00:00+00:00|2018-12-31 00:00:00+00:00|P|
|2017-10-01 00:00:00+00:00|2018-07-01 00:00:00+00:00|RH2|
|2011-01-01 00:00:00+00:00|2012-07-01 00:00:00+00:00|RH2|
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
## Adjusting data at NASA-U
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|DW1|time_shift|48.0|4|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|DW2|time_shift|48.0|4|
|2001-05-31 21:00:00+00:00|2023-06-18 15:00:00+00:00|HW1|hampel_filter|3.0|11514|
|2007-02-12 00:00:00+00:00|2007-04-16 00:00:00+00:00|HW1|min_filter|3.2|164|
|2007-08-01 00:00:00+00:00|2007-12-16 00:00:00+00:00|HW1|min_filter|2.75|0|
|2008-02-01 00:00:00+00:00|2008-04-30 00:00:00+00:00|HW1|min_filter|2.46|794|
|2011-04-01 00:00:00+00:00|2023-01-01 00:00:00+00:00|HW1|min_filter|1.39|19231|
|2011-05-31 21:00:00+00:00|2023-06-18 15:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2011-05-31 21:00:00+00:00|2016-10-09 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|1336|
|2013-07-01 00:00:00+00:00|2014-07-01 00:00:00+00:00|HW1|min_filter|3.0|0|
|2016-10-15 00:00:00+00:00|2016-11-15 00:00:00+00:00|HW1|min_filter|1.78|51|
|2016-10-15 00:00:00+00:00|2016-11-15 00:00:00+00:00|HW1|max_filter|1.87|28|
|2018-05-21 00:00:00+00:00|2023-06-18 15:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|1924|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|HW1|time_shift|48.0|4|
|2001-05-31 21:00:00+00:00|2023-06-18 15:00:00+00:00|HW2|hampel_filter|3.0|14235|
|2007-02-12 00:00:00+00:00|2007-04-16 00:00:00+00:00|HW2|min_filter|4.3|186|
|2007-08-01 00:00:00+00:00|2007-12-16 00:00:00+00:00|HW2|min_filter|3.72|0|
|2008-02-01 00:00:00+00:00|2008-04-30 00:00:00+00:00|HW2|min_filter|3.44|788|
|2011-05-31 21:00:00+00:00|2023-06-18 15:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2011-05-31 21:00:00+00:00|2023-01-01 00:00:00+00:00|HW2|min_filter|2.23|13919|
|2011-05-31 21:00:00+00:00|2023-01-01 00:00:00+00:00|HW2|max_filter|5.6|30|
|2011-05-31 21:00:00+00:00|2023-06-18 15:00:00+00:00|HW2|biweekly_upper_range_filter|0.3|5215|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|HW2|time_shift|48.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|ISWR|time_shift|48.0|4|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|NR|time_shift|48.0|4|
|2003-01-01 00:00:00+00:00|2018-05-22 00:00:00+00:00|OSWR|multiply|2.76205|0|
|2011-05-31 00:00:00+00:00|2023-06-18 15:00:00+00:00|OSWR|multiply|0.934|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|OSWR|time_shift|48.0|4|
|1999-05-14 00:00:00+00:00|2000-01-01 00:00:00+00:00|P|add|-30.0|0|
|2000-01-01 00:00:00+00:00|2005-05-26 00:00:00+00:00|P|add|-15.0|0|
|2016-07-01 00:00:00+00:00|2023-06-18 15:00:00+00:00|P|add|-40.0|0|
|2021-08-17 00:00:00+00:00|2022-05-17 00:00:00+00:00|P|add|45.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|P|time_shift|48.0|0|
|2012-05-09 00:00:00+00:00|2023-06-18 15:00:00+00:00|RH1|swap_with_RH2|0.0|-360|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|RH1|time_shift|48.0|4|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|RH2|time_shift|48.0|0|
|2017-12-15 00:00:00+00:00|2018-02-16 00:00:00+00:00|TA1|min_filter|-56.6|18|
|2010-03-20 00:00:00+00:00|2010-10-11 00:00:00+00:00|TA1|time_shift|48.0|4|
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
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_ISWR.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_OSWR.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_NR.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TA1.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TA2.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TA3.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TA4.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_RH1.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_RH2.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_VW1.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_VW2.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_DW1.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_DW2.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_P.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_HW1.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_HW2.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_V.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TA5.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TS1.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TS2.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TS3.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TS4.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TS5.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TS6.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TS7.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TS8.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TS9.jpeg)
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_TS10.jpeg)
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
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_HS1.jpeg)
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
![Adjusted and flagged data at NASA-U](../figures/L1_data_treatment/NASA-U_HS2.jpeg)
# 4 GITS
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
|2011-05-25 00:00:00+00:00|2013-01-01 00:00:00+00:00|P|
|2006-06-28 00:00:00+00:00|2007-07-05 00:00:00+00:00|TA1|
|2006-06-28 00:00:00+00:00|2007-07-05 00:00:00+00:00|TA3|
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
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW1|swap_with_HW2|0.5|15892|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW1|biweekly_upper_range_filter|0.5|5688|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW1|hampel_filter|2.0|2284|
|2019-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW1|max_filter|2.6|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|HW1|time_shift|520.0|8|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW2|max_filter|4.8|496|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW2|biweekly_upper_range_filter|0.5|21457|
|2009-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW2|hampel_filter|2.0|2664|
|2016-05-21 00:00:00+00:00|2019-10-22 00:00:00+00:00|HW2|biweekly_upper_range_filter|0.2|1062|
|2016-05-21 00:00:00+00:00|2016-10-22 00:00:00+00:00|HW2|biweekly_upper_range_filter|0.1|255|
|2019-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|HW2|max_filter|2.6|1193|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|HW2|time_shift|520.0|519|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|ISWR|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|NR|time_shift|520.0|520|
|2012-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|OSWR|multiply|0.934|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|OSWR|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|P|time_shift|520.0|520|
|1995-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|RH1|time_shift|520.0|520|
|1995-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|RH2|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TA1|time_shift|520.0|520|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TA2|time_shift|520.0|520|
|1990-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TA3|min_filter|-39.4|7184|
|2005-01-01 00:00:00+00:00|2008-01-01 00:00:00+00:00|TA3|add|-2.8|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TA3|time_shift|520.0|520|
|1990-01-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|TA4|min_filter|-39.4|5789|
|2001-01-01 00:00:00+00:00|2008-01-01 00:00:00+00:00|TA4|add|-2.8|0|
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|TA4|time_shift|520.0|520|
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
|2019-03-14 00:00:00+00:00|2019-04-29 01:00:00+00:00|VW2|time_shift|520.0|520|
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_ISWR.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_OSWR.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_NR.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TA1.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TA2.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TA3.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TA4.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_RH1.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_RH2.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_VW1.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_VW2.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_DW1.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_DW2.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_P.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_HW1.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_HW2.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_V.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TA5.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TS1.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TS2.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TS3.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TS4.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TS5.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TS6.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TS7.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TS8.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TS9.jpeg)
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_TS10.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1996-05-07 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|0.8|0|
|1997-05-01 11:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|1.0|0|
|1999-05-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|4.5|0|
|2010-05-03 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|9.0|0|
|2014-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|1.25|0|
|2016-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS1|add|2.0|0|
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1996-05-07 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|0.2|0|
|1997-05-17 11:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|1.4|0|
|1997-05-17 23:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|-0.7|0|
|1999-05-01 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|4.5|0|
|2010-05-03 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|9.25|0|
|2014-05-15 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|2.25|0|
|2016-05-23 00:00:00+00:00|2021-08-13 12:00:00+00:00|HS2|add|2.0|0|
![Adjusted and flagged data at GITS](../figures/L1_data_treatment/GITS_HS2.jpeg)
# 5 Humboldt
## Manual flagging of data at Humboldt
Flagging data:
|start time|end time|variable|
|-|-|-|
|1990-01-01 00:00:00+00:00|1996-07-01 00:00:00+00:00|TA1|
|2007-03-01 00:00:00+00:00|2007-05-04 00:00:00+00:00|TA3|
|2007-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW1|
|2007-01-01 00:00:00+00:00|2009-01-01 00:00:00+00:00|HW2|
|2003-05-27 18:00:00+00:00|2003-05-28 14:00:00+00:00|HW2|
|2020-06-04 18:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|
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
## Adjusting data at Humboldt
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|DW1|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|DW1|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|DW1|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|DW1|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|DW1|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|DW1|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|DW1|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|DW1|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|DW1|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|DW2|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|DW2|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|DW2|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|DW2|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|DW2|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|DW2|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|DW2|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|DW2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|DW2|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|HW1|time_shift|2954.0|248|
|2002-06-02 04:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|add|-0.5|0|
|2003-05-22 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|add|1.0|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|add|-1.8|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|biweekly_upper_range_filter|0.3|10887|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW1|hampel_filter|2.0|2618|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|HW1|time_shift|5604.0|1011|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|HW1|time_shift|2954.0|1108|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|HW1|time_shift|2954.0|987|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|HW1|time_shift|5611.0|1098|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|HW1|time_shift|2943.0|1266|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|HW1|time_shift|2198.0|798|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|HW1|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|HW1|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|HW2|time_shift|2954.0|248|
|2002-03-01 12:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|add|0.4|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|add|-1.0|0|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|biweekly_upper_range_filter|0.3|9685|
|2009-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|hampel_filter|2.0|4004|
|2011-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HW2|add|1.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|HW2|time_shift|5604.0|1501|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|HW2|time_shift|2954.0|1812|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|HW2|time_shift|2954.0|1028|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|HW2|time_shift|5611.0|1171|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|HW2|time_shift|2943.0|2237|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|HW2|time_shift|2198.0|751|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|HW2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|HW2|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|ISWR|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|ISWR|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|ISWR|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|ISWR|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|ISWR|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|ISWR|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|ISWR|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|ISWR|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|ISWR|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|NR|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|NR|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|NR|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|NR|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|NR|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|NR|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|NR|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|NR|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|NR|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|OSWR|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|OSWR|time_shift|5604.0|3220|
|2011-06-01 00:00:00+00:00|2023-03-05 08:00:00+00:00|OSWR|multiply|0.93|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|OSWR|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|OSWR|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|OSWR|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|OSWR|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|OSWR|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|OSWR|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|OSWR|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|P|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|P|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|P|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|P|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|P|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|P|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|P|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|P|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|P|time_shift|-24.0|25|
|1999-01-01 00:00:00+00:00|2023-03-05 08:00:00+00:00|RH1|swap_with_RH2|0.0|26594|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|RH1|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|RH1|time_shift|5604.0|3220|
|1995-01-01 00:00:00+00:00|2012-08-19 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|RH1|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|RH1|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|RH1|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|RH1|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|RH1|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|RH1|time_shift|-48.0|0|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|RH1|time_shift|-24.0|0|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|RH2|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|RH2|time_shift|5604.0|3220|
|1995-01-01 00:00:00+00:00|2012-08-19 00:00:00+00:00|RH2|ice_to_water|0.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|RH2|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|RH2|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|RH2|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|RH2|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|RH2|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|RH2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|RH2|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TA1|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TA1|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TA1|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TA1|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TA1|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TA1|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TA1|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TA1|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TA1|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TA2|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TA2|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TA2|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TA2|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TA2|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TA2|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TA2|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TA2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TA2|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TA3|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TA3|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TA3|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TA3|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TA3|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TA3|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TA3|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TA3|time_shift|-48.0|0|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TA3|time_shift|-24.0|0|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TA4|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TA4|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TA4|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TA4|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TA4|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TA4|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TA4|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TA4|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TA4|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TS1|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS1|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS1|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS1|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS1|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS1|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS1|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS1|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS1|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TS10|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS10|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS10|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS10|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS10|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS10|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS10|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS10|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS10|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TS2|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS2|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS2|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS2|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS2|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS2|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS2|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS2|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TS3|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS3|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS3|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS3|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS3|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS3|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS3|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS3|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS3|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TS4|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS4|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS4|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS4|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS4|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS4|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS4|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS4|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS4|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TS5|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS5|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS5|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS5|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS5|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS5|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS5|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS5|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS5|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TS6|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS6|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS6|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS6|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS6|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS6|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS6|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS6|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS6|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TS7|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS7|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS7|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS7|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS7|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS7|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS7|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS7|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS7|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TS8|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS8|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS8|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS8|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS8|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS8|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS8|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS8|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS8|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|TS9|time_shift|2954.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|TS9|time_shift|5604.0|0|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|TS9|time_shift|2954.0|0|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|TS9|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|TS9|time_shift|5611.0|0|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|TS9|time_shift|2943.0|0|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|TS9|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|TS9|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|TS9|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|V|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|V|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|V|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|V|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|V|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|V|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|V|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|V|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|V|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|VW1|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|VW1|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|VW1|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|VW1|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|VW1|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|VW1|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|VW1|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|VW1|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|VW1|time_shift|-24.0|25|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|VW2|time_shift|2954.0|248|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|VW2|time_shift|5604.0|3220|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|VW2|time_shift|2954.0|2824|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|VW2|time_shift|2954.0|1047|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|VW2|time_shift|5611.0|1272|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|VW2|time_shift|2943.0|2802|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|VW2|time_shift|2198.0|845|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|VW2|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|VW2|time_shift|-24.0|25|
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_ISWR.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_OSWR.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_NR.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TA1.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TA2.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TA3.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TA4.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_RH1.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_RH2.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_VW1.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_VW2.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_DW1.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_DW2.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_P.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_HW1.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_HW2.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_V.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TS1.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TS2.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TS3.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TS4.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TS5.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TS6.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TS7.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TS8.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TS9.jpeg)
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_TS10.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1999-05-04 18:00:00+00:00|2023-03-05 08:00:00+00:00|HS1|add|1.2|0|
|2003-05-22 00:00:00+00:00|2023-03-05 08:00:00+00:00|HS1|add|3.0|0|
|2010-03-01 00:00:00+00:00|2023-03-05 08:00:00+00:00|HS1|add|3.0|0|
|2015-05-20 00:00:00+00:00|2023-03-05 08:00:00+00:00|HS1|add|2.45|0|
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1999-05-04 18:00:00+00:00|2023-03-05 08:00:00+00:00|HS2|add|0.6|0|
|2003-05-22 00:00:00+00:00|2023-03-05 08:00:00+00:00|HS2|add|3.0|0|
|2010-03-01 00:00:00+00:00|2023-03-05 08:00:00+00:00|HS2|add|3.0|0|
|2011-02-25 00:00:00+00:00|2023-03-05 08:00:00+00:00|HS2|add|-1.0|0|
|2011-05-15 00:00:00+00:00|2023-03-05 08:00:00+00:00|HS2|add|1.0|0|
|2015-05-20 21:00:00+00:00|2023-03-05 08:00:00+00:00|HS2|add|2.45|0|
![Adjusted and flagged data at Humboldt](../figures/L1_data_treatment/Humboldt_HS2.jpeg)
# 6 Summit
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
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_ISWR.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_OSWR.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_NR.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TA1.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TA2.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TA3.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TA4.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_RH1.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_RH2.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_VW1.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_VW2.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_DW1.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_DW2.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_P.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_HW1.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_HW2.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_V.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TA5.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TS1.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TS2.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TS3.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TS4.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TS5.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TS6.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TS7.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TS8.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TS9.jpeg)
![Adjusted and flagged data at Summit](../figures/L1_data_treatment/Summit_TS10.jpeg)
# 7 Tunu-N
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
|2014-01-01 00:00:00+00:00|2014-04-26 00:00:00+00:00|OSWR|
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
## Adjusting data at Tunu-N
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2011-06-01 00:00:00+00:00|2012-06-01 00:00:00+00:00|DW1|rotate|90.0|0|
|2011-06-01 00:00:00+00:00|2012-06-01 00:00:00+00:00|DW2|rotate|90.0|0|
|2002-02-15 00:00:00+00:00|2002-02-16 00:00:00+00:00|HW1|max_filter|1.8|4|
|2008-04-28 00:00:00+00:00|2008-05-12 00:00:00+00:00|HW1|min_filter|3.42|71|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|biweekly_upper_range_filter|0.2|13942|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|hampel_filter|2.0|3757|
|2013-01-01 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|add|-0.2|0|
|2017-01-01 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW1|min_filter|0.6|32850|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|air_temp_sonic_correction|0.0|0|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|biweekly_upper_range_filter|0.2|48814|
|2009-05-15 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|hampel_filter|2.0|1656|
|2013-01-01 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|add|1.3|0|
|2015-05-22 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|add|-0.4|0|
|2017-01-01 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|max_filter|3.01|6374|
|2018-05-22 00:00:00+00:00|2023-06-20 13:00:00+00:00|HW2|add|-0.3|0|
|2021-01-05 00:00:00+00:00|2022-09-09 00:00:00+00:00|P|grad_filter|5.0|0|
|1990-01-01 00:00:00+00:00|2012-01-01 00:00:00+00:00|RH1|swap_with_RH2|0.0|2656|
|1996-01-01 00:00:00+00:00|2011-01-01 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1996-01-01 00:00:00+00:00|2011-01-01 00:00:00+00:00|RH2|ice_to_water|0.0|0|
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_ISWR.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_OSWR.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_NR.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TA1.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TA2.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TA3.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TA4.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_RH1.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_RH2.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_VW1.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_VW2.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_DW1.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_DW2.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_P.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_HW1.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_HW2.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_V.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TS1.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TS2.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TS3.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TS4.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TS5.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TS6.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TS7.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TS8.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TS9.jpeg)
![Adjusted and flagged data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TS10.jpeg)
# 8 DYE-2
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
|2019-10-01 00:00:00+00:00|2022-12-31 00:00:00+00:00|TA1|max_filter|4.0|19|
|2019-10-01 00:00:00+00:00|2022-12-31 00:00:00+00:00|TA2|max_filter|4.0|17|
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_ISWR.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_OSWR.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_NR.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TA1.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TA2.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TA3.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TA4.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_RH1.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_RH2.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_VW1.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_VW2.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_DW1.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_DW2.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_P.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_HW1.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_HW2.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_V.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TA5.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TS1.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TS2.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TS3.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TS4.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TS5.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TS6.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TS7.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TS8.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TS9.jpeg)
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_TS10.jpeg)
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
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1998-04-26 17:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|0.9|0|
|2000-05-13 00:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|2.45|0|
|2003-05-09 00:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|3.65|0|
|2006-05-07 16:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|2.5|0|
|2010-05-01 03:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|2.6|0|
|2017-05-22 20:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|2.5|0|
|2021-06-15 10:00:00+00:00|2023-06-14 12:00:00+00:00|HS2|add|2.1|0|
![Adjusted and flagged data at DYE-2](../figures/L1_data_treatment/DYE-2_HS2.jpeg)
# 10 Saddle
## Manual flagging of data at Saddle
Flagging data:
|start time|end time|variable|
|-|-|-|
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
|1990-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|TA1|swap_with_TA2|0.0|0|
|2000-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TA1|swap_with_TA2|0.0|0|
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_ISWR.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_OSWR.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_NR.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TA1.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TA2.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TA3.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TA4.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_RH1.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_RH2.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_VW1.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_VW2.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_DW1.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_DW2.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_P.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_HW1.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_HW2.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_V.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TA5.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TS1.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TS2.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TS3.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TS4.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TS5.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TS6.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TS7.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TS8.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TS9.jpeg)
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_TS10.jpeg)
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
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1999-04-16 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|2.5|0|
|2001-06-05 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|2.5|0|
|2001-12-25 01:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|-1.0|0|
|2004-06-12 08:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|5.0|0|
|2010-01-07 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|4.0|0|
|2014-05-24 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|4.0|0|
|2018-03-01 16:00:00+00:00|2021-10-16 17:00:00+00:00|HS2|add|2.0|0|
![Adjusted and flagged data at Saddle](../figures/L1_data_treatment/Saddle_HS2.jpeg)
# 11 South Dome
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
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_ISWR.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_OSWR.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_NR.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TA1.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TA2.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TA3.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TA4.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_RH1.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_RH2.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_VW1.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_VW2.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_DW1.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_DW2.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_P.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_HW1.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_HW2.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_V.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TA5.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TS1.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TS2.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TS3.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TS4.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TS5.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TS6.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TS7.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TS8.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TS9.jpeg)
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_TS10.jpeg)
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
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_HS1.jpeg)
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
![Adjusted and flagged data at South Dome](../figures/L1_data_treatment/SouthDome_HS2.jpeg)
# 12 NASA-E
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
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_ISWR.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_OSWR.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_NR.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TA1.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TA2.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TA3.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TA4.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_RH1.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_RH2.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_VW1.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_VW2.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_DW1.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_DW2.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_P.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_HW1.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_HW2.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_V.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TA5.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TS1.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TS2.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TS3.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TS4.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TS5.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TS6.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TS7.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TS8.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TS9.jpeg)
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_TS10.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2001-06-08 16:00:00+00:00|2022-10-07 06:00:00+00:00|HS1|add|2.5|0|
|2006-05-03 17:00:00+00:00|2022-10-07 06:00:00+00:00|HS1|add|2.4|0|
|2009-05-09 00:00:00+00:00|2022-10-07 06:00:00+00:00|HS1|add|-1.0|0|
|2009-05-09 00:00:00+00:00|2010-04-29 00:00:00+00:00|HS1|add|-0.5|0|
|2015-05-26 03:00:00+00:00|2022-10-07 06:00:00+00:00|HS1|add|2.0|0|
|2021-07-01 00:00:00+00:00|2022-10-07 06:00:00+00:00|HS1|add|0.9|0|
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2001-06-08 16:00:00+00:00|2022-10-07 06:00:00+00:00|HS2|add|2.5|0|
|2006-05-03 18:00:00+00:00|2022-10-07 06:00:00+00:00|HS2|add|2.4|0|
|2009-05-09 00:00:00+00:00|2022-10-07 06:00:00+00:00|HS2|add|-1.6|0|
|2011-06-02 00:00:00+00:00|2022-10-07 06:00:00+00:00|HS2|add|0.7|0|
|2015-05-26 03:00:00+00:00|2022-10-07 06:00:00+00:00|HS2|add|2.5|0|
![Adjusted and flagged data at NASA-E](../figures/L1_data_treatment/NASA-E_HS2.jpeg)
# 15 NASA-SE
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
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_ISWR.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_OSWR.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_NR.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TA1.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TA2.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TA3.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TA4.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_RH1.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_RH2.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_VW1.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_VW2.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_DW1.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_DW2.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_P.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_HW1.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_HW2.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_V.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TA5.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS1.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS2.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS3.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS4.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS5.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS6.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS7.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS8.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS9.jpeg)
![Adjusted and flagged data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS10.jpeg)
# 14 NGRIP
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
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_ISWR.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_OSWR.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_NR.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TA1.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TA2.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_RH1.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_RH2.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_VW1.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_VW2.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_DW1.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_DW2.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_P.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_HS1.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_HS2.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_HW1.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_HW2.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TS1.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TS2.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TS3.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TS4.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TS5.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TS6.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TS7.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TS8.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TS9.jpeg)
![Adjusted and flagged data at NGRIP](../figures/L1_data_treatment/NGRIP_TS10.jpeg)
# 23 NEEM
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
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_ISWR.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_OSWR.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_NR.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TA1.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TA2.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TA3.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TA4.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_RH1.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_RH2.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_VW1.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_VW2.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_DW1.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_DW2.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_P.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_HW1.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_HW2.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_V.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TA5.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TS1.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TS2.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TS3.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TS4.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TS5.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TS6.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TS7.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TS8.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TS9.jpeg)
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_TS10.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2008-08-13 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS1|add|1.8|0|
|2009-05-30 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS1|add|-0.5|0|
|2011-07-06 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS1|add|3.0|0|
|2016-05-23 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS1|add|2.2|0|
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2008-08-13 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS2|add|1.8|0|
|2009-05-30 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS2|add|-0.5|0|
|2011-07-06 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS2|add|3.0|0|
|2016-05-23 00:00:00+00:00|2022-10-07 05:00:00+00:00|HS2|add|2.5|0|
![Adjusted and flagged data at NEEM](../figures/L1_data_treatment/NEEM_HS2.jpeg)
# 24 EastGRIP
## Manual flagging of data at EastGRIP
Flagging data:
|start time|end time|variable|
|-|-|-|
|2022-04-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|TA3|
|2022-04-01 00:00:00+00:00|2023-06-22 12:00:00+00:00|RH1|
|2014-05-17 20:00:00+00:00|2014-05-17 21:00:00+00:00|HW2|
|2021-04-24 00:00:00+00:00|2023-06-22 12:00:00+00:00|HW2|
|2016-04-15 00:00:00+00:00|2016-05-15 00:00:00+00:00|HW1|
|2020-12-05 00:00:00+00:00|2023-06-22 12:00:00+00:00|HW1|
|2021-11-11 00:00:00+00:00|2023-06-22 12:00:00+00:00|VW1|
|2021-11-11 00:00:00+00:00|2023-06-22 12:00:00+00:00|DW1|
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
|2016-04-01 00:00:00+00:00|2016-10-01 00:00:00+00:00|P|biweekly_upper_range_filter|0.8|4076|
|2017-04-01 00:00:00+00:00|2017-10-01 00:00:00+00:00|P|biweekly_upper_range_filter|0.8|4098|
|2018-04-01 00:00:00+00:00|2018-10-01 00:00:00+00:00|P|biweekly_upper_range_filter|0.8|3262|
|2019-04-01 00:00:00+00:00|2019-10-01 00:00:00+00:00|P|biweekly_upper_range_filter|0.8|4046|
|2020-04-01 00:00:00+00:00|2020-10-01 00:00:00+00:00|P|biweekly_upper_range_filter|0.8|4272|
|2021-04-01 00:00:00+00:00|2021-10-01 00:00:00+00:00|P|biweekly_upper_range_filter|0.8|4217|
|2021-11-01 00:00:00+00:00|2022-04-20 00:00:00+00:00|TA1|min_filter|-40.0|2116|
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_TA1.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_TA2.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_TA3.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_TA4.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_RH1.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_RH2.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_VW1.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_VW2.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_DW1.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_DW2.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_P.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_HW1.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_HW2.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_V.jpeg)
![Adjusted and flagged data at EastGRIP](../figures/L1_data_treatment/EastGRIP_TA5.jpeg)
# 16 KAR
## Manual flagging of data at KAR
Flagging data:
|start time|end time|variable|
|-|-|-|
|1999-05-17 17:00:00+00:00|2001-06-07 13:00:00+00:00|RH2|
## Adjusting data at KAR
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH2|ice_to_water|0.0|0|
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_ISWR.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_OSWR.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_NR.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TA1.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TA2.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TA3.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TA4.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_RH1.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_RH2.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_VW1.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_VW2.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_DW1.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_DW2.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_P.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_HS1.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_HS2.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_V.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_HW1.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_HW2.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TS1.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TS2.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TS3.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TS4.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TS5.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TS6.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TS7.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TS8.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TS9.jpeg)
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_TS10.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at KAR](../figures/L1_data_treatment/KAR_HS2.jpeg)
# 18 KULU
## Manual flagging of data at KULU
No erroneous data listed for KULU
## Adjusting data at KULU
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|1995-01-01 00:00:00+00:00|2011-05-30 00:00:00+00:00|RH2|ice_to_water|0.0|0|
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_ISWR.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_OSWR.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_NR.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_TA1.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_TA2.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_TA3.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_TA4.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_RH1.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_RH2.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_VW1.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_VW2.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_DW1.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_DW2.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_P.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_HS1.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_V.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_HW1.jpeg)
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_HW2.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at KULU](../figures/L1_data_treatment/KULU_HS2.jpeg)
# 20 Aurora
## Manual flagging of data at Aurora
Flagging data:
|start time|end time|variable|
|-|-|-|
|2000-06-24 14:00:00+00:00|2001-05-06 00:00:00+00:00|OSWR|
## Adjusting data at Aurora
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2000-06-24 14:00:00+00:00|2001-05-06 00:00:00+00:00|RH1|ice_to_water|0.0|0|
|2000-06-24 14:00:00+00:00|2001-05-06 00:00:00+00:00|RH2|ice_to_water|0.0|0|
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_ISWR.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_OSWR.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_NR.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_TA1.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_TA2.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_TA3.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_RH1.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_VW1.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_VW2.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_DW1.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_DW2.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_P.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_HS1.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_V.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_HW1.jpeg)
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_HW2.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at Aurora](../figures/L1_data_treatment/Aurora_HS2.jpeg)
# 21 Petermann Glacier
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
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_ISWR.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_OSWR.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_NR.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TA1.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TA2.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TA3.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TA4.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_RH1.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_RH2.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_VW1.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_VW2.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_DW1.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_DW2.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_P.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_HS1.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_HS2.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_V.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_HW1.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_HW2.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TS1.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TS2.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TS3.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TS4.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TS5.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TS6.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TS7.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TS8.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TS9.jpeg)
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_TS10.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2003-01-01 00:00:00+00:00|2006-05-01 11:00:00+00:00|HS1|add|-0.3|0|
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2003-01-01 00:00:00+00:00|2006-05-01 11:00:00+00:00|HS2|add|-0.3|0|
![Adjusted and flagged data at Petermann Glacier](../figures/L1_data_treatment/PetermannGlacier_HS2.jpeg)
# 22 Petermann ELA
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
|2003-05-23 07:00:00+00:00|2022-04-12 18:00:00+00:00|TA2|max_filter|11.0|20|
|2003-05-23 07:00:00+00:00|2022-04-12 18:00:00+00:00|TA3|max_filter|11.0|9|
|2003-05-23 07:00:00+00:00|2022-04-12 18:00:00+00:00|TA4|max_filter|11.0|9|
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_ISWR.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_OSWR.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_NR.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TA1.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TA2.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TA3.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TA4.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_RH1.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_RH2.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_VW1.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_VW2.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_DW1.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_DW2.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_P.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_HW1.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_HW2.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_V.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TS1.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TS2.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TS3.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TS4.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TS5.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TS6.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TS7.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TS8.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TS9.jpeg)
![Adjusted and flagged data at Petermann ELA](../figures/L1_data_treatment/PetermannELA_TS10.jpeg)
# 33 SMS-PET
## Manual flagging of data at SMS-PET
No erroneous data listed for SMS-PET
## Adjusting data at SMS-PET
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2002-06-02 02:00:00+00:00|2004-05-14 15:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2002-06-02 02:00:00+00:00|2004-05-14 15:00:00+00:00|HW1|min_filter|0.7|40|
|2002-07-15 00:00:00+00:00|2003-05-07 15:30:00+00:00|HW1|biweekly_upper_range_filter|0.4|40|
|2003-09-01 00:00:00+00:00|2004-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|96|
![Adjusted and flagged data at SMS-PET](../figures/L1_data_treatment/SMS-PET_TA1.jpeg)
![Adjusted and flagged data at SMS-PET](../figures/L1_data_treatment/SMS-PET_TA2.jpeg)
![Adjusted and flagged data at SMS-PET](../figures/L1_data_treatment/SMS-PET_RH1.jpeg)
![Adjusted and flagged data at SMS-PET](../figures/L1_data_treatment/SMS-PET_VW1.jpeg)
![Adjusted and flagged data at SMS-PET](../figures/L1_data_treatment/SMS-PET_DW1.jpeg)
![Adjusted and flagged data at SMS-PET](../figures/L1_data_treatment/SMS-PET_HW1.jpeg)
![Adjusted and flagged data at SMS-PET](../figures/L1_data_treatment/SMS-PET_V.jpeg)
![Adjusted and flagged data at SMS-PET](../figures/L1_data_treatment/SMS-PET_ISWR.jpeg)
![Adjusted and flagged data at SMS-PET](../figures/L1_data_treatment/SMS-PET_OSWR.jpeg)
![Adjusted and flagged data at SMS-PET](../figures/L1_data_treatment/SMS-PET_NR.jpeg)
# 25 SMS1
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
![Adjusted and flagged data at SMS1](../figures/L1_data_treatment/SMS1_TA1.jpeg)
![Adjusted and flagged data at SMS1](../figures/L1_data_treatment/SMS1_TA2.jpeg)
![Adjusted and flagged data at SMS1](../figures/L1_data_treatment/SMS1_RH1.jpeg)
![Adjusted and flagged data at SMS1](../figures/L1_data_treatment/SMS1_VW1.jpeg)
![Adjusted and flagged data at SMS1](../figures/L1_data_treatment/SMS1_DW1.jpeg)
![Adjusted and flagged data at SMS1](../figures/L1_data_treatment/SMS1_HW1.jpeg)
# 26 SMS2
## Manual flagging of data at SMS2
No erroneous data listed for SMS2
## Adjusting data at SMS2
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2003-04-24 04:00:00+00:00|2006-05-10 15:00:00+00:00|HW1|air_temp_sonic_correction|0.0|0|
|2003-04-24 04:00:00+00:00|2006-05-10 15:00:00+00:00|HW1|min_filter|0.1|6660|
|2003-04-24 04:00:00+00:00|2006-05-10 15:00:00+00:00|HW1|max_filter|5.0|0|
|2003-08-01 00:00:00+00:00|2004-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|447|
|2004-08-26 00:00:00+00:00|2005-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|240|
|2005-09-01 00:00:00+00:00|2006-05-15 00:00:00+00:00|HW1|biweekly_upper_range_filter|0.4|404|
![Adjusted and flagged data at SMS2](../figures/L1_data_treatment/SMS2_TA1.jpeg)
![Adjusted and flagged data at SMS2](../figures/L1_data_treatment/SMS2_TA2.jpeg)
![Adjusted and flagged data at SMS2](../figures/L1_data_treatment/SMS2_RH1.jpeg)
![Adjusted and flagged data at SMS2](../figures/L1_data_treatment/SMS2_VW1.jpeg)
![Adjusted and flagged data at SMS2](../figures/L1_data_treatment/SMS2_DW1.jpeg)
![Adjusted and flagged data at SMS2](../figures/L1_data_treatment/SMS2_HW1.jpeg)
![Adjusted and flagged data at SMS2](../figures/L1_data_treatment/SMS2_V.jpeg)
# 27 SMS3
## Manual flagging of data at SMS3
No erroneous data listed for SMS3
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
![Adjusted and flagged data at SMS3](../figures/L1_data_treatment/SMS3_TA1.jpeg)
![Adjusted and flagged data at SMS3](../figures/L1_data_treatment/SMS3_TA2.jpeg)
![Adjusted and flagged data at SMS3](../figures/L1_data_treatment/SMS3_RH1.jpeg)
![Adjusted and flagged data at SMS3](../figures/L1_data_treatment/SMS3_VW1.jpeg)
![Adjusted and flagged data at SMS3](../figures/L1_data_treatment/SMS3_DW1.jpeg)
![Adjusted and flagged data at SMS3](../figures/L1_data_treatment/SMS3_HW1.jpeg)
![Adjusted and flagged data at SMS3](../figures/L1_data_treatment/SMS3_V.jpeg)
# 28 SMS4
## Manual flagging of data at SMS4
No erroneous data listed for SMS4
## Adjusting data at SMS4
No data to fix at SMS4
No data to fix at SMS4
# 29 SMS5
## Manual flagging of data at SMS5
No erroneous data listed for SMS5
## Adjusting data at SMS5
No data to fix at SMS5
No data to fix at SMS5
# 30 LAR1
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
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_ISWR.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_OSWR.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_NR.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_TA1.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_TA2.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_TA3.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_TA4.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_RH1.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_RH2.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_VW1.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_VW2.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_DW1.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_DW2.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_P.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_HS1.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_HS2.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_V.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_TA5.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_HW1.jpeg)
![Adjusted and flagged data at LAR1](../figures/L1_data_treatment/LAR1_HW2.jpeg)
# 31 LAR2
## Manual flagging of data at LAR2
No erroneous data listed for LAR2
## Adjusting data at LAR2
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2008-12-22 20:00:00+00:00|2011-11-15 13:00:00+00:00|ISWR|multiply|2.68|0|
|2008-12-22 20:00:00+00:00|2011-11-15 13:00:00+00:00|OSWR|multiply|2.88|0|
|2008-12-22 20:00:00+00:00|2011-11-15 13:00:00+00:00|RH1|ice_to_water|0.0|0|
|2008-12-22 20:00:00+00:00|2011-11-15 13:00:00+00:00|RH2|ice_to_water|0.0|0|
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_ISWR.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_OSWR.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_NR.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_TA1.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_TA2.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_TA3.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_TA4.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_RH1.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_RH2.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_VW1.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_VW2.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_DW1.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_DW2.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_P.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_HS1.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_HS2.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_V.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_TA5.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_HW1.jpeg)
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_HW2.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at LAR2](../figures/L1_data_treatment/LAR2_HS2.jpeg)
# 32 LAR3
## Manual flagging of data at LAR3
Flagging data:
|start time|end time|variable|
|-|-|-|
|2009-08-10 14:00:00+00:00|2011-11-08 14:00:00+00:00|RH2|
|2009-08-10 14:00:00+00:00|2009-08-10 16:00:00+00:00|HW1|
## Adjusting data at LAR3
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
|2009-08-10 14:00:00+00:00|2011-11-08 14:00:00+00:00|RH1|ice_to_water|0.0|0|
|2009-08-10 14:00:00+00:00|2011-11-08 14:00:00+00:00|RH2|ice_to_water|0.0|0|
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_ISWR.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_OSWR.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_NR.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_TA1.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_TA2.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_TA3.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_TA4.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_RH1.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_RH2.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_VW1.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_VW2.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_DW1.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_DW2.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_P.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_HS1.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_HS2.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_V.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_TA5.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_HW1.jpeg)
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_HW2.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_HS1.jpeg)
|start time|end time|variable|operation|value|number of removed samples|
|-|-|-|-|-|-|
![Adjusted and flagged data at LAR3](../figures/L1_data_treatment/LAR3_HS2.jpeg)

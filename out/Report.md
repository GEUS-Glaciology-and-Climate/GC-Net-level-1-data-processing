# 1 Swiss Camp
## Manual flagging of data at Swiss Camp
Flagging data:
Warning: HS1 not found
Warning: HS2 not found
|start time|end time|variable|
|-|-|-|
|1995-01-01 00:00:00+00:00|1996-06-23 00:00:00+00:00|HW1|
|1998-06-04 00:00:00+00:00|1999-04-02 00:00:00+00:00|HW1|
 
![Erroneous data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_HW1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-08-14 00:00:00+00:00|2012-05-24 00:00:00+00:00|HW2|
 
![Erroneous data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_HW2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2009-07-01 00:00:00+00:00|2009-07-01 00:00:00+00:00|ISWR|
|2011-02-15 00:00:00+00:00|2011-05-10 00:00:00+00:00|ISWR|
 
![Erroneous data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_ISWR_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2009-07-01 00:00:00+00:00|2009-07-01 00:00:00+00:00|OSWR|
|2011-02-15 00:00:00+00:00|2011-05-10 00:00:00+00:00|OSWR|
|2011-08-01 00:00:00+00:00|2012-05-10 00:00:00+00:00|OSWR|
 
![Erroneous data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_OSWR_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2015-06-01 00:00:00+00:00|2016-05-01 00:00:00+00:00|RH2|
 
![Erroneous data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_RH2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2015-06-01 00:00:00+00:00|2016-05-01 00:00:00+00:00|VW1|
 
![Erroneous data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_VW1_data_flagging.png)
 
## Adjusting data at Swiss Camp
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2022-08-03T19:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2022-08-03T19:00:00+00:00|biweekly_upper_range_filter|0.5|9349|
|2009-05-15T00:00:00+00:00|2022-08-03T19:00:00+00:00|hampel_filter|2.0|733|
 
![Adjusted data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1995-01-12T00:00:00+00:00|2000-01-01T00:00:00+00:00|max_filter|8.0|19148|
|2009-05-15T00:00:00+00:00|2022-08-03T19:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2022-08-03T19:00:00+00:00|biweekly_upper_range_filter|0.5|13732|
|2009-05-15T00:00:00+00:00|2022-08-03T19:00:00+00:00|hampel_filter|2.0|3296|
|2018-03-12T00:00:00+00:00|2018-05-12T00:00:00+00:00|max_filter|0.77|13|
 
![Adjusted data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_adj_HW2.jpeg)
 
### Adjusting ISWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2012-05-10T00:00:00+00:00|2022-08-03T19:00:00+00:00|swap_with_OSWR|0.0|0|
 
![Adjusted data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_adj_ISWR.jpeg)
 
### Adjusting OSWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-07T00:00:00+00:00|2022-08-03T19:00:00+00:00|multiply|0.934|0|
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|time_shift|2954.0|1705|
|1999-05-03T00:00:00+00:00|2022-10-17T02:00:00+00:00|add|1.2|0|
|2003-05-22T00:00:00+00:00|2022-10-17T02:00:00+00:00|add|3.0|0|
|2010-03-01T00:00:00+00:00|2022-10-17T02:00:00+00:00|add|3.0|0|
|2015-03-26T00:00:00+00:00|2022-10-17T02:00:00+00:00|add|2.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|time_shift|5604.0|1650|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|time_shift|2954.0|2876|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|time_shift|5611.0|1321|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|time_shift|2943.0|2942|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|time_shift|-24.0|25|
 
![Adjusted data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_adj_OSWR.jpeg)
 
### Adjusting P
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2019-11-15T00:00:00+00:00|2022-08-03T19:00:00+00:00|min_filter|856.0|5228|
 
![Adjusted data at Humboldt](../figures/L1_data_treatment/Humboldt_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2021-12-01 00:00:00+00:00|2022-06-16 00:00:00+00:00|time_shift|2954.0|1705|
|1999-05-03T00:00:00+00:00|2022-10-17T02:00:00+00:00|add|0.6|0|
|2003-05-22T00:00:00+00:00|2022-10-17T02:00:00+00:00|add|3.0|0|
|2010-03-01T00:00:00+00:00|2022-10-17T02:00:00+00:00|add|3.0|0|
|2012-05-25T00:00:00+00:00|2022-10-17T02:00:00+00:00|add|-1.0|0|
|2015-03-26T00:00:00+00:00|2022-10-17T02:00:00+00:00|add|2.0|0|
|2020-08-10 00:00:00+00:00|2020-12-24 12:00:00+00:00|time_shift|5604.0|1650|
|2019-12-10 00:00:00+00:00|2020-08-10 00:00:00+00:00|time_shift|2954.0|2876|
|2018-12-06 00:00:00+00:00|2019-01-19 20:00:00+00:00|time_shift|2954.0|0|
|2017-08-10 00:00:00+00:00|2017-10-04 00:00:00+00:00|time_shift|5611.0|1321|
|2016-12-03 00:00:00+00:00|2017-08-10 00:00:00+00:00|time_shift|2943.0|2942|
|2015-01-01 00:00:00+00:00|2015-02-18 06:00:00+00:00|time_shift|2198.0|0|
|2005-01-02 00:00:00+00:00|2006-05-04 00:00:00+00:00|time_shift|-48.0|48|
|2004-08-08 00:00:00+00:00|2005-01-01 00:00:00+00:00|time_shift|-24.0|25|
 
![Adjusted data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_adj_P.jpeg)
 
### Adjusting RH1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2011-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at Humboldt](../figures/L1_data_treatment/Humboldt_adj_HS2.jpeg)
 
 
![Adjusted data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_adj_RH1.jpeg)
 
### Adjusting RH2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2011-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_adj_RH2.jpeg)
 
# 6 Summit
## Manual flagging of data at Summit
Flagging data:
|start time|end time|variable|
|-|-|-|
|2017-11-17 00:00:00+00:00|2018-02-23 00:00:00+00:00|HW1|
|2018-11-10 00:00:00+00:00|2019-06-09 00:00:00+00:00|HW1|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_HW1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2017-12-17 00:00:00+00:00|2018-02-19 00:00:00+00:00|HW2|
|2018-11-20 00:00:00+00:00|2019-04-09 00:00:00+00:00|HW2|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_HW2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|1997-05-21 00:00:00+00:00|1998-07-01 00:00:00+00:00|TA3|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_TA3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS1|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS1|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_TS1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS10|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS10|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_TS10_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS2|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS2|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_TS2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS3|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS3|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_TS3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS4|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS4|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_TS4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS5|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS5|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_TS5_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS6|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS6|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_TS6_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS7|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS7|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_TS7_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS8|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS8|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_TS8_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-05-18 00:00:00+00:00|2022-01-01 00:00:00+00:00|TS9|
|1999-05-01 00:00:00+00:00|1999-05-15 00:00:00+00:00|TS9|
 
![Erroneous data at Summit](../figures/L1_data_treatment/Summit_TS9_data_flagging.png)
 
## Adjusting data at Summit
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2001-06-15T16:00:00+00:00|2003-12-13T17:00:00+00:00|add|0.78|0|
|2003-12-13T17:05:00+00:00|2005-05-04T19:00:00+00:00|add|0.37|0|
|2004-12-13T17:05:00+00:00|2005-07-04T19:00:00+00:00|min_filter|-4.0|852|
|2005-05-26T07:00:00+00:00|2008-09-13T01:05:00+00:00|add|0.72|0|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|biweekly_upper_range_filter|0.3|13009|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|hampel_filter|2.0|5776|
|2009-05-19T19:00:00+00:00|2010-08-06T23:05:00+00:00|add|-0.39|0|
 
![Adjusted data at Summit](../figures/L1_data_treatment/Summit_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2001-06-15T16:00:00+00:00|2003-12-13T17:00:00+00:00|add|0.62|0|
|2003-12-13T17:05:00+00:00|2004-03-02T16:05:00+00:00|add|0.84|0|
|2004-08-19T17:05:00+00:00|2005-05-04T21:00:00+00:00|add|0.84|0|
|2005-05-26T07:00:00+00:00|2010-08-06T23:05:00+00:00|add|0.39|0|
|2005-10-08T14:00:00+00:00|2006-03-17T14:05:00+00:00|add|0.87|0|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|biweekly_upper_range_filter|0.3|18067|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|hampel_filter|2.0|4119|
|2009-05-19T19:00:00+00:00|2010-08-06T23:05:00+00:00|add|-0.39|0|
 
![Adjusted data at Summit](../figures/L1_data_treatment/Summit_adj_HW2.jpeg)
 
### Adjusting OSWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-19T00:00:00+00:00|2022-09-20T23:00:00+00:00|multiply|0.91|0|
 
![Adjusted data at Summit](../figures/L1_data_treatment/Summit_adj_OSWR.jpeg)
 
### Adjusting P
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2016-05-22T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|-61.0|0|
|2019-04-28T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|38.0|0|
|2019-04-29T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|21.0|0|
 
![Adjusted data at Summit](../figures/L1_data_treatment/Summit_adj_P.jpeg)
 
### Adjusting RH1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2009-05-19T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at Summit](../figures/L1_data_treatment/Summit_adj_RH1.jpeg)
 
### Adjusting RH2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2009-05-19T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at Summit](../figures/L1_data_treatment/Summit_adj_RH2.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2002-01-19T00:00:00+00:00|2022-08-03T19:00:00+00:00|add|1.5|0|
|2003-01-19T00:00:00+00:00|2022-08-03T19:00:00+00:00|add|-0.6|0|
|2003-04-27T00:00:00+00:00|2022-08-03T19:00:00+00:00|add|0.4|0|
|2014-05-08T00:00:00+00:00|2022-08-03T19:00:00+00:00|add|-2.0|0|
 
![Adjusted data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2014-05-08T00:00:00+00:00|2022-08-03T19:00:00+00:00|add|-2.0|0|
 
![Adjusted data at Swiss Camp](../figures/L1_data_treatment/Swiss_Camp_adj_HS2.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1999-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|0.8|0|
|2001-06-10T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.0|0|
|2005-05-23T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|3.0|0|
|2010-08-16T21:00:00+00:00|2022-09-20T23:00:00+00:00|add|3.6|0|
|2016-05-22T21:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.6|0|
 
![Adjusted data at Summit](../figures/L1_data_treatment/Summit_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1999-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|0.8|0|
|2001-06-10T12:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.1|0|
|2005-05-26T14:00:00+00:00|2022-09-20T23:00:00+00:00|add|3.0|0|
|2010-08-18T14:00:00+00:00|2022-09-20T23:00:00+00:00|add|3.4|0|
|2016-05-22T14:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.5|0|
 
![Adjusted data at Summit](../figures/L1_data_treatment/Summit_adj_HS2.jpeg)
 
# 7 Tunu-N
## Manual flagging of data at Tunu-N
Flagging data:
|start time|end time|variable|
|-|-|-|
|2011-06-10 00:00:00+00:00|2013-05-23 00:00:00+00:00|HW1|
 
![Erroneous data at Tunu-N](../figures/L1_data_treatment/Tunu-N_HW1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-06-10 00:00:00+00:00|2013-05-23 00:00:00+00:00|HW2|
 
![Erroneous data at Tunu-N](../figures/L1_data_treatment/Tunu-N_HW2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2014-01-01 00:00:00+00:00|2014-04-26 00:00:00+00:00|ISWR|
 
![Erroneous data at Tunu-N](../figures/L1_data_treatment/Tunu-N_ISWR_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2014-01-01 00:00:00+00:00|2014-04-26 00:00:00+00:00|OSWR|
 
![Erroneous data at Tunu-N](../figures/L1_data_treatment/Tunu-N_OSWR_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|TA1|
 
![Erroneous data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TA1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|TA2|
 
![Erroneous data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TA2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|TA3|
 
![Erroneous data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TA3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|TA4|
 
![Erroneous data at Tunu-N](../figures/L1_data_treatment/Tunu-N_TA4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-01-01 00:00:00+00:00|2013-01-01 00:00:00+00:00|VW1|
 
![Erroneous data at Tunu-N](../figures/L1_data_treatment/Tunu-N_VW1_data_flagging.png)
 
## Adjusting data at Tunu-N
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2022-05-27T13:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2022-05-27T13:00:00+00:00|biweekly_upper_range_filter|0.2|13942|
|2009-05-15T00:00:00+00:00|2022-05-27T13:00:00+00:00|hampel_filter|2.0|3757|
 
![Adjusted data at Tunu-N](../figures/L1_data_treatment/Tunu-N_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2022-05-27T13:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2022-05-27T13:00:00+00:00|biweekly_upper_range_filter|0.2|39546|
|2009-05-15T00:00:00+00:00|2022-05-27T13:00:00+00:00|hampel_filter|2.0|1656|
 
![Adjusted data at Tunu-N](../figures/L1_data_treatment/Tunu-N_adj_HW2.jpeg)
 
### Adjusting P
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2021-01-05T00:00:00+00:00|2022-09-09T00:00:00+00:00|grad_filter|5.0|0|
 
![Adjusted data at Tunu-N](../figures/L1_data_treatment/Tunu-N_adj_P.jpeg)
 
### Adjusting RH1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2011-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at Tunu-N](../figures/L1_data_treatment/Tunu-N_adj_RH1.jpeg)
 
### Adjusting RH2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2011-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at Tunu-N](../figures/L1_data_treatment/Tunu-N_adj_RH2.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2001-06-07T16:00:00+00:00|2022-05-27T13:00:00+00:00|add|1.7|0|
|2002-02-27T00:00:00+00:00|2022-05-27T13:00:00+00:00|add|0.9|0|
|2008-04-26T16:00:00+00:00|2022-05-27T13:00:00+00:00|add|3.0|0|
|2018-05-19T00:00:00+00:00|2022-05-27T13:00:00+00:00|add|2.5|0|
|2019-06-26T00:00:00+00:00|2022-05-27T13:00:00+00:00|add|-2.5|0|
 
![Adjusted data at Tunu-N](../figures/L1_data_treatment/Tunu-N_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2001-06-07T16:00:00+00:00|2022-05-27T13:00:00+00:00|add|1.5|0|
|2004-05-13T16:00:00+00:00|2022-05-27T13:00:00+00:00|add|1.0|0|
|2007-04-05T16:00:00+00:00|2022-05-27T13:00:00+00:00|add|-0.5|0|
|2008-05-01T00:00:00+00:00|2022-05-27T13:00:00+00:00|add|3.2|0|
|2013-02-13T16:00:00+00:00|2022-05-27T13:00:00+00:00|add|-0.5|0|
|2015-05-25T16:00:00+00:00|2022-05-27T13:00:00+00:00|add|1.0|0|
 
![Adjusted data at Tunu-N](../figures/L1_data_treatment/Tunu-N_adj_HS2.jpeg)
 
# 8 DYE2
## Manual flagging of data at DYE2
Flagging data:
|start time|end time|variable|
|-|-|-|
|2002-05-19 01:00:00+00:00|2003-05-09 00:00:00+00:00|HW1|
|2015-06-07 01:00:00+00:00|2018-05-07 00:00:00+00:00|HW1|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_HW1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2002-01-01 01:00:00+00:00|2003-05-09 00:00:00+00:00|HW2|
|2010-03-25 01:00:00+00:00|2014-05-23 00:00:00+00:00|HW2|
|2018-06-01 01:00:00+00:00|2019-05-20 00:00:00+00:00|HW2|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_HW2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2004-06-15 01:00:00+00:00|2004-08-25 00:00:00+00:00|ISWR|
|2012-05-07 18:00:00+00:00|2012-05-12 00:00:00+00:00|ISWR|
|2004-05-09 15:00:00+00:00|2005-06-10 00:00:00+00:00|ISWR|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_ISWR_data_flagging.png)
 
Warning: OSR not found
|start time|end time|variable|
|-|-|-|
|2004-05-09 15:00:00+00:00|2005-06-10 00:00:00+00:00|OSWR|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_OSWR_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-05-26 09:00:00+00:00|2013-12-28 00:00:00+00:00|P|
|2010-05-21 07:00:02+00:00|2010-09-25 00:00:00+00:00|P|
|2013-06-13 01:00:00+00:00|2014-10-26 00:00:00+00:00|P|
|2002-01-14 10:00:00+00:00|2003-04-29 00:00:00+00:00|P|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_P_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2009-09-09 12:00:00+00:00|2010-05-02 00:00:00+00:00|RH1|
|1999-04-19 21:00:00+00:00|1999-10-17 00:00:00+00:00|RH1|
|2021-06-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|RH1|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_RH1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-02-09 12:00:00+00:00|2010-05-02 00:00:00+00:00|RH2|
|2012-11-06 22:00:00+00:00|2013-08-14 00:00:00+00:00|RH2|
|2013-10-27 07:59:57+00:00|2014-05-20 00:00:00+00:00|RH2|
|2012-02-11 04:59:00+00:00|2012-11-06 00:00:00+00:00|RH2|
|2016-01-01 00:00:00+00:00|2018-01-01 00:00:00+00:00|RH2|
|2010-01-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|RH2|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_RH2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|1999-10-15 01:00:00+00:00|2000-05-15 00:00:00+00:00|TA3|
|2009-06-15 01:00:00+00:00|2010-05-02 00:00:00+00:00|TA3|
|2018-09-27 01:00:00+00:00|2018-10-05 00:00:00+00:00|TA3|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TA3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|1996-09-14 22:00:00+00:00|1996-10-10 00:00:00+00:00|TA4|
|2009-05-19 21:00:00+00:00|2009-07-19 00:00:00+00:00|TA4|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TA4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS1|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS1|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TS1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS10|
|2000-05-01 00:00:00+00:00|2001-04-17 00:00:00+00:00|TS10|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS10|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TS10_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS2|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS2|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TS2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS3|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS3|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TS3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS4|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS4|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TS4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS5|
|2001-03-10 00:00:00+00:00|2001-04-20 00:00:00+00:00|TS5|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS5|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TS5_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS6|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS6|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TS6_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS7|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS7|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TS7_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS8|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS8|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TS8_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS9|
|1999-12-01 00:00:00+00:00|1999-12-10 00:00:00+00:00|TS9|
|2000-05-01 00:00:00+00:00|2001-04-17 00:00:00+00:00|TS9|
|2000-05-12 00:00:00+00:00|2000-05-18 00:00:00+00:00|TS9|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_TS9_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2016-01-01 00:00:00+00:00|2018-01-01 00:00:00+00:00|VW2|
 
![Erroneous data at DYE2](../figures/L1_data_treatment/DYE2_VW2_data_flagging.png)
 
## Adjusting data at DYE2
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1999-12-29T00:00:00+00:00|1999-12-31T00:00:00+00:00|min_filter|0.63|20|
|2001-06-04T00:00:00+00:00|2001-06-06T00:00:00+00:00|min_filter|1.45|1|
|2001-06-15T00:00:00+00:00|2002-05-20T12:00:00+00:00|add|-1.5|0|
|2009-05-16T00:00:00+00:00|2022-09-20T23:00:00+00:00|air_temp_sonic_correction|0.0|10|
|2009-05-16T00:00:00+00:00|2010-01-01T00:00:00+00:00|biweekly_upper_range_filter|0.15|626|
|2009-05-16T00:00:00+00:00|2020-09-20T00:00:00+00:00|hampel_filter|2.0|6454|
|2010-01-01T00:00:00+00:00|2010-05-12T00:00:00+00:00|biweekly_upper_range_filter|0.3|345|
|2010-05-12T00:00:00+00:00|2020-09-20T00:00:00+00:00|biweekly_upper_range_filter|0.4|6022|
 
![Adjusted data at DYE2](../figures/L1_data_treatment/DYE2_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1999-12-29T00:00:00+00:00|1999-12-31T00:00:00+00:00|min_filter|1.75|20|
|2001-06-04T00:00:00+00:00|2001-06-06T00:00:00+00:00|max_filter|2.7|4|
|2001-06-15T00:00:00+00:00|2002-05-20T12:00:00+00:00|add|-0.86|0|
|2003-05-10T00:00:00+00:00|2004-06-13T00:00:00+00:00|add|0.49|0|
|2009-05-16T00:00:00+00:00|2022-09-20T23:00:00+00:00|air_temp_sonic_correction|0.0|9|
|2009-05-16T00:00:00+00:00|2010-05-12T00:00:00+00:00|biweekly_upper_range_filter|0.2|443|
|2009-05-16T00:00:00+00:00|2020-09-20T00:00:00+00:00|hampel_filter|2.0|5701|
|2010-05-12T00:00:00+00:00|2020-09-20T00:00:00+00:00|biweekly_upper_range_filter|0.4|4540|
|2018-10-01T00:00:00+00:00|2022-12-31T00:00:00+00:00|max_filter|100.0|1|
 
![Adjusted data at DYE2](../figures/L1_data_treatment/DYE2_adj_HW2.jpeg)
 
### Adjusting OSWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-16T00:00:00+00:00|2022-09-20T23:00:00+00:00|multiply|0.934|0|
 
![Adjusted data at DYE2](../figures/L1_data_treatment/DYE2_adj_OSWR.jpeg)
 
### Adjusting RH1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2010-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at DYE2](../figures/L1_data_treatment/DYE2_adj_RH1.jpeg)
 
### Adjusting RH2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2010-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at DYE2](../figures/L1_data_treatment/DYE2_adj_RH2.jpeg)
 
### Adjusting TA1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1990-01-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|min_filter|-80.0|10|
|2019-10-01T00:00:00+00:00|2022-12-31T00:00:00+00:00|max_filter|4.0|26|
 
![Adjusted data at DYE2](../figures/L1_data_treatment/DYE2_adj_TA1.jpeg)
 
### Adjusting TA2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2019-10-01T00:00:00+00:00|2022-12-31T00:00:00+00:00|max_filter|4.0|24|
 
![Adjusted data at DYE2](../figures/L1_data_treatment/DYE2_adj_TA2.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1998-04-28T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|1.0|0|
|2000-05-12T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.2|0|
|2003-05-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|4.0|0|
|2006-05-10T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.2|0|
|2010-04-28T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.6|0|
 
![Adjusted data at DYE2](../figures/L1_data_treatment/DYE2_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1998-04-20T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|1.0|0|
|2000-05-12T13:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.2|0|
|2003-05-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|4.0|0|
|2004-06-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|0.75|0|
|2006-05-07T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.5|0|
|2014-05-25T16:00:00+00:00|2022-09-20T23:00:00+00:00|add|6.0|0|
|2017-05-25T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.0|0|
 
![Adjusted data at DYE2](../figures/L1_data_treatment/DYE2_adj_HS2.jpeg)
 
# 9 JAR1
## Manual flagging of data at JAR1
Flagging data:
|start time|end time|variable|
|-|-|-|
|2011-08-16 00:00:00+00:00|2012-01-01 00:00:00+00:00|ISWR|
|2010-07-19 00:00:00+00:00|2011-01-01 00:00:00+00:00|ISWR|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_ISWR_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-08-16 00:00:00+00:00|2012-01-01 00:00:00+00:00|OSWR|
|2010-07-19 00:00:00+00:00|2011-01-01 00:00:00+00:00|OSWR|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_OSWR_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|RH1|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_RH1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|RH2|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_RH2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|TA1|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TA1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|TA2|
|2010-10-01 00:00:00+00:00|2012-05-04 00:00:00+00:00|TA2|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TA2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|TA3|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TA3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-09-02 00:00:00+00:00|2008-05-08 00:00:00+00:00|TA4|
|2010-10-01 00:00:00+00:00|2011-06-05 00:00:00+00:00|TA4|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TA4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS1|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TS1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS10|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TS10_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS2|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TS2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS3|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TS3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS4|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TS4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS5|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TS5_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS6|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TS6_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS7|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TS7_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS8|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TS8_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-06-01 00:00:00+00:00|2019-09-08 01:00:00+00:00|TS9|
 
![Erroneous data at JAR1](../figures/L1_data_treatment/JAR1_TS9_data_flagging.png)
 
## Adjusting data at JAR1
### Adjusting DW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_DW1.jpeg)
 
### Adjusting DW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_DW2.jpeg)
 
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2019-09-08T01:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2019-09-08T01:00:00+00:00|hampel_filter|2.0|3173|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2019-09-08T01:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2019-09-08T01:00:00+00:00|hampel_filter|2.0|7573|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_HW2.jpeg)
 
### Adjusting ISWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|16|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_ISWR.jpeg)
 
### Adjusting NR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|14|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_NR.jpeg)
 
### Adjusting OSWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-06T00:00:00+00:00|2019-09-08T01:00:00+00:00|multiply|0.934|0|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_OSWR.jpeg)
 
### Adjusting P
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_P.jpeg)
 
### Adjusting RH1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|1|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_RH1.jpeg)
 
### Adjusting RH2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|1|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_RH2.jpeg)
 
### Adjusting TA1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TA1.jpeg)
 
### Adjusting TA2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TA2.jpeg)
 
### Adjusting TA3
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2018-02-01T00:00:00+00:00|2019-12-20T00:00:00+00:00|max_filter|9.0|215|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|1|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TA3.jpeg)
 
### Adjusting TA4
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2013-02-01T00:00:00+00:00|2015-12-20T00:00:00+00:00|max_filter|9.0|3469|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|1|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TA4.jpeg)
 
### Adjusting TA5
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|0|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TA5.jpeg)
 
### Adjusting TS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TS1.jpeg)
 
### Adjusting TS10
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TS10.jpeg)
 
### Adjusting TS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TS2.jpeg)
 
### Adjusting TS3
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TS3.jpeg)
 
### Adjusting TS4
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TS4.jpeg)
 
### Adjusting TS5
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TS5.jpeg)
 
### Adjusting TS6
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TS6.jpeg)
 
### Adjusting TS7
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TS7.jpeg)
 
### Adjusting TS8
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TS8.jpeg)
 
### Adjusting TS9
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_TS9.jpeg)
 
### Adjusting V
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_V.jpeg)
 
### Adjusting VW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_VW1.jpeg)
 
### Adjusting VW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|17|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_VW2.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1999-05-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2002-05-03T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-1.5|0|
|2002-09-14T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|1.0|0|
|2003-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-1.0|0|
|2008-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2010-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2011-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2014-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2015-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2017-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|25|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1999-05-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2002-05-03T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-1.5|0|
|2003-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-1.0|0|
|2008-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2010-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2011-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2014-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2015-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2017-04-24T00:00:00+00:00|2019-09-08T01:00:00+00:00|add|-2.0|0|
|2003-04-24 00:00:00+00:00|2005-05-07 00:00:00+00:00|time_shift|24.0|25|
 
![Adjusted data at JAR1](../figures/L1_data_treatment/JAR1_adj_HS2.jpeg)
 
# 10 Saddle
## Manual flagging of data at Saddle
Flagging data:
|start time|end time|variable|
|-|-|-|
|2014-10-09 00:00:00+00:00|2016-05-15 00:00:00+00:00|HW1|
|2017-08-16 00:00:00+00:00|2018-05-26 00:00:00+00:00|HW1|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_HW1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2012-09-18 00:00:00+00:00|2013-05-19 00:00:00+00:00|HW2|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_HW2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|RH2|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_RH2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-01-01 00:00:00+00:00|2016-01-01 00:00:00+00:00|TA1|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_TA1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS1|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_TS1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS10|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_TS10_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS2|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_TS2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS3|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_TS3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS4|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_TS4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS5|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_TS5_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS6|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_TS6_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS7|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_TS7_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS8|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_TS8_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2021-10-16 17:00:00+00:00|TS9|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_TS9_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2009-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|VW1|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_VW1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2009-01-01 00:00:00+00:00|2010-01-01 00:00:00+00:00|VW2|
 
![Erroneous data at Saddle](../figures/L1_data_treatment/Saddle_VW2_data_flagging.png)
 
## Adjusting data at Saddle
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2021-10-16T17:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2021-10-16T17:00:00+00:00|biweekly_upper_range_filter|0.5|34735|
|2009-05-15T00:00:00+00:00|2021-10-16T17:00:00+00:00|hampel_filter|2.0|1091|
 
![Adjusted data at Saddle](../figures/L1_data_treatment/Saddle_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2021-10-16T17:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2021-10-16T17:00:00+00:00|biweekly_upper_range_filter|0.5|17172|
|2009-05-15T00:00:00+00:00|2021-10-16T17:00:00+00:00|hampel_filter|2.0|1092|
 
![Adjusted data at Saddle](../figures/L1_data_treatment/Saddle_adj_HW2.jpeg)
 
### Adjusting OSWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2010-04-30T00:00:00+00:00|2021-10-16T17:00:00+00:00|multiply|0.934|0|
 
![Adjusted data at Saddle](../figures/L1_data_treatment/Saddle_adj_OSWR.jpeg)
 
### Adjusting RH1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2010-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at Saddle](../figures/L1_data_treatment/Saddle_adj_RH1.jpeg)
 
### Adjusting RH2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2010-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at Saddle](../figures/L1_data_treatment/Saddle_adj_RH2.jpeg)
 
### Adjusting TA3
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1990-01-01T00:00:00+00:00|2021-10-16T17:00:00+00:00|swap_with_TA4|0.0|-615|
 
![Adjusted data at Saddle](../figures/L1_data_treatment/Saddle_adj_TA3.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1998-04-21T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|0.4|0|
|1999-04-20T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|1.9|0|
|2001-06-05T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|2.6|0|
|2002-06-07T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|0.5|0|
|2004-06-11T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|2.5|0|
|2005-05-30T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|2.5|0|
|2007-05-22T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|-2.5|0|
|2008-04-28T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|2.5|0|
|2013-06-07T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|4.0|0|
|2017-09-07T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|1.5|0|
 
![Adjusted data at Saddle](../figures/L1_data_treatment/Saddle_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1999-04-16T11:00:00+00:00|2021-10-16T17:00:00+00:00|add|2.5|0|
|2001-05-23T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|2.5|0|
|2002-01-01T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|-1.0|0|
|2004-06-14T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|2.5|0|
|2005-03-27T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|2.5|0|
|2010-01-07T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|4.0|0|
|2014-05-21T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|4.0|0|
|2019-01-01T16:00:00+00:00|2021-10-16T17:00:00+00:00|add|2.0|0|
 
![Adjusted data at Saddle](../figures/L1_data_treatment/Saddle_adj_HS2.jpeg)
 
# 11 South Dome
## Manual flagging of data at South Dome
Flagging data:
|start time|end time|variable|
|-|-|-|
|2011-11-01 00:00:00+00:00|2012-03-12 00:00:00+00:00|HW1|
|2012-09-01 00:00:00+00:00|2014-05-12 00:00:00+00:00|HW1|
|2018-01-01 00:00:00+00:00|2018-05-12 00:00:00+00:00|HW1|
|2017-08-26 00:00:00+00:00|2021-06-21 16:00:00+00:00|HW1|
|2010-10-01 00:00:00+00:00|2010-12-01 00:00:00+00:00|HW1|
|2011-10-13 00:00:00+00:00|2012-10-01 00:00:00+00:00|HW1|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_HW1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2000-10-01 00:00:00+00:00|2013-05-21 00:00:00+00:00|P|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_P_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|1996-01-01 00:00:00+00:00|1999-06-01 00:00:00+00:00|RH2|
|2010-05-01 00:00:00+00:00|2011-06-01 00:00:00+00:00|RH2|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_RH2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-05-01 00:00:00+00:00|2011-06-01 00:00:00+00:00|TA2|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TA2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|1996-01-01 00:00:00+00:00|1999-06-01 00:00:00+00:00|TA4|
|2010-05-01 00:00:00+00:00|2011-06-01 00:00:00+00:00|TA4|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TA4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS1|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TS1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS10|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TS10_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS2|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TS2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS3|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TS3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS4|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TS4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS5|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TS5_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS6|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TS6_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS7|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TS7_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS8|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TS8_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2008-07-01 00:00:00+00:00|2021-06-21 16:00:00+00:00|TS9|
 
![Erroneous data at South Dome](../figures/L1_data_treatment/South_Dome_TS9_data_flagging.png)
 
## Adjusting data at South Dome
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1995-05-26T20:00:00+00:00|2021-06-21T16:00:00+00:00|max_filter|20.0|1|
|1996-05-15T00:00:00+00:00|2021-06-21T16:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2021-06-21T16:00:00+00:00|biweekly_upper_range_filter|0.3|58166|
|2009-05-15T00:00:00+00:00|2021-06-21T16:00:00+00:00|hampel_filter|2.0|1032|
 
![Adjusted data at South Dome](../figures/L1_data_treatment/South_Dome_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1995-05-26T20:00:00+00:00|2021-06-21T16:00:00+00:00|max_filter|20.0|1|
|1996-05-15T00:00:00+00:00|2021-06-21T16:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2021-06-21T16:00:00+00:00|biweekly_upper_range_filter|0.3|11549|
|2009-05-15T00:00:00+00:00|2021-06-21T16:00:00+00:00|hampel_filter|2.0|82|
 
![Adjusted data at South Dome](../figures/L1_data_treatment/South_Dome_adj_HW2.jpeg)
 
### Adjusting OSWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2021-06-21T16:00:00+00:00|multiply|0.934|0|
 
![Adjusted data at South Dome](../figures/L1_data_treatment/South_Dome_adj_OSWR.jpeg)
 
### Adjusting RH1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2003-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at South Dome](../figures/L1_data_treatment/South_Dome_adj_RH1.jpeg)
 
### Adjusting RH2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2003-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at South Dome](../figures/L1_data_treatment/South_Dome_adj_RH2.jpeg)
 
### Adjusting TS4
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2007-06-13T16:00:00+00:00|2008-07-01T00:00:00+00:00|biweekly_upper_range_filter|1.3|1600|
 
![Adjusted data at South Dome](../figures/L1_data_treatment/South_Dome_adj_TS4.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1998-04-17T00:00:00+00:00|2021-06-21T16:00:00+00:00|add|2.5|0|
|1999-04-22T15:00:00+00:00|2021-06-21T16:00:00+00:00|add|2.0|0|
|2001-06-07T00:00:00+00:00|2021-06-21T16:00:00+00:00|add|3.0|0|
|2005-05-26T20:00:00+00:00|2021-06-21T16:00:00+00:00|add|6.0|0|
|2006-07-18T01:00:00+00:00|2021-06-21T16:00:00+00:00|add|2.5|0|
|2007-04-23T01:00:00+00:00|2021-06-21T16:00:00+00:00|add|3.4|0|
|2009-05-16T18:00:00+00:00|2021-06-21T16:00:00+00:00|add|2.0|0|
|2014-05-25T20:00:00+00:00|2021-06-21T16:00:00+00:00|add|5.0|0|
|2015-05-25T20:00:00+00:00|2021-06-21T16:00:00+00:00|add|2.5|0|
|2017-05-23T00:00:00+00:00|2021-06-21T16:00:00+00:00|add|2.3|0|
 
![Adjusted data at South Dome](../figures/L1_data_treatment/South_Dome_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1998-04-17T00:00:00+00:00|2021-06-21T16:00:00+00:00|add|2.5|0|
|1999-04-22T15:00:00+00:00|2021-06-21T16:00:00+00:00|add|2.0|0|
|2001-06-07T00:00:00+00:00|2021-06-21T16:00:00+00:00|add|3.0|0|
|2005-05-26T20:00:00+00:00|2021-06-21T16:00:00+00:00|add|6.0|0|
|2007-04-23T01:00:00+00:00|2021-06-21T16:00:00+00:00|add|3.4|0|
|2009-05-16T18:00:00+00:00|2021-06-21T16:00:00+00:00|add|1.5|0|
|2011-03-25T18:00:00+00:00|2021-06-21T16:00:00+00:00|add|3.0|0|
|2013-04-22T18:00:00+00:00|2021-06-21T16:00:00+00:00|add|3.0|0|
|2015-04-29T18:00:00+00:00|2021-06-21T16:00:00+00:00|add|3.0|0|
|2017-05-23T00:00:00+00:00|2021-06-21T16:00:00+00:00|add|2.3|0|
|2020-01-23T00:00:00+00:00|2021-06-21T16:00:00+00:00|add|2.3|0|
 
![Adjusted data at South Dome](../figures/L1_data_treatment/South_Dome_adj_HS2.jpeg)
 
# 12 NASA-E
## Manual flagging of data at NASA-E
Flagging data:
|start time|end time|variable|
|-|-|-|
|2015-09-29 00:00:00+00:00|2019-03-01 00:00:00+00:00|HW2|
|2016-08-29 00:00:00+00:00|2019-01-01 00:00:00+00:00|HW2|
 
![Erroneous data at NASA-E](../figures/L1_data_treatment/NASA-E_HW2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2012-02-01 00:00:00+00:00|2013-06-01 00:00:00+00:00|RH1|
 
![Erroneous data at NASA-E](../figures/L1_data_treatment/NASA-E_RH1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2012-02-01 00:00:00+00:00|2013-06-01 00:00:00+00:00|TA3|
|1998-04-12 00:00:00+00:00|1998-11-15 00:00:00+00:00|TA3|
 
![Erroneous data at NASA-E](../figures/L1_data_treatment/NASA-E_TA3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2001-06-07 00:00:00+00:00|2001-06-08 00:00:00+00:00|TA4|
 
![Erroneous data at NASA-E](../figures/L1_data_treatment/NASA-E_TA4_data_flagging.png)
 
## Adjusting data at NASA-E
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|hampel_filter|2.0|11891|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|biweekly_upper_range_filter|0.2|3763|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|hampel_filter|2.0|357|
|2011-05-15T00:00:00+00:00|2019-05-15T00:00:00+00:00|min_filter|1.5|2880|
 
![Adjusted data at NASA-E](../figures/L1_data_treatment/NASA-E_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|hampel_filter|2.0|13490|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|biweekly_upper_range_filter|0.2|27489|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|hampel_filter|2.0|167|
 
![Adjusted data at NASA-E](../figures/L1_data_treatment/NASA-E_adj_HW2.jpeg)
 
### Adjusting OSWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2011-06-02T00:00:00+00:00|2022-09-20T23:00:00+00:00|multiply|0.934|0|
 
![Adjusted data at NASA-E](../figures/L1_data_treatment/NASA-E_adj_OSWR.jpeg)
 
### Adjusting RH1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2011-06-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at NASA-E](../figures/L1_data_treatment/NASA-E_adj_RH1.jpeg)
 
### Adjusting RH2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2011-06-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at NASA-E](../figures/L1_data_treatment/NASA-E_adj_RH2.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2001-06-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.5|0|
|2006-05-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.4|0|
|2009-05-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|-1.0|0|
|2011-06-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|1.5|0|
|2015-06-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.5|0|
 
![Adjusted data at NASA-E](../figures/L1_data_treatment/NASA-E_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2001-06-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.5|0|
|2006-05-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.4|0|
|2009-05-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|-1.0|0|
|2011-06-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|-1.0|0|
|2015-06-09T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.0|0|
 
![Adjusted data at NASA-E](../figures/L1_data_treatment/NASA-E_adj_HS2.jpeg)
 
# 13 CP2
## Manual flagging of data at CP2
No erroneous data listed for CP2
## Adjusting data at CP2
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1997-01-01T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|-5.67|0|
|1998-05-30T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.0|0|
|1999-05-27T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.0|0|
|2000-06-02T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.7|0|
 
![Adjusted data at CP2](../figures/L1_data_treatment/CP2_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1997-01-01T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|-5.52|0|
|1998-05-30T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.0|0|
|1999-05-27T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.0|0|
|2000-06-02T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.7|0|
 
![Adjusted data at CP2](../figures/L1_data_treatment/CP2_adj_HW2.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1998-05-30T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.0|0|
|1999-05-27T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.0|0|
|2000-06-02T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.7|0|
 
![Adjusted data at CP2](../figures/L1_data_treatment/CP2_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1998-05-30T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.0|0|
|1999-05-27T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.0|0|
|2000-06-02T00:00:00+00:00|2001-05-29T13:00:00+00:00|add|1.7|0|
 
![Adjusted data at CP2](../figures/L1_data_treatment/CP2_adj_HS2.jpeg)
 
# 14 NGRIP
## Manual flagging of data at NGRIP
Flagging data:
|start time|end time|variable|
|-|-|-|
|2005-09-01 00:00:00+00:00|2006-01-01 00:00:00+00:00|HS1|
 
![Erroneous data at NGRIP](../figures/L1_data_treatment/NGRIP_HS1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2005-09-01 00:00:00+00:00|2006-01-01 00:00:00+00:00|HS2|
 
![Erroneous data at NGRIP](../figures/L1_data_treatment/NGRIP_HS2_data_flagging.png)
 
## Adjusting data at NGRIP
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2006-01-01T00:00:00+00:00|2010-05-08T13:00:00+00:00|add|2.0|0|
 
![Adjusted data at NGRIP](../figures/L1_data_treatment/NGRIP_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2006-01-01T00:00:00+00:00|2010-05-08T13:00:00+00:00|add|2.0|0|
 
![Adjusted data at NGRIP](../figures/L1_data_treatment/NGRIP_adj_HS2.jpeg)
 
# 15 NASA-SE
## Manual flagging of data at NASA-SE
Flagging data:
|start time|end time|variable|
|-|-|-|
|2009-01-01 00:00:00+00:00|2011-05-19 00:00:00+00:00|HW1|
|2015-07-01 00:00:00+00:00|2016-05-19 00:00:00+00:00|HW1|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_HW1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-01-01 00:00:00+00:00|2011-05-26 00:00:00+00:00|HW2|
|2016-01-15 00:00:00+00:00|2016-05-19 00:00:00+00:00|HW2|
|2017-08-18 00:00:00+00:00|2018-05-26 00:00:00+00:00|HW2|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_HW2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2012-01-08 00:00:00+00:00|2021-06-01 00:00:00+00:00|TA1|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TA1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2012-01-08 00:00:00+00:00|2021-06-01 00:00:00+00:00|TA2|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TA2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS1|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS10|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS10_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS2|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS3|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS4|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS5|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS5_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS6|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS6_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS7|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS7_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS8|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS8_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-06-01 00:00:00+00:00|2019-09-26 09:00:00+00:00|TS9|
 
![Erroneous data at NASA-SE](../figures/L1_data_treatment/NASA-SE_TS9_data_flagging.png)
 
## Adjusting data at NASA-SE
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2002-05-18T00:00:00+00:00|2005-05-27T09:00:00+00:00|add|3.0|0|
|2003-05-10T09:00:00+00:00|2005-05-27T09:00:00+00:00|add|8.26|0|
|2009-05-15T00:00:00+00:00|2019-09-26T09:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2019-09-26T09:00:00+00:00|biweekly_upper_range_filter|0.5|20074|
|2009-05-15T00:00:00+00:00|2019-09-26T09:00:00+00:00|hampel_filter|2.0|4380|
 
![Adjusted data at NASA-SE](../figures/L1_data_treatment/NASA-SE_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2002-05-18T00:00:00+00:00|2005-05-27T09:00:00+00:00|add|3.0|0|
|2003-05-10T09:00:00+00:00|2005-05-27T09:00:00+00:00|add|9.56|0|
|2009-05-15T00:00:00+00:00|2019-09-26T09:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2019-09-26T09:00:00+00:00|biweekly_upper_range_filter|0.5|15533|
|2009-05-15T00:00:00+00:00|2019-09-26T09:00:00+00:00|hampel_filter|2.0|2943|
 
![Adjusted data at NASA-SE](../figures/L1_data_treatment/NASA-SE_adj_HW2.jpeg)
 
### Adjusting OSWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-04-26T00:00:00+00:00|2019-09-26T09:00:00+00:00|multiply|0.934|0|
 
![Adjusted data at NASA-SE](../figures/L1_data_treatment/NASA-SE_adj_OSWR.jpeg)
 
### Adjusting RH1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2009-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at NASA-SE](../figures/L1_data_treatment/NASA-SE_adj_RH1.jpeg)
 
### Adjusting RH2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2009-01-01T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at NASA-SE](../figures/L1_data_treatment/NASA-SE_adj_RH2.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2000-05-17T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.4|0|
|2002-05-17T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.5|0|
|2003-05-10T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.0|0|
|2005-05-27T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|4.2|0|
|2007-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|3.0|0|
|2008-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.0|0|
|2012-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.0|0|
|2013-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.0|0|
|2016-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.5|0|
|2018-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.0|0|
 
![Adjusted data at NASA-SE](../figures/L1_data_treatment/NASA-SE_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2000-05-17T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.4|0|
|2002-05-17T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.5|0|
|2003-05-10T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.0|0|
|2005-05-27T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|4.2|0|
|2007-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|3.0|0|
|2008-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.0|0|
|2012-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.0|0|
|2013-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.0|0|
|2016-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.5|0|
|2018-06-09T00:00:00+00:00|2019-09-26T09:00:00+00:00|add|2.0|0|
 
![Adjusted data at NASA-SE](../figures/L1_data_treatment/NASA-SE_adj_HS2.jpeg)
 
# 16 KAR
## Manual flagging of data at KAR
No erroneous data listed for KAR
## Adjusting data at KAR
No data to fix at KAR
No data to fix at KAR
# 17 JAR2
## Manual flagging of data at JAR2
No erroneous data listed for JAR2
## Adjusting data at JAR2
No data to fix at JAR2
No data to fix at JAR2
# 18 KULU
## Manual flagging of data at KULU
No erroneous data listed for KULU
## Adjusting data at KULU
# 19 JAR3
## Manual flagging of data at JAR3
No erroneous data listed for JAR3
## Adjusting data at JAR3
No data to fix at JAR3
No data to fix at JAR3
# 20 Aurora
## Manual flagging of data at Aurora
No erroneous data listed for Aurora
## Adjusting data at Aurora
No data to fix at Aurora
No data to fix at Aurora
# 21 Petermann Glacier
## Manual flagging of data at Petermann Glacier
No erroneous data listed for Petermann Glacier
## Adjusting data at Petermann Glacier
No data to fix at Petermann Glacier
No data to fix at Petermann Glacier
# 22 Petermann ELA
## Manual flagging of data at Petermann ELA
Flagging data:
|start time|end time|variable|
|-|-|-|
|2003-01-01 00:00:00+00:00|2011-05-23 00:00:00+00:00|RH1|
 
![Erroneous data at Petermann ELA](../figures/L1_data_treatment/Petermann_ELA_RH1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2003-01-01 00:00:00+00:00|2011-05-01 00:00:00+00:00|RH2|
 
![Erroneous data at Petermann ELA](../figures/L1_data_treatment/Petermann_ELA_RH2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-01-01 00:00:00+00:00|2015-01-01 00:00:00+00:00|TA1|
 
![Erroneous data at Petermann ELA](../figures/L1_data_treatment/Petermann_ELA_TA1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2011-01-01 00:00:00+00:00|2015-01-01 00:00:00+00:00|TA2|
 
![Erroneous data at Petermann ELA](../figures/L1_data_treatment/Petermann_ELA_TA2_data_flagging.png)
 
## Adjusting data at Petermann ELA
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2022-04-12T18:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2016-01-01T00:00:00+00:00|2022-04-12T18:00:00+00:00|biweekly_upper_range_filter|0.5|280|
|2016-01-01T00:00:00+00:00|2022-04-12T18:00:00+00:00|hampel_filter|2.0|1515|
 
![Adjusted data at Petermann ELA](../figures/L1_data_treatment/Petermann_ELA_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2022-04-12T18:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2015-07-01T00:00:00+00:00|2016-01-01T00:00:00+00:00|min_filter|1.4|3|
|2016-01-01T00:00:00+00:00|2022-04-12T18:00:00+00:00|biweekly_upper_range_filter|0.5|7096|
|2016-01-01T00:00:00+00:00|2019-01-01T00:00:00+00:00|max_filter|3.12|156|
|2016-01-01T00:00:00+00:00|2019-01-01T00:00:00+00:00|min_filter|2.4|928|
|2016-01-01T00:00:00+00:00|2022-04-12T18:00:00+00:00|hampel_filter|2.0|22|
 
![Adjusted data at Petermann ELA](../figures/L1_data_treatment/Petermann_ELA_adj_HW2.jpeg)
 
### Adjusting TA2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-05-23T07:00:00+00:00|2022-04-12T18:00:00+00:00|max_filter|11.0|20|
 
![Adjusted data at Petermann ELA](../figures/L1_data_treatment/Petermann_ELA_adj_TA2.jpeg)
 
### Adjusting TA3
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-05-23T07:00:00+00:00|2022-04-12T18:00:00+00:00|max_filter|11.0|9|
 
![Adjusted data at Petermann ELA](../figures/L1_data_treatment/Petermann_ELA_adj_TA3.jpeg)
 
### Adjusting TA4
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2003-05-23T07:00:00+00:00|2022-04-12T18:00:00+00:00|max_filter|11.0|9|
 
![Adjusted data at Petermann ELA](../figures/L1_data_treatment/Petermann_ELA_adj_TA4.jpeg)
 
# 23 NEEM
## Manual flagging of data at NEEM
Flagging data:
|start time|end time|variable|
|-|-|-|
|2010-07-15 00:00:00+00:00|2010-12-01 00:00:00+00:00|HW1|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_HW1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2010-07-15 00:00:00+00:00|2011-09-24 00:00:00+00:00|HW2|
|2013-02-05 00:00:00+00:00|2013-03-17 00:00:00+00:00|HW2|
|2017-12-26 00:00:00+00:00|2018-04-01 00:00:00+00:00|HW2|
|2019-01-01 00:00:00+00:00|2019-04-10 00:00:00+00:00|HW2|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_HW2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2009-01-01 00:00:00+00:00|2017-01-01 00:00:00+00:00|P|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_P_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2017-02-01 00:00:00+00:00|2018-05-01 00:00:00+00:00|RH2|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_RH2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2017-02-01 00:00:00+00:00|2018-05-09 00:00:00+00:00|TA3|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TA3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2018-05-04 00:00:00+00:00|2018-05-24 00:00:00+00:00|TA4|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TA4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-06-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS1|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TS1_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-06-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS10|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TS10_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-06-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS2|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TS2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-06-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS3|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TS3_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-06-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS4|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TS4_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-06-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS5|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TS5_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-06-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS6|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TS6_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-06-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS7|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TS7_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-06-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS8|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TS8_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2007-06-01 00:00:00+00:00|2022-09-20 23:00:00+00:00|TS9|
 
![Erroneous data at NEEM](../figures/L1_data_treatment/NEEM_TS9_data_flagging.png)
 
## Adjusting data at NEEM
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|biweekly_upper_range_filter|0.5|14836|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|min_filter|0.1|15195|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|hampel_filter|2.0|6262|
 
![Adjusted data at NEEM](../figures/L1_data_treatment/NEEM_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|biweekly_upper_range_filter|0.5|22328|
|2009-05-15T00:00:00+00:00|2022-09-20T23:00:00+00:00|hampel_filter|2.0|7037|
 
![Adjusted data at NEEM](../figures/L1_data_treatment/NEEM_adj_HW2.jpeg)
 
### Adjusting OSWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2009-05-30T00:00:00+00:00|2022-09-20T23:00:00+00:00|multiply|0.934|0|
 
![Adjusted data at NEEM](../figures/L1_data_treatment/NEEM_adj_OSWR.jpeg)
 
### Adjusting RH1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2009-05-15T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at NEEM](../figures/L1_data_treatment/NEEM_adj_RH1.jpeg)
 
### Adjusting RH2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|1996-01-01T00:00:00+00:00|2009-05-15T00:00:00+00:00|ice_to_water|0.0|0|
 
![Adjusted data at NEEM](../figures/L1_data_treatment/NEEM_adj_RH2.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2008-08-13T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|1.8|0|
|2009-05-30T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|0.5|0|
|2011-07-06T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|3.0|0|
|2016-05-23T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.5|0|
 
![Adjusted data at NEEM](../figures/L1_data_treatment/NEEM_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2008-08-13T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|1.8|0|
|2009-05-30T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|-1.5|0|
|2011-07-06T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.0|0|
|2016-05-23T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.0|0|
 
![Adjusted data at NEEM](../figures/L1_data_treatment/NEEM_adj_HS2.jpeg)
 
# 24 E-GRIP
## Manual flagging of data at E-GRIP
Flagging data:
Warning: ISWR not found
Warning: OSWR not found
## Adjusting data at E-GRIP
### Adjusting DW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2014-01-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|multiply|-1.0|0|
|2014-01-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|rotate|20.0|0|
|2014-01-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|rotate|30.0|0|
|2019-05-22T00:00:00+00:00|2022-09-20T23:00:00+00:00|rotate|185.0|0|
 
![Adjusted data at E-GRIP](../figures/L1_data_treatment/E-GRIP_adj_DW1.jpeg)
 
### Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2014-01-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2014-01-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|biweekly_upper_range_filter|0.4|9327|
|2014-01-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|hampel_filter|2.0|4562|
 
![Adjusted data at E-GRIP](../figures/L1_data_treatment/E-GRIP_adj_HW1.jpeg)
 
### Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2014-01-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2014-01-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|biweekly_upper_range_filter|0.4|6813|
|2014-01-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|hampel_filter|2.0|5131|
|2014-01-01T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|1.2|0|
 
![Adjusted data at E-GRIP](../figures/L1_data_treatment/E-GRIP_adj_HW2.jpeg)
 
### Adjusting HS1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2016-05-23T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.0|0|
 
![Adjusted data at E-GRIP](../figures/L1_data_treatment/E-GRIP_adj_HS1.jpeg)
 
### Adjusting HS2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2016-05-23T00:00:00+00:00|2022-09-20T23:00:00+00:00|add|2.0|0|
 
![Adjusted data at E-GRIP](../figures/L1_data_treatment/E-GRIP_adj_HS2.jpeg)
 
# 30 LAR1
## Manual flagging of data at LAR1
No erroneous data listed for LAR1
## Adjusting data at LAR1
### Adjusting ISWR
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2000-01-01T00:00:00+00:00|2012-01-01T00:00:00+00:00|swap_with_OSWR|0.0|0|
 
![Adjusted data at LAR1](../figures/L1_data_treatment/LAR1_adj_ISWR.jpeg)
 
# 31 LAR2
## Manual flagging of data at LAR2
No erroneous data listed for LAR2
## Adjusting data at LAR2
No data to fix at LAR2
No data to fix at LAR2
# 32 LAR3
## Manual flagging of data at LAR3
No erroneous data listed for LAR3
## Adjusting data at LAR3
No data to fix at LAR3
No data to fix at LAR3

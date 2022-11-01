* [0 Swiss Camp 10m](#s1)
  * [Manual flagging of data at Swiss Camp 10m](#s1-1)
  * [Adjusting data at Swiss Camp 10m](#s1-2)
      * [Adjusting HW1](#s1-2-1)
      * [Adjusting HW2](#s1-2-2)
      * [Adjusting P](#s1-2-3)
# <a id='s1' />0 Swiss Camp 10m
## <a id='s1-1' />Manual flagging of data at Swiss Camp 10m
Flagging data:
|start time|end time|variable|
|-|-|-|
|2017-08-21 00:00:00+00:00|2018-05-05 00:00:00+00:00|HW2|
 
![Erroneous data at Swiss Camp 10m](../figures/L1_data_treatment/Swiss_Camp_10m_HW2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2016-05-01 00:00:00+00:00|2017-06-01 00:00:00+00:00|OSWR|
 
![Erroneous data at Swiss Camp 10m](../figures/L1_data_treatment/Swiss_Camp_10m_OSWR_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2018-02-15 00:00:00+00:00|2018-05-05 00:00:00+00:00|P|
 
![Erroneous data at Swiss Camp 10m](../figures/L1_data_treatment/Swiss_Camp_10m_P_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2015-05-15 00:00:00+00:00|2016-05-15 00:00:00+00:00|TA2|
 
![Erroneous data at Swiss Camp 10m](../figures/L1_data_treatment/Swiss_Camp_10m_TA2_data_flagging.png)
 
|start time|end time|variable|
|-|-|-|
|2015-05-15 00:00:00+00:00|2016-05-15 00:00:00+00:00|TA3|
 
![Erroneous data at Swiss Camp 10m](../figures/L1_data_treatment/Swiss_Camp_10m_TA3_data_flagging.png)
 
## <a id='s1-2' />Adjusting data at Swiss Camp 10m
### <a id='s1-2-1' />Adjusting HW1
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2014-01-01T00:00:00+00:00|2019-05-04T18:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2014-01-01T00:00:00+00:00|2019-05-04T18:00:00+00:00|biweekly_upper_range_filter|0.5|2602|
|2014-01-01T00:00:00+00:00|2019-05-04T18:00:00+00:00|hampel_filter|2.0|3797|
 
![Adjusted data at Swiss Camp 10m](../figures/L1_data_treatment/Swiss_Camp_10m_adj_HW1.jpeg)
 
### <a id='s1-2-2' />Adjusting HW2
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2014-01-01T00:00:00+00:00|2019-05-04T18:00:00+00:00|air_temp_sonic_correction|0.0|0|
|2014-01-01T00:00:00+00:00|2019-05-04T18:00:00+00:00|biweekly_upper_range_filter|0.5|8517|
|2014-01-01T00:00:00+00:00|2019-05-04T18:00:00+00:00|hampel_filter|2.0|2714|
|2014-05-09T21:00:00+00:00|2019-05-04T18:00:00+00:00|add|9.0|0|
 
![Adjusted data at Swiss Camp 10m](../figures/L1_data_treatment/Swiss_Camp_10m_adj_HW2.jpeg)
 
### <a id='s1-2-3' />Adjusting P
|start time|end time|operation|value|number of removed samples|
|-|-|-|-|-|
|2014-01-01T00:00:00+00:00|2019-05-05T00:00:00+00:00|add|-96.5|0|
 
![Adjusted data at Swiss Camp 10m](../figures/L1_data_treatment/Swiss_Camp_10m_adj_P.jpeg)
 

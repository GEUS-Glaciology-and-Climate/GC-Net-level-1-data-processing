* [0 Swiss Camp 10m](#s1)
  * [Removing erroneous data at Swiss Camp 10m](#s1-1)
  * [Adjusting data at Swiss Camp 10m](#s1-2)
* [1 Swiss Camp](#s2)
  * [Removing erroneous data at Swiss Camp](#s2-1)
  * [Adjusting data at Swiss Camp](#s2-2)
* [2 Crawford Point 1](#s3)
  * [Removing erroneous data at Crawford Point 1](#s3-1)
  * [Adjusting data at Crawford Point 1](#s3-2)
* [3 NASA-U](#s4)
  * [Removing erroneous data at NASA-U](#s4-1)
  * [Adjusting data at NASA-U](#s4-2)
      * [Adjusting HS2](#s4-2-1)
      * [Adjusting HS1](#s4-2-2)
* [4 GITS](#s5)
  * [Removing erroneous data at GITS](#s5-1)
  * [Adjusting data at GITS](#s5-2)
* [5 Humboldt](#s6)
  * [Removing erroneous data at Humboldt](#s6-1)
  * [Adjusting data at Humboldt](#s6-2)
* [6 Summit](#s7)
  * [Removing erroneous data at Summit](#s7-1)
# <a id='s1' />0 Swiss Camp 10m
## <a id='s1-1' />Removing erroneous data at Swiss Camp 10m
No erroneous data listed for Swiss Camp 10m
## <a id='s1-2' />Adjusting data at Swiss Camp 10m
No data to fix at Swiss Camp 10m
# <a id='s2' />1 Swiss Camp
## <a id='s2-1' />Removing erroneous data at Swiss Camp
Flagging data:
Warning: interpreting RelativeHumidity1Perc as RH1
|start time|end time|variable|
|-|-|-|
|2015-01-01 00:00:00+00:00|2017-01-01 00:00:00+00:00|RH1|
 
![Erroneous data at Swiss Camp](figures/Swiss_Camp_RH1_data_flagging.png)
 
Warning: interpreting RelativeHumidity2Perc as RH2
|start time|end time|variable|
|-|-|-|
|2015-01-01 00:00:00+00:00|2017-01-01 00:00:00+00:00|RH2|
 
![Erroneous data at Swiss Camp](figures/Swiss_Camp_RH2_data_flagging.png)
 
Warning: interpreting ShortwaveRadiationDownWm2 as ISWR
|start time|end time|variable|
|-|-|-|
|1997-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|ISWR|
|1996-01-05 00:00:00+00:00|2019-01-01 00:00:00+00:00|ISWR|
 
![Erroneous data at Swiss Camp](figures/Swiss_Camp_ISWR_data_flagging.png)
 
Warning: interpreting ShortwaveRadiationUpWm2 as OSWR
|start time|end time|variable|
|-|-|-|
|1997-01-01 00:00:00+00:00|1999-01-01 00:00:00+00:00|OSWR|
 
![Erroneous data at Swiss Camp](figures/Swiss_Camp_OSWR_data_flagging.png)
 
## <a id='s2-2' />Adjusting data at Swiss Camp
# <a id='s3' />2 Crawford Point 1
## <a id='s3-1' />Removing erroneous data at Crawford Point 1
No erroneous data listed for Crawford Point 1
## <a id='s3-2' />Adjusting data at Crawford Point 1
No data to fix at Crawford Point 1
# <a id='s4' />3 NASA-U
## <a id='s4-1' />Removing erroneous data at NASA-U
No erroneous data listed for NASA-U
## <a id='s4-2' />Adjusting data at NASA-U
Replacing SnowHeight(m) by HS2
### <a id='s4-2-1' />Adjusting HS2
|start time|end time|operation|value|
|-|-|-|-|
|2003-06-03T16:00:00+00:00|nan|add|-8.0|
|2006-04-26T00:30:00+00:00|nan|add|6.27|
|2009-04-20T16:00:00+00:00|nan|add|-11.0|
|2011-06-01T22:00:00+00:00|nan|add|-1.7|
|2014-05-31T00:00:00+00:00|nan|add|-5.0|
 
![Adjusted data at NASA-U](figures/NASA-U_adj_HS2.jpeg)
 
Replacing SurfaceHeight(m) by HS1
### <a id='s4-2-2' />Adjusting HS1
|start time|end time|operation|value|
|-|-|-|-|
|2003-06-03T16:00:00+00:00|nan|add|-8.0|
|2009-04-20T16:00:00+00:00|nan|add|-4.7|
|2011-06-01T22:00:00+00:00|nan|add|-1.58|
|2015-01-15T00:00:00+00:00|nan|add|-3.5|
 
![Adjusted data at NASA-U](figures/NASA-U_adj_HS1.jpeg)
 
# <a id='s5' />4 GITS
## <a id='s5-1' />Removing erroneous data at GITS
Flagging data:
Warning: interpreting AirPressurehPa as P
|start time|end time|variable|
|-|-|-|
|1998-05-01 00:00:00+00:00|1998-07-01 00:00:00+00:00|P|
 
![Erroneous data at GITS](figures/GITS_P_data_flagging.png)
 
Warning: interpreting AirTemperature1C as TA1
|start time|end time|variable|
|-|-|-|
|1998-05-01 00:00:00+00:00|1998-07-01 00:00:00+00:00|TA1|
|2013-09-04 21:00:00+00:00|2014-05-21 00:00:00+00:00|TA1|
|1999-04-01 00:00:00+00:00|1999-12-01 00:00:00+00:00|TA1|
 
![Erroneous data at GITS](figures/GITS_TA1_data_flagging.png)
 
Warning: interpreting AirTemperature2C as TA2
|start time|end time|variable|
|-|-|-|
|1998-05-01 00:00:00+00:00|1998-07-01 00:00:00+00:00|TA2|
|1999-04-01 00:00:00+00:00|1999-12-01 00:00:00+00:00|TA2|
 
![Erroneous data at GITS](figures/GITS_TA2_data_flagging.png)
 
Warning: interpreting AirTemperature3C as TA3
|start time|end time|variable|
|-|-|-|
|2013-09-04 21:00:00+00:00|2014-05-21 00:00:00+00:00|TA3|
|1999-04-01 00:00:00+00:00|1999-12-01 00:00:00+00:00|TA3|
 
![Erroneous data at GITS](figures/GITS_TA3_data_flagging.png)
 
Warning: interpreting AirTemperature4C as TA4
|start time|end time|variable|
|-|-|-|
|1999-04-01 00:00:00+00:00|1999-12-01 00:00:00+00:00|TA4|
 
![Erroneous data at GITS](figures/GITS_TA4_data_flagging.png)
 
Warning: interpreting RelativeHumidity1Perc as RH1
|start time|end time|variable|
|-|-|-|
|1998-05-01 00:00:00+00:00|1998-07-01 00:00:00+00:00|RH1|
 
![Erroneous data at GITS](figures/GITS_RH1_data_flagging.png)
 
Warning: interpreting RelativeHumidity2Perc as RH2
|start time|end time|variable|
|-|-|-|
|1998-05-01 00:00:00+00:00|1998-07-01 00:00:00+00:00|RH2|
 
![Erroneous data at GITS](figures/GITS_RH2_data_flagging.png)
 
Warning: interpreting ShortwaveRadiationDownWm2 as ISWR
|start time|end time|variable|
|-|-|-|
|2014-01-01 11:00:00+00:00|2019-01-01 00:00:00+00:00|ISWR|
|2001-02-01 00:00:00+00:00|2001-04-24 00:00:00+00:00|ISWR|
|2019-02-01 00:00:00+00:00|2019-04-05 00:00:00+00:00|ISWR|
 
![Erroneous data at GITS](figures/GITS_ISWR_data_flagging.png)
 
Warning: interpreting ShortwaveRadiationUpWm2 as OSWR
|start time|end time|variable|
|-|-|-|
|2014-01-01 11:00:00+00:00|2019-01-01 00:00:00+00:00|OSWR|
|2001-02-01 00:00:00+00:00|2001-04-24 00:00:00+00:00|OSWR|
|2019-02-01 00:00:00+00:00|2019-04-05 00:00:00+00:00|OSWR|
 
![Erroneous data at GITS](figures/GITS_OSWR_data_flagging.png)
 
Warning: interpreting WindSpeed1ms as VW1
|start time|end time|variable|
|-|-|-|
|1998-05-01 00:00:00+00:00|1998-07-01 00:00:00+00:00|VW1|
|1999-04-01 00:00:00+00:00|1999-12-01 00:00:00+00:00|VW1|
 
![Erroneous data at GITS](figures/GITS_VW1_data_flagging.png)
 
Warning: interpreting WindSpeed2ms as VW2
|start time|end time|variable|
|-|-|-|
|1998-05-01 00:00:00+00:00|1998-07-01 00:00:00+00:00|VW2|
|1999-04-01 00:00:00+00:00|1999-12-01 00:00:00+00:00|VW2|
 
![Erroneous data at GITS](figures/GITS_VW2_data_flagging.png)
 
## <a id='s5-2' />Adjusting data at GITS
# <a id='s6' />5 Humboldt
## <a id='s6-1' />Removing erroneous data at Humboldt
No erroneous data listed for Humboldt
## <a id='s6-2' />Adjusting data at Humboldt
# <a id='s7' />6 Summit
## <a id='s7-1' />Removing erroneous data at Summit
Flagging data:
Warning: interpreting AirPressurehPa as P
|start time|end time|variable|
|-|-|-|
|2015-12-24 21:00:00+00:00|2016-05-24 00:00:00+00:00|P|
 
![Erroneous data at Summit](figures/Summit_P_data_flagging.png)
 
Warning: interpreting AirTemperature1C as TA1
|start time|end time|variable|
|-|-|-|
|1996-05-13 10:59:57+00:00|1999-01-09 00:00:00+00:00|TA1|
|2009-12-03 13:59:00+00:00|2010-04-19 00:00:00+00:00|TA1|
 
![Erroneous data at Summit](figures/Summit_TA1_data_flagging.png)
 
Warning: interpreting AirTemperature2C as TA2
|start time|end time|variable|
|-|-|-|
|1996-05-13 10:59:57+00:00|1999-01-09 00:00:00+00:00|TA2|
|2009-12-03 13:59:00+00:00|2010-04-19 00:00:00+00:00|TA2|
 
![Erroneous data at Summit](figures/Summit_TA2_data_flagging.png)
 
Warning: interpreting AirTemperature3C as TA3
|start time|end time|variable|
|-|-|-|
|1996-05-13 10:59:57+00:00|1999-01-09 00:00:00+00:00|TA3|
|2006-12-21 22:59:00+00:00|2007-04-15 00:00:00+00:00|TA3|
|2009-12-03 13:59:00+00:00|2010-04-19 00:00:00+00:00|TA3|
 
![Erroneous data at Summit](figures/Summit_TA3_data_flagging.png)
 
Warning: interpreting AirTemperature4C as TA4
|start time|end time|variable|
|-|-|-|
|2006-12-21 22:59:00+00:00|2007-04-15 00:00:00+00:00|TA4|
|2009-12-03 13:59:00+00:00|2010-04-19 00:00:00+00:00|TA4|
 
![Erroneous data at Summit](figures/Summit_TA4_data_flagging.png)
 
Warning: IceTemperature1 not found
Warning: IceTemperature10 not found
Warning: IceTemperature2 not found
Warning: IceTemperature3 not found
Warning: IceTemperature4 not found
Warning: IceTemperature5 not found
Warning: IceTemperature6 not found
Warning: IceTemperature7 not found
Warning: IceTemperature8 not found
Warning: IceTemperature9 not found
Warning: interpreting RelativeHumidity1Perc as RH1
|start time|end time|variable|
|-|-|-|
|1996-05-13 10:59:57+00:00|1999-12-31 00:00:00+00:00|RH1|
|1996-05-13 10:59:57+00:00|1998-02-07 00:00:00+00:00|RH1|
|2002-11-03 00:00:00+00:00|2003-02-26 00:00:00+00:00|RH1|
|2005-10-15 22:00:02+00:00|2006-03-04 00:00:00+00:00|RH1|
 
![Erroneous data at Summit](figures/Summit_RH1_data_flagging.png)
 
Warning: interpreting RelativeHumidity2Perc as RH2
|start time|end time|variable|
|-|-|-|
|1996-05-13 10:59:57+00:00|1999-12-31 00:00:00+00:00|RH2|
|2000-09-05 12:00:00+00:00|2000-11-17 00:00:00+00:00|RH2|
|1996-05-13 10:59:57+00:00|1998-02-07 00:00:00+00:00|RH2|
|2002-11-03 00:00:00+00:00|2003-02-26 00:00:00+00:00|RH2|
|2005-10-15 22:00:02+00:00|2006-03-04 00:00:00+00:00|RH2|
 
![Erroneous data at Summit](figures/Summit_RH2_data_flagging.png)
 
Warning: interpreting ShortwaveRadiationDownWm2 as ISWR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        figures and output folders already exist

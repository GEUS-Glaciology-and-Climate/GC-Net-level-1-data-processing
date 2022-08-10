	program Klima

c ****************************************************************************
c       read Campell met data from the ETH camp in Greenland
c       change jd and time to jd_time
c       10 m tower, datalogger outside on tower (station klima)
c       pyranometer: up # 12875, channel 1, close to mast (cal. 106.49)
c       pyranometer: down # 12798, channel 2, above down looking (cal. 105.89)
c       net radiometer: #90094, channel 3
c       program : 5-22-97 Syno City
c ****************************************************************************

	character*20 in
	integer ich
	real jd,time,a1,min,hour,xmin,r1(3),r2(3)
	real licore1,licore2
	real wind(3),ta1(3),t1(3),t2(3),hum(3)
	real jd_t,net(3),wdir,press

c   Li-Core calibration coefficients (6-15-93)
	licore1=106.49
	licore2=105.89

c   UUB coefficients for air temperature
	a=-9.0763671
	b=0.704343
	c=0.00919
	d=0.000137
	e=0.00000116676
	f=0.00000000400674

	print *,'give input file name '
	read(*,'(a)') in
	open(1,file=in)

c	print *,'give name output '
c	read(*,'(a)') out1
	open(2,file='rad.dat')
 2020	format('  Jul.Day  S(up) S(dw)   Alb  net_rad')
	write(2,2020)

c	print *,'give name output '
c	read(*,'(a)') out2
	open(3,file='t_w_h.dat')
c 2030   format('  Julian    Wind   Wind   Wind   Temp')
c 2031   format('    Day      mean   max   dir     C')
c	write(3,2030)
c	write(3,2031)
	
	do 100 i=1,100000

	read(1,*,end=6000) ich

	if(ich.eq.205.or.ich.eq.206) goto 101
	if(ich.eq.103) goto 102

 101	backspace (1)
	read(1,*,end=6000) ich,jd,time,wind(1),t1(1),t2(1),hum(1),
     1  wind(2),t1(2),t2(2),hum(2),
     2  wind(3),t1(3),t2(3),hum(3),wdir,press

c    change jd and time in real
	if(time.eq.0) then
	hour=0.
	goto 150
	else
	endif

	min=time-(aint(time/100.))*100.
	if(min.eq.0) goto 160
	min=min/60.
 160    hour=aint(time/100.)
	hour=(hour+min)/24.
 150    continue
	jd_t=jd + hour

c     correction for wrong offset during winter 95/96
	if(t1(1).le.300.) goto 161
	t1(1)=t1(1)-400
	t1(2)=t1(2)-400
	t1(3)=t1(3)-400 
  161	continue

	do 165 l=1,3
c    convert UUB thermister reading to temperature      
	ta1(l)=a+b*t1(l)+c*(t1(l)**2)+d*(t1(l)**3)+e*(t1(l)**4)+
     1  f*(t1(l)**5)
  165	continue
	
	press=press+800.
					       
	write(3,2032) jd_t,(wind(n),n=1,3),(ta1(n),n=1,3),(t2(n),n=1,3),
     1  (hum(n),n=1,3),wdir,press
 2032   format(f9.3,9f7.2,3f7.1,f6.1,f7.1)
	goto 100
	
 102	continue
	backspace (1)
	do 500 ii=1,3
	read(1,*,end=7000) ich,r1(ii),r2(ii),net(ii)

c    change jd and time in real
	if(time.eq.0) then
	hour=0.
	min=min+xmin
	min=min/60.
	goto 170
	else
	endif
	min=time-(aint(time/100.))*100.+xmin
	if(min.eq.0) goto 180
	min=min/60.
 180   hour=aint(time/100.)
 170   hour=(hour+min)/24.
	jd_t=jd + hour
	xmin=xmin+60.
	
c    convert Li-Core mV to W/m2
	r1(ii)=r1(ii)*licore1
	r2(ii)=r2(ii)*licore2
	if(r1(ii).lt.0.) r1(ii)=0.
	if(r2(ii).lt.0.) r2(ii)=0.

c    calculate albedo
	if(r1(ii).eq.0) goto 190
	if(r2(ii).eq.0) goto 190 
	a1=r2(ii)/r1(ii)*100
	goto 195

  190	a1=0
	a2=0
  195	continue

c    convert net radiation mv to W/m2
c	new net radiation sensor in 97 (old one from Boulder)	
	net(ii)=net(ii)*13.3

	write(2,2002) jd_t,r1(ii),r2(ii),a1,net(ii)
 2002   format(f9.3,2f8.1,1f5.0,f7.1)
  
  500   continue

  100   continue

 6000   continue
 7000   continue
	end

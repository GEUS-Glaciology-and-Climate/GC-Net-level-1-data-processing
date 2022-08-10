	program Klima

c ****************************************************************************
c       read Campell met data from the ETH camp in Greenland
c       change jd and time to jd_time
c       10 m tower, datalogger outside on tower (station klima)
c       
c       pyranometer: up # 12875, channel 1, close to mast (cal. 106.49)
c       pyranometer: up # 12798, channel 2, above down looking (cal. 105.89)
c       pyronometer: down # 12880, channel 3, down (cal. 105.92)
c       net radiometer: #90094, channel 4
c
c       program : 5-22-97 Syno City 
c       modified in Hobart 8-20-97

c     modified to format for long time record
c ****************************************************************************

	character*20 in
	integer ich,flag,year,flag1,flag2
	real jd,time,a1,hour,r1,r2,r3
	real licore1,licore2,licore3
	real wind(3),ta1(3),t1(3),t2(3),hum(3)
	real jd_t,net,wdir,press

c   Li-Core calibration coefficients (6-15-93)
	licore1=106.49
	licore2=105.89
	licore3=105.92

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
	open(2,file='r_96-97.dat')
c 2020	format('  Jul.Day  S1(up) S2(up)   S(dw)   Alb1  Alb2  net_rad')
c	write(2,2020)

c	print *,'give name output '
c	read(*,'(a)') out2
	open(3,file='t_96-97.dat')
c 2030   format('  Julian    Wind   Wind   Wind   Temp')
c 2031   format('    Day      mean   max   dir     C')
c	write(3,2030)
c	write(3,2031)   

      flag=0
      flag1=0
      flag2=0
	
	do 100 i=1,200000
	read(1,*,end=6000) ich

	if(ich.eq.205.or.ich.eq.206) goto 101
	if(ich.eq.103) goto 102

  101 flag=1
      backspace (1)
  103 read(1,*,end=6000) ich,jd,time,wind(1),t1(1),t2(1),hum(1),
     1  wind(2),t1(2),t2(2),hum(2),
     2  wind(3),t1(3),t2(3),hum(3),wdir,press

c     change hour to decimal hour
      hour=(time/100.)/24.
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
	      
	
	jd=jd_t
	
	if(jd .le. 366.875 .and. flag1 .eq. 0) year=1996
      if(flag1 .eq. 1) year=1997
	
	write(3,2032) year,jd_t,wind(1),wdir,t2(1)
 2032   format(1x,i5,f9.3,3f9.2)
 
      if(jd .ge. 366.8) flag1=1

	goto 100

  102 if(flag.eq.0) goto 100
	backspace (1)
	read(1,*,end=7000) ich,r1,r2,r3,net
      
c    convert Li-Core mV to W/m2
	r1=r1*licore1
	r2=r2*licore2
	r3=r3*licore3
	if(r1.lt.0.) r1=0.
	if(r2.lt.0.) r2=0.
	if(r3.lt.0.) r3=0.

c    calculate albedo
	if(r1.eq.0) goto 190
	if(r2.eq.0) goto 190 
	a1=r3/r1*100
	a2=r3/r2*100
	goto 195

  190	a1=0
	a2=0
  195	continue

c    convert net radiation mv to W/m2
c	new net radiation sensor in 97 (old one from Boulder)	
	net=net*13.3
      
      if(jd_t.le. 366.985 .and. flag2.eq.0) year=1996
      if(flag2.eq.1) year=1997
      
	write(2,2002) year,jd_t,r1,r3,net
 2002   format(i5,f9.3,2f8.1,f7.1)
      
      if(jd_t.gt. 366.94) flag2=1
      
c     add one hour
      jd_t=jd_t + 0.0417      
      
  100   continue

 6000   continue
 7000   continue
	end

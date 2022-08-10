	program Klima

c ****************************************************************************
c       read Campell met data from the ETH camp in Greenland
c       change jd and time to jd_time
c       10 m tower, datalogger outside on tower (station klima)
c       
c       pyranometer: up # 12875, channel 1, close to mast (cal. 106.49)
c       pyranometer: down # 12798, channel 2, above down looking (cal. 105.89)
c       net radiometer: #92263 (+)=8.02, (-)=12.12, channel 3
c     
c     two RM-Young, two CS500 temp/hum on hourly logging (now in 98)

c       program : 5-22-97 Syno City 
c       modified in Hobart 8-20-97
c       modified in Syno city 5/23/98 
c       modified in Syno City 5/31/99
c ****************************************************************************

	character*20 in
	integer ich,year
	real yr,jd,time,a1,hour,r1,r2
	real licore1,licore2
	real t1(3),t2(3),hum1(3),hum2(3),wind1(3),wind2(3)
	real jd_t,net,wdir1,wdir2

c   Li-Core calibration coefficients (6-15-93)
	licore1=106.49
	licore2=105.89

	print *,'give input file name '
	read(*,'(a)') in
	open(1,file=in)

c	print *,'give name output '
c	read(*,'(a)') out1
	open(2,file='rad.dat')
c 2020	format('  Jul.Day  S1(up) S(dw) Alb1  net_rad')
c	write(2,2020)

c	print *,'give name output '
c	read(*,'(a)') out2
	open(3,file='tow_all.dat')

c	print *,'give name output '
c	read(*,'(a)') out2
	open(4,file='t_w_h.dat')


c	write(3,2030)
c	write(3,2031)   

	
	do 100 i=1,200000

      read(1,*,end=6000) ich,yr,jd,time,r1,r2,net,
     1  t1(1),t2(1),hum1(1),hum2(1),wind1(1),wind2(1),
     2  t1(2),t2(2),hum1(2),hum2(2),wind1(2),wind2(2),
     3  t1(3),t2(3),hum1(3),hum2(3),wind1(3),wind2(3),
     2  wdir1,wdir2

c     change hour to decimal hour
      hour=(time/100.)/24.
	jd_t=jd + hour

c    convert Li-Core mV to W/m2
	r1=r1*licore1
	r2=r2*licore2
	if(r1.lt.0.) r1=0.
	if(r2.lt.0.) r2=0.

c    calculate albedo
	if(r1.eq.0) goto 190
	if(r2.eq.0) goto 190 
	a1=r2/r1*100
	goto 195

  190	a1=0
	
  195	continue

c    convert net radiation mv to W/m2
c	new net radiation sensor in 97 (old one from Boulder)	
	if(net.ge.0) net=net*8.02
	if(net.lt.0) net=net*12.12
	      
	write(3,2032) yr,jd_t,r1,r2,a1,net,
     1  (t1(n),n=1,3),(t2(n),n=1,3),
     2  (hum1(n),n=1,3),(hum2(n),n=1,3),
     3  (wind1(n),n=1,3),(wind2(n),n=1,3),
     4  wdir1,wdir2

 2032   format(f5.0,f9.3,2f8.1,f6.1,f8.2,6f6.1,6f6.1,6f6.1,f8.1,f8.1)
      
	year=yr
	write(2,2021) year,jd_t,r1,r2,net
 2021 format(1x,I5,1x,F9.3,1x,2(F8.1,1x),1x,F7.1)

	write(4,2023) year,jd_t,wind1(1),wdir1,t1(1)
 2023 format(1x,I5,F9.3,3F9.2)

  100   continue
 6000   continue
	end

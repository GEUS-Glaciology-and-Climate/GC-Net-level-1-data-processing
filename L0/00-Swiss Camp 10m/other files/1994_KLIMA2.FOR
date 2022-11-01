	program Klima2

c ****************************************************************************
c       read Campell met data from the ETH camp in Greenland
c       change jd and time to jd_time
c       10 m tower, datalogger outside on tower (station klima)
c       pyranometer: up # 12875, channel 1, close to mast (cal. 106.49)
c       pyranometer: up # 12798, channel 2, above down looking (cal. 105.89)
c       pyronometer: down # 12880, channel 3, down (cal. 105.92)
c       net radiometer: #90094, channel 4
c       program : 6-15-93 Syno City
c
c       combine temp and rad in one file at 3 hours interval
c
c ****************************************************************************

	character*20 in
	integer ich,num
	real jd,time,licore(3),a1,a2,min,hour,xmin
	real wind,wmax,tair,jd_t,r(3),net,wdir,ta,taa

c   Li-Core calibration coefficients (6-15-93)
	licore(1)=106.49
	licore(2)=105.89
	licore(3)=105.92

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

c       print *,'give name output '
c       read(*,'(a)') out1
c        open(2,file='rad.dat')
c 2020   format('  Jul.Day  S1(up)  S2(up)  S(dw)   Alb1 Alb2  net_rad')
c        write(2,2020)

c       print *,'give name output '
c       read(*,'(a)') out2
c        open(3,file='tem_win.dat')
c 2030   format('  Julian    Wind   Wind   Wind   Temp')
c 2031   format('    Day      mean   max   dir     C')
c        write(3,2030)
c        write(3,2031)

	open(4,file='t_w_r.dat')
	
	do 100 i=1,100000

	read(1,*,end=6000) ich

	if(ich.eq.202) then
	backspace (1)
	read(1,*,end=6000) ich,jd,time,wind,wmax,tair,wdir

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


c    convert UUB thermister reading to temperature      
	ta=a+b*tair+c*(tair**2)+d*(tair**3)+e*(tair**4)+f*(tair**5)
					       
c        write(3,2032) jd_t,wind,wmax,wdir,ta
c 2032   format(f9.3,2f7.2,f7.1,f6.1)
	else
	endif
	
	xmin=0.
	num=0
	do 500 ii=1,10
	read(1,*,end=7000) ich,r(1),r(2),r(3),net

	num=num+1

	if(ich.eq.202) then
	backspace (1)
	goto 100
	else
	endif

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
	do 200 l=1,3
	r(l)=r(l)*licore(l)
  200   continue        

c    calculate albedo
	if(r(1).eq.0) goto 190
	if(r(2).eq.0) goto 190 
	a1=r(3)/r(1)*100
	a2=r(3)/r(2)*100
	goto 195

  190   a1=0
	a2=0
  195   continue

c    convert net radiation mv to W/m2
	net=net*13.3

c        write(2,2002) jd_t,(r(l),l=1,3),a1,a2,net
c 2002   format(f9.3,3f8.1,2f5.0,f7.1)
  
	if(num.eq.1) then
	taa=ta+273.15
	if(taa.gt.273.15) taa=273.15
	taa=(0.0000000567*0.97*(taa**4))+net
	
	write(4,2042) jd_t,wind,wmax,wdir,ta,
     1   (r(l),l=1,3),a1,a2,net,taa
 2042   format(f9.3,2f7.2,f7.1,f6.1,3f8.1,2f6.0,2f7.1)
	else
	endif	

  500   continue

  100   continue

 6000   continue
 7000   continue
	end

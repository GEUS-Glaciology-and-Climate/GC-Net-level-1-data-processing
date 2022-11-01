	program Klima

c ****************************************************************************
c       read Campell met data from the ETH camp in Greenland
c       change jd and time to jd_time
c       10 m tower, datalogger outside on tower (station klima)
c       pyranometer: up # 12875, channel 1, close to mast (cal. 106.49)
c       pyranometer: up # 12798, channel 2, above down looking (cal. 105.89)
c       pyronometer: down # 12880, channel 3, down (cal. 105.92)
c	net radiometer: #90094, channel 4
c       program : 6-15-93 Syno City
c ****************************************************************************

	character*20 in,out1
	integer ich
	real jd,time,licore(3),a1,a2,min,hour
	real wind,wmax,tair,jd_t,r(3),net,wdir,ta

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

	print *,'give name output '
	read(*,'(a)') out1
	open(2,file=out1)

	do 100 i=1,100000
	
   	read(1,*,end=6000) ich,jd,time,wind,r(1),r(2),r(3),net,wmax,tair,
     1                     wdir

c    change jd and time in real
	if(time.eq.0) then
	time=0.
	goto 150
	else
	endif
	min=time-(aint(time/100.))*100.
	if(min.eq.0) goto 160
	min=min/60.
 160	hour=aint(time/100.)
	hour=(hour+min)/24.
  150   continue
	jd_t=jd + hour

c    convert UUB thermister reading to temperature      
	ta=a+b*tair+c*(tair**2)+d*(tair**3)+e*(tair**4)+f*(tair**5)

c    convert Li-Core mV to W/m2
	do 200 l=1,3
	r(l)=r(l)*licore(l)
  200   continue        

c    calculate albedo
	a1=r(3)/r(1)
	a2=r(3)/r(2)

c    convert net radiation mv to W/m2
	net=net*13.3

	write(2,2001) jd_t,ta,wind,wmax,wdir,(r(l),l=1,3),a1,a2,net
 2001   format(f9.3,f6.1,2f8.3,f8.1,3f7.1,2f5.2,f7.1)
     
  100   continue

 6000   continue
	end

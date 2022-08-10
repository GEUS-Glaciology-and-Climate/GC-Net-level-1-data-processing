	program RAD

c ****************************************************************************
c       read Campell met data from the Humboldt camp in Greenland
c       change jd and time to jd_time
c       pyronometer: down # 12880, channel 3, down (cal. 105.92)
c       net radiometer: #95117
c       program : 8-5-96
c ****************************************************************************

	character*20 in
	real jd,time,sin,sout,min,hour
	real jd_t,net,ti1,ta1,ta2,lout,lnet,lin,ta
	
	print *,'give input file name '
	read(*,'(a)') in
	open(1,file=in)

c	print *,'give name output '
c	read(*,'(a)') out1
	open(2,file='rad_all.dat')
 2020	format('  Jul.Day  S1(up) S1(up) S(dw) net_rad lnet lout lin')
	write(2,2020)

	do 100 i=1,100000

	read(1,*,end=6000) ich,jd,time,sin,sout,net,ti1,ta1,ta2

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

c    convert Li-Core mV to W/m2
	sin=sin*200
	sout=sout*200

c    convert net radiation mv to W/m2
	if(net.gt.0) net=net*9.29
	if(net.lt.0) net=net*11.62

c    calculate the longwave out radiaton from air temp
	ta=(ta1+ta2)/2	
	lout=((ta+273.15)**4.)*0.97*.0000000567	
	lout=lout*(-1)

c    calculate the net longwave radiation
	lnet=(sin-sout)*(-1)+net

c    calculate the longwave incoming radiation
  	lin=lnet-lout	

	write(2,2002) jd_t,sin,sin,sout,net,lnet,lout,lin
 2002   format(f9.3,3f8.1,4f7.1)
  
  500   continue

  100   continue

 6000   continue
 7000   continue
	end

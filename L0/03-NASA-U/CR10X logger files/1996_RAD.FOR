	program RAD

c ****************************************************************************
c       read Campell met data from the NASA-U camp in Greenland
c       change jd and time to jd_time
c       pyronometer: down # 12880, channel 3, down (cal. 105.92)
c       net radiometer: #95094
c       program : 8-5-96
c ****************************************************************************

	real jd,sin,sout,sta,yr
	real jd_t,net,ti1,ta1,ta2,lout,lnet,lin,ta
	
c	print *,'give input file name '
c	read(*,'(a)') in
	open(1,file='nasa_U.dat')

c	print *,'give name output '
c	read(*,'(a)') out1
	open(2,file='rad_all.dat')
 2020	format('  Jul.Day  S1(up) S1(up) S(dw) net_rad lnet lout lin')
	write(2,2020)

	do 100 i=1,100000

	read(1,*,end=6000) sta,yr,jd,sin,sout,net,ta1,ta2

	if(sin.ge.2000) goto 100
	if(ta1.ge.100) goto 100
	if(net.gt.2000) goto 100
	if(sin.gt.2000) goto 100

c    change jd and time in real
c	if(time.eq.0) then
c	hour=0.
c	goto 150
c	else
c	endif

c	min=time-(aint(time/100.))*100.
c	if(min.eq.0) goto 160
c	min=min/60.
c160    hour=aint(time/100.)
c	hour=(hour+min)/24.
c 150    continue
	jd_t=jd + hour

c    convert Li-Core mV to W/m2
c	sin=sin*200
c	sout=sout*200

c    convert net radiation mv to W/m2
c	if(net.gt.0) net=net*9.29
c	if(net.lt.0) net=net*11.62

c    calculate the longwave out radiaton from air temp
	ta=(ta1+ta2)/2	
	lout=((ta+273.15)**4.)*0.97*.0000000567	
	lout=lout*(-1)

c    calculate the net longwave radiation
	lnet=(sin-sout)*(-1)+net

c    calculate the longwave incoming radiation
  	lin=lnet-lout	

	if(lnet.ge.2000) goto 100
	if(lout.ge.2000) goto 100
	if(lin.ge.2000) goto 100

	write(2,2002) jd,sin,sin,sout,net,lnet,lout,lin
 2002   format(f9.3,3f9.1,4f8.1)
  
  500   continue

  100   continue

 6000   continue
 7000   continue
	end

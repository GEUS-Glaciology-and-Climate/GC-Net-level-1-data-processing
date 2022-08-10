	program AWS

c ****************************************************************************
c       read Campell met data from the GITS camp in Greenland
c       change jd and time to jd_time
c       pyronometer: down # 12880, channel 3, down (cal. 105.92)
c       net radiometer: #95095
c       program : 9-3-96
c ****************************************************************************

c	character*20 in
	real jd,time,sin,sout,min,hour
        real jd_t,net,ti1,ti2,ta1,ta2,hum1,hum2,w1,w2,
     &  wdir1,press,sh1,s1,sa1
	
c	print *,'give input file name '
c	read(*,'(a)') in
	open(1,file='git95-96.dat')

	print *,'aws GITS compiling '
c	read(*,'(a)') out1
	open(2,file='gi95_96.dat')

c 2020   format('  Jul.Day  S1(up) S1(up) S(dw) net_rad lnet lout lin')
c        write(2,2020)


         sa1=0.

c    read first line and get the original snow height, make T corrections

        read(1,*,end=6000) ich,jd,time,sin,sout,net,ti1,ti2,ta1,ta2,
     &  hum1,hum2,w1,w2,wdir1,press,sh1

c    correct snow height sensor data with temperature
        sh1=sh1*sqrt(((ta2+ta2)/2+273.15)/273.15)

        s1=sh1

        backspace(1)
           
	do 100 i=1,100000

        read(1,*,end=6000) ich,jd,time,sin,sout,net,ti1,ti2,ta1,ta2,
     &  hum1,hum2,w1,w2,wdir1,press,sh1



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
	if(net.gt.0) net=net*9.35
	if(net.lt.0) net=net*11.66

c    correct snow height sensor data with temperature
        sh1=s1-sh1*sqrt(((ta2+ta2)/2+273.15)/273.15)
    
        if(sh1.ge.(sa1+0.12) .or.sh1.lt.(sa1-0.2)) sh1=sa1
	
c     correction for offset (+800) for pressure
	press=press+800

        write(2,2002) jd_t,sin,sout,net,ta1,ta2,hum1,hum2,w1,w2,
     &  wdir1,press,sh1,sh1,ti1,ti2
 2002   format(f9.3,3f8.1,8f8.1,2f6.3,2f8.1)

	sa1=sh1
  
  500   continue

  100   continue

 6000   continue
 7000   continue
	end

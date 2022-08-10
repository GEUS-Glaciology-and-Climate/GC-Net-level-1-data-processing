	program AWS

c ****************************************************************************
c       read Campell met data from the NASA_U camp in Greenland
c       change jd and time to jd_time
c       pyronometer: down # 12880, channel 3, down (cal. 105.92)
c       net radiometer: #95117
c       program : 9-3-96
c ****************************************************************************

c	character*20 in
	real jd,time,sin,sout,min,hour
        real jd_t,net,ti1,ta1,ta2,hum1,hum2,w1,w2,
     &  wdir1,press,sh1,sh2,s1,s2,sa1,sa2
	
c	print *,'give input file name '
c	read(*,'(a)') in
	open(1,file='nas95-96.dat')

	print *,'aws NASA_U compiling '
c	read(*,'(a)') out1
	open(2,file='na95_96.dat')

c 2020   format('  Jul.Day  S1(up) S1(up) S(dw) net_rad lnet lout lin')
c        write(2,2020)


         sa1=0.
         sa2=0.

c    read first line and get the original snow height, make T corrections

        read(1,*,end=6000) ich,jd,jd_t,sin,sout,net,ta1,ta2,
     &  hum1,hum2,w1,w2,wdir1,press,sh1,sh2,ti1

c    correct snow height sensor data with temperature
c        sh1=sh1*sqrt(((ta2+ta2)/2+273.15)/273.15)
c        sh2=sh2*sqrt(((ta2+ta2)/2+273.15)/273.15)
	
        s1=sh1
        s2=sh2

        backspace(1)
           
	do 100 i=1,100000

        read(1,*,end=6000) ich,jd,jd_t,sin,sout,net,ta1,ta2,
     &  hum1,hum2,w1,w2,wdir1,press,sh1,sh2,ti1

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
c150    continue
c	jd_t=jd + hour

c    convert Li-Core mV to W/m2
c	sin=sin*200
c	sout=sout*200

c    convert net radiation mv to W/m2
c	if(net.gt.0) net=net*9.29
c	if(net.lt.0) net=net*11.62

c    correct snow height sensor data with temperature
c        sh1=s1-sh1*sqrt(((ta2+ta2)/2+273.15)/273.15)
c        sh2=s2-sh2*sqrt(((ta2+ta2)/2+273.15)/273.15)
 
	sh1=s1-sh1
	sh2=s2-sh2
	   
        if(sh1.ge.3. .or.sh1.lt.-2.) sh1=sa1
        if(sh2.ge.3. .or.sh2.lt.-2.) sh2=sa2
	
c    correction for offset (+800) for pressure
c	press=press+800

        write(2,2002) jd_t,sin,sout,net,ta1,ta2,hum1,hum2,w1,w2,
     &  wdir1,press,sh1,sh2,ti1
 2002   format(f9.3,3f8.1,8f8.1,2f6.3,f8.1)

	sa1=sh1
	sa2=sh2
  
  500   continue

  100   continue

 6000   continue
 7000   continue
	end

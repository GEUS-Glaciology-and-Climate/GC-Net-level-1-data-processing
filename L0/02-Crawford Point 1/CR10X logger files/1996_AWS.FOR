	program AWS

c ****************************************************************************
c       read Campell met data from the Crawfort camp in Greenland
c       change jd and time to jd_time
c       net radiometer: #95093
c       program : 9-3-96
c ****************************************************************************

c	character*20 in
	real jd,time,sin,sout,min,hour
        real jd_t,net,ta1,ta2,hum1,hum2,w1,w2,
     &  wdir1,wdir2,press,sh1,sh2,s1,s2,sa1,sa2,ti(10)
	
c	print *,'give input file name '
c	read(*,'(a)') in
	open(1,file='cra95-96.dat')

	print *,'aws Crawfort compiling '
c	read(*,'(a)') out1
	open(2,file='cr95_96.dat')

         sa1=0.
         sa2=0.

c    read first line and get the original snow height, make T corrections

        read(1,*,end=6000) ich,jd,time,sin,sout,net,ta1,ta2,
     &  hum1,hum2,w1,w2,wdir1,wdir2,press,sh1,sh2,(ti(k),k=1,10)

c    correct snow height sensor data with temperature
        sh1=sh1*sqrt(((ta1+ta2)/2+273.15)/273.15)
        sh2=sh2*sqrt(((ta1+ta2)/2+273.15)/273.15)

        s1=sh1
        s2=sh2

        backspace(1)
           
	do 100 i=1,100000

        read(1,*,end=6000) ich,jd,time,sin,sout,net,ta1,ta2,
     &  hum1,hum2,w1,w2,wdir1,wdir2,press,sh1,sh2,(ti(k),k=1,10)

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

c    correct snow height sensor data with temperature
        sh1=s1-sh1*sqrt(((ta1+ta2)/2+273.15)/273.15)
        sh2=s2-sh2*sqrt(((ta1+ta2)/2+273.15)/273.15)
    
        if(sh1.ge.(sa1+0.15) .or. sh1.lt.(sa1-0.2)) sh1=sa1
        if(sh2.ge.(sa2+0.15) .or. sh2.lt.(sa2-0.2)) sh2=sa2
	
c    correction for offset (+800) for pressure
c	press=press+800

        write(2,2002) jd_t,sin,sout,net,ta1,ta2,hum1,hum2,w1,w2,
     &  wdir1,wdir2,press,sh1,sh2,(ti(k),k=1,10)
 2002   format(f9.3,3f8.1,9f8.1,2f6.3,10f8.1)

	sa1=sh1
	sa2=sh2
  
  500   continue

  100   continue

 6000   continue
 7000   continue
	end

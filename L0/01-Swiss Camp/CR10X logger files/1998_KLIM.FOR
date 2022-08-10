	program Klima

c ****************************************************************************
c       read Campell met data from the ETH camp in Greenland
c       change jd and time to jd_time

c ****************************************************************************

	character*20 in
	integer ich,year
	real yr,jd,time,dd(22),jd_t
		

c   Li-Core calibration coefficients (6-15-93)
	licore1=106.49
	licore2=105.89

	print *,'give input file name '
	read(*,'(a)') in
	open(1,file=in)
				  
	open(4,file='t_w_h.dat')

		
	do 100 i=1,200000

	yr=1998
      read(1,*,end=6000) ich,jd,time,(dd(k),k=1,22)
  

c     change hour to decimal hour
      hour=(time/100.)/24.
	jd_t=jd + hour

	year=yr

	if(jd_t.lt.145.75) then
	write(4,2023) year,jd_t,dd(18),dd(20),dd(12)
 2023 format(1x,I5,F9.3,3F9.2)
	else
	endif

  100   continue
 6000   continue
	end

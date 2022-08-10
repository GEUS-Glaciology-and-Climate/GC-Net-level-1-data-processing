	program Summit_Profile

c ****************************************************************************
c       reads Summit profile data and converts to JD_decimal_hour 
c	  combines the two profile data files by checking the time stamp
c	  1. profile data with 3 temp levels in the air
c	  2. profile data with surface temperature data and snow height
c 
c       Boulder 6 March 2003 

c ****************************************************************************

c	character*20 in
	integer n,nn,m
	real num,jd,hour,data(50000,11),data1(50000,3)
	real jd_h1(50000),jd_h2(50000),min,h

c	print *,'give input file name '
c	read(*,'(a)') in
c	open(1,file=in)


	open(1,file='PRO_all.dat')
	open(2,file='PRO2_all.dat')
	open(3,file='profile.dat')
	
     	n=0

	do 100 i=1,200000
	
	read(1,*,end=6000) num,jd,hour,(data(i,k),k=1,11)
	n=n+1
	
c     change hour to decimal hour and decimal minute
      h=hour/100
	min=hour - (INT(h)*100)
	h=INT(h)+(min/60.)
	jd_h1(i)=jd+(h/24.)
      
  100 continue
 6000 continue

	nn=0

	do 200 i=1,200000
	
	read(2,*,end=7000) num,jd,hour,(data1(i,k),k=1,3)
	nn=nn+1
	
c     change hour to decimal hour and decimal minute
      h=hour/100
	min=hour - (INT(h)*100)
	h=INT(h)+(min/60.)
	jd_h2(i)=jd+(h/24.)
      
  200 continue
 7000 continue

c	if(n.ge.nn) n=nn
	m=0
c	n=nn

	do 300 i=1,n-50
  350	if(jd_h1(i+m).eq.jd_h2(i)) then
      goto 500
	else
	m=m+1
	n=n-1
	goto 350
	endif 
	

  500	write(3,2003) jd_h1(i+m),(data(i+m,k),k=1,11),
     1              jd_h2(i),(data1(i,k),k=1,3)
 2003 format(1x,f9.5,3f8.2,3f8.2,3f9.3,2f9.2,1x,f9.5,f8.2,f9.3,f9.2)
  300	continue
      

  
	end

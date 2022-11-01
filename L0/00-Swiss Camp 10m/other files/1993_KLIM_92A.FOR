	program Klim_92a

c ****************************************************************************
c       reads met.dat for 92-93 and adds the year in front and convert hour to decimal hour 
c       modified in Hobart 8-20-97

c     modified to format for long time record
c ****************************************************************************

	character*20 in
	integer year,flag1
	real jd,data(3),hour

	print *,'give input file name '
	read(*,'(a)') in
	open(1,file=in)


	open(2,file='t_92-93.dat')

       flag1=0
	
	do 100 i=1,200000
	read(1,*,end=6000) jd,(data(k),k=1,3)

	
c     change hour to decimal hour
      hour=(jd-INT(jd))*100/24
      jd=INT(jd)+hour
      
      if(jd .le. 365.875 .and. flag1 .eq. 0) year=1992
      if(flag1 .eq. 1) year=1993
      
      data(2)=999.
      
	write(2,2002) year,jd,(data(k),k=1,3)
 2002 format(1x,i5,f9.3,3f9.2)

      
      if(jd .ge. 365.8) flag1=1
      
  100 continue
 6000 continue
	end

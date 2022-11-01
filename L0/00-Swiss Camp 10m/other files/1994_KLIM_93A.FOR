	program Klim_93a

c ****************************************************************************
c       reads met.dat for 93-94 and adds the year in front  
c       modified in Hobart 8-20-97

c     modified to format for long time record
c ****************************************************************************

	character*20 in
	integer year,flag1
	real jd,data(4)

	print *,'give input file name '
	read(*,'(a)') in
	open(1,file=in)


	open(2,file='t_93-94.dat')

       flag1=0
	
	do 100 i=1,200000
	read(1,*,end=6000) jd,(data(k),k=1,4)

	
      if(jd .le. 365.875 .and. flag1 .eq. 0) year=1993
      if(flag1 .eq. 1) year=1994
      
	write(2,2002) year,jd,data(1),data(3),data(4)
 2002 format(1x,i5,f9.3,3f9.2)

      
      if(jd .ge. 365.8) flag1=1
      
  100 continue
 6000 continue
	end

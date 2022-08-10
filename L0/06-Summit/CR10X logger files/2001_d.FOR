 	program aws_time_slice

c	reads monthly AWS file and write out ALL DATA for a specified time period
 
c	Boulder 3-12.2003

	character*20 in1,out
      integer num,year,n
	real r(37),jd,jd1,jd2
                          
                                    
	print *,'give file name of AWS file'
	read(*,'(a)') in1
	open(1,file=in1)
	
	print *,'give name for out file'
	read(*,'(a)') out
	open(3,file=out)

	print *,'- program working -'
      
	year1=2000
	JD1=121
	JD2=244
	n=0
	          
      
	do 100 k=1,1000000
	n=n+1
	print *,n
	read(1,*,end=5000) num,year,jd,(r(i),i=1,37)
	if(year.ne.2000) goto 100
	if(year.gt.2000) goto 100
	if(jd.lt.jd1) goto 100
	if(jd.gt.jd2)goto 100  

      write(3,3001) num,year,jd,(r(i),i=1,37)
 3001 format(i3,1x,i5,1x,f10.4,33f8.2,4f10.0) 

  100 continue
       
  
 5000	continue
      print *,n

	end

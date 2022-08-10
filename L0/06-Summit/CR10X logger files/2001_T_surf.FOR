 	program Temp_surf

c	Read Summit 2000-2002 profile tower data and extrapolates the
c	temp profile with liner approach to surface temp. for all three combination.
	
 
c	Boulder 3-12.2003

	character*20 in1,out
      integer year,jd,time
	real jdt,r(20),m1,m2,m3,b1,b2,b3,t01,t02,t03,d1,d2,d3
                          
                                    
	print *,'give file name of AWS file'
	read(*,'(a)') in1
	open(1,file=in1)
	
	print *,'give name for out file'
	read(*,'(a)') out
	open(3,file=out)

	print *,'- program working -'
      
	         
      
	do 100 k=1,1000000
	read(1,*,end=5000) year,jd,jdt,time,(r(i),i=1,20)

	if(r(1).eq.999) goto 100
	if(r(2).eq.999) goto 100
	if(r(3).eq.999) goto 100
	if(r(11).eq.999) goto 100
	if(r(1).eq.r(2)) goto 100
	if(r(1).eq.r(3)) goto 100
	if(r(2).eq.r(3)) goto 100
	

	m1=(r(15)-r(14))/(r(2)-r(1))
	m2=(r(16)-r(14))/(r(3)-r(1))
	m3=(r(16)-r(15))/(r(3)-r(2))


	b1=r(14)-m1*r(1)
	b2=r(14)-m2*r(1)
	b3=r(15)-m3*r(2)
	
	t01=-b1/m1
	t02=-b2/m2
	t03=-b3/m3	

	d1=r(11)-t01
	d2=r(11)-t02
	d3=r(11)-t03

      write(3,3001) year,jdt,r(1),r(2),r(3),r(11),t01,t02,t03,d1,d2,d3
 3001 format(1x,i4,1x,f10.4,10f9.3) 

  100 continue
       
  
 5000	continue
      
	end

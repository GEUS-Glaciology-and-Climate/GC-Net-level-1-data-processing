	Program AWS_Tunu
c     reads AWS data file and combines in one data line
c     calibration for the radiometers will be included
c     Tunu 5-27-96

	Real in(17),in1(17),in2(17),c4,c5
c       Character*20 in1,out1
	
c       print *,'give input file '
c       read(*,'(a)') in1
	open(1,file='tunu.dat')

c       print *,'give outfile '
c       read(*,'(a)') out1
	open(2,file='tunu_aws.dat')


c   calibration coefficients for li-core radiometer
	c4=1
	c5=1

   
c  net rad: (+) 9.43, (-) 11.66 


	print *,'compiling: reading tunu.dat file'
      
c   read radiation file
	do 200 k=1,100000
	read(1,*,end=5000) (in(ii),ii=1,17)

	if(in(1).eq.61) then
	do 300 ii=1,17
	in1(ii)=in(ii)
 300    continue       
	endif

	if(in(1).eq.62) then
	do 400 ii=1,17
	in2(ii)=in(ii)
 400    continue       
	endif

	if(in1(3).eq.in2(3)) then
	if(in1(7).gt.0) in(7)=in(7)*9.43
	if(in1(7).le.0) in(7)=in(7)*11.66
	in1(4)=in1(4)*c4
	in1(5)=in1(5)*c5
	write(2,2000) (in1(ii),ii=2,17),(in2(ii),ii=4,17) 
 2000   format(f5.0,f6.0,28f9.2)            
	endif
  
  200   continue

 5000   continue
	end

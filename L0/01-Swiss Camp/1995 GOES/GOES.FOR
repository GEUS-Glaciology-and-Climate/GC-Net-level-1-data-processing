	Program aero
c	Split data set to 10 min and hourly values
c	Muliply with calibration coefficients
c	Thule 6-4-95

	Integer nt
	Real in(30),c(30),t
	Character*20 in1,out1,out2
	
	print *,'give input file '
	read(*,'(a)') in1
	open(1,file=in1)

	print *,'give outfile for 10 min values '
	read(*,'(a)') out1
	open(2,file=out1)

	print *,'give outfile for hourly values'
	read(*,'(a)') out2
	open(3,file=out2)

	do 100 i=1,30
	c(i)=1
  100	continue

c   calibration coefficients for radiometer
	c(5)=111.7318
	c(6)=124.224
	c(7)=113.766
	c(8)=109.89
	c(9)=246.9135
	c(10)=116.279
	c(11)=13.2
	c(12)=5.405
	c(24)=10
	c(26)=100
	c(27)=100

	do 200 k=1,100000
	read(1,*,end=5000) (in(ii),ii=1,30)
	
	do 300 i=1,30
	in(i)=in(i)*c(i)
  300	continue


	nt=(int(in(4)/100))*100
	t=in(4)-nt

 2000	format(4f6.0,26(f7.1,1X))

	if(t.eq.58) then
	write(3,2000) (in(ii),ii=1,30)
	else
	write(2,2000) (in(ii),ii=1,30)
	endif

  200	continue

 5000	continue
	end
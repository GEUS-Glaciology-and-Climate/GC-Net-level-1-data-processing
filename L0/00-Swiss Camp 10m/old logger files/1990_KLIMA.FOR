	program Klima

c ****************************************************************************
c       read met data file from the ETH camp in Greenland: 1990 and 1991
c       10 m tower, datalogger outside on tower (station klima)
c	temp, wind, wind_dir, pressure, relative humidity
c
c       program : 11-1-94: Boulder
c ****************************************************************************

	character*20 in
	integer day,month,year,hour,min
	real p(5),px(5),jd,xhour,xjd

	print *,'give input file name '
	read(*,'(a)') in
	open(1,file=in)


c	print *,'give name output '
c	read(*,'(a)') out2
	open(3,file='tem_win.dat')

	jd=152
	xjd=0

	do 500 ii=1,10000

	do 50 kk=1,5
	px(kk)=0.
   50	continue
	
	n=1

	do 100 i=1,18

	read(1,1001,end=6000) day,month,year,hour,min,(p(l),l=1,5)
 1001	format(i2,1x,i2,1x,i2,1x,i2,1x,i2,1x,5f9.2)

	do 150 kk=1,5
	px(kk)=px(kk)+p(kk)
  150	continue
  100	continue

	do 250 kk=1,5
	px(kk)=px(kk)/18.
  250	continue

	if(hour.eq.0) jd=jd+1
	xhour=(float(hour))/100

	xjd=jd+xhour

	write(3,2001) xjd,(px(l),l=1,3)
 2001	format(f9.2,5f9.2)


  500	continue

 6000   continue
	end

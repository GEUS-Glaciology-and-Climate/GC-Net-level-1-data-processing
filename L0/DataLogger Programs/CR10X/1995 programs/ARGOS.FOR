	Program Argos
c	Converts ARGOS binary data to Campbell measurements
c	Sondy 5-30-95, Boulder 7-3-95

	Real in(16),binval(16),val(16),nval(16)
	Real out(16)
	integer id,sta,da(7),nn
	Character*20 in1
	Character*1 num(20)
	
	print *,'give input file '
	read(*,'(a)') in1
	open(1,file=in1)

	open(2,file='narvik.dat')
	open(3,file='gits.dat')
	open(4,file='hum.dat')	


c   loop for x data transmissions
   15	do 25 ii=1,1000000

c   read first character of id: 0(1463)
	read(1,1001,end=5000) (num(kk),kk=1,20)
	if(num(1).eq.'0'.and. num(2).eq.'1') then
	backspace(1)
	read(1,*) id,sta
        goto 30
        else
	if(num(7).eq.'1'.and.num(8).eq.'9') then
	backspace(1)
	goto 30
	else
	endif
	goto 15
	endif
 1001	format(20a)

   30	read(1,1002,end=5000) (da(m),m=1,7),(val(n),n=1,4)
   	read(1,1003,end=5000) (val(n),n=5,8)
	read(1,1003,end=5000) (val(n),n=9,12)
	read(1,1003,end=5000) (val(n),n=13,16)
 1002	format(6x,i4,6(1x,i2),4(f11.0,2x))
 1003	format(28x,4(f11.0,2x))

c   data transmission of 16 data points
	do 50 i=1,16

	binval(i)=val(i)
	Do 100 k=1,16
	In(k)=0.
	if(val(i).ge.(2**(16-k))) then
	In(k)=1.
	val(i)=binval(i) - (2**(16-k))
	binval(i)=val(i)
	else
	endif
  100	continue

	nval(i)=0
	Do 200 k=4,16
	if(in(k).eq.1) then
	nval(i)=nval(i) + (2**(16-k))
	else
	endif
  200	continue	

	if(In(1).eq.1) nval(i)=nval(i)*(-1)
	if(In(2).eq.0.and.In(3).eq.0) out(i)=nval(i)
	if(In(2).eq.0.and.In(3).eq.1) out(i)=nval(i)/10
	if(In(2).eq.1.and.In(3).eq.0) out(i)=nval(i)/100
	if(In(2).eq.1.and.In(3).eq.1) out(i)=nval(i)/1000

   50	continue
	if(sta.eq.24739) nn=2
	if(sta.eq.24740) nn=3
	if(sta.eq.24741) nn=4
	
	write(nn,2001) (da(m),m=1,7),sta,(out(n),n=1,16)
 2001	format(i4,1x,6(i2,1x),I7,f6.0,f7.0,14(f10.3))

   25 	continue	

 5000	continue
	end
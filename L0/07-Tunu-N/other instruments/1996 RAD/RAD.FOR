	Program Rad
c       Inserts calibration coefficients for Epply rad
c     Calculates the Total Hemispheric Radiation (THR)
c     Tunu 6-19-96

	Real in(12),c(7),ineddy(10)
	Real Ft,Fk,Fc,Bc,Ftd,Fn,Fp,Fh
	Real Vt,Vb,Vn,Vc,Vh,Vl,mVc,mVh,mVl,Th,Tl
	Real THR,Q,LTHR
	Real wind,corr,den0,den1,den2,den
c	Character*20 in1,out1
	
c	print *,'give input file '
c	read(*,'(a)') in1
	open(1,file='rad.dat')

c	print *,'give outfile '
c	read(*,'(a)') out1
	open(2,file='rad.out')

c  Open eddy fulx file for wind speed, and go to JD 139, 1500
	open(3,file='d:\greenl\eddy\eddy.dat')

	do 50 ii=1,697
	read(3,*)
  50	continue

c   calibration coefficients for radiometer
	c(4)=109.89
	c(5)=113.766
	c(6)=246.9135
c  net rad: (+) 9.43, (-) 11.66 

	
c   calibration coefficients for THR
      Ft  = 0.10567
      Fk  = 1.02601
      Fc  = 0.99239
      Bc  = 0.53147
      Ftd = 1.00967
      Fh  = 0.96631
      Fp  = 9.52258
      Fn  =11.8597

	print *,'compiling: reading rad.dat and eddy.dat files'
      
 2001   format(' ID ',' jd ','  hour  ','  s(in)  ','  s(out) ',
     &  '  l(in) ','  net ','  net_thr ','all_in ','l_thr(out) ')
	write(2,2001)

c   read radiation file
	do 200 k=1,100000
	read(1,*,end=5000) (in(ii),ii=1,12)
	      
c   read eddy file for wind speed
        read(3,*,end=5000) (ineddy(ll),ll=1,10)
	wind=ineddy(9)   

	Vt=in(8)
	Vb=in(9)                       
	Vc=in(10)
	Vh=in(11)
	Vl=in(12)
	
	Tc=Vc*Fc+Bc                     
		 
	mVc=(Tc-273.15)*58.327591 +
     & ((Tc-273.15)**2)*5.3761106E-2 -
     & ((Tc-273.15)**3)*5.2870656E-5 +
     & ((Tc-273.15)**4)*1.535284E-8 
					   
	mVh=mVc + 1000*Vh
	mVl=mVc + 1000*Vl
	   
	Th=mVh*1.7022525E-2       - 
     &     (mVh**2)*2.209724E-7   +
     &     (mVh**3)*5.4809314E-12 -
     &     (mVh**4)*5.7669892E-17 +
     &      273.15
     
	Tl=(mVl)*1.7022525E-2     - 
     &     (mVl**2)*2.209724E-7   +
     &     (mVl**3)*5.4809314E-12 -
     &     (mVl**4)*5.7669892E-17 +
     &      273.15

c   Total Hemispheric Radiation upper Flux
      THR=((Vt*Ft+Vc*Fc+Bc)**4)*5.9812E-8 - 
     &     Ftd*(Th**4)*3.1152E-9 +
     &     Vt*Fk*11.216 +
     &     (Vt*Ft+Vc*Fc+Bc-Th)*Fh*3.5657 
		   
c   Net Radation 
      Vn=Vt-Vb
      if(Vn.ge.0) Q=Vn*Fp
      if(Vn.lt.0) Q=Vn*Fn      
      
      do 300 i=4,6
	in(i)=in(i)*c(i)
  300   continue

	if(in(7).gt.0) in(7)=in(7)*9.43
	if(in(7).le.0) in(7)=in(7)*11.66

c Wind correction assuming wind speed is monitored, and there is no
c    ventilator present (testing prgrm with constant 5 m/s wind)
c    the next line must be replaced with actual wind speeds.

	corr=1.0
	if(Q.gt.0) then
	   den0=wind**(0.65)    
	   den1=0.041*(1-2**(-den0))
	   den2=(0.0008*wind)/(.01+wind**2)
	   den=1-den1-den2
	    if(den.eq.0.) goto 100      
	   corr=1.0/den
	endif

 100    if(Q.lt.0) corr=1.0/(1.01-0.022*(1-1.28**(-wind)))

c Correcting THR for wind
	THR=THR*corr
	
	Q=Q*corr

	LTHR=THR-in(4)

 2000   format(f4.0,f6.0,f6.0,7(f7.1,1X))
	write(2,2000) (in(ii),ii=1,7),Q,THR,LTHR
  200   continue

 5000   continue
	end

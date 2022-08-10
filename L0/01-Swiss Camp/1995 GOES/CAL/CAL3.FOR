c -------------------------------------------------------------------------
c                                                       Jason Box
c program: CAL3.FOR
c this is the mega program to perform relative calibration for temperature
c humidity and wind sensors from greenland 1994 data.
c -------------------------------------------------------------------------
      integer hcount
      real t1,t2,t3,h1,h2,h3,w1,w2,w3,dh21,dh23,
     * dw31,dw32,ph21,ph23,pw31,pw32,hsum1,hsum2,
     * t1mult1,t2mult1,t3mult1,t1mult2,t2mult2,
     * t3mult2,t1mult3,t2mult3,t3mult3,t1mult4,t2mult4,t3mult4,
     * wcount1,wcount2,w1sum1,w1sum2,w2sum1,w2sum2,
     * w1mult1,w1mult2,w2mult1,w2mult2,
     * hmult1,hmult2

      open(unit=1,file='cal3.dat',status='old')
      open(unit=2,file='dt3_1.dat')
      open(unit=3,file='dt3_2.dat')
      open(unit=4,file='dt3_3.dat')
      open(unit=5,file='dt3_4.dat')
      open(unit=6,file='dwnd_1.dat')
      open(unit=7,file='dwnd_2.dat')
c      open(unit=66,file='wnd_dev.dat')
c      open(unit=11,file='dhum_all.dat')
      open(unit=14,file='cal3.d',status='old')
      open(unit=15,file='tem_cor.dat')
c      open(unit=16,file='wnd_cor.dat')
      open(unit=20,file='coef.dat')
      open(unit=33,file='tem_dev.dat')
c      open(unit=88,file='hum_dev.dat')
c      open(unit=90,file='hum_cor.dat')
      open(unit=89,file='fwtc_dev.dat')
c ------- temp      
      count=0
      count1=0
      count2=0
      count3=0
      count4=0
      sum1a=0
      sum1b=0
      sum1c=0      
      sum2a=0
      sum2b=0      
      sum2c=0      
      sum3a=0
      sum3b=0
      sum3c=0
      sum4a=0
      sum4b=0
      sum4c=0
      sum4d=0
      t1mult1=0
      t2mult1=0
      t3mult1=0
      t1mult2=0
      t2mult2=0
      t3mult2=0
      t1mult3=0
      t2mult3=0
      t3mult3=0
      t1mult4=0
      t2mult4=0
      t3mult4=0

c ------- wind
      w1count1=0
      w1count2=0
      w1sum1=0
      w1sum2=0
      w2count1=0
      w2count2=0
      w2sum1=0
      w2sum2=0
      w1mult1=0
      w2mult2=0
      w1mult2=0
      w2mult1=0

      do 100 i=1,30000 
       read(1,*,end=99) jd,tm,t1,t2,t3,h1,h2,h3,w1,w2,w3,
     * tc1,tc2,tc3
      wndmean=(w1+w2+w3)/3
c ---------------------------------------------------------------
c                   get % deviation from t107 # 3 - t107 #1
      if((i.gt.17).and.(wndmean.gt.2).and.(t3.lt.-4.5)) then 
       if((t1.gt.-20).and.(t1.lt.5))then 
        dt31=0
        pt31=0
        dt31=t3-t1
        pt31=dt31/t3
       endif
c ----------------------------------------------------------------
c                                same as above: t107 # 3 - t107 # 2
       if((t3.gt.-20).and.(t3.lt.5))then
        dt32=0
        pt32=0
        dt32=t3-t2
        pt32=dt32/t3
       endif
c ----------------------------------------------------------------
c                    write deviations to file for viewing purposes       
c       
       if((ptc1t1.gt.-0.2).and.(ptc1t1.lt.0.2)) then
        write(33,103)t3,pt31,pt32
103     format(4f15.5)
       endif
c *----------------------------------------------------------------*
c   perform class ordered % deviation averages
c
       if((ptc1t2.gt.-0.2).and.(ptc1t2.le.0.2)) then
        if((t3.gt.-13.14).and.(t3.le.-10.819))then        
         count1=count1+1
         sum1a=sum1a+pt31
         sum1b=sum1b+pt32
         write(2,*) t3,count1,sum1a,sum1b,wndmean
        endif
        if((t3.gt.-10.819).and.(t3.le.-8.498))then
         count2=count2+1
         sum2a=sum2a+pt31
         sum2b=sum2b+pt32
         write(3,*) tc1,count2,sum2a,sum2b,wndmean
        endif
        if((tc1.ge.-8.498).and.(tc1.le.-6.177))then        
         count3=count3+1
         sum3a=sum3a+pt31
         sum3b=sum3b+pt32
         write(4,*) tc1,count3,sum3a,sum3b,wndmean
        endif
        if((t1.gt.-6.177).and.(t1.le.-3.856))then
         count4=count4+1
         sum4a=sum4a+pt31
         sum4b=sum4b+pt32
         write(5,*) tc1,count4,sum4a,sum4b,wndmean
        endif
       endif
       print*,i
      endif
c ---------------------------------------------------------------+       
c ---------------------------------------------------------------+
c                                       wind sensor calibration
       dw31=w3-w1
       pw31=dw31/w3
       dw32=w3-w2
       pw32=dw32/w3
       
c       write(66,*) w3,pw31,pw32

c       if((pw31.gt.-0.041).and.(pw31.lt.0.019)) then
        if((w3.ge.1.4).and.(w3.le.2.648)) then
         wcount1=wcount1+1
         w1sum1=w1sum1+pw31
         w2sum1=w2sum1+pw32         
         write(6,*) w3,wcount1,w1sum1,w2sum1
        endif
        if((w3.gt.2.648).and.(w3.lt.3.93))then
         wcount2=wcount2+1
         w1sum2=w1sum2+pw31
         w2sum2=w2sum2+pw32
         write(7,*) w3,wcount2,w1sum2,w2sum2
        endif
c       endif
c      endif
c ------------------------------------------------------------
c                                   humidity sensor calibration
       dh21=h2-h1
       ph21=dh21/h2
       dh23=h2-h3
       ph23=dh23/h2
c       write(88,883) h2,ph21,ph23
c 883    format(3f12.6)

       hcount=hcount+1
       hsum1=hsum1+ph21
       hsum2=hsum2+ph23
c       write(11,*) hcount,hsum1,hsum2 
c ------------------------------------- end hmuidity calibration

100    continue       
99     goto 111

111    if(count1.ne.0) then       
        t1mult1=sum1a/count1
        t2mult1=sum1b/count1
       endif
       if(count2.ne.0) then
        t1mult2=sum2a/count2
        t2mult2=sum2b/count2
       endif
       if(count3.ne.0)then
        t1mult3=sum3a/count3
        t2mult3=sum3b/count3
       endif
       if(count4.ne.0) then
        t1mult4=sum4a/count4
        t2mult4=sum4b/count4
       endif
       if(wcount1.ne.0)then
        w1mult1=w1sum1/wcount1
        w2mult1=w2sum1/wcount1
       endif
       if(wcount2.ne.0)then
        w1mult2=w1sum2/wcount2
        w2mult2=w2sum2/wcount2
       endif

      hmult1=hsum1/hcount
      hmult2=hsum2/hcount
      
      t1mult1=1.0+t1mult1
      t2mult1=1.0+t2mult1
      t1mult2=1.0+t1mult2
      t2mult2=1.0+t2mult2
      t1mult3=1.0+t1mult3
      t2mult3=1.0+t2mult3
      t1mult4=1.0+t1mult4
      t2mult4=1.0+t2mult4

      w1mult1=1.0+w1mult1
      w1mult2=1.0+w1mult2      
      w2mult1=1.0+w2mult1
      w2mult2=1.0+w2mult2
      hmult1=1.0+hmult1
      hmult2=1.0+hmult2

      write(20,*) '  AERO SENSOR CALIBRATION #3, GREENLAND 1994 DATA  '
      write(20,*) '............ correction coefficients ...............'
      write(20,*) ' relative calibration to fine wire Thermo. Cpl. # 1'
      write(20,*) ' '
      write(20,*) '------------------ temp sensors --------------------'
      write(20,*) '     relative calibration to temp sensor # 3'
      write(20,*) '     class 1 mult   -13.14.ge.Tc3.le.-10.819'
      write(20,*) '                               107 #1    =',t1mult1
      write(20,*) '                               107 #2    =',t2mult1
      write(20,*) '     class 2 mult   -10.819.gt.Tc3.le.-8.492'
      write(20,*) '                               107 #1    =',t1mult2
      write(20,*) '                               107 #2    =',t2mult2
      write(20,*) '     class 3 mult   -8.492.gt.Tc3.le.-6.177'
      write(20,*) '                               107 #1    =',t1mult3
      write(20,*) '                               107 #2    =',t2mult3
      write(20,*) '     class 4 mult   -6.177.gt.Tc3.le.-3.856'
      write(20,*) '                               107 #1    =',t1mult3
      write(20,*) '                               107 #2    =',t2mult3
      write(20,*) 'sensor id #s: t1(3891); t2(5291); t3(5274)'
      write(20,*) ' '
      write(20,*) '----------------- wind sensors -------------------'
      write(20,*) 'relative calibration to wind sensor # 3'
      write(20,*) '        class 1  1.4.gt.w3.le.2.648'
      write(20,*) '                            sensor #1    =',w1mult1
      write(20,*) '                            sensor #2    =',w2mult1 
      write(20,*) '        class 2  2.68.gt.w3.le.3.93'
      write(20,*) '                            sensor #1    =',w1mult2
      write(20,*) '                            sensor #2    =',w2mult2 
      write(20,*) 'sensor id #s: w1(2460); w2(2454); w3(2465)'
      write(20,*) ' '     
      write(20,*) '--------------- humidity sensors -----------------'
      write(20,*) 'relative calibration to sensor # 2'
      write(20,*) 'one class humidity interval:87.209%-92.189%'                       =',hmult1
      write(20,*) '                            sensor #1    =',hmult1
      write(20,*) '                            sensor #3    =',hmult2   
      write(20,*) 'sensor id #s: h1(3831); h2(5291); h3(5274)'
c --------------------------------------------------------------------     
c  re read input file      
      do 106 i=1,30000 
       read(14,*,end=999) jd,tm,t1,t2,t3,h1,h2,h3,w1,w2,w3,
     * tc1,tc2,tc3
c ------------------------------------------------------------
c filter out flagged temperature data
      if((t1.lt.-20).and.(t1.gt.5)) then
        t1=9
      endif
      if((t2.lt.-20).and.(t2.gt.5)) then
        t2=9
      endif
      if((t3.lt.-20).and.(t3.gt.5)) then
        t3=9
      endif
c ----------------------------------------------- start temp comparison
c  check to see if temp corrections are good
       if((t3.gt.-13.14).and.(tc3.le.-10.819))then     
        t1=t1*t1mult1
        t2=t2*t2mult1
c        
        dtc1t1=0
        ptc1t1=0
        dtc1t1=t3-t1
        ptc1t1=dtc1t1/t3
c
        dtc1t2=0
        ptc1t2=0
        dtc1t2=t3-t2
        ptc1t2=dtc1t2/t3
c
       if((ptc1t1.gt.-0.2).and.(ptc1t1.le.0.2)) then 
        write(15,405) t3,ptc1t1,ptc1t2
       endif
       endif
       if((t3.gt.-10.819).and.(t3.le.-8.498))then    
        t1=t1*t1mult2
        t2=t2*t2mult2
c        
        dtc1t1=0
        ptc1t1=0
        dtc1t1=t3-t1
        ptc1t1=dtc1t1/t3
c
        dtc1t2=0
        ptc1t2=0
        dtc1t2=t3-t2
        ptc1t2=dtc1t2/t3
c
       if((ptc1t1.gt.-0.2).and.(ptc1t1.le.0.2)) then 
        write(15,405) t3,ptc1t1,ptc1t2
       endif
       endif
       if((tc1.ge.-8.498).and.(tc1.le.-6.177))then
        t1=t1*t1mult3
        t2=t2*t2mult3
c        
        dtc1t1=0
        ptc1t1=0
        dtc1t1=t3-t1
        ptc1t1=dtc1t1/t3
c
        dtc1t2=0
        ptc1t2=0
        dtc1t2=t3-t2
        ptc1t2=dtc1t2/t3
c
       if((ptc1t1.gt.-0.2).and.(ptc1t1.le.0.2)) then 
        write(15,405) tc1,ptc1t1,ptc1t2
       endif
       endif
       if((tc1.gt.-6.177).and.(tc1.lt.-3.856))then           
        t1=t1*t1mult4
        t2=t2*t2mult4
c        
        dtc1t1=0
        ptc1t1=0
        dtc1t1=t3-t1
        ptc1t1=dtc1t1/t3
c
        dtc1t2=0
        ptc1t2=0
        dtc1t2=t3-t2
        ptc1t2=dtc1t2/t3
c
       if((ptc1t1.gt.-0.2).and.(ptc1t1.le.0.2)) then 
        write(15,405) tc1,ptc1t1,ptc1t2
405     format(4f12.6)
       endif
       endif
c ------------------------------------------------- end temp comparison         
        if((h2.ge.84).and.(h2.le.92.1))then        
         h1=h1*hmult1
         dh21=h2-h1
         ph21=dh21/h2
         h3=h3*hmult2
         dh23=h2-h3
         ph23=dh23/h2
c         write(90,447) h1,h2,h3,ph21,ph23
c 447      format(5f10.4)
        endif
c ------------------------------------------- start wind comparison      
c see if wind corrections actually work!
c
c ---------------------- incorporate class correction terms        
        if((w3.ge.1.4).and.(w3.le.2.648)) then
         w1=w1*w1mult1
         w2=w2*w2mult1 
        endif
        if((w3.gt.2.648).and.(w3.le.3.93))then
         w1=w1*w1mult2
         w2=w2*w2mult2
        endif
c -------------------------------       
       dw31=0
       dw32=0
       pw31=0
       pw32=0

       dw31=w3-w1
       pw31=dw31/w3
       dw32=w3-w2
       pw32=dw32/w3
c --------------------------- compare dataset
c       write(16,404) w3,pw31,pw32
c 404    format(3f12.6)
c ------------------------------------------------- end wind comparison

106    continue
999    goto 333
333    print*,'You too can learn the skills that will put YOU in the' 
       print*,'drivers seat.  Cal DTI today! 650-5050'       
       print*,'Success is just a phone call away!'
      end

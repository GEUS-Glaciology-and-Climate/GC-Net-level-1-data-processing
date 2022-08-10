PROGRAM AWSFLUX
c -----------------------------------------------------------------------
c                                                      last edited 6-3-95
c
c       This program takes measured input data from Greenland automatic
c  Weather Stations and performs the Aerodynamic Profile calculations
c  to derive latent and sensible heat fluxes.  Calibration coefficients
c  for radiometers are applied.  Those coeficiets for temperature/Rhum
c  and wind sensors should also be applied, but are not yet.
c  The ground heat flux is derived here, experimentally, as a residual
c  of the energy balance equation: [Net Rad]=[Qh + Qe + Qg], therefore,
c  Qg = [Net - Qh - Qe]
c  The program outputs several other parameters including: 
c  albedo, snow height corrected for speed of sound dependance on 
c  temperature; julian solar time; 
c
c      At the end of the program, the following data are outputted... 
c
c      WRITE (2,3000) jt,SWin,SWref,net,tc,t1,t3,h1,h3,U1,U2,wdir,
c    * sd1x,sd2x,QH,QE,ri,albedo,dtdz,drhdz,dudz,Qg
c ---------------------------------------------------------------------
        implicit none
      integer kc,i
c ============================================= Met input variables
      real jt,jd,tm,tr,sd1x,sd2x,sd1,sd2,
     * SWin,SWref,NET,TC,U1,U2,T1,T3,H1,H3,WDIr
c -----------------------------------------------------------------
c ======================= Aerodynamic Profile calculation variables
      REAL QCHA,Q11,Q33,Q1,Q3,G,TAVG,TCHA,ZCHA,UCHA,S1M
      REAL W0,W9,W1,W2,RI,X1,X2,XX1,QH,QE,po
      REAL E1,E3,CA,press,W3,W4,S1X
      REAL Z1,Z2,Z3,Q21,Q22,Q23,Q24
      REAL*8 BB,AA,CC,EE,TT,GG,FF,DD,LL,KK,II,MM,ZZ,YY
      REAL*8 BBB,AAA,CCC,EEE,TTT,GGG,FFF,DDD,LLL,KKK,III
      REAL*8 MMM,ZZZ,YYY,KA,KB
      REAL SPHA,DENA,T1K,T3K
c ----------------------------------------------------------------
c ==================================== Other Calculation Variables
      real Qg
      REAL albedo,dtdz,drhdz,dudz
c ----------------------------------------------------------------
c ==================================================== Input Files
      OPEN (UNIT=1, FILE='awsargun.dat',STATUS='OLD') 
      OPEN (UNIT=2, FILE='un_flux.dat')
        open(unit=3,file='wind.dat')
c ----------------------------------------------------------------
 
25    DO 8000 I=1,70000
35      READ(1,*,end=999) kc,JD,tm,SWin,SWref,NET,TC,T1,T3,
     *  h1,H3,U1,U2,WDIR,press,sd1,sd2
c ---------------------------------------------------------------------
c ======================================== Julian Solar Time Conversion
        jt=jd+(tm/2400)                             
        jt=jt-0.1375
        print*,jt
c ----------------------------------------------------------------------
        if(press.lt.700) then
          press=750
        endif
c =========================================== gradients
        dtdz=(t3-t1)/2
        drhdz=(h3-h1)/2
        dudz=(U2-U1)/2
c ------------------------------------------------------
c ============================================ constants
      CA = 1300.0
      Z1 = 2.71
      Z3 = 4.06                                                                                                                                                                                                                          
c ------------------------------------------------------
c =============================== Temperature to Kelvins
      T1K = T1 + 273.15
      T3K = T3 + 273.15
c ------------------------------------------------------
c ======================================================
c   DENA WILL CALCULATE THE DENSITY OF AIR
c   DENSITY OF AIR = (M * press / R * TEMP)
c   WHERE (M/R)=3.4897 g mol K / J
c   press SHOULD BE IN Pa
c   TEMP SHOULD BE IN K

c         g mol K N / N M M M K

c THE RESULT WILL BE IN g/m3
      
      DENA = (3.4897*(press*100))/T3K

c NOW CONVERT THE DENSITY FROM g TO Kg
      DENA = DENA/1000.0
c --------------------------------------------------------
c =========================================================
c SPHA WILL CALCULATE THE SPECIFIC HEAT OF AIR
c (HEAT CAPACITY OF AIR) = (SPECIFIC HEAT of AIR) * (DENSITY OF AIR)     
c (SPECIFIC HEAT of AIR) = 1004 J/Kg K      
      
       SPHA = 1004.0
c  *******************************************************************

      BB =373.16/T1K
      AA=-7.90298*(BB - 1.0)
      
      CC=373.16/T1K
      EE=5.02808*LOG10(CC)

      TT=T1K/373.16
      GG=(1 - TT)
      FF=10**(11.344*GG)
      DD=1.3816E-7*(FF-1)

      LL=(373.16/T1K)-1
      KK=10**(-3.49149*LL)
      KA=KK-1
      II=8.1328E-3*KA
      MM=LOG10(1013.25)

      ZZ = AA + EE - DD + II + MM
      YY=10**ZZ

      E1=YY*100/100

      BBB=373.16/T3K
      AAA=-7.90298*(BBB - 1.0)
      CCC=373.16/T3K
      EEE=5.02808*LOG10(CCC)
      TTT=T3K/373.16
      GGG=(1 - TTT)
      FFF=10**(11.344*GGG)
      DDD=1.3816E-7*(FFF - 1)

      LLL=(373.16/T3K)-1
      KKK=10**(-3.49149*LLL)
      KB=KKK-1
      III=8.1328E-3*KB
      MMM=LOG10(1013.25)

      ZZZ = AAA + EEE - DDD + III + MMM
      YYY = 10**ZZZ

      E3=YYY*100/100

c ================================== potential temperature conversion
      PO=1000
      
      T1K=T1K*(PO/press)**.286
      T3K=T3K*(PO/press)**.286
c -------------------------------------------------------------------
      TAVG = (T1K + T3K)/2
      TCHA = T3K - T1K
      UCHA = U2 - U1
      ZCHA = Z3 - Z1
      
      G = 9.8
      
      IF (UCHA.EQ.0.0) THEN
         UCHA = UCHA + 0.001
      ENDIF

      X1 = (G/TAVG)
      X2 = (TCHA/ZCHA)/(UCHA/ZCHA)**2
  
      RI = X1*X2

c ======================================= Stability Parameterizations
c ======================================= based on richardson number.
      IF (RI.EQ.0) THEN
         S1M=1
         S1X=1
      ENDIF
      
      IF (RI.GE..19) THEN
         S1M=83.333
         S1X=S1M
      ENDIF
      
      IF (RI.GT.0.AND.RI.LT..19) THEN
        S1M = (1 - 5.2*RI)**(-1)
        S1X=S1M
      ENDIF

      IF (RI.LT.0.AND.RI.GE.-.03) THEN
         S1M = (1 - 18*RI)**(-.25)
         S1X=S1M
      ENDIF

      IF (RI.LT.-.03) THEN
        S1M = (1 - 18*RI)**(-.25)
        S1X=S1M/1.3
      ENDIF

      IF (S1X.EQ.0) THEN
         S1X=.0001
      ENDIF
      IF (S1M.EQ.0) THEN
         S1M=.0001
      ENDIF
c -----------------------------------------------------------------
      W0 = Z3/Z1
      W9 = LOG(W0)
      
      W1=.4*TCHA
      W2=W1/(S1X*W9)
      
      W3=.4*UCHA
      W4=W3/(S1M*W9)

      QH=DENA*SPHA*W2*W4
      QH=QH*(-1)

c      PRINT 10, QH
c 10    FORMAT (1X,'SENSIBLE HEAT FLUX = ',F9.4,' W/METER SQUARED')

      Q1 = h1*E1/100
      Q3 = H3*E3/100
      
      Q11 = .622*Q1/(press - .378*Q1)
      Q33 = .622*Q3/(press - .378*Q3)

      QCHA = Q33 - Q11

      XX1 = W9
      Q21 = .4*QCHA
      Q22 = Q21/(S1X*W9)
      Q23 = .4*UCHA
      Q24 = Q23/(S1M*W9)

      QE = DENA*2.5E6*Q22*Q24
      QE=QE*(-1)
      
c      PRINT 20, QE
c 20    FORMAT (1X,'LATENT HEAT FLUX = ',F9.4,' W/METER SQUARED')

c      IF (QH.LT.-500) THEN
c          GOTO 35
c      ENDIF
c      IF (QE.LT.-500) THEN
c          GOTO 35
c      ENDIF
c
c      IF (QE.GT.1000) THEN
c          GOTO 35
c      ENDIF
c      IF (QH.GT.1000) THEN
c          GOTO 35
c      ENDIF
c      IF (QH.LT.0.001.AND.QH.GT.-0.001) THEN
c         QH=0.0
c      ENDIF
c      IF (QE.LT.0.001.AND.QE.GT.-0.001) THEN
c         QE=0.0
c      ENDIF
c =================================================== flag filtering
        if(sd1.lt.3) sd1=-99
        if(sd2.lt.3.5) sd2=-99
        if(press.lt.700) press=-99
        if(net.lt.-20) net=-99
        if((QH.lt.-200).or.(QH.gt.200)) QH=-99
        if((QE.lt.-200).or.(QE.gt.200)) QE=-99
        if((Ri.lt.-5).or.(Ri.gt.5)) Ri=-99
c ------------------------------------------------------------------
c =========================================== radiometer multipliers
c       Net Rad ID# Q95094 
        if(net.gt.0)then
          net=net*9.08          
        else
          net=net*11.36
        endif
c ++++++++++++++++++++++++++++++++++++
c       Li-Cor Pyranometer Multipliers
        SWin=SWin*170
        SWref=SWref*170
        if(SWin.lt.SWref)Swin=Swref
c -----------------------------------------------------------------
c =============================== snow depth temperature correction
        tr=T1K/273.15
        tr=(tr)**0.5
        sd1x=sd1*tr
        sd2x=sd2*tr
        if((sd1x.lt.0).or.(sd1x.gt.5)) sd1x=-99
        if((sd2x.lt.0).or.(sd2x.gt.5)) sd2x=-99
c ----------------------------------------------------------------
c ============================ Ground Flux as residual calculation
        Qg=(net-Qh-Qe)
c ----------------------------------------------------------------
c ============================================= Albedo Calculation
        if(SWin.eq.0)SWin=0.0001
        albedo=SWref/SWin
        if(albedo.gt.1.0)albedo=-99
c ----------------------------------------------------------------
c ============================================ Output data to file
      WRITE (2,3000) jt,SWin,SWref,net,tc,t1,t3,h1,h3,U1,U2,wdir,
     * sd1x,sd2x,QH,QE,ri,albedo,dtdz,drhdz,dudz,Qg
3000  FORMAT (22F8.2)
        write(3,*) U2
8000  CONTINUE
999   stop
      END


% plot of wx data
load C:\Campbellsci\LoggerNet\Parcawx_wind_1.dat
% date,wind(m/s)
load C:\Campbellsci\LoggerNet\Parcawx_winddir_1.dat
% date,dir(M)
load C:\Campbellsci\LoggerNet\Parcawx_wind_2.dat
% date,wind(m/s)
load C:\Campbellsci\LoggerNet\Parcawx_winddir_2.dat
% date,dir(M)
load C:\Campbellsci\LoggerNet\Parcawx_temp.dat 
% date,temp(deg C)
load C:\NEEM\wxseason.txt
% date(in days - no year),temp(deg C),wind(knots),dir(M)
%
Parcawx_winddir_1T(:,1)=Parcawx_winddir_1(:,1);
Parcawx_winddir_1T(:,2)=-45+Parcawx_winddir_1(:,2);
Parcawx_winddir_2T(:,1)=Parcawx_winddir_2(:,1);
Parcawx_winddir_2T(:,2)=-45+Parcawx_winddir_2(:,2);
for i=1:10685
    if Parcawx_winddir_1T(i,2)<0
        Parcawx_winddir_1T(i,2)=360+Parcawx_winddir_1T(i,2);
    end
    if Parcawx_winddir_2T(i,2)<0
        Parcawx_winddir_2T(i,2)=360+Parcawx_winddir_2T(i,2);
    end
end
wxseason(:,6)= -45+wxseason(:,4);
for i=1:5121
    if wxseason(i,6)<0
        wxseason(i,6)=360+wxseason(i,6);
    end
end
%
% PARCA has 10685 lines
% Split into years PARCA
%  2006: 1 to 3801
%  2007: 3802 to 8492
%  2008: 8493-10685  (moved 63.45 days to fit NEEM wx)
%
% NEEM has 5121 lines
%
%Compare data
%
figure(1)  % temp
plot(Parcawx_temp(:,1),Parcawx_temp(:,2),'k')
hold on
plot(2008+wxseason(:,1)./365,wxseason(:,2),'r')
grid
axis([2006 2009 -50 0])
xlabel('Time')
ylabel('Temperature (deg C)')
title('Temperature; red NEEM, black PARCA 1')
figure(2)  % temp 2008
plot(Parcawx_temp(:,1),Parcawx_temp(:,2),'k')
hold on
plot(2008+wxseason(:,1)./365,wxseason(:,2),'r')
grid
axis([2008.5 2008.62 -20 0])
xlabel('Time')
ylabel('Temperature (deg C)')
title('Temperature; red NEEM, black PARCA 1')
%
figure(3)  % wind speed
plot(Parcawx_wind_1(:,1),Parcawx_wind_1(:,2),'k.')
hold on
plot(Parcawx_wind_2(:,1),Parcawx_wind_2(:,2),'b.')
plot(2008+wxseason(:,1)./365,0.5*wxseason(:,3),'r')
grid
axis([2006 2009 0 16])
xlabel('Time')
ylabel('Wind speed (m/s)')
title('Wind Speed; red NEEM, black PARCA 1, blue PARCA 2')
figure(4)  % wind speed 2008
plot(Parcawx_wind_1(:,1),Parcawx_wind_1(:,2),'k.')
hold on
plot(Parcawx_wind_2(:,1),Parcawx_wind_2(:,2),'b.')
plot(2008+wxseason(:,1)./365,0.5*wxseason(:,3),'r')
grid
axis([2008.5 2008.62 0 16])
xlabel('Time')
ylabel('Wind speed (m/s)')
title('Wind Speed; red NEEM, black PARCA 1, blue PARCA 2')
figure(5)  % wind direction
plot(Parcawx_winddir_1T(:,1),Parcawx_winddir_1T(:,2),'k.')
hold on
%plot(Parcawx_winddir_2T(:,1),Parcawx_windir_2T(:,2),'b.')
plot(2008+wxseason(:,1)./365,wxseason(:,6),'r')
grid
axis([2006 2009 0 360])
xlabel('Time')
ylabel('Wind direction (T)')
title('Wind Direction; red NEEM, black PARCA 1, blue PARCA 2')
axis([2006 2009 0 360])
figure(6)  % wind direction 2008
plot(Parcawx_winddir_1T(:,1),Parcawx_winddir_1T(:,2),'k.')
hold on
%plot(Parcawx_winddir_2T(:,1),Parcawx_windir_2T(:,2),'b.')
plot(2008+wxseason(:,1)./365,wxseason(:,6),'r')
grid
axis([2008.5 2008.62 0 360])
xlabel('Time')
ylabel('Wind direction (T)')
title('Wind Direction; red NEEM, black PARCA 1, blue PARCA 2')
%
%  wind direction statistics
%
P_0_2006=windselect(0,Parcawx_wind_1(1:3801,:),Parcawx_winddir_1T(1:3801,:));
P_5_2006=windselect(5,Parcawx_wind_1(1:3801,:),Parcawx_winddir_1T(1:3801,:));
P_10_2006=windselect(10,Parcawx_wind_1(1:3801,:),Parcawx_winddir_1T(1:3801,:));
P_0_2007=windselect(0,Parcawx_wind_1(3802:8492,:),Parcawx_winddir_1T(3802:8492,:));
P_5_2007=windselect(5,Parcawx_wind_1(3802:8492,:),Parcawx_winddir_1T(3802:8492,:));
P_10_2007=windselect(10,Parcawx_wind_1(3802:8492,:),Parcawx_winddir_1T(3802:8492,:));
P_0_2008=windselect(0,Parcawx_wind_1(8493:10685,:),Parcawx_winddir_1T(8493:10685,:));
P_5_2008=windselect(5,Parcawx_wind_1(8493:10685,:),Parcawx_winddir_1T(8493:10685,:));
P_10_2008=windselect(10,Parcawx_wind_1(8493:10685,:),Parcawx_winddir_1T(8493:10685,:));
P_0_NEEM=windselect(0,[wxseason(:,1),0.5*wxseason(:,3)],wxseason(:,[1,6]));
P_5_NEEM=windselect(5,[wxseason(:,1),0.5*wxseason(:,3)],wxseason(:,[1,6]));
P_10_NEEM=windselect(10,[wxseason(:,1),0.5*wxseason(:,3)],wxseason(:,[1,6]));
Save_mean(1,:)=[mean(P_0_2006(:,3)),mean(P_5_2006(:,3)),mean(P_10_2006(:,3))];
Save_mean(2,:)=[mean(P_0_2007(:,3)),mean(P_5_2007(:,3)),mean(P_10_2007(:,3))];
Save_mean(3,:)=[mean(P_0_2008(:,3)),mean(P_5_2008(:,3)),mean(P_10_2008(:,3))];
Save_mean=int16(Save_mean);
%
figure(7) %all winds
plot(P_0_2006(:,2).*sin((P_0_2006(:,3)/180*pi)),P_0_2006(:,2).*cos((P_0_2006(:,3)/180*pi)),'k.')
hold on
plot(P_0_2007(:,2).*sin((P_0_2007(:,3)/180*pi)),P_0_2007(:,2).*cos((P_0_2007(:,3)/180*pi)),'b.')
plot(P_0_2008(:,2).*sin((P_0_2008(:,3)/180*pi)),P_0_2008(:,2).*cos((P_0_2008(:,3)/180*pi)),'g.')
plot(P_0_NEEM(:,2).*sin((P_0_NEEM(:,3)/180*pi)),P_0_NEEM(:,2).*cos((P_0_NEEM(:,3)/180*pi)),'r.')
axis([-15 15 -15 15])
grid
axis square
title('Wind Rose; black PARCA 2006; blue PARCA 2007; green PARCA 2008; red NEEM 2008')
%
figure(8) %winds more than 5 m/s
plot(P_5_2006(:,2).*sin((P_5_2006(:,3)/180*pi)),P_5_2006(:,2).*cos((P_5_2006(:,3)/180*pi)),'k.')
hold on
plot(P_5_2007(:,2).*sin((P_5_2007(:,3)/180*pi)),P_5_2007(:,2).*cos((P_5_2007(:,3)/180*pi)),'b.')
plot(P_5_2008(:,2).*sin((P_5_2008(:,3)/180*pi)),P_5_2008(:,2).*cos((P_5_2008(:,3)/180*pi)),'g.')
plot(P_5_NEEM(:,2).*sin((P_5_NEEM(:,3)/180*pi)),P_5_NEEM(:,2).*cos((P_5_NEEM(:,3)/180*pi)),'r.')
axis([-15 15 -15 15])
grid
axis square
title('Wind Rose; black PARCA 2006; blue PARCA 2007; green PARCA 2008; red NEEM 2008')
%
figure(9) %winds more than 10 m/s
plot(P_10_2006(:,2).*sin((P_10_2006(:,3)/180*pi)),P_10_2006(:,2).*cos((P_10_2006(:,3)/180*pi)),'k.')
hold on
plot(P_10_2007(:,2).*sin((P_10_2007(:,3)/180*pi)),P_10_2007(:,2).*cos((P_10_2007(:,3)/180*pi)),'b.')
plot(P_10_2008(:,2).*sin((P_10_2008(:,3)/180*pi)),P_10_2008(:,2).*cos((P_10_2008(:,3)/180*pi)),'g.')
plot(P_10_NEEM(:,2).*sin((P_10_NEEM(:,3)/180*pi)),P_10_NEEM(:,2).*cos((P_10_NEEM(:,3)/180*pi)),'r.')
axis([-15 15 -15 15])
grid
axis square
title('Wind Rose; black PARCA 2006; blue PARCA 2007; green PARCA 2008; red NEEM 2008')
%
figure(10)
subplot(1,1,1)
title('Wind direction stat.; black all; blue >5 m/s; red >10 m/s')
subplot(3,2,1)
[n,out]=hist(P_0_2006(:,3),36);
bar(out,n,'k')
hold on
histmax=600;
axis([0 360 0 histmax])
plot([mean(P_0_2006(:,3)),mean(P_0_2006(:,3))],[0 histmax],'k')
[n,out]=hist(P_5_2006(:,3),36);
bar(out,n,'b')
plot([mean(P_5_2006(:,3)),mean(P_5_2006(:,3))],[0 histmax],'b')
[n,out]=hist(P_10_2006(:,3),36);
bar(out,n,'r')
hold on
plot([mean(P_10_2006(:,3)),mean(P_10_2006(:,3))],[0 histmax],'r')
title('2006 direction(True)')
text(250,histmax*.9, ['all :',num2str(Save_mean(1,1))])
text(250,histmax*.75,['> 5:',num2str(Save_mean(1,2))])
text(250,histmax*.6, ['>10:',num2str(Save_mean(1,3))])
%
subplot(3,2,3)
[n,out]=hist(P_0_2007(:,3),36);
bar(out,n,'k')
hold on
histmax=800;
axis([0 360 0 histmax])
plot([mean(P_0_2007(:,3)),mean(P_0_2007(:,3))],[0 histmax],'k')
[n,out]=hist(P_5_2007(:,3),36);
bar(out,n,'b')
plot([mean(P_5_2007(:,3)),mean(P_5_2007(:,3))],[0 histmax],'b')
[n,out]=hist(P_10_2007(:,3),36);
bar(out,n,'r')
hold on
plot([mean(P_10_2007(:,3)),mean(P_10_2007(:,3))],[0 histmax],'r')
title('2007 direction(True)')
text(250,histmax*.9, ['all :',num2str(Save_mean(2,1))])
text(250,histmax*.75,['> 5:',num2str(Save_mean(2,2))])
text(250,histmax*.6, ['>10:',num2str(Save_mean(2,3))])
%
subplot(3,2,5)
[n,out]=hist(P_0_2008(:,3),36);
bar(out,n,'k')
hold on
histmax=400;
axis([0 360 0 histmax])
plot([mean(P_0_2008(:,3)),mean(P_0_2008(:,3))],[0 histmax],'k')
[n,out]=hist(P_5_2008(:,3),36);
bar(out,n,'b')
plot([mean(P_5_2008(:,3)),mean(P_5_2008(:,3))],[0 histmax],'b')
[n,out]=hist(P_10_2008(:,3),36);
bar(out,n,'r')
hold on
plot([mean(P_10_2008(:,3)),mean(P_10_2008(:,3))],[0 histmax],'r')
title('2008  direction(True)')
text(250,histmax*.9, ['all :',num2str(Save_mean(3,1))])
text(250,histmax*.75,['> 5:',num2str(Save_mean(3,2))])
text(250,histmax*.6, ['>10:',num2str(Save_mean(3,3))])
subplot(3,2,2)
[n,out]=hist(P_0_2006(:,2),36);
bar(out,n,'g')
histmax=500;
axis([0 15 0 histmax])
title('2006 speed(m/s)')
subplot(3,2,4)
[n,out]=hist(P_0_2007(:,2),36);
bar(out,n,'g')
histmax=500;
axis([0 15 0 histmax])
title('2007 speed(m/s)')
subplot(3,2,6)
[n,out]=hist(P_0_2008(:,2),36);
bar(out,n,'g')
histmax=300;
axis([0 15 0 histmax])
title('2008 speed(m/s)')
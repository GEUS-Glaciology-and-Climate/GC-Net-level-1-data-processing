function data_select = windselect(windspeed,data_speed, data_dir)
%
[n,m]=size(data_speed);
icount=0;
for i=1:n
    if data_speed(i,2)>windspeed
        icount=icount+1;
        data_select(icount,1:2)=data_speed(i,:);
        data_select(icount,3)=data_dir(i,2);
    end
end
    

import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import datetime as dt
from scipy.stats import pearsonr
f=xr.open_dataset("D:/test_data/air.mon.mean.nc")

t=f.air.loc[f.time.dt.month.isin([12,1,2])].loc['1979-12-01':'2020-03-01',850,50:30,110:130]
print(t)

print('*'*100)

#t1和t2是等效的
t1=np.array(f.air.loc[f.time.dt.month.isin([12,1,2])].loc['1979-12-01':'2020-03-01',850,50:30,110:130].mean('lat').mean('lon')).reshape((41,3)).mean(1)
t2=np.array(f.air.loc[f.time.dt.month.isin([12,1,2])].loc['1979-12-01':'2020-03-01',850,50:30,110:130]).mean((1,2)).reshape((41,3)).mean(1)
print(t1)

#载入场数据
f1=xr.open_dataset("D:/test_data/hgt.mon.mean.nc")
z=np.array(f.air.loc[f.time.dt.month.isin([12,1,2])].loc['1979-12-01':'2020-03-01',500]).reshape((41,3,73,144)).mean(1)
lat=f1.lat
lon=f1.lon
# print(f1)
# print('*'*100)
# print(z)
#对经纬度进行循环，计算相关系数
r,p=np.zeros((73,144)),np.zeros((73,144))
for i in range(len(lat)):
    for j in range(len(lon)):
        r[i,j],p[i,j]=pearsonr(t1,z[:,i,j])

#绘图


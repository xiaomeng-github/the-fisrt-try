import pandas as pd
import numpy as np
f=pd.read_csv("D:/test_data/1957_2012_tm_year_avg.txt",sep='\s+',names=['sta','lat','lon','alt','year','tm'],na_values=-99.90)
# print(f)
data1=f.loc[f.year==2006]
data=data1.dropna(axis=0,how='any')
print(data.shape,data1.shape)
lat=data.lat.values/100

lon=data.lon.values/100
tm=data.tm.values
sta=data.sta.values
print(type(data))
print(data.agg({'min','max'}))

#Cressman插值
from metpy.interpolate import inverse_distance_to_grid
lon_grid=np.arange(75,133,1)
lat_grid=np.arange(16,53,1)
lon_gridmesh,lat_gridmesh=np.meshgrid(lon_grid,lat_grid)
# print(lon_gridmesh)
#r为搜索半径
tm_grid=inverse_distance_to_grid(lon,lat,tm,lon_gridmesh,lat_gridmesh,r=15,min_neighbors=3)
print(tm_grid)

#克里金插值
# from pykrige.ok import OrdinartKriging
# #创建一个实例对象
# krige=OrdinartKriging(lon,lat,tm,variogram_model='linear',verbose=False,enable_plotting=False)
# lon_grid=np.arange(75,133,1)
# lat_grid=np.arange(16,53,1)
# tm_grid,ss=krige.execute('grid',lon_grid,lat_grid)


#xarray从网格数据插值到站点数据
import xarray as xr
tm_data=xr.DataArray(tm_grid,coords=[lat_grid,lon_grid],dims=['lat','lon'])
lat=xr.DataArray(lat,coords=[sta],dims=['sta'])
lon=xr.DataArray(lon,coords=[sta],dims=['sta'])
tm_sta=tm_data.interp(lon=lon,lat=lat,method='linear')
print(tm)
print('*'*100)
print(tm_sta)

#网格到网格的插值
tm_data=xr.DataArray(tm_grid,coords=[lat_grid,lon_grid],dims=['lat','lon'])
print(tm_data)
lon_grid25=np.arange(75,133,2.5)
lat_grid25=np.arange(16,53,2.5)
tm_grid25=tm_data.interp(lon=lon_grid25,lat=lat_grid25,method='linear')
print(tm_grid25)


#网格数据时间插值
import datetime as dt
file=xr.open_dataset("D:/test_data/air.mon.mean.nc")
data2=file.air.loc[np.array(['1979-01-01','1979-02-01','1979-04-01','1979-05-01'],dtype=np.datetime64),850]
# print(data2)
#插值三月份的数据
data2_interp=data2.interp(time=np.array(['1979-01-01','1979-02-01','1979-03-01','1979-04-01','1979-05-01'],dtype=np.datetime64),method='linear')
data3_ori=file.air.loc[np.array(['1979-03-01'],dtype=np.datetime64),850]
data3_inte=file.air.loc[np.array(['1979-03-01'],dtype=np.datetime64),850]
data3_ori=np.array(data3_ori)
data3_inte=np.array(data3_inte)
print(data3_ori)
print(data3_inte)

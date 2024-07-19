import numpy
import pandas
import xarray as xr
data=xr.open_dataset("D:/CN05.1_Pre_2022_daily_025x025.nc")
print(data)
print('*'*100)
#读取6月到12月
# print(data.pre)
data_six_dec=data.pre.loc['2022-06-01':'2022-12-01',:,:] #必须加上变量名称
# print(data_six_dec)

import datetime as dt
# print(data.time.dt.month) #array([ 1,  1,  1, ..., 12, 12, 12], dtype=int64)
# print(data.time.dt.month.isin([6,7,8])) #array([False, False, False, False])

#读取夏季的数据
data_summer=data.pre.loc[data.time.dt.month.isin([6,7,8])]
# print(data_summer)
# print(data_summer.shape)
# print(data_summer.time)
time=data_summer.time
lat=data_summer.lat.values #变为熟悉的形式
lon=data_summer.lon
# print(time)
# print(lon)
print(lat,type(lat))
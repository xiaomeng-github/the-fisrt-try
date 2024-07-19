import numpy as np
import xarray as xr
from datetime import datetime
tem=xr.open_dataset("D:/test_data/t1980_2010.nc")
print(tem)
#选取某一点的8月份的温度数据进行分析
t2m=tem.air.loc[tem.time.dt.month.isin(8),39.047,120]-273.15
print(t2m) #DataArray类型的数据结构
data=t2m.time
time_occur=data[t2m>28]
print(time_occur)


#比较万能的方法是：
t2m=np.array(t2m)
t2m=t2m.reshape((31,31))
date=[]
for y in range(t2m.shape[0]):
    for d in range(t2m.shape[1]):
        if t2m[y,d]>28:
            date.append(datetime(year=(1980+y),month=8,day=(d+1)))
# print(date)
from pandas.core.frame import DataFrame
date=DataFrame({'date':date})
print(date)
print(date.date.values)
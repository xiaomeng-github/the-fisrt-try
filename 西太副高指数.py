import numpy as np
import xarray as xr
import datetime as dt
f_z=xr.open_dataset("D:/test_data/hgt.mon.mean.nc")
z1=f_z.hgt.loc[f_z.time.dt.month.isin([6,7,8])].loc['1979-01-01':'2020-12-01',500,:,90:180]
lon=z1.lon
z1_array=np.array(z1).reshape((42,3,73,37)).mean((1))


#索取西伸脊点指数
wpsh_wp=np.zeros((42))

for i in range(z1_array.shape[0]):
    for j in range(z1_array.shape[2]):
        if z1_array[i,:,j].max()>=5880:
            wpsh_wp[i]=lon[j]
            break
    if wpsh_wp[i]==0:
        for j in range(z1_array.shape[2]):
            if z1_array[i, :, j].max() >= 5870:
                wpsh_wp[i] = lon[j]
                break

#面积指数
# wpsh_area=np.zeros((42))
z2=f_z.hgt.loc[f_z.time.dt.month.isin([6,7,8])].loc['1979-01-01':'2020-12-01',500,:10,110:180]
z2_array=np.array(z2).reshape((42,3,33,29)).mean((1))
print(z2_array)
wpsh_area=np.sum(z2_array>5880,axis=(1,2))
print(wpsh_area)

#强度指数
z3=f_z.hgt.loc[f_z.time.dt.month.isin([6,7,8])].loc['1979-01-01':'2020-12-01',500,:10,110:180]
z3_array=np.array(z2).reshape((42,3,33,29)).mean((1))
z3_array=z3_array-5880
z3_array[z3_array<0]=0
wpsh_int=np.sum(z3_array>5880,axis=(1,2))/10


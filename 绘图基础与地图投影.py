import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
fig=plt.figure(figsize=(12,8))
# for i in range(6):
#     ax=fig.add_subplot(2,3,i+1)
#     ax.text(0.5,0.5,f'{i+1}',fontsize=20,ha='center',va='center')
#     ax.text(0.5,0.2,f'ax=fig.add_subpot(2,3,{i+1})',ha='center',va='center')
# ax2=fig.add_axes((0.3,0.5,0.3,0.2))
# ax2.text(0.5,0.5,'ax=fig.add_axes()',fontsize=20,ha='center',va='center')
# plt.show()


#添加子图
# ax1=fig.add_axes((0.1,0.1,0.8,0.8))
# ax2=fig.add_axes((0.7,0.1,0.1,0.2))
# plt.show()

#引入地理坐标看子图的区别
f_u=xr.open_dataset("D:/test_data/uwnd.mon.mean.nc")
u=f_u['uwnd'].loc['1979-12-01',1000]
lat=u.lat
lon=u.lon
fig1=plt.figure(figsize=(15,15))


ax1=fig1.add_axes((0.1,0.1,0.5,0.4),projection=ccrs.PlateCarree())

ax1.contourf(lon,lat,u,transform=ccrs.PlateCarree())

ax2=fig1.add_axes((0.7,0.1,0.5,0.4))
ax2.contourf(lon,lat,u)
plt.show()


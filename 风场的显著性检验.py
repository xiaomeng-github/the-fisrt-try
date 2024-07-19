import xarray as xr
import numpy as np
import datetime as dt
import cartopy.crs as ccrs
import cartopy.feature as cfea
import cartopy.mpl.ticker as cticker
import matplotlib.pyplot as plt
from scipy.stats import linregress

f_t=xr.open_dataset("D:/test_data/air.mon.mean.nc")

t=np.array(f_t.air.loc[f_t.time.dt.month.isin([12,1,2])].loc['1979-12-01':'2020-03-01',850,50:30,110:130]).mean((1,2)).reshape((41,3)).mean(1)
# t1=np.array(f_t.air.loc[f_t.time.dt.month.isin([12,1,2])].loc['1979-12-01':'2020-03-01',850,50:30,110:130].mean('lat').mean('lon')).reshape((41,3))

f_u=xr.open_dataset("D:/test_data/uwnd.mon.mean.nc")

u=np.array(f_u.uwnd.loc[f_u.time.dt.month.isin([12,1,2])].loc['1979-12-01':'2020-03-01',500]).reshape((41,3,73,144)).mean((1))
f_v=xr.open_dataset("D:/test_data/vwnd.mon.mean.nc")
v=np.array(f_v.vwnd.loc[f_u.time.dt.month.isin([12,1,2])].loc['1979-12-01':'2020-03-01',500]).reshape((41,3,73,144)).mean((1))


lat=f_v.lat
lon=f_v.lon
print(t.shape,u.shape)
su,pu=np.zeros((73,144)),np.zeros((73,144))
sv,pv=np.zeros((73,144)),np.zeros((73,144))

for i in range(len(lat)):
    for j in range(len(lon)):
        su[i,j],_,_,pu[i,j],_=linregress(t,u[:,i,j])
        sv[i,j],_,_,pv[i,j],_=linregress(t,v[:,i,j])


print(su)
print(pu)
fig=plt.figure(figsize=(12,8))
proj=ccrs.PlateCarree(central_longitude=180)
leftlon,righlon,lowerlat,upperlat=(0,180,0,90)
img_extent=[leftlon,righlon,lowerlat,upperlat]
ax=fig.add_axes((0.1,0.1,0.8,0.8),projection=proj)
ax.set_extent(img_extent,crs=ccrs.PlateCarree())

ax.add_feature(cfea.COASTLINE)
ax.set_xticks(np.arange(leftlon,righlon+60,60),crs=ccrs.PlateCarree())
ax.set_yticks(np.arange(lowerlat,upperlat+30,30),crs=ccrs.PlateCarree())
lon_formatter=cticker.LongitudeFormatter()
lat_formatter=cticker.LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)

# ax.quiver(lon[::2],lat[::2],su[::2,::2],sv[::2,::2],transform=ccrs.PlateCarree(),scale=60,cmap=plt.cm.jet)
# plt.show()


#显著性检验
su_tep=su.copy()
sv_tem=sv.copy()

su_tep[pu>0.1]=np.nan
su_tep[pv>0.1]=np.nan
sv_tem[pu>0.1]=np.nan
sv_tem[pv>0.1]=np.nan

ax.quiver(lon[::2],lat[::2],su_tep[::2,::2],sv_tem[::2,::2],transform=ccrs.PlateCarree(),scale=60,cmap=plt.cm.jet)
plt.show()
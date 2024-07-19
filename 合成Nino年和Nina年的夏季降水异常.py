import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import datetime as dt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker

# a=np.array([15.4,14.6,15.8,14.8,15.0,15.1,15.1,15.0,15.2,15.4,14.8,15.0,15.1,14.7,16.0,15.7,15.4,14.5,15.1,
# 15.3,15.5,15.1,15.6,15.1,15.1,14.9,15.5,15.3,15.3,15.4,15.7,15.2,15.5,15.5,15.6,15.1,15.1,16.0,16.0,16.8])
# a_std=(a-a.mean())/a.std()
# year=np.arange(1979,2019,1)
#
# fig=plt.figure(figsize=(12,8))
# ax1=fig.add_axes((0.1,0.1,0.8,0.4))  #画子图，图中图
# ax1.plot(year,a_std)
# ax1.axhline(1,c='k')
# ax1.axhline(-1,c='k')
# plt.show()



nino_year=np.array([1951,1957,1963,1965,1968,1972,1976,1977,1979,1982,1986,1991,1994,1997,2002,
2004,2006,2009,2014])
nina_year=np.array([1950,1954,1964,1970,1973,1975,1984,1988,2000,2007,2010,2011])
f=xr.open_dataset("D:/test_data/precip.mon.mean.nc")
# print(f)
#夏季的月均降水降水
pre_clim=f.precip.loc[f.time.dt.month.isin([6,7,8])]
pre_nino=f.precip.loc[(f.time.dt.month.isin([6,7,8]) & (f.time.dt.year.isin(nino_year)))]
pre_nina=f.precip.loc[(f.time.dt.month.isin([6,7,8]) & (f.time.dt.year.isin(nina_year)))]
# print(pre_nina)
#提取经纬度
lon=f.loc
lat=f.lat
#判断异常
print(pre_nino.mean('time'))
pre_nino_ano=pre_nino.mean('time')*92-pre_clim.mean('time')*92  #np.array(pre_clim).mean((0))
pre_nina_ano=pre_nina.mean('time')*92-pre_clim.mean('time')*92  #np.array(pre_clim).mean((0))
print(pre_nina_ano)

#绘图显示
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.4],projection = ccrs.PlateCarree(central_longitude=115))
ax1.set_extent([60,150,0,60], crs=ccrs.PlateCarree())
ax1.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax1.add_feature(cfeature.LAKES, alpha=0.5)
ax1.set_xticks(np.arange(60,150+30,30), crs=ccrs.PlateCarree())
ax1.set_yticks(np.arange(0,60+30,30), crs=ccrs.PlateCarree())
lon_formatter = cticker.LongitudeFormatter()
lat_formatter = cticker.LatitudeFormatter()
ax1.xaxis.set_major_formatter(lon_formatter)
ax1.yaxis.set_major_formatter(lat_formatter)
ax1.set_title('(a) Pre. anomaly in Nino years',loc='left',fontsize=18)
c1 = ax1.contourf(lon,lat, pre_nino_ano,levels =np.arange(-80,90,10) ,
                     extend = 'both', transform=ccrs.PlateCarree(), cmap=plt.cm.BrBG)

ax2 = fig.add_axes([0.6, 0.1, 0.8, 0.4],projection = ccrs.PlateCarree(central_longitude=115))
ax2.set_extent([60,150,0,60], crs=ccrs.PlateCarree())
ax2.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax2.add_feature(cfeature.LAKES, alpha=0.5)
ax2.set_xticks(np.arange(60,150+30,30), crs=ccrs.PlateCarree())
ax2.set_yticks(np.arange(0,60+30,30), crs=ccrs.PlateCarree())
ax2.xaxis.set_major_formatter(lon_formatter)
ax2.yaxis.set_major_formatter(lat_formatter)
ax2.set_title('(b) Pre. anomaly in Nina years',loc='left',fontsize=18)
c2 = ax2.contourf(lon,lat, pre_nina_ano, zorder=0,levels =np.arange(-80,90,10) ,
                     extend = 'both', transform=ccrs.PlateCarree(), cmap=plt.cm.BrBG)
position=fig.add_axes([0.58, 0.02,  0.35, 0.025])
fig.colorbar(c1,cax=position,orientation='horizontal',format='%d',)
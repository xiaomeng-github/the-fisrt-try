import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.util import add_cyclic_point

f_u=xr.open_dataset("D:/test_data/uwnd.mon.mean.nc")
u=f_u['uwnd'].loc['1979-12-01',1000]
lat=u.lat
lon=u.lon

cyclic_data,cyclic_lons=add_cyclic_point(u,coord=lon) #去除白线

fig=plt.figure(figsize=(15,5))
ax1 = fig.add_axes((0, 0, 0.8, 0.8),projection=ccrs.PlateCarree(central_longitude=120))
ax1.contourf(lon,lat,u,transform=ccrs.PlateCarree())
ax1.add_feature(cfeature.COASTLINE.with_scale('50m'))

ax2 = fig.add_axes((0.4, 0.1, 0.8, 0.8),projection=ccrs.PlateCarree(central_longitude=240))
ax2.contourf(cyclic_lons,lat,cyclic_data,transform=ccrs.PlateCarree())
ax2.add_feature(cfeature.COASTLINE.with_scale('50m'))

plt.show()

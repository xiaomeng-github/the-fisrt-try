import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.util import add_cyclic_point
import matplotlib.path as mpath


f_u=xr.open_dataset("D:/test_data/uwnd.mon.mean.nc")
u=f_u['uwnd'].loc['1979-12-01',1000]
lat=u.lat
lon=u.lon

leftlon,rightlon,lowerlat,upperlat=(0,180,30,80)


fig=plt.figure(figsize=(15,15))

ax1=fig.add_axes((0.1,0.1,0.6,0.6),projection=ccrs.LambertConformal(central_longitude=90,central_latitude=45))
path=mpath.Path([[leftlon,lowerlat],[rightlon,lowerlat],[rightlon,upperlat],[leftlon,upperlat],[leftlon,lowerlat]]).interpolated(20)
transpath=(ccrs.PlateCarree()._as_mpl_transform(ax1)-ax1.transData).transform_path(path)
ax1.set_extent((0,180,30-20,80))
ax1.set_boundary(transpath)


ax1.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax1.gridlines(draw_labels=True,x_inline=False,y_inline=False)
ax1.contourf(lon,lat,u,transform=ccrs.PlateCarree())
plt.show()
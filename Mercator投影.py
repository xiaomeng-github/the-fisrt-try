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
fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(1,2,1,projection=ccrs.Mercator())
ax1.add_feature(cfeature.COASTLINE.with_scale('50m'))
gl1=ax1.gridlines(draw_labels=True,x_inline=False,y_inline=False)
gl1.xlabels_top=False
gl1.ylabels_right=False
plt.show()
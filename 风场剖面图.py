import matplotlib.pyplot as plt
import xarray as xr

f_u=xr.open_dataset("D:/test_data/uwnd.mon.mean.nc")
u=f_u['uwnd'].loc[f_u.time.dt.month.isin([6,7,8])].loc['1979-01-01':'2019-12-01',1000:100,45:30,:].mean(['lat','time'])
f_w=xr.open_dataset("D:/test_data/omega.mon.mean.nc")
w=f_w['omega'].loc[f_w.time.dt.month.isin([6,7,8])].loc['1979-01-01':'2019-12-01',1000:100,45:30,:].mean(['lat','time'])


level=f_u['level'].loc[1000:100]
lon=f_u['lon']

##错误出现在在figure中F大写
fig=plt.figure(figsize=(15,8))

ax=fig.add_axes((0.1,0.1,0.8,0.8))

ax.set_yscale('symlog')
ax.set_yticks([1000,500,300,200,100])
ax.set_yticklabels(['1000','500','300','200','100'])
ax.invert_yaxis()

ax.set_ylabel('Level',fontsize=16)
ax.set_xlabel('Longitute',fontsize=16)
ax.quiver(lon[::2],level,u[:,::2],w[:,::2]*(-150),scale=150)
plt.show()


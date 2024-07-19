from scipy.stats import pearsonr
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

x=np.random.random(40)
y=np.random.random(40)
print(x)
t=13
silide_cor=np.zeros((40))
for i in range(0+6,40-6,1):
    print(i)
    silide_cor[i]=pearsonr(x[i-6:i+7],y[i-6:i+7])[0]
silide_cor[silide_cor==0]=np.nan

silide_cor=xr.DataArray(silide_cor,coords=[np.arange(40)],dims=['year'])
print(silide_cor)
silide_cor.plot()
plt.ylim(-1,1)
plt.xlim(0,40)
plt.axhline(0.48,ls='--')
plt.axhline(0.55,ls='-')
plt.axhline(-0.48,ls='--')
plt.axhline(-0.55,ls='-')
plt.show()
import numpy as np

a=np.array([1,2,3,4,5,6,np.nan,8,9,10])
print(a.mean())
print(a.nanmean())
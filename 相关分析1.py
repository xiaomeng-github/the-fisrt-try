from scipy.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt

a=np.array([4,6,8,4,1,0,3,5,9,8,5,3,6,7,4,9,8,3,1,5,6,4,0,1,8])
b=np.array([9,8,5,9,3,6,2,7,7,6,3,0,1,4,5,8,9,6,15,3,7,8,2,4,5])

fig=plt.figure(figsize=(12,8))
# plt.plot(np.arange(a.shape[0]),a,color='r',linewidth=4,label='a')
# plt.plot(np.arange(b.shape[0]),b,color='b',linewidth=4,label='b')
# plt.legend()
# plt.show()
ax=fig.add_axes((0.1,0.1,0.4,0.3))
ax.plot(np.arange(a.shape[0]),a,color='r',linewidth=4,label='a')
ax.plot(np.arange(b.shape[0]),b,color='b',linewidth=4,label='b')
ax.legend()

print('Rab={}'.format(pearsonr(a,b)[0]))

#加入线性趋势
a1=2*np.arange(a.shape[0])+a
b1=2*np.arange(b.shape[0])+b
ax1=fig.add_axes((0.4,0.4,0.4,0.3))
ax1.plot(np.arange(a.shape[0]),a1,color='r',linewidth=4,label='a1')
ax1.plot(np.arange(b.shape[0]),b1,color='b',linewidth=4,label='b1')
ax1.legend()
plt.show()
print('Rab={}'.format(pearsonr(a,b)[0]))
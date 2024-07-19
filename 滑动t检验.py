import numpy as np
import matplotlib.pyplot as plt
#步长需要不断调整
def slidet(inputdata,step):
    inputdata=np.array(inputdata)
    n=inputdata.shape[0]#n=len(inputdata)
    n1=step
    n2=step
    t=np.zeros(n)
    for i in range(step,n-step-1):
        x1=inputdata[i-step:i]
        x2=inputdata[i:i+step]
        x1_mean=np.mean(x1) #若序列中有na，则需要将函数改为np.nanmean
        x2_mean=np.mean(x2)
        s1=np.var(x1)
        s2=np.var(x2)
        s=np.sqrt((n1*s1+n2*s2)/(n1+n2-2))
        t[i]=(x1_mean-x2_mean)/(s*np.sqrt(1/n1+1/n2))
    t[:step]=np.nan
    t[n-step+1:]=np.nan
    return t

a=[15.4,14.6,15.8,14.8,15.0,15.1,15.1,15.0,15.2,15.4,
   14.8,15.0,15.1,14.7,16.0,15.7,15.4,14.5,15.1,15.3,
   15.5,15.1,15.6,15.1,14.9,15.5,15.3,15.3,15.4,15.4,
   15.7,15.2,15.5,15.5,15.6,15.1,15.1,16.0,16.0,16.8,
   16.2,16.2,16,15.6,15.9,16.2,16.7,15.8,16.2,15.9,
   15.8,15.5,15.9,16.8,15.5,15.8,15.0,14.9,15.3,16.0,
   16.1,16.5,15.5,15.6,16.1,15.6,16.0,15.4,15.5,15.2,
   15.4,15.6,15.1,15.8,15.5,16.0,15.2,15.8,16.2,16.2,
   15.2,15.7,16.0,16.0,15.7,15.9,15.7,16.7,15.3,16.1]
t=slidet(a,10)
# print(t)
plt.figure(figsize=(10,5))
plt.plot(t,'r')
plt.axhline(1.8598)
plt.axhline(-1.8595,alpha=0.5)
#共用x轴，绘制出原始数据
plt.twinx()
plt.plot(a,'k')

plt.show()
import numpy as np
import matplotlib.pyplot as plt

def mktest(inputdata):
    inputdata=np.array(inputdata)
    n=inputdata.shape[0]
    sk=np.zeros(n)
    UFk=np.zeros(n)
    r=0
    for i in range(1,n):
        for j in range(i):
            if inputdata[i]>inputdata[j]:
                r+=1
        sk[i]=r
        E=(i+1)*i/4
        Var=(i+1)*i*(2*i+7)/72
        UFk[i]=(sk[i]-E)/np.sqrt(Var)

    inputdataT=inputdata[::-1]
    sk2 = np.zeros(n)
    UBk = np.zeros(n)
    r = 0
    for i in range(1,n):
        for j in range(i):
            if inputdataT[i]>inputdataT[j]:
                r+=1
        sk2[i] = r
        E = (i + 1) * i / 4
        Var = (i + 1) * i * (2 * i + 7) / 72
        UBk[i] = (sk[i] - E) / np.sqrt(Var)
    UBk2=UBk[::-1]

    return UFk,UBk2

a=[15.4,14.6,15.8,14.8,15.0,15.1,15.1,15.0,15.2,15.4,
   14.8,15.0,15.1,14.7,16.0,15.7,15.4,14.5,15.1,15.3,
   15.5,15.1,15.6,15.1,14.9,15.5,15.3,15.3,15.4,15.4,
   15.7,15.2,15.5,15.5,15.6,15.1,15.1,16.0,16.0,16.8,
   16.2,16.2,16.0,15.6,15.9,16.2,16.7,15.8,16.2,15.9,
   15.8,15.5,15.9,16.8,15.5,15.8,15.0,14.9,15.3,16.0,
   16.1,16.5,15.5,15.6,16.1,15.6,16.0,15.4,15.5,15.2,
   15.4,15.6,15.1,15.8,15.5,16.0,15.2,15.8,16.2,16.2,
   15.2,15.7,16.0,16.0,15.7,15.9,15.7,16.7,15.3,16.1]
uf,ub=mktest(a)
plt.figure(figsize=(10,5))
plt.plot(uf,'r',label='UFk')
plt.plot(ub,'k',label='UBk')
plt.legend()
plt.axhline(1.96)
plt.axhline(-1.96)
plt.show()
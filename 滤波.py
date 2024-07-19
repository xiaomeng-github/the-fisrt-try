import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
x = np.array([ 1.438037  ,  0.56234264,  0.3169084 ,  0.06911968,  0.5665623 ,
        1.5300182 ,  0.58640814,  0.31758106,  1.4876018 , -0.7618939 ,
        0.35573307, -0.95838505, -0.92782617, -0.5511353 ,  0.14957434,
       -1.0467534 , -0.46021378, -0.46028218, -1.4724817 , -0.06936611,
       -0.43971166,  1.8169147 , -1.605958  , -1.0131035 , -1.1547837 ,
        0.15563792, -0.25747752, -1.3881027 , -0.68700427, -0.2095188 ,
        1.7450378 ,  0.3366057 ,  0.93491715,  1.080349  ,  0.27542242,
       -1.605958  ,  1.9339806 , -0.9839922 ,  0.39519355])

sample_fre=1 #采样频率
nyquist_frequency=sample_fre*0.5 #防止信号混叠，所需定义的最小采样频率
cutoff=1/10 #截至频率，采取低频讯号，周期为10
lowcut=cutoff/nyquist_frequency

cutoff=1/3 #三年以下的信号提取出来
highcut=cutoff/nyquist_frequency

#创建滤波器
b,a,*_=signal.butter(2,lowcut,'lowpass')
x_low=signal.filtfilt(b,a,x)

b,a,*_=signal.butter(2,highcut,'highpass')
x_high=signal.filtfilt(b,a,x)

b,a,*_=signal.butter(2,[lowcut,highcut],'bandpass')
x_band=signal.filtfilt(b,a,x)

plt.figure(figsize=(10,5))
plt.ylim(-2,2)
plt.axhline(0,linestyle='-',c='k')
plt.plot(x,c='k')

plt.plot(x_low,c='r',label='low')
plt.plot(x_high,c='g',label='high')
plt.plot(x_band,c='b',label='band')
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

a = np.array([ 1.438037  ,  0.56234264,  0.3169084 ,  0.06911968,  0.5665623 ,
        1.5300182 ,  0.58640814,  0.31758106,  1.4876018 , -0.7618939 ,
        0.35573307, -0.95838505, -0.92782617, -0.5511353 ,  0.14957434,
       -1.0467534 , -0.46021378, -0.46028218, -1.4724817 , -0.06936611,
       -0.43971166,  1.8169147 , -1.605958  , -1.0131035 , -1.1547837 ,
        0.15563792, -0.25747752, -1.3881027 , -0.68700427, -0.2095188 ,
        1.7450378 ,  0.3366057 ,  0.93491715,  1.080349  ,  0.27542242,
       -1.605958  ,  1.9339806 , -0.9839922 ,  0.39519355])

plt.figure(figsize=(10,5))
# plt.ylim(-3,3)
plt.axhline(0,linestyle="-",c='k')
# plt.plot(a,c='k')
# plt.show()

a_9_valid=np.convolve(a,np.repeat(1/9,9),mode='valid')
a_9_full=np.convolve(a,np.repeat(1/9,9),mode='full')
a_9_same=np.convolve(a,np.repeat(1/9,9),mode='same')
# plt.plot(a_9_valid,color='r')
# plt.plot(a_9_full,color='g')
# plt.plot(a_9_same,color='b')
# plt.show()

#调整x轴的格式，使其对应起来


plt.plot(np.arange(-4,43),a_9_full,color='b')
plt.plot(np.arange(39),a_9_same,color='g')
plt.plot(np.arange(4,35),a_9_valid,color='r')
plt.plot(a,c='k')
plt.show()
import numpy as np
import xarray as xr
import datetime as dt
#简单示例
# arr=np.array([1,1,1,1,1,0,0,1,1,0])
# print(arr)
# print(arr[1:])
# print(arr[:-1])
# tem=arr[1:]+arr[:-1]
# if arr[0]==0:
#     tem=np.insert(tem,0,0)
# else:
#     tem=np.insert(tem,0,1)
# print(tem)
'''此代码是基于31年的每年31天的气温数据'''

tem=xr.open_dataset("D:/test_data/t1980_2010.nc")
print(tem)
#选取某一点的8月份的温度数据进行分析
t2m=tem.air.loc[tem.time.dt.month.isin(8),39.047,120]-273.15
t2m_array=np.array(t2m)
# print(t2m_array)
import matplotlib.pyplot as plt
# fig,ax=plt.subplots(1,1)
# ax.hist(t2m_array,bins=30)
# plt.show()

#极端事件指数（绝对）
print(t2m_array.shape)
#判断有多少天的温度大于28度
# day=0
# for i in range(t2m_array.shape[0]):
#     if(t2m_array[i]>28):
#         day+=1
# print(day)
# print((t2m_array>28).sum())
#
# #判断每年中8月份温度大于28度发天数
t2_re=t2m_array.reshape((31,31))
print(t2_re)
# print(t2_re.shape)
# days=np.zeros((31))
# for i in range(t2_re.shape[0]):
#     for j in range(t2_re.shape[1]):
#         if t2_re[i,j]>28:
#             days[i]+=1
# print(days)
# print((t2_re>28).sum(axis=1))  #等效于循环结构


#连续天数
days=np.zeros((31,31))
days[t2_re>26]=1
print(days)


t6=np.zeros(31)
for y in range(t2_re.shape[0]):
# for y in range(9,10):
    #逐日错位相加
    tmp=days[y,1:]+days[y,:-1]
    if days[y,0]==0: #上次错误出现在这里
        tmp=np.insert(tmp,0,0)
    else:
        tmp=np.insert(tmp,0,1)
    print(tmp)
    print(len(tmp))
    # print(days[y])
    loc=np.arange(t2_re.shape[1])
    # print(loc)
    loc=loc[tmp==1]
    print(loc)
    #跳位循环
    d=[]
    for i in range(0,loc.shape[0],2):
        n=loc[i+1]-loc[i]
        d.append(n)
    print(d)
    #判断一年中大于6天的个数
    d=np.array(d)
    t6[y]=d[d>6].sum()
    # print(t6)
print(t6)
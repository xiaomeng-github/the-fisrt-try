import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

x=np.array([[1,2],[1.5,1.8],[5,8],[8,8],[1,0.6],[9,11]])
plt.scatter(x[:,0],x[:,1])
# plt.show()


clf=KMeans(n_clusters=2) #将模型分为两组
clf.fit(x) #将数据放入模型
centers=clf.cluster_centers_ #获取两组数据点的中心点
labels=clf.labels_ #获取每组数据点所属的分类
# print(centers)
# print(labels)

#分类结果
for i in range(len(labels)):
    plt.scatter(x[i][0],x[i][1],c=('r' if labels[i]==0 else 'b'))
plt.scatter(centers[:,0],centers[:,1],marker='*',s=100) #s表示大小
# plt.show()

##预测
predict=[[2,1],[6,9]]
label=clf.predict(predict)

for i in range(len(label)):
    plt.scatter(predict[i][0],predict[i][1],c=('r' if label[i]==0 else 'b'))
# plt.show()


from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


#判断模型的好坏
feature,true_labels=make_blobs(n_samples=200,centers=3,cluster_std=2.75,random_state=42)
# print(feature)
# print(true_labels)

##标准化数据？？？
scaler=StandardScaler()
scaled_feature=scaler.fit_transform(feature)
# print(scaler)
# print(scaled_feature)


##SSE
# sse=[]
# for k in range(1,11):
#     kmean=KMeans(n_clusters=k)
#     kmean.fit(scaled_feature)
#     sse.append(kmean.inertia_)
#
# plt.plot(range(1,11),sse)
# plt.xticks(range(1,11))
# plt.xlabel('number of cluster')
# plt.ylabel('sse')
# plt.show()

##轮廓系数法

silhouette_coefficients=[]
for k in range(2,11):
    kmean=KMeans(n_clusters=k)
    kmean.fit(scaled_feature)
    score=silhouette_score(scaled_feature,kmean.labels_)
    silhouette_coefficients.append(score)
plt.plot(range(2,11),silhouette_coefficients)
plt.xticks(range(2,11))
plt.xlabel('number of cluster')
plt.ylim(0,1)
plt.ylabel('silhouette coefficient')
plt.show()
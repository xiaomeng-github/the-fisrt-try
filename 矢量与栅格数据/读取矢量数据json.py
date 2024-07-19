from osgeo import ogr
import requests
import matplotlib.pyplot as plt

ur1 = 'https://geojson.cn/api/data/china.topo.json' #https://geojson.cn/api/data/china.topo.json

r = requests.get(ur1, timeout=30)
status = r.raise_for_status()  # 返回网址状态 r.status_code
r.encoding = r.apparent_encoding  # 编码格式

# print(r.text[0:1000]) #查看获取到的数据
# print(r.text)
# 得到datasource
ds = ogr.Open(r.text)  # 'osgeo.ogr.DataSource'

# 获得layer,只有一个图层
lyr = ds.GetLayer(0)  # sgeo.ogr.Layer

# 查看图层有多少个features
print(lyr.GetFeatureCount())

# 遍历layer每一个要素,即每一个feature
for row in lyr:
    name = row.GetField('name')  # 也可以通过索引进行打印输出
    # print('name:', name)
    geom=row.geometry() #得到geometry属性:类型、坐标,即封闭的环 Mulpolygon，两个括号
    # print(geom)
    #得到线围绕的环，即外边界
    ring=geom.GetGeometryRef(0) #得到polygon，线类型，一个括号
    # print(ring)
    coords=ring.GetPoints()  #点坐标
    # print(coords)

    x,y=zip(*coords)
    plt.plot(x,y,'black')
    plt.fill(x,y,'p')

    i=x[0]
    j=x[0]
    plt.text(i,j,name)
plt.axis('equal')
plt.show()



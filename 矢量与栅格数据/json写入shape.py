import matplotlib.pyplot as plt
from osgeo import ogr  #矢量数据读取
import requests
from osgeo import osr  #坐标系统
import json

ur1='https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'

r=requests.get(ur1,timeout=30)
r.raise_for_status()
r.encoding=r.apparent_encoding
print(requests.head(ur1).headers)


geojsonData=json.loads(r.text) #读取json文件内容 class:dict字典类型
#driver得到datasource，datasource得到layer
driver=ogr.GetDriverByName('ESRI Shapefile') #驱动器
ds2=driver.CreateDataSource('test_cx.shp')  #默认当前路径，可以给出绝对路径

targetSR=osr.SpatialReference()  #空间参考
targetSR.ImportFromEPSG(4326) #Geo WGS84
layer2=ds2.CreateLayer('testcx',targetSR,geom_type=ogr.wkbPoint)

#T通过layer创建属性表,
fieldDefn=ogr.FieldDefn('region',ogr.OFTString)
fieldDefn.SetWidth(200) #宽度
layer2.CreateField(fieldDefn)
layer2.CreateField(ogr.FieldDefn('latitude',ogr.OFTReal)) #ogr.OFTReal数据类型
layer2.CreateField(ogr.FieldDefn('longitude',ogr.OFTReal))
layer2.CreateField(ogr.FieldDefn('id'),ogr.OFTInteger)
layer2.CreateField(ogr.FieldDefn('Magnitude',ogr.OFTReal)) #震级
layer2.CreateField(ogr.FieldDefn('Depth',ogr.OFTReal))

i=0
allFeatures=geojsonData['features']
for fea in allFeatures:
    row=fea['properties']
    region=row['place']
    magnitude=row['mag']
    if magnitude is None:
        continue
    if(magnitude and float(magnitude))>=1:
        lat=fea['geometry']['coordinates'][0]
        log=fea['geometry']['coordinates'][1]
        deep=fea['geometry']['coordinates'][2]
        #开始写入

        featureDefn=layer2.GetLayerDefn() #所有的features的属性表
        feature=ogr.Feature(featureDefn) #创建feature对象，具有那个表结构
        #填写内容
        feature.SetField('id',i)
        feature.SetField('Re  gion',region)
        feature.SetField('Latitude',lat)
        feature.SetField('longitude',log)
        feature.SetField('Magnitude',magnitude)
        feature.SetField("Depth",deep)

        point=ogr.Geometry(ogr.wkbPoint)
        point.AddPoint(float(lat),float(log)) #给点添加位置信息，点坐标
        feature.SetGeometry(point)

        layer2.CreateFeature(feature)   #在layer属性表里添加一行
        i+=1

        plt.plot(float(lat),float(log),'o',markersize=5)
plt.axis('equal')
plt.show()

del ds2  #如果不删除，就不会写到硬盘里面，释放占据的内存空间
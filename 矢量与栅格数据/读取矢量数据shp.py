#读取shp中的点、线、面并且显示
import matplotlib.pyplot as plt
import requests
from osgeo import ogr

driver=ogr.GetDriverByName('ESRI Shapefile')

#面
# ds=ogr.Open(r"C:\Users\TAN\Desktop\date\china_Province_shp\省级行政区.shp")
# # print("ds.type",type(ds)) #DataSource
# layer_polygon=ds.GetLayer(0)
# for row in layer_polygon:
#     print(row.GetField(1))
#     geom=row.geometry()
#     ring=geom.GetGeometryRef(0)
#     coords=ring.GetPoints()
#     x,y=zip(*coords)
#     plt.plot(x,y,'k')
#     plt.fill(x,y,'p')
# print('geometry:',geom)
# print('ring',ring)
# print('geomtryname:',geom.GetGeomtryName())
#线,中国一级河流
ds1=ogr.Open("C:/Users/TAN/Desktop/date/R1/hyd1_4p.shp")
# print("ds.type",type(ds)) #DataSource
layer_line=ds1.GetLayer(0)
for feature in layer_line:

    geom=feature.geometry()

    coords=geom.GetPoints()
    if coords is None:
        continue
    x,y=zip(*coords)
    plt.plot(x,y,'r')
plt.show()
# print('geometry:',geom)
# print('geomtryname:',geom.GetGeometryName())

#点，中国居民点
# ds2 = ogr.Open(r"C:/Users/TAN/Desktop/date/County_pt/XianCh_point.shp")
# # print("ds.type",type(ds)) #DataSource
# layer_Point = ds2.GetLayer(0)
# for feature in layer_Point:
#
#     geom = feature.geometry()
#
#     x=geom.GetX()
#     y=geom.GetY()
#     plt.plot(x, y, 'o',markersize=5,color='k')
#     plt.text(x,y,'test')
# # plt.show()
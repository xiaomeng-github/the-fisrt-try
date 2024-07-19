import os
from osgeo import ogr
from osgeo import osr
import json
import requests
import matplotlib.pyplot as plt

#显示multipolygon
def myDispalyMultiPolygon(myMultipolygon):
    for i in range(myMultipolygon.GetGeometryCount()):
        ring=myMultipolygon.GetGeometryRef(i) #得到每一个polygon
        subring=ring.GetGeometryRef(0)  #得到闭环线的所以坐标
        coords=subring.GetPoints()
        x,y=zip(*coords) #将x,y坐标解包
        plt.plot(x,y,'black')
        plt.fill(x,y,'p')

#自适应显示polygon和multipolygon
def myDisplayPolygon(lyr):
    for row in lyr:
        print('row:',row)
        geom=row.geometry
        print('geom:',geom.GetGeometryName(),'count:',geom.GetGeomtryCount())
        print('geom:',geom)
        if (geom.GetGeometryName()=='MULTIPOLYGON'):
            for i in range(geom.GetGeomtryCount()):
                ring=geom.GetGeomtryRef(i)
                print('ring:',ring)
                subring=ring.GetGeometryRef(0)
                print('subring:',subring)
                coords=subring.GetPoints()
                print('coords:',coords)
                x,y=zip(*coords)
                plt.plot(x,y,'black')
                plt.fill(x,y,'p')
        else:
            ring=geom.GetFeometryRef(0)
            print('ring:',ring)
            coords=ring.GetPoints()
            print('coords:',coords)
            x,y=zip(*coords)

        plt.plot(x,y,'black')
        plt.fill(x,y,'p')

#由Geojson创建Multipolygon
def creatMultiPolygonFromPloygonJson():
    myMultipolygon=ogr.Geometry(ogr.wkbMultiPolygon) #创建空的multipolygon
    ds=ogr.Open('china.json')
    lyr=ds.GetLayer()
    for feature in lyr:
        geom=feature.geometry()
        myMultipolygon.AddGeometry(geom)
    print(myMultipolygon)
    return myMultipolygon
#由Geojson创建shp

















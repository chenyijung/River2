from django.db import models

# Create your models here.
class RiverStation(models.Model):
    riverName = models.CharField(max_length=10) #河川名稱
    areaName = models.CharField(max_length=10) #流域別
    stationName = models.CharField(max_length=10) #監測站名稱
    riverStandard = models.CharField(max_length=10,null=True) #水體分類標準
    riverstationNumber = models.IntegerField(default=0) #監測站編號
    distanceKM = models.CharField(max_length=10,null=True) #距離流口距離（公里）
    stationAddress = models.TextField(max_length=50) #監測站位址（地址）
    stationLocationEast = models.CharField(max_length=10) #監測站座標（東經）
    stationLocationNorth = models.CharField(max_length=10) #監測站座標（北緯）
    stationModeBridge = models.CharField(max_length=10,null=True) #採樣方式（橋上）
    stationModeRiver = models.CharField(max_length=10,null=True) #採樣方式（河中）
    stationModeRiverside = models.CharField(max_length=10,null=True) #採樣方式（岸邊）
    monitorItem = models.TextField(max_length=100,null=True) #監測項目


#    def __str__(self):
#       return self.name

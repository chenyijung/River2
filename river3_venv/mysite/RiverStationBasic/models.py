from django.db import models

# Create your models here.
class RiverStation(models.Model):
    riverName = models.CharField("河川名",max_length=10) #河川名稱

    areaName = models.CharField("流域別",max_length=10) #流域別
    stationName = models.CharField("監測站名稱",max_length=10) #監測站名稱
    riverStandard = models.CharField("水體分類標準",max_length=10,null=True) #水體分類標準
    riverstationNumber = models.IntegerField("監測站編號",default=0) #監測站編號
    distanceKM = models.CharField("距離流口距離（公里）",max_length=10,null=True) #距離流口距離（公里）
    stationAddress = models.TextField("監測站位址（地址）",max_length=50) #監測站位址（地址）
    stationLocationEast = models.CharField("監測站座標（東經）",max_length=10) #監測站座標（東經）
    stationLocationNorth = models.CharField("監測站座標（北緯）",max_length=10) #監測站座標（北緯）
    stationModeBridge = models.CharField("採樣方式（橋上）",max_length=10,null=True) #採樣方式（橋上）
    stationModeRiver = models.CharField("採樣方式（河中）",max_length=10,null=True) #採樣方式（河中）
    stationModeRiverside = models.CharField("採樣方式（岸邊）",max_length=10,null=True) #採樣方式（岸邊）
    monitorItem = models.TextField("監測項目",max_length=100,null=True) #監測項目

    class Meta:
        verbose_name="河川測站基本資料"
        verbose_name_plural="河川測站基本資料"

#    def __str__(self):
#       return self.name

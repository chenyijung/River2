from django.db import models

# Create your models here.
class OceanInspectModel(models.Model):
    riverName = models.CharField(max_length=10,null=True) #河川名稱
    stationName = models.CharField(max_length=10,null=True) #監測站名稱
    riverstationNumber = models.IntegerField(default=0,null=True) #監測站編號
    riverStandard = models.CharField(max_length=10,null=True) #水體分類等級
    inspectDate = models.DateField(null=True) #採樣日期
    inspectTime = models.TimeField(null=True) #採樣時間
    inspectAirTemp = models.FloatField(null=True) #氣溫
    inspectCMS = models.FloatField(null=True) #水流量
    inspectWaterTemp = models.FloatField(null=True) #水溫
    inspectPH = models.FloatField(null=True) #PH值
    inspectO2 = models.FloatField(null=True) #溶氧量
    inspectTN = models.FloatField(null=True) #總氮
    inspectTP = models.FloatField(null=True) #總磷
    inspectBOD = models.FloatField(null=True) #生化需氧量
    inspectCOD = models.FloatField(null=True) #化學需氧量
    inspectSS = models.FloatField(null=True) #懸浮固體
    inspectCd = models.FloatField(null=True) #鎘
    inspectPb = models.FloatField(null=True) #鉛
    inspectCr = models.FloatField(null=True) #鉻
    inspectNi = models.FloatField(null=True) #鎳
    inspectCu = models.FloatField(null=True) #銅
    inspectZn = models.FloatField(null=True) #鋅
    inspectMn = models.FloatField(null=True) #錳
    inspectEle = models.IntegerField(default=0,null=True) #導電度
    inspectCFU = models.FloatField(null=True) #大腸桿菌群
    inspectMPN = models.FloatField(null=True)#腸球菌
    inspectN2 = models.FloatField(null=True) #氨氣
    inspectPSU = models.FloatField(null=True) #鹽度
    inspectNTU = models.FloatField(null=True) #濁度
    inspectPO34 = models.FloatField(null=True) #磷酸鹽
    inspectSixOy = models.FloatField(null=True) #矽酸鹽
    inspectNO3N = models.FloatField(null=True) #硝酸鹽氮
    inspectNO2N = models.FloatField(null=True) #亞硝酸鹽氮
    inspectComment = models.TextField(max_length=100,null=True)#備註

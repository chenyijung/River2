from django.db import models

# Create your models here.
class RiverInspectModel(models.Model):
    riverName = models.CharField("河川名稱",max_length=10,null=True) #河川名稱
    stationName = models.CharField("監測站名稱",max_length=10,null=True) #監測站名稱
    riverstationNumber = models.IntegerField("監測站編號",default=0,null=True) #監測站編號
    riverStandard = models.CharField("水體分類等級",max_length=10,null=True) #水體分類等級
    inspectDate = models.DateField("採樣日期",null=True) #採樣日期
    inspectTime = models.TimeField("採樣時間",null=True) #採樣時間
    inspectAirTemp = models.FloatField("氣溫",null=True) #氣溫
    inspectCMS = models.FloatField("水流量",null=True) #水流量
    inspectWaterTemp = models.FloatField("水溫",null=True) #水溫
    inspectPH = models.FloatField("PH值",null=True) #PH值
    inspectO2 = models.FloatField("溶氧量",null=True) #溶氧量
    inspectTN = models.FloatField("總氮",null=True) #總氮
    inspectTP = models.FloatField("總磷",null=True) #總磷
    inspectBOD = models.FloatField("生化需氧量",null=True) #生化需氧量
    inspectCOD = models.FloatField("化學需氧量",null=True) #化學需氧量
    inspectSS = models.FloatField("懸浮固體",null=True) #懸浮固體
    inspectCd = models.FloatField("鎘",null=True) #鎘
    inspectPb = models.FloatField("鉛",null=True) #鉛
    inspectCr = models.FloatField("鉻",null=True) #鉻
    inspectNi = models.FloatField("鎳",null=True) #鎳
    inspectCu = models.FloatField("銅",null=True) #銅
    inspectZn = models.FloatField("鋅",null=True) #鋅
    inspectMn = models.FloatField("錳",null=True) #錳
    inspectEle = models.IntegerField("導電度",default=0,null=True) #導電度
    inspectCFU = models.FloatField("大腸桿菌群",null=True) #大腸桿菌群
    inspectAnionic = models.FloatField("陰離子界面活性劑",null=True)#陰離子界面活性劑
    inspectN2 = models.FloatField("氨氣",null=True) #氨氣
    inpectOrgC = models.FloatField("總有機碳",null=True)#總有機碳
    inspectPers = models.FloatField("透視度",null=True)#透視度
    inspectOil = models.FloatField("油脂",null=True)#油脂
    inspectNTU = models.FloatField("濁度",null=True)#濁度
    inspectNO3N = models.FloatField("硝酸鹽氮",null=True)#硝酸鹽氮
    inspectNO2N = models.FloatField("亞硝酸鹽氮",null=True)#亞硝酸鹽氮
    inspectComment = models.TextField("備註",max_length=100,null=True) #備註


class RiverInspectExport(models.Model):
    stationName = models.CharField("河川名稱",max_length=10,null=True) #河川名稱
    inspectO2 = models.FloatField("溶氧量",null=True) #溶氧量
    inspectBOD = models.FloatField("生化需氧量",null=True) #生化需氧量
    inspectSS = models.FloatField("懸浮固體",null=True) #懸浮固體
    inspectN2 = models.FloatField("氨氣",null=True) #氨氣
    RPI_Point= models.FloatField("RPI值",null=True) #RPI值
    RPI_Result= models.TextField("污染程度",max_length=100,null=True) #污染程度


class RiverInspectExportWQI(model.Models):
    stationName = models.CharField("水質測站",max_length=10,null=True) #監測站名稱
    inspectPH = models.FloatField("PH值",null=True) #PH值
    inspectO2 = models.FloatField("溶氧量",null=True) #溶氧量
    inspectBOD = models.FloatField("生化需氧量",null=True) #生化需氧量
    inspectSS = models.FloatField("懸浮固體",null=True) #懸浮固體
    inspectCFU = models.FloatField("大腸桿菌群",null=True) #大腸桿菌群
    inspectN2 = models.FloatField("氨氣",null=True) #氨氣
    inspectTP = models.FloatField("總磷",null=True) #總磷
    riverStandardPoint = models.FloatField("水體分類等級",max_length=10,null=True) #水體分類等級-點數
    riverStandard = models.CharField("水體分類",max_length=10,null=True) #水體分類

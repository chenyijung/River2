# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OceanInspect', '0005_delete_oceaninspectexport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oceaninspectmodel',
            options={'verbose_name': '海洋監測報表', 'verbose_name_plural': '海洋監測報表'},
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectAirTemp',
            field=models.FloatField(verbose_name='氣溫', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectBOD',
            field=models.FloatField(verbose_name='生化需氧量', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectCFU',
            field=models.FloatField(verbose_name='大腸桿菌群', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectCMS',
            field=models.FloatField(verbose_name='水流量', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectCOD',
            field=models.FloatField(verbose_name='化學需氧量', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectCd',
            field=models.FloatField(verbose_name='鎘', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectComment',
            field=models.TextField(verbose_name='備註', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectCr',
            field=models.FloatField(verbose_name='鉻', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectCu',
            field=models.FloatField(verbose_name='銅', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectDate',
            field=models.DateField(verbose_name='採樣日期', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectEle',
            field=models.IntegerField(verbose_name='導電度', null=True, default=0),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectMPN',
            field=models.FloatField(verbose_name='腸球菌', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectMn',
            field=models.FloatField(verbose_name='錳', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectN2',
            field=models.FloatField(verbose_name='氨氣', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectNO2N',
            field=models.FloatField(verbose_name='亞硝酸鹽氮', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectNO3N',
            field=models.FloatField(verbose_name='硝酸鹽氮', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectNTU',
            field=models.FloatField(verbose_name='濁度', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectNi',
            field=models.FloatField(verbose_name='鎳', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectO2',
            field=models.FloatField(verbose_name='溶氧量', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectPH',
            field=models.FloatField(verbose_name='PH值', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectPO34',
            field=models.FloatField(verbose_name='磷酸鹽', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectPSU',
            field=models.FloatField(verbose_name='鹽度', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectPb',
            field=models.FloatField(verbose_name='鉛', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectSS',
            field=models.FloatField(verbose_name='懸浮固體', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectSixOy',
            field=models.FloatField(verbose_name='矽酸鹽', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectTN',
            field=models.FloatField(verbose_name='總氮', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectTP',
            field=models.FloatField(verbose_name='總磷', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectTime',
            field=models.TimeField(verbose_name='採樣時間', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectWaterTemp',
            field=models.FloatField(verbose_name='水溫', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='inspectZn',
            field=models.FloatField(verbose_name='鋅', null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='riverName',
            field=models.CharField(verbose_name='河川名稱', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='riverStandard',
            field=models.CharField(verbose_name='水體分類等級', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='riverstationNumber',
            field=models.IntegerField(verbose_name='監測站編號', null=True, default=0),
        ),
        migrations.AlterField(
            model_name='oceaninspectmodel',
            name='stationName',
            field=models.CharField(verbose_name='監測站名稱', max_length=10, null=True),
        ),
    ]

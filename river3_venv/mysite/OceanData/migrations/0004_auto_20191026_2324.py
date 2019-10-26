# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OceanData', '0003_auto_20191025_1919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oceandatamodel',
            options={'verbose_name': '海洋測站基本資料', 'verbose_name_plural': '海洋測站基本資料'},
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='areaName',
            field=models.CharField(verbose_name='流域別', max_length=10),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='distanceKM',
            field=models.TextField(verbose_name='距離流口距離（公里）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='monitorItem',
            field=models.TextField(verbose_name='監測項目', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='riverName',
            field=models.CharField(verbose_name='河川名稱', max_length=10),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='riverStandard',
            field=models.CharField(verbose_name='水體分類標準', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='riverstationNumber',
            field=models.IntegerField(verbose_name='監測站編號', default=0),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='stationAddress',
            field=models.TextField(verbose_name='監測站位址（地址）', max_length=50),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='stationLocationEast',
            field=models.CharField(verbose_name='監測站座標（東經）', max_length=10),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='stationLocationNorth',
            field=models.CharField(verbose_name='監測站座標（北緯）', max_length=10),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='stationModeBridge',
            field=models.CharField(verbose_name='採樣方式（船上）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='stationModeRiver',
            field=models.CharField(verbose_name='採樣方式（河中）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='stationModeRiverside',
            field=models.CharField(verbose_name='採樣方式（岸邊）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='oceandatamodel',
            name='stationName',
            field=models.CharField(verbose_name='監測站名稱', max_length=10),
        ),
    ]

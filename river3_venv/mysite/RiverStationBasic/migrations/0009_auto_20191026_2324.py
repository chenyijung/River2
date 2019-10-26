# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverStationBasic', '0008_auto_20191025_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='riverstation',
            options={'verbose_name': '河川測站基本資料', 'verbose_name_plural': '河川測站基本資料'},
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='areaName',
            field=models.CharField(verbose_name='流域別', max_length=10),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='distanceKM',
            field=models.CharField(verbose_name='距離流口距離（公里）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='monitorItem',
            field=models.TextField(verbose_name='監測項目', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='riverName',
            field=models.CharField(verbose_name='河川名', max_length=10),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='riverStandard',
            field=models.CharField(verbose_name='水體分類標準', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='riverstationNumber',
            field=models.IntegerField(verbose_name='監測站編號', default=0),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationAddress',
            field=models.TextField(verbose_name='監測站位址（地址）', max_length=50),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationLocationEast',
            field=models.CharField(verbose_name='監測站座標（東經）', max_length=10),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationLocationNorth',
            field=models.CharField(verbose_name='監測站座標（北緯）', max_length=10),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationModeBridge',
            field=models.CharField(verbose_name='採樣方式（橋上）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationModeRiver',
            field=models.CharField(verbose_name='採樣方式（河中）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationModeRiverside',
            field=models.CharField(verbose_name='採樣方式（岸邊）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationName',
            field=models.CharField(verbose_name='監測站名稱', max_length=10),
        ),
    ]

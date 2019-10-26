# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeachData', '0003_auto_20191025_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beachdatamodel',
            options={'verbose_name': '海灘測站基本資料', 'verbose_name_plural': '海灘測站基本資料'},
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='areaName',
            field=models.CharField(verbose_name='流域別', max_length=10, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='distanceKM',
            field=models.TextField(verbose_name='距離流口距離（公里）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='monitorItem',
            field=models.TextField(verbose_name='監測項目', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='riverName',
            field=models.CharField(verbose_name='河川名稱', max_length=10, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='riverStandard',
            field=models.CharField(verbose_name='水體分類標準', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='riverstationNumber',
            field=models.IntegerField(verbose_name='監測站編號', default=0),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationAddress',
            field=models.TextField(verbose_name='監測站位址（地址）', max_length=50, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationLocationEast',
            field=models.CharField(verbose_name='監測站座標（東經）', max_length=10, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationLocationNorth',
            field=models.CharField(verbose_name='監測站座標（北緯）', max_length=10, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationModeBridge',
            field=models.CharField(verbose_name='採樣方式（船上）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationModeRiver',
            field=models.CharField(verbose_name='採樣方式（河中）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationModeRiverside',
            field=models.CharField(verbose_name='採樣方式（岸邊）', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationName',
            field=models.CharField(verbose_name='監測站名稱', max_length=10, default=0),
            preserve_default=False,
        ),
    ]

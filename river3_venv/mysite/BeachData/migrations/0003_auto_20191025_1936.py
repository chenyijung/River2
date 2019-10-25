# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeachData', '0002_auto_20191025_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beachdatamodel',
            name='areaName',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='distanceKM',
            field=models.TextField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='monitorItem',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='riverName',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='riverStandard',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='riverstationNumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationAddress',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationLocationEast',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationLocationNorth',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationModeBridge',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationModeRiver',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationModeRiverside',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='beachdatamodel',
            name='stationName',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

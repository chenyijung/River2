# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OceanData', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oceandatamodel',
            old_name='NameTest',
            new_name='areaName',
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='distanceKM',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='monitorItem',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='riverName',
            field=models.CharField(max_length=10, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='riverStandard',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='riverstationNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='stationAddress',
            field=models.TextField(max_length=50, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='stationLocationEast',
            field=models.CharField(max_length=10, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='stationLocationNorth',
            field=models.CharField(max_length=10, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='stationModeBridge',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='stationModeRiver',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='stationModeRiverside',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='oceandatamodel',
            name='stationName',
            field=models.CharField(max_length=10, default=1),
            preserve_default=False,
        ),
    ]

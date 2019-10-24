# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiverStation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('riverName', models.CharField(max_length=10)),
                ('areaName', models.CharField(max_length=10)),
                ('stationName', models.CharField(max_length=10)),
                ('riverStandard', models.CharField(max_length=10)),
                ('riverstationNumber', models.CharField(max_length=10)),
                ('distanceKM', models.CharField(max_length=10)),
                ('stationAddress', models.CharField(max_length=10)),
                ('stationLocationEast', models.CharField(max_length=10)),
                ('stationLocationNorth', models.CharField(max_length=10)),
                ('stationModeBridge', models.CharField(max_length=10)),
                ('stationModeRiver', models.CharField(max_length=10)),
                ('stationModeRiverside', models.CharField(max_length=10)),
                ('monitorItem', models.CharField(max_length=10)),
            ],
        ),
    ]

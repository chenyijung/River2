# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverStationBasic', '0005_riverstation_testdata1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riverstation',
            name='TestData1',
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='distanceKM',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='monitorItem',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='riverStandard',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationAddress',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationModeBridge',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationModeRiver',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationModeRiverside',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OceanInspectModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('riverName', models.CharField(max_length=10, null=True)),
                ('stationName', models.CharField(max_length=10, null=True)),
                ('riverstationNumber', models.IntegerField(null=True, default=0)),
                ('riverStandard', models.CharField(max_length=10, null=True)),
                ('inspectDate', models.DateField(null=True)),
                ('inspectTime', models.TimeField(null=True)),
                ('inspectAirTemp', models.FloatField(null=True)),
                ('inspectCMS', models.FloatField(null=True)),
                ('inspectWaterTemp', models.FloatField(null=True)),
                ('inspectPH', models.FloatField(null=True)),
                ('inspectO2', models.FloatField(null=True)),
                ('inspectTN', models.FloatField(null=True)),
                ('inspectTP', models.FloatField(null=True)),
                ('inspectBOD', models.FloatField(null=True)),
                ('inspectCOD', models.FloatField(null=True)),
                ('inspectSS', models.FloatField(null=True)),
                ('inspectCd', models.FloatField(null=True)),
                ('inspectPb', models.FloatField(null=True)),
                ('inspectCr', models.FloatField(null=True)),
                ('inspectNi', models.FloatField(null=True)),
                ('inspectCu', models.FloatField(null=True)),
                ('inspectZn', models.FloatField(null=True)),
                ('inspectMn', models.FloatField(null=True)),
                ('inspectEle', models.IntegerField(null=True, default=0)),
                ('inspectCFU', models.FloatField(null=True)),
                ('inspectMPN', models.FloatField(null=True)),
                ('inspectN2', models.FloatField(null=True)),
                ('inspectPSU', models.FloatField(null=True)),
                ('inspectNTU', models.FloatField(null=True)),
                ('inspectPO34', models.FloatField(null=True)),
                ('inspectSixOy', models.FloatField(null=True)),
                ('inspectNO3N', models.FloatField(null=True)),
                ('inspectNO2N', models.FloatField(null=True)),
                ('inspectComment', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]

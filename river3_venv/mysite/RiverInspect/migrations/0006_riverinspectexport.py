# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverInspect', '0005_auto_20191025_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiverInspectExport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('stationName', models.CharField(max_length=10, null=True)),
                ('inspectO2', models.FloatField(null=True)),
                ('inspectBOD', models.FloatField(null=True)),
                ('inspectSS', models.FloatField(null=True)),
                ('inspectN2', models.FloatField(null=True)),
                ('RPI_Point', models.FloatField(null=True)),
                ('RPI_Result', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]

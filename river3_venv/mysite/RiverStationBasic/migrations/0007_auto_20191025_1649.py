# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverStationBasic', '0006_auto_20191025_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riverstation',
            name='distanceKM',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='monitorItem',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='riverstationNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='stationAddress',
            field=models.TextField(max_length=50),
        ),
    ]

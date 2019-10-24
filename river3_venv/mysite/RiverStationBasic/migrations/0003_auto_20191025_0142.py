# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverStationBasic', '0002_auto_20191025_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riverstation',
            name='TestData1',
            field=models.IntegerField(verbose_name=5),
        ),
        migrations.AlterField(
            model_name='riverstation',
            name='TestData2',
            field=models.IntegerField(verbose_name=5),
        ),
    ]

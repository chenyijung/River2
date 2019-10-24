# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverStationBasic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='riverstation',
            name='TestData1',
            field=models.IntegerField(verbose_name=0, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='riverstation',
            name='TestData2',
            field=models.IntegerField(verbose_name=0, default=0),
            preserve_default=False,
        ),
    ]

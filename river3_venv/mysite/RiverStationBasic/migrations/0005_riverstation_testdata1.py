# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverStationBasic', '0004_auto_20191025_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='riverstation',
            name='TestData1',
            field=models.IntegerField(default=0),
        ),
    ]

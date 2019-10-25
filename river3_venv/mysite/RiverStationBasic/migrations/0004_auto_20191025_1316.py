# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverStationBasic', '0003_auto_20191025_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riverstation',
            name='TestData1',
        ),
        migrations.RemoveField(
            model_name='riverstation',
            name='TestData2',
        ),
    ]

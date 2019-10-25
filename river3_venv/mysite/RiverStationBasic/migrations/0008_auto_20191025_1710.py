# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverStationBasic', '0007_auto_20191025_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riverstation',
            name='distanceKM',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

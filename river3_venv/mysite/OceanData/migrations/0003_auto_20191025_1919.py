# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OceanData', '0002_auto_20191025_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oceandatamodel',
            name='distanceKM',
            field=models.TextField(max_length=10, null=True),
        ),
    ]

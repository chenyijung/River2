# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OceanInspect', '0002_oceaninspectexport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oceaninspectexport',
            name='TestName',
        ),
        migrations.AddField(
            model_name='oceaninspectexport',
            name='TestDataEX',
            field=models.IntegerField(null=True),
        ),
    ]

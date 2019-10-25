# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverInspect', '0002_auto_20191025_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectEle',
            field=models.IntegerField(null=True),
        ),
    ]

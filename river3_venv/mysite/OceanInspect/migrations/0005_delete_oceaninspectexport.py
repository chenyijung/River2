# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OceanInspect', '0004_merge'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OceanInspectExport',
        ),
    ]

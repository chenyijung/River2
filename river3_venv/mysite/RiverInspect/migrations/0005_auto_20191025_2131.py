# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverInspect', '0004_auto_20191025_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectDate',
            field=models.DateField(null=True),
        ),
    ]

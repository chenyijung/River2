# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverInspect', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectTime',
            field=models.TimeField(null=True),
        ),
    ]

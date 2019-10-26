# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverInspect', '0006_riverinspectexport'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiverInspectExportWQI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('stationName', models.CharField(verbose_name='水質測站', max_length=10, null=True)),
                ('inspectPH', models.FloatField(verbose_name='PH值', null=True)),
                ('inspectO2', models.FloatField(verbose_name='溶氧量', null=True)),
                ('inspectBOD', models.FloatField(verbose_name='生化需氧量', null=True)),
                ('inspectSS', models.FloatField(verbose_name='懸浮固體', null=True)),
                ('inspectCFU', models.FloatField(verbose_name='大腸桿菌群', null=True)),
                ('inspectN2', models.FloatField(verbose_name='氨氣', null=True)),
                ('inspectTP', models.FloatField(verbose_name='總磷', null=True)),
                ('riverStandardPoint', models.FloatField(verbose_name='水體分類等級', max_length=10, null=True)),
                ('riverStandard', models.CharField(verbose_name='水體分類', max_length=10, null=True)),
            ],
            options={
                'verbose_name': '河川監測WQI(輸出)',
                'verbose_name_plural': '河川監測WQI(輸出)',
            },
        ),
        migrations.AlterModelOptions(
            name='riverinspectexport',
            options={'verbose_name': '河川監測RPI(輸出)', 'verbose_name_plural': '河川監測RPI(輸出)'},
        ),
        migrations.AlterModelOptions(
            name='riverinspectmodel',
            options={'verbose_name': '河川監測報表', 'verbose_name_plural': '河川監測報表'},
        ),
        migrations.AlterField(
            model_name='riverinspectexport',
            name='RPI_Point',
            field=models.FloatField(verbose_name='RPI值', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectexport',
            name='RPI_Result',
            field=models.TextField(verbose_name='污染程度', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectexport',
            name='inspectBOD',
            field=models.FloatField(verbose_name='生化需氧量', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectexport',
            name='inspectN2',
            field=models.FloatField(verbose_name='氨氣', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectexport',
            name='inspectO2',
            field=models.FloatField(verbose_name='溶氧量', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectexport',
            name='inspectSS',
            field=models.FloatField(verbose_name='懸浮固體', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectexport',
            name='stationName',
            field=models.CharField(verbose_name='河川名稱', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inpectOrgC',
            field=models.FloatField(verbose_name='總有機碳', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectAirTemp',
            field=models.FloatField(verbose_name='氣溫', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectAnionic',
            field=models.FloatField(verbose_name='陰離子界面活性劑', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectBOD',
            field=models.FloatField(verbose_name='生化需氧量', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectCFU',
            field=models.FloatField(verbose_name='大腸桿菌群', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectCMS',
            field=models.FloatField(verbose_name='水流量', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectCOD',
            field=models.FloatField(verbose_name='化學需氧量', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectCd',
            field=models.FloatField(verbose_name='鎘', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectComment',
            field=models.TextField(verbose_name='備註', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectCr',
            field=models.FloatField(verbose_name='鉻', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectCu',
            field=models.FloatField(verbose_name='銅', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectDate',
            field=models.DateField(verbose_name='採樣日期', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectEle',
            field=models.IntegerField(verbose_name='導電度', null=True, default=0),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectMn',
            field=models.FloatField(verbose_name='錳', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectN2',
            field=models.FloatField(verbose_name='氨氣', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectNO2N',
            field=models.FloatField(verbose_name='亞硝酸鹽氮', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectNO3N',
            field=models.FloatField(verbose_name='硝酸鹽氮', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectNTU',
            field=models.FloatField(verbose_name='濁度', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectNi',
            field=models.FloatField(verbose_name='鎳', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectO2',
            field=models.FloatField(verbose_name='溶氧量', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectOil',
            field=models.FloatField(verbose_name='油脂', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectPH',
            field=models.FloatField(verbose_name='PH值', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectPb',
            field=models.FloatField(verbose_name='鉛', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectPers',
            field=models.FloatField(verbose_name='透視度', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectSS',
            field=models.FloatField(verbose_name='懸浮固體', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectTN',
            field=models.FloatField(verbose_name='總氮', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectTP',
            field=models.FloatField(verbose_name='總磷', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectTime',
            field=models.TimeField(verbose_name='採樣時間', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectWaterTemp',
            field=models.FloatField(verbose_name='水溫', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='inspectZn',
            field=models.FloatField(verbose_name='鋅', null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='riverName',
            field=models.CharField(verbose_name='河川名稱', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='riverStandard',
            field=models.CharField(verbose_name='水體分類等級', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='riverstationNumber',
            field=models.IntegerField(verbose_name='監測站編號', null=True, default=0),
        ),
        migrations.AlterField(
            model_name='riverinspectmodel',
            name='stationName',
            field=models.CharField(verbose_name='監測站名稱', max_length=10, null=True),
        ),
    ]

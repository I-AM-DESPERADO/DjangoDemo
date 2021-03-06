# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-06 19:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RadioCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_url', models.URLField(max_length=255, verbose_name='\u5e7f\u64ad\u56fe\u7247')),
                ('note', models.CharField(max_length=255, verbose_name='\u8bf4\u660e')),
                ('picture_timestamp', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RadioConstent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_id', models.IntegerField(verbose_name='\u97f3\u9891\u8282\u76ee')),
                ('program_picture_url', models.URLField(max_length=255, verbose_name='\u56fe\u7247URL')),
                ('program_audio_url', models.URLField(max_length=255, verbose_name='\u97f3\u9891URL')),
                ('program_timestamp', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('program_introduction', models.CharField(max_length=255, null=True)),
                ('program_audio_duration', models.CharField(max_length=255, null=True)),
                ('program_audio_anchor', models.CharField(max_length=255, null=True)),
                ('program_audio_category', models.CharField(max_length=255, null=True)),
                ('note', models.CharField(max_length=255, null=True, verbose_name='\u5e7f\u64ad\u8bf4\u660e')),
            ],
            options={
                'verbose_name': '\u5e7f\u64ad\u5b9e\u4f53',
                'verbose_name_plural': '\u5e7f\u64ad\u5b9e\u4f53',
            },
        ),
        migrations.CreateModel(
            name='RadioProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=255, verbose_name='\u8282\u76ee\u540d\u79f0')),
                ('program_date', models.CharField(max_length=255, verbose_name='\u6570\u636e')),
                ('note', models.CharField(max_length=255, null=True, verbose_name='\u8bf4\u660e')),
                ('program_picture_url', models.URLField(max_length=255, verbose_name='\u56fe\u7247URL')),
            ],
            options={
                'verbose_name': '\u5e7f\u64ad\u8282\u76ee\u4fe1\u606f',
                'verbose_name_plural': '\u5e7f\u64ad\u8282\u76ee\u4fe1\u606f',
            },
        ),
    ]

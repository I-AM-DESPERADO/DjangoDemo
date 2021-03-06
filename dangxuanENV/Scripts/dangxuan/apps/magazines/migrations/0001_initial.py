# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-06 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MagazineList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.CharField(max_length=255, verbose_name='\u6742\u5fd7\u5217\u8868\u540d')),
                ('magazine_program_id', models.IntegerField(verbose_name='\u6742\u5fd7\u680f\u76eeID')),
                ('list_content', models.CharField(max_length=255, verbose_name='\u6742\u5fd7\u5217\u8868\u5185\u5bb9')),
                ('list_writer', models.CharField(max_length=255, verbose_name='\u5217\u8868\u5199\u5165\u4eba')),
                ('insert_time', models.DateTimeField(verbose_name='\u63d2\u5165\u65f6\u95f4')),
                ('note', models.CharField(max_length=255, null=True, verbose_name='\u8bf4\u660e')),
            ],
            options={
                'verbose_name': '\u6742\u5fd7\u5217\u8868\u4fe1\u606f',
                'verbose_name_plural': '\u6742\u5fd7\u5217\u8868\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='MagazineLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_logo_url', models.URLField(max_length=255, verbose_name='\u7b2c\u4e00logo\u7684URl')),
                ('second_logo_url', models.URLField(max_length=255, verbose_name='\u7b2c\u4e8clogo\u7684URL')),
                ('timestamp', models.TimeField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('note', models.CharField(max_length=255, null=True, verbose_name='\u8bf4\u660e')),
                ('logo_flag', models.CharField(max_length=3, verbose_name='logo\u6807\u5fd7')),
            ],
            options={
                'verbose_name': '\u6742\u5fd7LOGO',
                'verbose_name_plural': '\u6742\u5fd7LOGO',
            },
        ),
        migrations.CreateModel(
            name='MagazineProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magazine_journal_no', models.CharField(max_length=255, verbose_name='\u6742\u5fd7\u671f\u520a\u7f16\u53f7')),
                ('magazine_journal_title', models.CharField(max_length=255, verbose_name='\u6742\u5fd7\u671f\u520a\u540d\u79f0')),
                ('magazine_journal_picture_url', models.URLField(max_length=255, verbose_name='\u56fe\u7247URL')),
                ('magazine_journal_timestamp', models.TimeField(max_length=255, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('magazine_journal_article_number', models.IntegerField(null=True, verbose_name='\u6742\u5fd7\u6587\u7ae0\u53f7')),
                ('note', models.CharField(max_length=255, null=True, verbose_name='\u8bf4\u660e')),
            ],
            options={
                'verbose_name': '\u6742\u5fd7\u680f\u76ee\u4fe1\u606f',
                'verbose_name_plural': '\u6742\u5fd7\u680f\u76ee\u4fe1\u606f',
            },
        ),
    ]

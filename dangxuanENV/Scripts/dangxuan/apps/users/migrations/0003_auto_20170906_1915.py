# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-06 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170906_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='MyRoleId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.MyRole', verbose_name='\u89d2\u8272id'),
        ),
    ]

# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class RadioContent(models.Model):
    program_id = models.IntegerField(verbose_name=u'音频节目')
    program_picture_url = models.URLField(max_length=255, verbose_name=u'图片URL')
    program_audio_url = models.URLField(max_length=255, verbose_name=u'音频URL')
    program_timestamp = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    program_introduction = models.CharField(max_length=255,null=True)
    program_audio_duration = models.CharField(max_length=255,null=True)
    program_audio_anchor = models.CharField(max_length=255, null=True)
    program_audio_category = models.CharField(max_length=255, null=True)
    note = models.CharField(max_length=255,verbose_name=u'广播说明', null=True)

    class Meta:
        verbose_name = u'广播实体'
        verbose_name_plural = verbose_name


class RadioProgram(models.Model):
    program_name = models.CharField(max_length=255, verbose_name=u'节目名称')
    program_date = models.CharField(max_length=255, verbose_name=u'数据')
    note = models.CharField(max_length=255, verbose_name=u'说明', null=True)
    program_picture_url = models.URLField(max_length=255,verbose_name=u'图片URL')

    class Meta:
        verbose_name = u'广播节目信息'
        verbose_name_plural = verbose_name


class RadioCarousel(models.Model):
    picture_url = models.URLField(max_length=255,verbose_name=u'广播图片')
    note = models.CharField(max_length=255, verbose_name=u'说明')
    picture_timestamp = models.TimeField()


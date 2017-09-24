# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class TelivisionProgram(models.Model):
    television_title = models.CharField(verbose_name=u'电视节目名称', max_length=255)
    note = models.CharField(verbose_name=u'描述', max_length=255,null=True)

    class Meta:
        verbose_name = u"电视节目信息"
        verbose_name_plural = verbose_name


class TelevisionProgramContent(models.Model):
    television_program_id = models.ForeignKey(TelivisionProgram,verbose_name=u'电视节目id')
    thumbnails_url = models.URLField(verbose_name=u'缩略图URL', max_length=255)
    video_url = models.URLField(verbose_name=u'视频URL', max_length=255)
    video_introduction = models.CharField(verbose_name=u'视频介绍', max_length=255)
    video_timestamp = models.TimeField(verbose_name=u'加入时间')
    note = models.CharField(verbose_name=u'说明', max_length=255,null=True)

    class Meta:
        verbose_name = u'电视节目实体信息'
        verbose_name_plural = verbose_name


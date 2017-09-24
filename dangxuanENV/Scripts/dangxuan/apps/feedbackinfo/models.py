# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class FeedbackInfo(models.Model):
    feedbacktitle = models.CharField(verbose_name=u'反馈题目',max_length=255)
    feedbackcontent = models.TextField(verbose_name=u'反馈内容',null=True)
    username = models.CharField(verbose_name=u'反馈用户',max_length=255,null=True)
    feedback_timestamp = models.TimeField(verbose_name=u'加入时间')

    class Meta:
        verbose_name = u'反馈信息'
        verbose_name_plural = verbose_name

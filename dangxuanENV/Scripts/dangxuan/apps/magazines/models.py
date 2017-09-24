# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class MagazineList(models.Model):
    list_title = models.CharField(verbose_name=u'杂志列表名',max_length=255)
    magazine_program_id = models.IntegerField(verbose_name=u'杂志栏目ID')
    list_content = models.CharField(verbose_name=u'杂志列表内容', max_length=255)
    list_writer = models.CharField(verbose_name=u'列表写入人', max_length=255)
    insert_time = models.DateTimeField(verbose_name=u'插入时间')
    note = models.CharField(verbose_name=u'说明',null=True,max_length=255)

    class Meta:
        verbose_name = u'杂志列表信息'
        verbose_name_plural = verbose_name


class MagazineLogo(models.Model):
    first_logo_url = models.URLField(verbose_name=u'第一logo的URl', max_length=255)
    second_logo_url = models.URLField(verbose_name=u'第二logo的URL', max_length=255)
    timestamp = models.TimeField(verbose_name=u'创建时间')
    note = models.CharField(verbose_name=u'说明', max_length=255, null=True)
    logo_flag = models.CharField(verbose_name=u'logo标志', max_length=3)

    class Meta:
        verbose_name = u'杂志LOGO'
        verbose_name_plural = verbose_name



class MagazineProgram(models.Model):
    magazine_journal_no = models.CharField(verbose_name=u'杂志期刊编号', max_length=255)
    magazine_journal_title = models.CharField(verbose_name=u'杂志期刊名称', max_length=255)
    magazine_journal_picture_url = models.URLField(verbose_name=u'图片URL', max_length=255)
    magazine_journal_timestamp = models.TimeField(verbose_name=u'创建时间', max_length=255)
    magazine_journal_article_number = models.IntegerField(verbose_name=u'杂志文章号', null=True)
    note = models.CharField(verbose_name=u'说明', max_length=255, null=True)

    class Meta:
        verbose_name = u'杂志栏目信息'
        verbose_name_plural = verbose_name


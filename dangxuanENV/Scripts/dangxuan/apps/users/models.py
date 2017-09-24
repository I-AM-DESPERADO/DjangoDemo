# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from  datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class MyRole(models.Model):
    Code = models.CharField(max_length=255, verbose_name=u'角色代码')
    CreateTime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    CreateUserId = models.IntegerField(verbose_name=u'创建用户', null=True)
    Name = models.CharField(max_length=255, verbose_name=u'名称')
    Remarks = models.CharField(max_length=255, verbose_name=u'介绍')

    class Meta:
        verbose_name = '角色信息'
        verbose_name_plural = verbose_name


class Department(models.Model):
    code = models.CharField(max_length=255,verbose_name=u'部门代码', null=True)
    ContactNumber = models.CharField(max_length=255,verbose_name=u'联系数字', null=True)
    CreateTime = models.DateTimeField(default=datetime.now,verbose_name=u'创建时间', null=True)
    CreateUserId = models.IntegerField(verbose_name=u'创建用户', null=True)
    IsDeleted = models.IntegerField(verbose_name=u'是否删除', choices=((0, u'删除'),(1, u'存在')),default=1)
    Manager = models.CharField(max_length=255, verbose_name=u'负责人', null=True)
    Name = models.CharField(max_length=255,verbose_name=u'名称')
    ParentId = models.IntegerField(verbose_name=u'父部门id', null=True)
    Remarks = models.CharField(max_length=255,verbose_name=u'介绍', null=True)

    class Meta:
        verbose_name = '部门信息'
        verbose_name_plural = verbose_name


class UserProfile(AbstractUser):
    CreateTime = models.DateTimeField(default=datetime.now,verbose_name=u'创建时间', null=True)
    CreateUserId = models.IntegerField(verbose_name=u'创建用户', null=True)
    DepartmentId = models.ForeignKey(Department,verbose_name=u'所属部门', null=True)
    IsDeleted = models.IntegerField(verbose_name=u'是否删除', choices=((0, u'删除'),(1, u'存在')), default=1)
    MobileNumber = models.CharField(max_length=255, verbose_name=u'手机号码', null=True)
    Name = models.CharField(verbose_name=u'姓名', max_length=255)
    Remarks = models.CharField(max_length=255, verbose_name=u'介绍', null=True)
    MyRoleId = models.ForeignKey(MyRole,verbose_name=u'角色id', null=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class Menu(models.Model):
    Code = models.CharField(max_length=255,verbose_name=u'目录代码', null=True)
    Icon = models.CharField(max_length=255,null=True)
    Name = models.CharField(max_length=255,verbose_name=u'名称')
    ParentId = models.IntegerField(verbose_name=u'父集目录id', null=True)
    Remarks = models.CharField(max_length=255,verbose_name=u'介绍', null=True)
    SerialNumber = models.IntegerField()
    Type = models.IntegerField()
    Url = models.CharField(max_length=255,verbose_name=u'目录url', null=True)

    class Meta:
        verbose_name = u'菜单信息'
        verbose_name_plural = verbose_name





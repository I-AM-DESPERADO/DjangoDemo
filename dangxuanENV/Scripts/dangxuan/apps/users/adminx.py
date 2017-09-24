# -*- coding: utf-8 -*-
__author__ = 'tz'
__date__ = '2017/9/6 20:33'

import xadmin
from .models import Department,MyRole,Menu
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettiing(object):
    site_title = "党宣项目"
    site_footer = "NewThreat团队技术支持"
    menu_style = 'accordion'


class DepartmentAdmin(object):

    list_display = ['code', 'ContactNumber', 'CreateTime', 'CreateUserId', 'IsDeleted', 'Manager', 'Name', 'ParentId', 'Remarks']
    search_fields = ['code', 'ContactNumber', 'CreateUserId', 'IsDeleted', 'Manager', 'Name', 'ParentId', 'Remarks']
    list_filter = ['code', 'ContactNumber', 'CreateTime', 'CreateUserId', 'IsDeleted', 'Manager', 'Name', 'ParentId', 'Remarks']


class MyRoleAdmin(object):

    list_display = ['Code', 'CreateTime', 'CreateUserId', 'Name', 'Remarks']
    search_fields = ['Code', 'CreateUserId', 'Name', 'Remarks']
    list_filter = ['Code', 'CreateTime', 'CreateUserId', 'Name', 'Remarks']


class MenuAdmin(object):

    list_display = ['Code', 'Icon', 'Name', 'ParentId', 'Remarks', 'SerialNumber', 'Type', 'Url']
    search_fields = ['Code', 'Icon', 'Name', 'ParentId', 'Remarks', 'SerialNumber', 'Type', 'Url']
    list_filter = ['Code', 'Icon', 'Name', 'ParentId', 'Remarks', 'SerialNumber', 'Type', 'Url']


xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(MyRole, MyRoleAdmin)
xadmin.site.register(Menu, MenuAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettiing)
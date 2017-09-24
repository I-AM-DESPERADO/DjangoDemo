# _*_ coding: utf-8 _*_
__author__ = 'root'
__date__ = '2017/9/4 18:45'

import xadmin
from .models import Course,Lesson,vidio,CourseResourse


class CourseAdmin(object):

    list_display = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_num','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_num']
    list_filter = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_num','add_time']


class LessonAdmin(object):

    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course','name','add_time']


class vidioAdmin(object):

    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson','name','add_time']



class CourseResourseAdmin(object):

    list_display = ['course','name','download','add_time']
    search_fields = ['course','name','download']
    list_filter = ['course','name','download','add_time']


xadmin.site.register(CourseResourse,CourseResourseAdmin)
xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(vidio,vidioAdmin)

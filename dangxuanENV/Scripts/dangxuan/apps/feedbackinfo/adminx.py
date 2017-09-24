# -*- coding: utf-8 -*-
__author__ = 'tz'
__date__ = '2017/9/6 20:33'

import xadmin
from .models import FeedbackInfo


class FeedbackInfoAdmin(object):

    list_display = ['feedbacktitle', 'feedbackcontent', 'username', 'feedback_timestamp']
    search_fields = ['feedbacktitle', 'feedbackcontent', 'username']
    list_filter = ['feedbacktitle', 'feedbackcontent', 'username', 'feedback_timestamp']


xadmin.site.register(FeedbackInfo, FeedbackInfoAdmin)
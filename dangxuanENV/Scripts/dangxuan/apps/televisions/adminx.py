# -*- coding: utf-8 -*-
__author__ = 'tz'
__date__ = '2017/9/6 20:33'

import xadmin
from .models import TelivisionProgram,TelevisionProgramContent


class TelivisionProgramAdmin(object):

    list_display = ['television_title', 'note']
    search_fields = ['television_title', 'note']
    list_filter = ['television_title', 'note']


class TelevisionProgramContentAdmin(object):

    list_display = ['television_program_id', 'thumbnails_url', 'video_url', 'video_introduction', 'video_timestamp', 'note']
    search_fields = ['television_program_id', 'thumbnails_url', 'video_url', 'video_introduction', 'note']
    list_filter = ['television_program_id', 'thumbnails_url', 'video_url', 'video_introduction', 'video_timestamp', 'note']


xadmin.site.register(TelivisionProgram,TelivisionProgramAdmin)
xadmin.site.register(TelevisionProgramContent,TelevisionProgramContentAdmin)


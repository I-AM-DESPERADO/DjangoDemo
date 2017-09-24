# -*- coding: utf-8 -*-
__author__ = 'tz'
__date__ = '2017/9/6 20:33'
import xadmin
from .models import RadioCarousel,RadioContent,RadioProgram


class RadioCarouselAdmin(object):

    list_display = ['picture_url', 'note', 'picture_timestamp']
    search_fields = ['picture_url', 'note']
    list_filter = ['picture_url', 'note', 'picture_timestamp']


class RadioContentAdmin(object):

    list_display = ['program_id', 'program_picture_url', 'program_audio_url','program_timestamp','program_introduction',
                    'program_audio_duration', 'program_audio_anchor', 'program_audio_category', 'note']
    search_fields = ['program_id', 'program_picture_url', 'program_audio_url', 'program_introduction',
                     'program_audio_duration', 'program_audio_anchor', 'program_audio_category', 'note']
    list_filter = ['program_id', 'program_picture_url', 'program_audio_url','program_timestamp','program_introduction',
                    'program_audio_duration', 'program_audio_anchor', 'program_audio_category', 'note']


class RadioProgramAdmin(object):

    list_display = ['program_name', 'program_date', 'note', 'program_picture_url']
    search_fields = ['program_name', 'note', 'program_picture_url']
    list_filter = ['program_name', 'program_date', 'note', 'program_picture_url']

xadmin.site.register(RadioCarousel,RadioCarouselAdmin)
xadmin.site.register(RadioContent,RadioContentAdmin)
xadmin.site.register(RadioProgram,RadioProgramAdmin)
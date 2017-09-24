# -*- coding: utf-8 -*-
__author__ = 'tz'
__date__ = '2017/9/6 20:33'


import xadmin
from .models import MagazineList,MagazineLogo,MagazineProgram


class MagazineListAdmin(object):

    list_display = ['list_title', 'magazine_program_id', 'list_content', 'list_writer', 'insert_time', 'note']
    search_fields = ['list_title', 'magazine_program_id', 'list_content', 'list_writer', 'note']
    list_filter = ['list_title', 'magazine_program_id', 'list_content', 'list_writer', 'insert_time', 'note']


class MagazineLogoAdmin(object):

    list_display = ['first_logo_url', 'second_logo_url', 'timestamp', 'note', 'logo_flag']
    search_fields = ['first_logo_url', 'second_logo_url', 'note', 'logo_flag']
    list_filter = ['first_logo_url', 'second_logo_url', 'timestamp', 'note', 'logo_flag']


class MagazineProgramAdmin(object):

    list_display = ['magazine_journal_no', 'magazine_journal_title', 'magazine_journal_picture_url', 'magazine_journal_timestamp', 'magazine_journal_article_number', 'note']
    search_fields = ['magazine_journal_no', 'magazine_journal_title', 'magazine_journal_picture_url', 'magazine_journal_article_number', 'note']
    list_filter = ['magazine_journal_no', 'magazine_journal_title', 'magazine_journal_picture_url', 'magazine_journal_timestamp', 'magazine_journal_article_number', 'note']


xadmin.site.register(MagazineList, MagazineListAdmin)
xadmin.site.register(MagazineLogo, MagazineLogoAdmin)
xadmin.site.register(MagazineProgram, MagazineProgramAdmin)

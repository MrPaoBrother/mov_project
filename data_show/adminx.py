# -*- coding: utf-8 -*-

from __future__ import absolute_import
import xadmin
from .models import *


@xadmin.sites.register(MovieDetail)
class MovieDetailAdmin(object):
    list_display = ('id', 'mov_name', 'mov_rate', 'mov_url')
    # readonly_fields = ('')
    search_fields = ['mov_name']


@xadmin.sites.register(MovieComments)
class MovieCommentsAdmin(object):
    list_display = ('id', 'comment_user', 'comment_time', 'comment_like', 'comment_content', 'mov_id_id')

    search_fields = ['comment_content']
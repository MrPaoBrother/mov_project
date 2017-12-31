# -*- coding: utf-8 -*-

from __future__ import absolute_import
import xadmin
from .models import *


@xadmin.sites.register(MovieDetail)
class MovieDetailAdmin(object):
    list_display = ('id', 'mov_name', 'mov_rate', 'mov_url')
    # readonly_fields = ('')
    search_fields = ['id', 'mov_name']


@xadmin.sites.register(MovieComments)
class MovieCommentsAdmin(object):
    list_display = ('id', 'comment_user', 'comment_time', 'comment_like', 'comment_content', 'mov_id_id')

    search_fields = ['comment_content']


@xadmin.sites.register(MovieMsg)
class MovieMsgAdmin(object):
    list_display = ('id', 'director', 'actors', 'type', 'release_date', 'intro', 'mov_id')

    search_fields = ['mov_id', 'director', 'actors', 'type']


@xadmin.sites.register(MovieData)
class MovieDataAdmin(object):
    list_display = ('id', 'mov_name', 'mov_director', 'mov_actors', 'mov_type', 'mov_release', 'mov_rate', 'mov_intro', 'mov_url')

    search_fields = ['id', 'mov_name', 'mov_director', 'mov_actors', 'mov_type']


@xadmin.sites.register(MovieFenci)
class MovieFenciAdmin(object):
    list_display = ('id', 'mov_id', 'comment_id', 'comment_words')

    search_fields = ['id', 'mov_id', 'comment_words']


@xadmin.sites.register(MovieWords)
class MovieWordsAdmin(object):
    list_display = ('word', 'counts')

    search_fields = ['word']



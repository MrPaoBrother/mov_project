# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
# Create your models here.


@python_2_unicode_compatible
class MovieDetail(models.Model):
    mov_name = models.CharField(max_length=50, default="影片名称", verbose_name="电影名称")
    mov_rate = models.CharField(max_length=50, default="好评率", verbose_name="好评率")
    mov_url = models.CharField(max_length=100, default="url", verbose_name="链接")

    def __str__(self):
        return "电影详情"

    class Meta:
        verbose_name = "电影详情"
        verbose_name_plural = verbose_name
        db_table = 'movie_detail'


@python_2_unicode_compatible
class MovieComments(models.Model):
    comment_user = models.CharField(max_length=50, default="评论人", verbose_name="评论人")
    comment_time = models.CharField(max_length=50, default="评论时间", verbose_name="评论时间")
    comment_like = models.FloatField(default=.0, verbose_name="点赞数(好评率)")
    comment_content = models.TextField(default="说点什么")
    mov_id_id = models.IntegerField(default=0, verbose_name="影片id")

    def __str__(self):
        return "评论内容"

    class Meta:
        verbose_name = "评论内容"
        verbose_name_plural = verbose_name
        db_table = 'movie_comments'
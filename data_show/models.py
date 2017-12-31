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


@python_2_unicode_compatible
class MovieMsg(models.Model):
    director = models.CharField(max_length=50, default="导演", verbose_name="导演")
    actors = models.TextField(default="演员", verbose_name="演员")
    type = models.CharField(max_length=100, default="类型", verbose_name="类型")
    release_date = models.CharField(max_length=100, default="地方/发布时间", verbose_name="发布地/时间")
    intro = models.TextField(default='简介', verbose_name="电影简介")
    mov_id = models.IntegerField(default=0, verbose_name='电影id')

    def __str__(self):
        return "电影"

    class Meta:
        verbose_name = "其他信息"
        verbose_name_plural = verbose_name
        db_table = 'mov_msg'


# 汇总表
@python_2_unicode_compatible
class MovieData(models.Model):
    mov_name = models.CharField(max_length=200, default="影片名称", verbose_name="影片名称")
    mov_director = models.CharField(max_length=200, default="导演", verbose_name="导演")
    mov_actors = models.TextField(default="演员", verbose_name="演员")
    mov_type = models.CharField(max_length=200, default="类型", verbose_name="类型")
    mov_release = models.CharField(max_length=100, default="发布地/时间", verbose_name="发布地/时间")
    mov_rate = models.CharField(max_length=50, default="好评率", verbose_name="好评率")
    mov_intro = models.TextField(default="简介", verbose_name="简介")
    mov_url = models.CharField(max_length=200, default="链接", verbose_name="链接")

    def __str__(self):
        return "综合信息"

    class Meta:
        verbose_name = "综合信息"
        verbose_name_plural = verbose_name
        db_table = 'mov_data'


@python_2_unicode_compatible
class MovieFenci(models.Model):
    mov_id = models.IntegerField(default=0, verbose_name="电影id")
    comment_id = models.IntegerField(default=0, verbose_name="评论id")
    comment_words = models.TextField(default="", verbose_name="评论分词")

    def __str__(self):
        return "影评分词信息"

    class Meta:
        verbose_name = "影评分词信息"
        verbose_name_plural = verbose_name
        db_table = 'mov_fenci'


@python_2_unicode_compatible
class MovieWords(models.Model):
    word = models.CharField(max_length=100, default="词汇", verbose_name="词汇")
    counts = models.IntegerField(default=0, verbose_name="出现频次")

    def __str__(self):
        return "词频信息"

    class Meta:
        verbose_name = "词频信息"
        verbose_name_plural = verbose_name
        db_table = 'mov_words'
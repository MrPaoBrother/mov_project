# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
'''
default_db_host = '127.0.0.1'
default_db_name = 'xm'
default_db_user = 'root'
default_db_password = '123456'
default_key_words = '夏老师作业'
default_spider_api = 'mov_pub'
'''
default_db_host = '45.77.150.109'
default_db_name = 'xm'
default_db_user = 'Ubuntu'
default_db_password = '****************'
default_key_words = '夏老师作业'
default_spider_api = 'mov_pub'


@python_2_unicode_compatible
class MovSpider(models.Model):
    platform = models.CharField(max_length=20, default=default_spider_api, verbose_name='使用的爬虫接口')
    days_range = models.IntegerField(verbose_name='时间范围')
    key_words = models.CharField(max_length=16, default=default_key_words, verbose_name='关键字')

    current_status = models.CharField(max_length=4, default='就绪', verbose_name='当前状态')
    description = models.TextField(blank=True, null=True, verbose_name='描述')

    db_host = models.CharField(max_length=16, default=default_db_host, verbose_name='Host')
    db_name = models.CharField(max_length=32, default=default_db_name, verbose_name='数据库名')
    db_user = models.CharField(max_length=32, default=default_db_user, verbose_name='用户名')
    db_password = models.CharField(max_length=32, default=default_db_password, verbose_name='密码')

    def __str__(self):
        return '影评爬取'

    class Meta:
        verbose_name = '影评爬取'
        verbose_name_plural = verbose_name
        db_table = 'mov_spider'


@python_2_unicode_compatible
class MovMasterSpider(models.Model):
    platform = models.CharField(max_length=20, default=default_spider_api, verbose_name='使用的爬虫接口')
    days_range = models.IntegerField(verbose_name='时间范围')
    key_words = models.CharField(max_length=16, default=default_key_words, verbose_name='关键字')

    current_status = models.CharField(max_length=4, default='就绪', verbose_name='当前状态')
    description = models.TextField(blank=True, null=True, verbose_name='描述')

    db_host = models.CharField(max_length=16, default=default_db_host, verbose_name='Host')
    db_name = models.CharField(max_length=32, default=default_db_name, verbose_name='数据库名')
    db_user = models.CharField(max_length=32, default=default_db_user, verbose_name='用户名')
    db_password = models.CharField(max_length=32, default=default_db_password, verbose_name='密码')

    def __str__(self):
        return '影评爬取-Master'

    class Meta:
        verbose_name = '影评爬取-Master'
        verbose_name_plural = verbose_name
        db_table = 'mov_master_spider'

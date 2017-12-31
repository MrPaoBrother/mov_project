# -*- coding: utf-8 -*-

from __future__ import absolute_import
from xadmin import views
import xadmin
from .models import *
from .button_post import start_button, result_button, result_url
from data_show.models import MovieDetail, MovieComments, MovieMsg


@xadmin.sites.register(views.website.IndexView)
class MainDashboard(object):
    # 设置了一些主页的小工具
    widgets = [
        [
            {"type": "html",
             "title": "Welcome!",
             "content": "<h3>影评系统管理平台</h3><p>欢迎使用！</p>"},

        ],
        [
            {"type": "qbutton",
             "title": "Quick Start",
             "btns": [{"model": MovMasterSpider},
                      {"model": MovieDetail},
                      {"model": MovieComments},
                      {"model": MovieMsg}
                      ]},
            {"type": "addform", "model": MovMasterSpider}
        ]
    ]


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    # 可选主题，使用默认主题
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    site_title = '影评系统分布式管理平台'
    site_footer = '数据分析小项目'

    # global_search_models = [BaiduindexSpider, ]
    # 为模型设置图标
    # global_models_icon = {
    #     BaiduindexSpider: "fa fa-eye",
    # }
    # accordion
    menu_style = 'default'


@xadmin.sites.register(MovMasterSpider)
class WechatMasterSpiderAdmin(object):

    def start_spider(self, instance):
        if instance.current_status == '就绪':
            url = "'run?spider_name=general_html_spider&platform_name=微信&db_host=%s&db_name=%s&db_user=%s&spider_id=%s&days_range=%s'" \
                  % (instance.db_host, instance.db_name, instance.db_user, instance.id, instance.days_range)
            return start_button%url
        if instance.current_status == '结束':
            return """<button class ="btn btn-success" onclick="window.open('http://www.baidu.com')" >start</button>"""

    def watch_log(self, instance):
        return """<button class = "btn btn-success" onclick = "window.open('/log')"> watch</button>"""

    def watch_result(self, instance):
        url = result_url % ('微信', instance.id, instance.db_host, instance.db_name, instance.db_user)
        print 'url:' + url
        return result_button % url

    start_spider.short_description = "control"
    start_spider.allow_tags = True
    start_spider.is_column = True

    watch_log.short_description = "log"
    watch_log.allow_tags = True
    watch_log.is_column = True

    watch_result.short_description = "result"
    watch_result.allow_tags = True
    watch_result.is_column = True

    list_display = ('id', 'key_words', 'days_range', 'current_status', 'description', 'db_name', 'start_spider',
                    'watch_log', 'watch_result')
    readonly_fields = ('platform', 'current_status',)
    search_fields = ['key_words']


@xadmin.sites.register(MovSpider)
class WechatSpiderAdmin(object):

    def start_spider(self, instance):
        if instance.current_status == '就绪':
            url = "'run?spider_name=general_html_spider&platform_name=微信&db_host=%s&db_name=%s&db_user=%s&spider_id=%s&days_range=%s'" \
                  % (instance.db_host, instance.db_name, instance.db_user, instance.id, instance.days_range)
            return start_button%url
        if instance.current_status == '结束':
            return """<button class ="btn btn-success" onclick="window.open('http://www.baidu.com')" >start</button>"""

    def watch_log(self, instance):
        return """<button class = "btn btn-success" onclick = "window.open('/log')"> watch</button>"""

    def watch_result(self, instance):
        url = result_url % ('微信', instance.id, instance.db_host, instance.db_name, instance.db_user)
        print 'url:' + url
        return result_button % url

    start_spider.short_description = "control"
    start_spider.allow_tags = True
    start_spider.is_column = True

    watch_log.short_description = "log"
    watch_log.allow_tags = True
    watch_log.is_column = True

    watch_result.short_description = "result"
    watch_result.allow_tags = True
    watch_result.is_column = True

    list_display = ('id', 'key_words', 'days_range', 'current_status', 'description', 'db_name', 'start_spider',
                    'watch_log', 'watch_result')
    readonly_fields = ('platform', 'current_status',)
    search_fields = ['key_words']



# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

# from learn_xadmin.celery_client import app
from spider_celery import app
from dao import redis_conn_1
from dao import redis_conn_15
from pagination import paginate, DB
import json
from spider_board import models

# ORM中数据库表名的映射
tables_dict = {
    '电影详情': 'MovDetailSpider',
    '电影评论' : 'MovCommentsSpider',
    '其他信息' : 'MovMsgSpider',
}


platform_dict = {
    u'豆瓣': 1,
    u'腾讯': 2,
    u'暴风': 3,
}


def log(request):
    return render_to_response('realtime_log.html')


def fresh(request):
    article_success = redis_conn_15.zcount("sort:article", 1, 1)
    article_fail = redis_conn_15.zcount("sort:article", 0, 0)
    article_exist = redis_conn_15.zcount("sort:article", 2, 2)
    news_success = redis_conn_15.zcount("sort:news_detail", 1, 1)
    news_fail = redis_conn_15.zcount("sort:news_detail", 0, 0)
    if redis_conn_1.get("status")==None:
        status="running"
    else:
        status=redis_conn_1.get("status")
    report_dict = {"article_success": article_success,
                   "article_fail": article_fail,
                   "article_exist": article_exist,
                   "news_success": news_success,
                   "news_fail": news_fail,
                   "status":status}
    return HttpResponse(json.dumps(report_dict), content_type='application/json')


def test(request):
    return render_to_response('test.html')


@csrf_exempt
def run(request):
    GET_dict = request.GET.dict()
    print "GET_dict",GET_dict
    spider_name = GET_dict.pop(u'spider_name')
    platform_name = GET_dict.pop(u'platform_name')
    platform_id = platform_dict[platform_name]
    spider_id = GET_dict.pop(u'spider_id')
    dbtable_name = tables_dict[platform_name.encode('utf-8')]
    dbhost = GET_dict.pop(u'db_host')
    dbname = GET_dict.pop(u'db_name')
    dbuser = GET_dict.pop(u'db_user')
    dbpassword = getattr(models, dbtable_name).objects.get(id=spider_id).db_password

    result = app.send_task('spider_task.run_spider',
                           args=[spider_name, platform_name, spider_id, dbhost, dbname, dbuser, dbpassword],
                           kwargs=GET_dict)
    return render_to_response('success.html')


@csrf_exempt
def result(request):
    GET_dict = request.GET.dict()
    print GET_dict
    platform_name = GET_dict.get(u'platform_name')
    platform_id = platform_dict[platform_name]
    spider_id = GET_dict.get(u'spider_id')
    dbtable_name = tables_dict[platform_name.encode('utf-8')]
    dbhost = GET_dict.get('db_host')
    dbname = GET_dict.get('db_name')
    dbuser = GET_dict.get('db_user')
    dbpassword = getattr(models, dbtable_name).objects.\
        get(id=spider_id, db_host=dbhost, db_name=dbname, db_user=dbuser).db_password

    querys = ''
    for w, q in GET_dict.items():
        querys += '&'+ w + '=' + q
    querys = querys[1:]

    db = DB(host=dbhost, user=dbuser, passwd=dbpassword, db=dbname)
    current_paginate = paginate(db, platform_id, spider_id, 1, 10)
    return render_to_response('result_page.html', context={
        'current_paginate': current_paginate.dict(),
        'querys': querys,
    })


@csrf_exempt
def result_page(request, page='1'):
    GET_dict = request.GET.dict()
    print GET_dict
    platform_name = GET_dict.get(u'platform_name')
    platform_id = platform_dict[platform_name]
    spider_id = GET_dict.get(u'spider_id')
    dbtable_name = tables_dict[platform_name.encode('utf-8')]
    dbhost = GET_dict.get('db_host')
    dbname = GET_dict.get('db_name')
    dbuser = GET_dict.get('db_user')
    dbpassword = getattr(models, dbtable_name).objects.\
        get(id=spider_id, db_host=dbhost, db_name=dbname, db_user=dbuser).db_password

    querys = ''
    for w, q in GET_dict.items():
        querys += '&'+ w + '=' + q
    querys = querys[1:]

    db = DB(host=dbhost, user=dbuser, passwd=dbpassword, db=dbname)
    current_paginate = paginate(db, platform_id, spider_id, int(page), 10)
    return render_to_response('result_page.html', context={
        'current_paginate': current_paginate.dict(),
        'querys': querys,
    })




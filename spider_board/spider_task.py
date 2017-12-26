# -*- coding:utf8 -*-
from spider_celery import app
# from scrapy.crawler import CrawlerProcess
# from scrapy.conf import settings
# from billiard.process import Process
import subprocess


@app.task(bind=True)
def run_spider(self, *args, **kw):
    print args
    print '--------------------------'
    print kw
    # exec_spider = 'python D:/TAL/xes_app_scrapy_redis_master/scrapy_weixin.py'
    # execute(exec_spider)
    # run_wei_xin_spider()
    # os.system(exec_spider)
    subprocess.check_call('D:/TAL/xes_app_scrapy_redis_master/scrapy_weixin.py')
    print "开始爬取......."



'''class UrlCrawlerScript(Process):
    def __init__(self, spider, platform_name, spider_id, dbhost, dbname, dbuser, dbpassword, karg):
        Process.__init__(self)
        self.crawler = CrawlerProcess(settings)
        self.spider = spider
        self.platform_name = platform_name
        self.karg = karg
        self.spider_id = spider_id
        self.dbhost = dbhost
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpassword = dbpassword

    def run(self):
        self.crawler.crawl(self.spider, self.platform_name, self.spider_id, host=self.dbhost, dbname=self.dbname, user=self.dbuser, password=self.dbpassword, **self.karg)
        self.crawler.start()


@app.task(bind=True)
def run_spider(self, spider, platform_name, spider_id, dbhost, dbname, dbuser, dbpassword, **karg):
    crawler = UrlCrawlerScript(spider, platform_name, spider_id, dbhost, dbname, dbuser, dbpassword, karg)
    crawler.run()'''

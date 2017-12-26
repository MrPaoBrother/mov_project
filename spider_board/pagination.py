# -*- coding: UTF-8 -*-

import MySQLdb
from math import ceil

class DB(object):

    #def __init__(self, host='103.235.226.201', user='stat2016', passwd='stat2016', db='spider_system'):
    def __init__(self, host='127.0.0.1', user='root', passwd='123456', db='tal_db'):
        port = 3306
        charset = 'utf8mb4'
        # 打开数据库连接
        self.db = MySQLdb.connect(host=host,
                             user=user,
                             passwd=passwd,
                             db=db,
                             port=port,
                             charset=charset,
                             use_unicode=True,
                             )

        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()


def paginate(db, platform_id, spider_id, page, pre_page):
    offset = (page - 1) * 10

    db = db
    cursor = db.cursor
    cursor.execute("SELECT * FROM articles WHERE platform_id = '{}' AND spider_id = '{}' LIMIT {}, {}".format(platform_id, spider_id, offset, pre_page))
    items = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM articles WHERE platform_id = '{}' AND spider_id = '{}'".format(platform_id, spider_id))
    total = cursor.fetchone()[0]

    db.close()

    return Pagination(page, pre_page, total, items)


class Pagination(object):

    def __init__(self, page, per_page, total, items):
        self.page = page
        self.per_page = per_page
        self.total = total
        self.items = items

    @property
    def next_num(self):
        return self.page + 1

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def pre_num(self):
        return self.page - 1

    @property
    def has_next(self):
        return self.page < self.pages

    @property
    def pages(self):
        if self.per_page == 0:
            pages = 0
        else:
            pages = int(ceil(self.total / float(self.per_page)))
        return pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num

    def dict(self):
        pages = [page for page in self.iter_pages()]
        d = dict(
            next_num=self.next_num,
            pre_num=self.pre_num,
            has_next=self.has_next,
            has_prev=self.has_prev,
            items=self.items,
            pages=pages,
            page=self.page,
        )

        return d


# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-27 10:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spider_board', '0004_auto_20170726_1631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BaiduindexSpider',
        ),
    ]

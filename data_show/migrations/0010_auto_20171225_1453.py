# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-25 06:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data_show', '0009_auto_20171225_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='views_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ignoreurl',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 25, 6, 53, 12, 312000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemmeta',
            name='updatetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 25, 6, 53, 12, 310000, tzinfo=utc)),
        ),
    ]

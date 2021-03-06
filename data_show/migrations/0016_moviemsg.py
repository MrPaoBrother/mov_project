# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-28 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_show', '0015_auto_20171226_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.CharField(default='\u5bfc\u6f14', max_length=50, verbose_name='\u5bfc\u6f14')),
                ('actors', models.TextField(default='\u6f14\u5458', verbose_name='\u6f14\u5458')),
                ('type', models.CharField(default='\u6f14\u5458', max_length=100, verbose_name='\u6f14\u5458')),
                ('release_date', models.CharField(default='\u5730\u65b9/\u53d1\u5e03\u65f6\u95f4', max_length=100, verbose_name='\u53d1\u5e03\u5730/\u65f6\u95f4')),
                ('intro', models.TextField(default='\u7b80\u4ecb', verbose_name='\u7535\u5f71\u7b80\u4ecb')),
                ('mov_id', models.IntegerField(default=0, verbose_name='\u7535\u5f71id')),
            ],
            options={
                'db_table': 'mov_msg',
                'verbose_name': '\u5176\u4ed6\u4fe1\u606f',
                'verbose_name_plural': '\u5176\u4ed6\u4fe1\u606f',
            },
        ),
    ]

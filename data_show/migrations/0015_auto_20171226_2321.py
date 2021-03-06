# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-26 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_show', '0014_auto_20171225_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_user', models.CharField(default='\u8bc4\u8bba\u4eba', max_length=50, verbose_name='\u8bc4\u8bba\u4eba')),
                ('comment_time', models.CharField(default='\u8bc4\u8bba\u65f6\u95f4', max_length=50, verbose_name='\u8bc4\u8bba\u65f6\u95f4')),
                ('comment_like', models.FloatField(default=0.0, verbose_name='\u70b9\u8d5e\u6570(\u597d\u8bc4\u7387)')),
                ('comment_content', models.TextField(default='\u8bf4\u70b9\u4ec0\u4e48')),
                ('mov_id_id', models.IntegerField(default=0, verbose_name='\u5f71\u7247id')),
            ],
            options={
                'db_table': 'movie_comments',
                'verbose_name': '\u8bc4\u8bba\u5185\u5bb9',
                'verbose_name_plural': '\u8bc4\u8bba\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='MovieDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mov_name', models.CharField(default='\u5f71\u7247\u540d\u79f0', max_length=50, verbose_name='\u7535\u5f71\u540d\u79f0')),
                ('mov_rate', models.CharField(default='\u597d\u8bc4\u7387', max_length=50, verbose_name='\u597d\u8bc4\u7387')),
                ('mov_url', models.CharField(default='url', max_length=100, verbose_name='\u94fe\u63a5')),
            ],
            options={
                'db_table': 'movie_detail',
                'verbose_name': '\u7535\u5f71\u8be6\u60c5',
                'verbose_name_plural': '\u7535\u5f71\u8be6\u60c5',
            },
        ),
        migrations.DeleteModel(
            name='APIToken',
        ),
        migrations.DeleteModel(
            name='ArticleDetail',
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
        migrations.DeleteModel(
            name='Classify',
        ),
        migrations.DeleteModel(
            name='IgnoreUrl',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='ItemMeta',
        ),
        migrations.DeleteModel(
            name='WeiXin',
        ),
    ]

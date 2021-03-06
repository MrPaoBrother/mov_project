# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-31 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_show', '0016_moviemsg'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mov_name', models.CharField(default='\u5f71\u7247\u540d\u79f0', max_length=200, verbose_name='\u5f71\u7247\u540d\u79f0')),
                ('mov_director', models.CharField(default='\u5bfc\u6f14', max_length=200, verbose_name='\u5bfc\u6f14')),
                ('mov_actors', models.TextField(default='\u6f14\u5458', verbose_name='\u6f14\u5458')),
                ('mov_type', models.CharField(default='\u7c7b\u578b', max_length=200, verbose_name='\u7c7b\u578b')),
                ('mov_release', models.CharField(default='\u53d1\u5e03\u5730/\u65f6\u95f4', max_length=100, verbose_name='\u53d1\u5e03\u5730/\u65f6\u95f4')),
                ('mov_rate', models.CharField(default='\u597d\u8bc4\u7387', max_length=50, verbose_name='\u597d\u8bc4\u7387')),
                ('mov_intro', models.TextField(default='\u7b80\u4ecb', verbose_name='\u7b80\u4ecb')),
                ('mov_url', models.CharField(default='\u94fe\u63a5', max_length=200, verbose_name='\u94fe\u63a5')),
            ],
            options={
                'db_table': 'mov_data',
                'verbose_name': '\u7efc\u5408\u4fe1\u606f',
                'verbose_name_plural': '\u7efc\u5408\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='MovieFenci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mov_id', models.IntegerField(default=0, verbose_name='\u7535\u5f71id')),
                ('comment_id', models.IntegerField(default=0, verbose_name='\u8bc4\u8bbaid')),
                ('comment_words', models.TextField(default='', verbose_name='\u8bc4\u8bba\u5206\u8bcd')),
            ],
            options={
                'db_table': 'mov_fenci',
                'verbose_name': '\u5f71\u8bc4\u5206\u8bcd\u4fe1\u606f',
                'verbose_name_plural': '\u5f71\u8bc4\u5206\u8bcd\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='MovieWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(default='\u8bcd\u6c47', max_length=100, verbose_name='\u8bcd\u6c47')),
                ('count', models.IntegerField(default=0, verbose_name='\u51fa\u73b0\u9891\u6b21')),
            ],
            options={
                'db_table': 'mov_words',
                'verbose_name': '\u8bcd\u9891\u4fe1\u606f',
                'verbose_name_plural': '\u8bcd\u9891\u4fe1\u606f',
            },
        ),
        migrations.AlterField(
            model_name='moviemsg',
            name='type',
            field=models.CharField(default='\u7c7b\u578b', max_length=100, verbose_name='\u7c7b\u578b'),
        ),
    ]

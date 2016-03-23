# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usercenter', '0004_auto_20160323_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('guid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('description', models.TextField(verbose_name='描述')),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('owner_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usercenter.UserAccount', verbose_name='拥有者')),
            ],
            options={
                'verbose_name': '项目表',
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='ProjectClassifyFirst',
            fields=[
                ('guid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='一级分类名称')),
            ],
            options={
                'verbose_name': '项目一级分类表',
                'db_table': 'project_classify_first',
            },
        ),
        migrations.CreateModel(
            name='ProjectClassifySecond',
            fields=[
                ('guid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='二级分类名称')),
                ('classify_first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ProjectClassifyFirst', verbose_name='一级分类名称')),
                ('projects', models.ManyToManyField(related_name='项目列表', to='project.Project')),
            ],
            options={
                'verbose_name': '项目二级分类表',
                'db_table': 'project_classify_second',
            },
        ),
    ]

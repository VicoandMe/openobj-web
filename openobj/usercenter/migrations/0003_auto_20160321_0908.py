# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0002_auto_20160321_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='mobile',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='手机号'),
        ),
    ]

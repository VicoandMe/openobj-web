# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0003_auto_20160321_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='password',
            field=models.CharField(max_length=256, verbose_name='密码'),
        ),
    ]

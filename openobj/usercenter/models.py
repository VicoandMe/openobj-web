# coding:utf8
from django.db import models
from django.utils.timezone import now


# Create your models here.


class User(models.Model):
    account = models.CharField(max_length=200, verbose_name=u'用户名')
    password = models.CharField(max_length=200, verbose_name=u'密码')
    nickname = models.CharField(max_length=50, verbose_name=u'昵称')
    insert_time = models.DateTimeField(default=now, verbose_name=u'插入时间')
    update_time = models.DateTimeField(verbose_name=u'更新时间', blank=True, null=True)

    def __unicode__(self):
        return self.account

    class Meta:
        db_table = 'user'
        verbose_name = u'用户表'

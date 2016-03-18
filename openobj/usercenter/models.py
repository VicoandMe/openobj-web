# coding:utf8
from django.db import models
from django.utils.timezone import now


# Create your models here.


class UserAccount(models.Model):
    guid = models.AutoField(primary_key=True)
    account = models.CharField(max_length=200, verbose_name='用户名')
    password = models.CharField(max_length=200, verbose_name='密码')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    insert_time = models.DateTimeField(default=now, verbose_name='插入时间')
    update_time = models.DateTimeField(verbose_name='更新时间', blank=True, null=True)

    def __unicode__(self):
        return self.account

    class Meta:
        db_table = 'user'
        verbose_name = u'用户表'

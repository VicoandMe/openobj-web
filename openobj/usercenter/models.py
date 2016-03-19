# coding:utf8
from django.db import models
from django.utils.timezone import now


# Create your models here.


class UserAccount(models.Model):
    guid = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='邮箱')
    email_verified = models.BooleanField(default=False, verbose_name='邮箱验证确认状态')
    mobile = models.CharField(max_length=20, verbose_name='手机号')
    mobile_verified = models.BooleanField(default=False, verbose_name='手机号验证确认状态')
    user_name = models.CharField(max_length=200, verbose_name='用户名')
    password = models.CharField(max_length=200, verbose_name='密码')
    register_source = models.IntegerField(default=0, verbose_name='注册来源')
    is_locked = models.BooleanField(default=False, verbose_name='锁定状态')
    creation_time = models.DateTimeField(default=now, verbose_name='创建时间')
    last_login_time = models.DateTimeField(default=now, verbose_name='最后一次登录时间', blank=True, null=True)
    login_fail_count = models.IntegerField(default=0, verbose_name='登录失败统计')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user_account'
        verbose_name = '用户表'


class UserInformation(models.Model):
    user_account = models.ForeignKey(UserAccount)
    nick_name = models.CharField(max_length=50, verbose_name='昵称')
    first_name = models.CharField(max_length=50, verbose_name='名')
    last_name = models.CharField(max_length=50, verbose_name='姓')
    sex = models.IntegerField(verbose_name='性别')
    birthday = models.DateTimeField(verbose_name='生日')
    avatar = models.CharField(max_length=200, verbose_name='头像')

    def __str__(self):
        return self.nick_name

    class Meta:
        db_table = 'user_information'
        verbose_name = '用户信息表'


class UserLoginHistory(models.Model):
    user_account = models.ForeignKey(UserAccount)
    login_time = models.DateTimeField(default=now, verbose_name='登录时间')
    login_source = models.IntegerField(default=0, verbose_name='登录来源')
    login_result = models.BooleanField(default=True, verbose_name='登录结果状态')

    class Meta:
        db_table = 'user_login_history'
        verbose_name = '用户登录历史表'


class UserEmailVerifyCode(models.Model):
    user_account = models.ForeignKey(UserAccount)
    email = models.EmailField(verbose_name='邮箱')
    code = models.CharField(max_length=200, verbose_name='验证码')
    valid_time = models.DateTimeField(default=now, verbose_name='确认时间')

    class Meta:
        db_table = "user_email_verify_code"
        verbose_name = '用户邮箱验证表'


class User3rdAuthorization(models.Model):
    user_account = models.ForeignKey(UserAccount)
    auth_type = models.IntegerField(verbose_name='用户类型')
    user_app_identity = models.IntegerField()
    user_identity = models.IntegerField()
    auth_time = models.DateTimeField(default=now)
    auth_data = models.CharField(max_length=200)

    class Meta:
        db_table = 'user_3rd_authorization'
        verbose_name = '用户第三方授权登录表'

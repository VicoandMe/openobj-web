# coding:utf8
from django.db import models
from django.utils.timezone import now
from libs import passwd_util


# Create your models here.


class UserAccount(models.Model):
    WEB = 'web'
    REGISTER_FROM = (
        (WEB, '网站'),
    )
    guid = models.UUIDField(primary_key=True)
    email = models.EmailField(verbose_name='邮箱')
    email_verified = models.BooleanField(default=False, verbose_name='邮箱验证确认状态')
    mobile = models.CharField(max_length=16, verbose_name='手机号', blank=True, null=True)
    mobile_verified = models.BooleanField(default=False, verbose_name='手机号验证确认状态')
    user_name = models.CharField(max_length=16, verbose_name='用户名', blank=True, null=True)
    password = models.CharField(max_length=256, verbose_name='密码')
    register_source = models.CharField(max_length=32, choices=REGISTER_FROM, default=WEB, verbose_name='注册来源')
    is_locked = models.BooleanField(default=False, verbose_name='锁定状态')
    creation_time = models.DateTimeField(default=now, verbose_name='创建时间')
    last_login_time = models.DateTimeField(default=now, verbose_name='最后一次登录时间')
    login_fail_count = models.IntegerField(default=0, verbose_name='连续登录失败统计')

    def save(self, *args, **kwargs):
        try:
            user = UserAccount.objects.get(guid=self.guid)
            if user.password != self.password:
                self.password = passwd_util.hash_password(self.password)
        except UserAccount.DoesNotExist:
            self.password = passwd_util.hash_password(self.password)
        super(UserAccount, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user_account'
        verbose_name = '用户表'


class UserInformation(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    SEX = (
        (MALE, '男'),
        (FEMALE, '女'),
    )
    user_account = models.ForeignKey(UserAccount)
    nick_name = models.CharField(max_length=32, verbose_name='昵称', blank=True, null=True)
    first_name = models.CharField(max_length=32, verbose_name='名', blank=True, null=True)
    last_name = models.CharField(max_length=32, verbose_name='姓', blank=True, null=True)
    sex = models.CharField(max_length=32, choices=SEX, verbose_name='性别', blank=True, null=True)
    birthday = models.DateTimeField(verbose_name='生日', blank=True, null=True)
    avatar = models.CharField(max_length=1024, verbose_name='头像', blank=True, null=True)

    def __str__(self):
        return self.nick_name

    class Meta:
        db_table = 'user_information'
        verbose_name = '用户信息表'


class UserLoginHistory(models.Model):
    WEB = 'web'
    LOGIN_FROM = (
        (WEB, '网站'),
    )
    user_account = models.ForeignKey(UserAccount)
    login_time = models.DateTimeField(default=now, verbose_name='登录时间')
    login_source = models.CharField(max_length=32, choices=LOGIN_FROM, default=WEB, verbose_name='登录来源')
    login_result = models.BooleanField(default=True, verbose_name='登录结果状态')

    class Meta:
        db_table = 'user_login_history'
        verbose_name = '用户登录历史表'


class UserEmailVerifyCode(models.Model):
    FIRST_REG = 'first_reg'
    REPLACE = 'replace'
    VERIFY = (
        (FIRST_REG, '首次注册'),
        (REPLACE, '更换'),
    )
    user_account = models.ForeignKey(UserAccount)
    verify_type = models.CharField(max_length=32, choices=VERIFY, default=FIRST_REG, verbose_name='验证类型')
    code = models.CharField(max_length=1024, verbose_name='验证码')
    valid_time = models.DateTimeField(default=now, verbose_name='过期时间')

    class Meta:
        db_table = 'user_email_verify_code'
        verbose_name = '用户邮箱验证表'


class UserNewEmail(models.Model):
    user_account = models.ForeignKey(UserAccount)
    email = models.EmailField(verbose_name='邮箱')
    creation_time = models.DateTimeField(default=now, verbose_name='创建时间')

    class Meta:
        db_table = 'user_new_email'
        verbose_name = '用户新邮箱表'


class User3rdAuthorization(models.Model):
    user_account = models.ForeignKey(UserAccount)
    auth_type = models.CharField(max_length=32, verbose_name='用户类型')
    user_app_identity = models.CharField(max_length=128, verbose_name='应用内唯一id')
    user_identity = models.CharField(max_length=128, verbose_name='第三方唯一id')
    auth_time = models.DateTimeField(default=now, verbose_name='授权时间')
    auth_data = models.TextField(verbose_name='第三方返回的数据')

    class Meta:
        db_table = 'user_3rd_authorization'
        verbose_name = '用户第三方授权登录表'

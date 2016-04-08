import datetime
import re
import uuid

from django.utils.timezone import now
from common import const
from libs import passwd_util
from libs.message_service.email_message import email_message
from usercenter.models import UserAccount, UserEmailVerifyCode
from usercenter.models import UserInformation
from usercenter.models import UserLoginHistory
from . import settings


def check_user_name(username):
    """
    检测用户名
    :param username:
    :return:
    """
    if not username:
        return const.FAIL_STATUS, "用户名不能为空"
    if not re.match('^[_0-9a-zA-Z]+$', username):
        return const.FAIL_STATUS, "用户名不合法，账户名仅包含数字，字母和'_'"
    account_size = len(username)
    if account_size < 6 or account_size > 20:
        return const.FAIL_STATUS, "用户名长度为6-20个字符"
    try:
        UserAccount.objects.get(user_name=username)
        return const.FAIL_STATUS, "用户名已存在"
    except UserAccount.DoesNotExist:
        return const.SUCCESS_STATUS, "OK"
    return const.FAIL_STATUS, "ERROR"


def check_email(email):
    """
    检测邮箱
    :param email:
    :return:
    """
    if not email:
        return const.FAIL_STATUS, "邮箱不能为空"
    if not re.match(
            r"^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$",
            email):
        return const.FAIL_STATUS, "邮箱格式错误,请输入正确的邮箱!"
    return const.SUCCESS_STATUS, "OK"


def check_password(password):
    """
    检测密码
    :param password:
    :return:
    """
    if not password:
        return const.FAIL_STATUS, "密码不能为空"
    password_size = len(password)
    if password_size < 6 or password_size > 20:
        return const.FAIL_STATUS, "密码长度为6-20个字符"
    return const.SUCCESS_STATUS, "OK"


def register(request, username, email, password):
    """
    注册
    """
    status, msg = check_user_name(username)
    if status != const.SUCCESS_STATUS:
        return status, msg

    status, msg = check_email(email)
    if status != const.SUCCESS_STATUS:
        return status, msg

    try:
        UserAccount.objects.get(email=email)
        return const.FAIL_STATUS, "邮箱已存在"
    except UserAccount.DoesNotExist:
        pass

    status, msg = check_password(password)
    if status != const.SUCCESS_STATUS:
        return status, msg

    user = UserAccount.objects.create(guid=uuid.uuid4(), email=email, user_name=username, password=password)
    UserInformation.objects.create(user_account=user)

    url_host = '{0}/usercenter/email/verify'.format("http://" + request.get_host())
    send_register_email(user, url_host)

    return status, msg


def login(request, email, password):
    """
    登录
    """
    status, msg = check_email(email)
    if status != const.SUCCESS_STATUS:
        return status, msg

    try:
        user = UserAccount.objects.get(email=email)
        if not passwd_util.check_password(user.password, password):
            UserLoginHistory.objects.create(login_result=False, user_account=user)
            user.login_fail_count += 1
            user.save()
            return const.FAIL_STATUS, "账户或密码错误"
    except UserAccount.DoesNotExist:
        return const.FAIL_STATUS, "账户不存在"

    UserLoginHistory.objects.create(user_account=user)
    user.login_fail_count = 0
    user.save()

    request.session['guid'] = str(user.guid)
    return status, msg


def change_password(user_guid, old_pwd, new_pwd):
    user = UserAccount.objects.get(guid=user_guid)
    if not passwd_util.check_password(user.password, old_pwd):
        return const.FAIL_STATUS, "原密码错误"
    else:
        user.password = new_pwd
        user.save()
        return const.SUCCESS_STATUS, "密码修改成功"


def send_register_email(user, url_host):
    """
    发送激活邮件
    """

    code = str(uuid.uuid4()).replace("-", "")
    vtime = now() + datetime.timedelta(days=1)

    try:
        uevc = UserEmailVerifyCode.objects.get(user_account=user)
        uevc.code = code
        uevc.valid_time = vtime
        uevc.save()
    except UserEmailVerifyCode.DoesNotExist:
        UserEmailVerifyCode.objects.create(user_account=user, code=code, valid_time=vtime)

    url = url_host + "?code=" + code

    body = settings.REG_EMAIL_CONTENT_TEMPLATE.format(url=url, username=user.user_name,
                                                      date_now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    msg = email_message()
    msg.subject = settings.REG_EMAIL_SUBJECT
    msg.from_user = const.NOREPLY_EMAIL
    msg.to_user = user.email
    msg.body = body
    msg.send()
    return True


def verify_register_email(email_code):
    try:
        if not email_code:
            return const.FAIL_STATUS, "验证失败"

        uevc = UserEmailVerifyCode.objects.get(code=email_code, valid_time__gte=now())
        uevc.user_account.email_verified = True
        uevc.user_account.save()

        uevc.delete()

        return const.SUCCESS_STATUS, "OK"

    except UserEmailVerifyCode.DoesNotExist:
        return const.FAIL_STATUS, "验证失败"
    return const.FAIL_STATUS, "未知错误"


def get_user_account(user_guid):
    user = UserAccount.objects.get(guid=user_guid)
    data = dict()
    data['email'] = user.email
    data['email_verified'] = user.email_verified
    data['user_name'] = user.user_name
    return data

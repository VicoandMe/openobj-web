import hashlib
import re
from common import const
from usercenter.models import UserAccount


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
    if not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email):
        return const.FAIL_STATUS, "邮箱格式错误,请输入正确的邮箱!"
    try:
        UserAccount.objects.get(email=email)
        return const.FAIL_STATUS, "邮箱已存在"
    except UserAccount.DoesNotExist:
        return const.SUCCESS_STATUS, "OK"
    return const.FAIL_STATUS, "ERROR"


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


def register(username, email, password):
    """
    注册
    :param username:
    :param email:
    :param password:
    :return:
    """
    status, msg = check_user_name(username)
    if status != const.SUCCESS_STATUS:
        return status, msg

    status, msg = check_email(email)
    if status != const.SUCCESS_STATUS:
        return status, msg

    status, msg = check_password(password)
    if status != const.SUCCESS_STATUS:
        return status, msg

    pw_bytes = password.encode('utf-8')
    user_password = hashlib.md5(pw_bytes).hexdigest()
    UserAccount.objects.create(email=email, user_name=username, password=user_password)
    return const.SUCCESS_STATUS, 'OK'


def login(email, password):
    """
    登录
    :param email:
    :param password:
    :return:
    """
    status, msg = check_email(email)
    if status != const.SUCCESS_STATUS:
        return status, msg

    status, msg = check_password(password)
    if status != const.SUCCESS_STATUS:
        return status, msg

    pw_bytes = password.encode('utf-8')
    user_password = hashlib.md5(pw_bytes).hexdigest()

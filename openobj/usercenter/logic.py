import hashlib
import re
import uuid
from common import const
from usercenter.models import UserAccount
from usercenter.models import UserLoginHistory
from usercenter.models import UserInformation
from libs import passwd_util


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


def register(username, email, password):
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

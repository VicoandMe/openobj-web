from .models import UserInformation
from .models import UserAccount, UserEmailVerifyCode
from .models import UserLoginHistory
from . import logic
from common import const
from libs import passwd_util

def checkorigin_password(username,password):
    """
    检测原始密码是否正确
    :param password:
    :return:
    """
    user = UserAccount.objects.get(user_name=username)
    if not password:
        return const.FAIL_STATUS, "原始密码不能为空"
    password_size = len(password)
    if password_size < 6 or password_size > 20:
        return const.FAIL_STATUS, "密码长度为6-20个字符"
    if not passwd_util.check_password(user.password, password):
            return const.FAIL_STATUS, "原始密码错误"
    return const.SUCCESS_STATUS, "OK"

def passwordsave(request,username,nowpassword,newpassword):
    status,msg = checkorigin_password(username,nowpassword)
    if status != const.SUCCESS_STATUS:
        return status,msg
    user = UserAccount(user_name=username)
    user.password = newpassword
    user.save()
    return status.msg








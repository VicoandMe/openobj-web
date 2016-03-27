import hashlib
import random
import re
import string
import uuid

from django.utils.timezone import now

from common import const
from libs.send_email import send_mail
from . import settings
from usercenter.models import UserAccount, UserEmailVerifyCode
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

    url_host = '{0}/usercenter/email/verify'.format(request.get_host())
    send_verify_email(user, user.email, url_host, UserEmailVerifyCode.FIRST_REG, )

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


def send_verify_email(user, email, url_host, email_type):
    """
    发送激活邮箱
    """
    email_type_str = "激活"
    if email_type == UserEmailVerifyCode.REPLACE:
        email_type_str = "更换"

    body = """
    <body style="margin:0;padding: 0; background:#edf1e3;color:#6e6e6e;">
    <table cellspacing="0" cellpadding="0" border="0" width="100%">
        <tr>
            <td bgcolor="#edf1e3" width="100%" style="padding: 40px;">
                <table cellspacing="0" cellpadding="0" style="margin: 0 auto;font-family: 'Microsoft Yahei',arial,sans-serif;border-collapse:collapse">
                    <tr>
                        <td style="padding-bottom: 10px;width:200px;height:50px;"><img src="http://dash.tangowifi.com/static/images/tango_logo.png" alt="TangoWiFi" /></td>
                        <td width="240px" style="text-align: right;vertical-align: bottom;padding-bottom: 10px;"></td>
                        <td width="200px" style="text-align: right;vertical-align: bottom;padding-bottom: 10px; color: #828284;">{email_type_str}邮箱验证</td>
                    </tr>
                    <tr>
                        <td colspan="3" height="10px" style="background: #e68781 url(http://dash.tangowifi.com/static/images/tango_gapemail.jpg) no-repeat;"></td>
                    </tr>
                    <tr>
                        <td colspan="3" height="340px" width="600px" bgcolor="#fff" style="border: 1px solid #ddd;border-top: 0;border-bottom: 0">
                            <div style="padding: 25px 55px;">
                                <p style="margin: 0 0 25px 0;">亲爱的OpenObj用户，您好！</p>
                                <p> 请点击下面连接来{email_type_str}OpenObj账号：</p>                                <!-- 验证URL -->
                                <p style="margin: 0 0 25px 0;"><a href="{url_host}?d={d}&code={code}&type={email_type}" style="color: #1b77ff;">{url_host}?d={d}&code={code}&type={email_type}</a></p>
                                <!-- end -->
                                <p style="margin: 25px 0; line-height: 1.5em;">为了确保您的账号安全，该链接仅24小时内访问有效，24小时后需重新发送验证连接。如果以上连接无法点击，请您选择并复制整个链接，打开浏览器窗口并将其粘贴到地址栏中。然后单击"转到"按钮或按键盘上的 Enter 键。</p>
                                <p style="margin: 0; padding: 15px 0 0 0;">请勿直接回复邮件！</p>
                                <p style="margin: 5px 0 0 0; padding: 0;">TangoWiFi</p>
                                <p style="margin: 5px 0 0 0; padding: 0;">{now_time}</p>
                            </div>
                        </td>
                     </tr>
                     <tr>
                        <td colspan="3" height="10px" style="background: #e68781 url(http://dash.tangowifi.com/static/images/tango_gapemail.jpg) no-repeat;"></td>
                    </tr>
                    <tr><td colspan="3"><p style="text-align: center;color: #828284; font-size: .8em;">Copyright©2015-2015 TangoWiFi Inc</p></td></tr>
                </table>
            </td>
        </tr>
    </table>
</body>"""
    code = ''.join(random.sample(string.ascii_lowercase + string.digits, 32))
    try:
        uevc = UserEmailVerifyCode.objects.get(user_account=user, verify_type=email_type)
        uevc.code = code
        uevc.valid_time = now()
        uevc.save()
    except UserEmailVerifyCode.DoesNotExist:
        UserEmailVerifyCode.objects.create(user_account=user, verify_type=email_type, code=code)
    dt = now()
    body = body.format(url_host='http://' + url_host, d=user.guid, code=code,
                       email_type_str=email_type_str,email_type=email_type,
                       now_time=dt.strftime('%Y年%m月%d日'))
    send_mail(settings.EMAIL_SERVER_NAME, settings.NOREPLY_EMAIL, email, 'OpenObj(www.openobj.com)邮箱验证', body,
              settings.EMAIL_PWD)
    return True


def email_verify_code(guid, code, email_type):
    try:
        user = UserAccount.objects.get(guid=guid)
        uevc = UserEmailVerifyCode.objects.get(user_account=user, verify_type=email_type)
        if code == uevc.code:
            user.email_verified = True
            user.save()
            return const.SUCCESS_STATUS, "OK"
    except:
        return const.FAIL_STATUS, "未知错误"
    return const.FAIL_STATUS, "未知错误"

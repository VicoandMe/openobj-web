# coding:utf8
import os
from django.utils.timezone import now

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TangoWifi.settings")
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib
import string
from django.conf import settings


def send_mail(server_name, fromaddr, toaddr, subject, body, fromaddr_pwd):
    """
    发送邮件
    """
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    msg["Accept-Language"] = "zh-CN"
    msg["Accept-Charset"] = "ISO-8859-1,utf-8"
    msg.attach(MIMEText(body, 'html', 'utf-8'))
    server = smtplib.SMTP(server_name)
    server.login(fromaddr, fromaddr_pwd)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    return True


if __name__ == '__main__':
    fromaddr = settings.TANGO_EMAIL
    toaddr = "703979707@qq.com"
    body = """
        <table cellspacing="0" cellpadding="0" border="0" width="100%">
            <tr>
                <td bgcolor="#edf1e3" width="100%" style="padding: 40px;">
                    <table cellspacing="0" cellpadding="0" style="margin: 0 auto;font-family: 'Microsoft Yahei',arial,sans-serif;border-collapse:collapse">
                        <tr>
                            <td width="300px" height="50px"><img src="https://passport.wiwide.com/static/images/wiwide-logoemail.jpg" alt="迈外迪" /></td>
                            <td width="300px" style="text-align: right;vertical-align: bottom;padding-bottom: 5px;">邮箱验证</td>
                        </tr>
                        <tr>
                            <td colspan="2" height="10px" style="background: #e68781 url(https://passport.wiwide.com/static/images/wiwide_gapemail.jpg) no-repeat;"></td>
                        </tr>
                        <tr>
                            <td colspan="2" height="340px" width="600px" bgcolor="#fff" style="border: 1px solid #ddd;border-top: 0;border-bottom: 0">
                                <div style="padding: 25px 55px;">
                                    <p style="margin: 0 0 25px 0;">亲爱的迈外迪用户，您好！</p>
                                    <p>点击下面的链接即可激活账号并绑定邮箱</p>
                                    <p style="margin: 0 0 25px 0;"><a href="{url}" style="color: #1b77ff;">{url}</a></p>
                                    <p style="margin: 25px 0; line-height: 1.5em;">为了确保您的账号安全，该链接仅24小时内访问有效，24小时后需重新发送验证连接。如果以上连接无法点击，请您选择并复制整个链接，打开浏览器窗口并将其粘贴到地址栏中。然后单击"转到"按钮或按键盘上的 Enter 键。</p>
                                    <p style="margin: 0; padding: 15px 0 0 0;">请勿直接回复邮件！</p>
                                    <p style="margin: 5px 0 0 0; padding: 0;">迈外迪</p>
                                    <p style="margin: 5px 0 0 0; padding: 0;">{date_now}</p>
                                </div>
                            </td>
                        </tr>
                        <tr bgcolor="#f7f7f7" style="border: 1px solid #ddd; border-bottom: 0;">
                            <td>
                                <table width="100%" style="padding: 15px 0;">
                                    <tr>
                                    <td width="50px"></td>
                                    <td width="48px" height="48px" style="background: url(https://passport.wiwide.com/static/images/emailweibo.png) no-repeat;padding-right: 10px;"></td>
                                    <td><p style="margin: 0; padding: 0;">@WiWide迈外迪</p><p style="margin: 0; padding: 0; color: #828284; font-size: .8em;">关注最新动态</p></td>
                                    </tr>
                                </table>
                            </td>
                            <td><table width="100%" style="padding: 15px 0;">
                                    <tr>
                                    <td width="50px"></td>
                                    <td width="48px" height="48px" style="background: url(https://passport.wiwide.com/static/images/emailweibo.png) no-repeat; padding-right: 10px;"></td>
                                    <td><p style="margin: 0; padding: 0;">400&nbsp;6500&nbsp;311</p><p style="margin: 0; padding: 0; color: #828284; font-size: .8em;">24小时服务</p></td>
                                    </tr>
                                </table></td>
                        </tr>
                         <tr>
                            <td colspan="2" height="10px" style="background: #e68781 url(https://passport.wiwide.com/static/images/wiwide_gapemail.jpg) no-repeat;"></td>
                        </tr>
                        <tr><td colspan="2"><p style="text-align: center;color: #828284; font-size: .8em;">Copyright?2007-2014 WiWide Inc 迈外迪科技 沪ICP备08023648</p></td></tr>
                    </table>
                </td>
            </tr>
        </table>
    """.format(url='http://www.baidu.com', date_now=now().strftime('%Y-%m-%d %H:%M:%S'))

    send_mail(settings.SERVER_NAME, fromaddr, toaddr, 'test', body, settings.TANGO_EMAIL_PWD)

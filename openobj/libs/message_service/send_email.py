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


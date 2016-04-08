# coding:utf8
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from libs.message_service.base_message import base_message
from common import const

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TangoWifi.settings")


class email_message(base_message):
    display_name = ""
    attachments = []

    def send(self):
        return
        msg = MIMEMultipart()
        msg['From'] = self.from_user
        msg['To'] = self.to_user
        msg['Subject'] = self.subject
        msg["Accept-Language"] = "zh-CN"
        msg["Accept-Charset"] = "ISO-8859-1,utf-8"
        msg.attach(MIMEText(self.body, 'html', 'utf-8'))
        server = smtplib.SMTP(const.EMAIL_SERVER_NAME)
        server.login(self.from_user, const.EMAIL_PWD)
        text = msg.as_string()
        server.sendmail(self.from_user, self.to_user, text)

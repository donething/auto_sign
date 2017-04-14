# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class MailSender:
    @staticmethod
    def send_mail(subject, content):
        "发送邮件"
        msg = MIMEText(content, "plain", "utf-8")
        msg["From"] = Header("donething", "utf-8")
        msg["To"] = Header("donething", "utf-8")
        msg["Subject"] = Header(subject, "utf-8")
        try:
            mail = smtplib.SMTP()
            mail.connect("smtp.126.com", 25)
            mail.login("donething@126.com", "i42kMN8XYvQvf2sN")
            mail.sendmail("donething@126.com", "donething@126.com", msg.as_string())
            mail.quit()
            print("邮件发送成功！")
        except smtplib.SMTPException as error:
            print("邮件发送失败：" + error.strerror)

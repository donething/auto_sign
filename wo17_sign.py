# -*- coding: utf-8 -*-
import requests
from mail_sender import MailSender
from comm import Comm
import configparser


class Wo17:
    def __init__(self):
        cp = configparser.ConfigParser()
        cp.read("config.conf")
        self.__headers = {
            "User-Agent": cp.get("wo17", "agent"),
            "Host": cp.get("wo17", "host"),
            "Referer": cp.get("wo17", "referer"),
            "Cookie": cp.get("wo17", "cookie")
        }

    def do_sign(self):
        "一起沃签到"
        sign = requests.get("http://17wo.cn/signin/sign", headers=self.__headers)
        if sign.text.find("恭喜您获得") >= 0:
            print(Comm.time() + " 自动签到成功！")
            return True
        elif sign.text.find("已签到") >= 0:
            print(Comm.time() + " 重复签到！")
            return True
        else:
            print(Comm.time() + " 自动签到失败：" + sign.text)
            MailSender.send_mail(Comm.time() + " 自动签到失败！", sign.text)
            return False

    def do_redpocket(self):
        "一起沃领红包"
        redpocket = requests.get("http://17wo.cn/redPacket/openRedPacket", headers=self.__headers)
        if redpocket.text.find("抽到") >= 0:
            print(Comm.time() + " 自动领取红包成功！")
            return True
        elif redpocket.text.find("已领取") >= 0:
            print(Comm.time() + " 重复领取红包！")
            return True
        else:
            print(Comm.time() + " 自动领取红包失败：" + redpocket.text)
            MailSender.send_mail(Comm.time() + " 自动领取红包失败！", redpocket.text)
            return False

    def do_draw(self):
        "一起沃抽奖。"
        "由于系统限制，每天最多只能抽5次。这里适当提高点次数"
        num = 6
        for i in range(num):
            draw = requests.get("http://17wo.cn/integalPrize/draw", headers=self.__headers)
            print("第%d次抽奖结果：%s" % (i+1, draw.text))
        return True

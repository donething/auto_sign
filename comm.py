# -*- coding: utf-8 -*-
import time
import configparser
import os


class Comm:
    @staticmethod
    def time():
        str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return str_time

    @staticmethod
    def get_config():
        cp = configparser.ConfigParser()
        # 需要指定绝对路径，以在shell脚本中调用Python程序
        config = (os.path.join(os.path.dirname(__file__), "config.conf"))
        cp.read(config)
        return cp

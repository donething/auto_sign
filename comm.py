# -*- coding: utf-8 -*-
import time


class Comm:
    @staticmethod
    def time():
        str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return str_time

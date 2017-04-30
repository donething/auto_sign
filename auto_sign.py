# -*- coding: utf-8 -*-
from wo17_sign import Wo17
from comm import Comm


# 一起沃签到、领红包
print("========= %s 开始一起沃自动签到 =========" % Comm.time())
wo17 = Wo17()
if wo17.do_sign():          # 签到
    wo17.do_redpocket()     # 红包
    wo17.do_draw()          # 抽奖
    wo17.do_draw_17days()   # 签到满17天，额外抽奖一次


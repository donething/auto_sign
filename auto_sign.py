# -*- coding: utf-8 -*-
from wo17_sign import Wo17


# 一起沃签到、领红包
print("=================开始一起沃自动签到=================")
wo17 = Wo17()
wo17.do_sign()
wo17.do_redpocket()
wo17.do_draw()


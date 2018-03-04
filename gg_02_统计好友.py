# -*- coding:utf-8 -*-
# @Author: Gg
# @Time: 2018/3/1 11:09

from wxpy import *

# 在电脑上登录网页版版微信,并启用缓存实现自动登录
bot = Bot(cache_path=True)

#统计
friends = bot.friends()
print(friends.stats_text())
# print(friends)

# 进入Python命令行,保持程序运行,方便调试
embed()
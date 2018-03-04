# -*- coding:utf-8 -*-
# @Author: Gg
# @Time: 2018/3/1 11:09

from wxpy import *

# 在电脑上登录网页版版微信,并启用缓存实现自动登录
bot = Bot(cache_path=True)

# 查找好友,发送消息
# try:
#     my_friend = bot.friends().search('李多')[0]
# except Exception as r1:
#     print("r1:{}".format(r1))
# else:
#     # send：动态发送不同类型消息，默认为本文
#     # send_image：发送图片
#     my_friend.send('hello,长按关注我的公众号.')
#
#     try:
#         my_friend.send_image('../WechatIMG24.jpeg')
#     except Exception as r2:
#         print("r1:{}".format(r2))

# 查找群,发送消息
try:
    my_friend = bot.groups().search('哑巴群^_^')[0]
except Exception as r1:
    print("r1:{}".format(r1))
else:
    # send：动态发送不同类型消息，默认为本文
    # send_image：发送图片
    my_friend.send('hello,长按关注我的公众号.')

    try:
        my_friend.send_image('../WechatIMG24.jpeg')
    except Exception as r2:
        print("r1:{}".format(r2))


# 进入Python命令行,保持程序运行,方便调试
embed()

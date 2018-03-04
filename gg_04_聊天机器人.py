# -*- coding:utf-8 -*-
# @Author: Gg
# @Time: 2018/3/1 12:03


from wxpy import *

bot = Bot(cache_path=True)  # 在电脑上登录网页版版微信，并启用缓存
# 搜索好友，并指定。bot.friends().search的搜索结果是一个列表，所以记得指定元素[]
my_friend = bot.friends().search('李多')[0]
my_group = bot.groups().search('哑巴群^_^')[0]
# apikey,在此处输入图灵机器人的key
tuling = Tuling(api_key='133d7c74209642acbef445624446088e')


# wxpy中通过预先注册方式实现消息自动处理#预先注册是指预先将特定聊天对象的特定类型消息，
# 注册到对应的处理函数，以实现自动回复等功能。
@bot.register(my_friend)  # 预先注册
def reply_my_friend(msg):
    tuling.do_reply(msg)
    print(msg)


@bot.register(my_group)
def reply_my_group(msg):
    tuling.do_reply(msg)
    print(msg)


# wxpy的embed() 可在堵塞线程的同时，进入 Python 命令行，方便调试，一举两得。
embed()

# -*- coding: utf-8 -*-

# 本插件为默认插件，将在 qqbot 启动时自动加载。
# 如果不希望加载本插件，可以在配置文件中的 plugins 选项中删除 qqbot.plugins.schedrestart 。

# 本插件将在每天的固定时间 fresh-restart 一次，重启时间可以在配置文件中的 pluginsConf 中设置
# 示例： "pluginsConf" : {"qqbot.plugins.schedrestart": "8:00"}

from qqbot import QQBotSched as qqbotsched
from qqbot.utf8logger import INFO

def onPlug(bot):
    groupName = None
    tTime = '9:00'
	#tTime = bot.conf.pluginsConf.get(__name__, '9:00')
    content = '各位早上好'
    sendMsgOnTime(tTime, content, groupName)
    #sendMsgOnTime(time, content, groupName1)

    tTime = '12:00'
    content = '各位中午好'
    sendMsgOnTime(tTime, content, groupName)
	#sendMsgOnTime(time, content, groupName1)

    tTime = '15:30'
    content = '各位下午好'
    sendMsgOnTime(tTime, content, groupName)

    tTime = '21:00'
    content = '各位晚上好'
    sendMsgOnTime(tTime, content, groupName)
    #sendMsgOnTime(time, content, groupName1)
    

#指定时间发送群消息
def sendMsgOnTime(time, content, groupName):
    hour, minute = time.split(':')
    @qqbotsched(hour=hour, minute=minute)
    def schedStart(_bot):
        groups = None
        if groupName is not None:
            groups = _bot.List('group', groupName)
        else:
            groups = _bot.List('group')
        if groups is not None:
        	for group in groups:
        		_bot.SendTo(group, content)

    INFO('已创建计划任务： %s %s', time, content)

def onUnplug(bot):
    INFO('已删除计划任务： %s ', __name__)

# -*- coding: utf-8 -*-

# 插件加载方法： 
# 先运行 qqbot ，启动成功后，在另一个命令行窗口输入： qq plug qqbot.plugins.sample

import sqlite3

conn = sqlite3.connect("qqbot.db")

c = conn.cursor()
#c.execute(''' ''')

#input()
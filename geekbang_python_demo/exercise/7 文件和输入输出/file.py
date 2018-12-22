#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time
# 1. 创建一个文件，并写入当前日期
# 2. 再次打开这个文件，读取文件的前4个字符后退出

# fo = open("foo.txt", "w")
# fo.write("当前日期"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
# fo.close()

# 1. 创建一个文件，并写入当前日期
import datetime
now = datetime.datetime.now()
with open('c.txt', 'w') as f:
    # 注意write( )方法写入的内容是字符串类型
    f.write(str(now))


# 2. 再次打开这个文件，读取文件的前4个字符后退出
with open('c.txt', 'r') as f:
    text_4 = f.read()
    print(text_4)
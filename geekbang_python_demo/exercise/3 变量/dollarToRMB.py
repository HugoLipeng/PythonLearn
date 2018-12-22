#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 定义美元
dollar = int(input("请输入需要兑换的美元数值："));
# 定义汇率
exchange = 6.4696

# 输出结果
print('{dol}美元兑换的人民币数量为{yuan}'.format(dol=dollar, yuan=dollar * exchange))




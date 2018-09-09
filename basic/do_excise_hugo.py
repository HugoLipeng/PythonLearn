#!/usr/bin/env python 
# -*- coding:utf-8 -*-


print("a is {}, b is {} okay".format("a","b"))

string = 'hugo'

print(len(string))
print(id(string))

# 空列表
variable = []
variable = list()

range_numbers = list(range(10))
# 列表推导式
new_numbers = [numbers*10 for numbers in range_numbers]
print(new_numbers)

#字典推导式
dict_numbers = {numbers:'A' for numbers in range_numbers}
print(dict_numbers)

# 元组推导式
tuple_numbers = (numbers*20 for numbers in range_numbers)
#生成器
tuple(tuple_numbers)
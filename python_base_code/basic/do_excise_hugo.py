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


# Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
# 短路计算  在做布尔运算时，只要能提前确定计算结果，它就不会往后算了，直接返回结果
a = 'python'
print('hello,', a or 'world')

b = ''
print('hello,', b or 'world')


# 对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print(x * 10 + y)


# 针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print(s)

# 定义可变参数
def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)
print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))

# 集合是指包含一组元素的数据结构，我们已经介绍的包括：
# 1. 有序集合：list，tuple，str和unicode；
# 2. 无序集合：set
# 3. 无序集合并且具有 key-value 对：dict
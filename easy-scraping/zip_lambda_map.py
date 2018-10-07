#!/usr/bin/env python 
# -*- coding:utf-8 -*-


# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

a = [1,2,3]
b = [4,5,6]

# for zip
# zip函数接受任意多个（包括0个和1个）序列作为参数，合并后返回一个tuple列表
list(zip(a,b))
list(zip(a,a,b))
for i, j in zip(a,b):
    print(i,j)

#for lambda
# lambda定义一个简单的函数，实现简化代码的功能，看代码会更好理解。
# fun = lambda x,y : x+y, 冒号前的x,y为自变量，冒号后x+y为具体运算。
def f1(x,y):
    return x+y
f2= lambda x, y : x + y
print(f1(1,2))
print(f2(1,2))

# for map
# map是把函数和参数绑定在一起。
print(list(map(f1, [1],[2])))
print(list(map(f2, [2,3],[4,5])))
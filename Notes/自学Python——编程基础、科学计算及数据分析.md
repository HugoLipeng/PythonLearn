# 自学Python——编程基础、科学计算及数据分析

<https://github.com/lijin-thu/notes-python> 学习笔记：

1，ipython 解释器  
在命令行输入 ipython 进入；  
2，ipython notebook  
3，Anaconda是一个很好用的Python IDE  

4，变量：  
类型	例子

整数  	-100  
浮点数	 3.1416  
字符串	'hello'  
列表	[1, 1.2, 'hello']  
字典	{'dogs': 5, 'pigs': 3}  
Numpy数组	array([1, 2, 3])  

长整型	1000000000000L  
布尔型	True, False  
元组	('ring', 1000)  
集合	{1, 2, 3}  
Pandas类型	DataFrame, Series  
自定义	Object Oriented Classes  

5，String  
可以用 dir 函数查看所有可以使用的方法  

6，base64  
> import base64  
> base64.b64encode(b'binary\x00string')  
> b'YmluYXJ5AHN0cmluZw=='  
> base64.b64decode(b'YmluYXJ5AHN0cmluZw==')  
> b'binary\x00string'

7，分片： var[lower:upper:step]  

8，代码块 ==> 相同缩进  

```
x = -0.5  
if x > 0:  
    print "Hey!"
    print "x is positive"
    print "This is still part of the block"
print "This isn't part of the block, and will always 


This isn't part of the block, and will always print.
```  


9，列表推导式  
一般用循环生成列表：

```
values = [10, 21, 4, 7, 12]
squares = []
for x in values:
    squares.append(x**2)
print squares
```  

列表推导式可以使用更简单的方法来创建这个列表：  

```
values = [10,21,4,7,12]
squares = [x**2 for x in values x <= 10]
print(squares)  
square_set = {x**2 for x in values if x <= 10}
print(square_set)
square_dict = {x: x**2 for x in values if x <= 10}
print(square_dict)
```  


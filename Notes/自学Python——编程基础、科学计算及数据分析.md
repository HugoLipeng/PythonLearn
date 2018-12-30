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

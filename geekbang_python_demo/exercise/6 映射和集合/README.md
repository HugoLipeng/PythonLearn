# 练习一 字典的使用

1. 定义一个字典，分别使用a、b、c、d作为字典的关键字，值为任意内容
2. 为该字典增加一个元素‘c':'cake'后，将字典输出到屏幕 
3. 取出字典中关键字为d的值
```python
dict = {"a":123,"b":234,"c":456,"d":223233}

dict['c'] = 'cake'
print(dict)

print(dict['d'])
```

# 练习二 集合的使用
1. 将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕

```python
str1 = 'hello'
print(set(str1))
```
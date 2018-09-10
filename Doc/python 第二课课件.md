
    人生苦短，我用python

# python第二课

### 课程内容
    1、 条件判断
    2、 循环
    3、 函数
    4、 类

### 条件判断


```python
if condition:
    do somthing
else:
    do somthing
```

### 应用题：小姐姐买水果，合计金额为32.5元，水果店搞活动，满30打九折，求小姐姐的实际花费？


```python
total_cost = 32.5

if total_cost > 30:
    discount = 0.9
else:
    discount = 1
    
total_cost *= discount
print('小姐姐的实际花费为： {}元'.format(total_cost))
```

    小姐姐的实际花费为： 29.25元


### 应用题：如果购买水果消费超过30元，打九折，超过50元，打八折，求小姐姐实际花费？


```python
total_cost = 32.5
is_vip = True

if total_cost > 50:
    if is_vip:
        discount = 0.8
    else:
        discount = 1
elif total_cost > 30:
    discount = 0.9
else:
    discount = 1

total_cost *= discount
print("总花费为: {} 元".format(total_cost))
```

    总花费为: 29.25 元


### 重点

    1、条件判断可以任意组合
        第一层意思：elif可以有0到任意多个，else可有可无
        第二层意思：条件判断可以进行嵌套
    2、着重来看一下condition


```python
bool(''), bool({}), bool([])
```




    (False, False, False)




```python
condition = {}
if condition:
    print('True')
else:
    print('False')
```

    False


### 从理解的角度来讲，一个值被当做布尔值，概念上更像是有与没有的区别。

and or not 

### 布尔型变量做运算


```python
a = True
b = False
print('a and b is {}'.format(a and b))

print('a or b is {}'.format(a or b))
```

    a and b is False
    a or b is True


### 非布尔型变量做 and or not 运算


```python
a = ''
b = []
print(bool(b))

print('a and b is {}'.format(a and b))
print('a or b is {}'.format(a or b))
```

    False
    a and b is 
    a or b is []



```python
# 非布尔型变量 and 运算
a = [1,2,3]
b = 10
print(b and a)

# 非布尔型变量 or 运算
a = 'ni hao'
b = {'apple': 100}
print(a or b)

# 非布尔型变量 not 运算，永远返回True 或者 False
print(not b)
```

    [1, 2, 3]
    ni hao
    False


### 条件判断的近亲 - 断言


```python
if not condition:
    crash program
    
# 它的意思就是说：我断言它肯定是这样的，如果不这样，那我就崩溃
```


```python
age = 19
assert age == 18, '她竟然不是18岁'
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-36-80eeb9c59e3f> in <module>()
          1 age = 19
    ----> 2 assert age == 18, '她竟然不是18岁'
    

    AssertionError: 她竟然不是18岁


### 循环

    for 循环    - 遍历循环
    while 循环  - 条件


```python
costs = [3,4,12,23,43,100]
for cost in costs:
    print('消费 {} 元'.format(str(cost).center(10)))
```

    消费     3      元
    消费     4      元
    消费     12     元
    消费     23     元
    消费     43     元
    消费    100     元


#### 生成一个长度为20的随机列表


```python
import random

random_numbers = []
while len(random_numbers) < 20:
    random_numbers.append(random.randint(1,10))
    
print(random_numbers, len(random_numbers))
```

    [5, 6, 10, 5, 2, 2, 6, 3, 5, 6, 6, 8, 4, 3, 6, 10, 8, 4, 1, 2] 20


### 编程建议： 就是只要能使用for循环，就不要使用while循环。


```python
random_numbers = []
for i in range(20):
    random_numbers.append(random.randint(1,10))

print(random_numbers, len(random_numbers))
```

    [8, 10, 7, 9, 2, 2, 6, 3, 9, 8, 7, 2, 7, 4, 10, 6, 9, 2, 8, 8] 20


### 什么时候必须用while循环：当循环的条件跟数量没有关系时，只能用while

### 题目：往空列表中添加随机数，知道添加的数为9，则终止


```python
random_numbers = []
while (9 not in random_numbers):
    random_numbers.append(random.randint(1,10))

print(random_numbers, len(random_numbers))
```

    [6, 3, 7, 5, 9] 5


### 重点： 只有一个元素的列表
#### 问题：a = [1,2,3]， b = 1,   c = (b in a), 大家猜测一下，c是一个什么类型，它是不是一个元组呢？


```python
# 死循环演示
import time

number = 0
while True:
    time.sleep(1)
    number += 1
    print('hello world. {} '.format(number), end='\r')
```

    hello world. 66 


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-102-1c1b54bbf361> in <module>()
          3 number = 0
          4 while True:
    ----> 5     time.sleep(1)
          6     number += 1
          7     print('hello world. {} '.format(number), end='\r')


    KeyboardInterrupt: 



```python
a = [1]
b = (1,)
type(a), type(b), b, len(b)
```




    (list, tuple, (1,), 1)




```python
random_numbers
```




    [6, 3, 7, 5, 9]



### continue 跳过


```python
random_numbers = [2,3,5,6,8]
```


```python
for number in random_numbers:
    if number % 2 == 0:
        print('{} is 偶数'.format(number))
    else:
        continue
        
    print('没有跳过')
```

    2 is 偶数
    没有跳过
    6 is 偶数
    没有跳过
    8 is 偶数
    没有跳过


### 跳出循环


```python
for number in random_numbers:
    if number % 2 == 0:
        print('{} is 偶数'.format(number))
    else:
        break
    
    print('没有结束')
```

    2 is 偶数
    没有结束


#### 循环中的else: 如果再循环过程中没有碰到break 语句，就会执行else里的代码


```python
random_numbers = [4,2,4]
for number in random_numbers:
    if number % 2 == 0:
        print('{} is 偶数'.format(number))
    else:
        break
    
    print('没有结束')
else:
    print("全是偶数")
```

    4 is 偶数
    没有结束
    2 is 偶数
    没有结束
    4 is 偶数
    没有结束
    全是偶数


### for 循环可以构建推导式


```python
# 所谓推导式，就是一种从一个数据序列构建另一个数据序列的方法。
```


```python
random_numbers = list(range(10))
random_numbers
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
new_numbers = []
for number in random_numbers:
    new_numbers.append(number*10)

new_numbers
```




    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]



### 列表推导式


```python
new_numbers = [number*10 for number in random_numbers]
new_numbers
```




    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]



### 字典推导式


```python
dict_numbers = {number: 'A' for number in random_numbers}
dict_numbers
```




    {0: 'A',
     1: 'A',
     2: 'A',
     3: 'A',
     4: 'A',
     5: 'A',
     6: 'A',
     7: 'A',
     8: 'A',
     9: 'A'}




```python
tuple_numbers = (number*10 for number in random_numbers)
tuple_numbers
```




    <generator object <genexpr> at 0x1024730a0>



### 生成器


```python
tuple(tuple_numbers)
```




    ()



### 函数


```python
varibal = {
    'a': 100,
    'b': 100,
    'c': 200
}
```


```python
varibal['a']
```




    100




```python
varibal.items()
```




    dict_items([('a', 100), ('b', 100), ('c', 200)])




```python
[key for key, value in varibal.items() if value == 100]
```




    ['a', 'b']



### 函数 - 抽象概念


```python
def get_keys(dict_varibal, value):
    return [k for k, v in dict_varibal.items() if v == value]
```


```python
get_keys(varibal, 200)
```




    ['c']



###    函数是组织好的，可重复使用的，能够完成特定功能的代码块，它是代码块的抽象。


```python
get_keys({'a': 40}, 40)
```




    ['a']



### 位置参数是不可以交换位置


```python
get_keys(40, {'a': 40})
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-165-56a757bc2396> in <module>()
    ----> 1 get_keys(40, {'a': 40})
    

    <ipython-input-162-2a83166bc68e> in get_keys(dict_varibal, value)
          1 def get_keys(dict_varibal, value):
    ----> 2     return [k for k, v in dict_varibal.items() if v == value]
    

    AttributeError: 'int' object has no attribute 'items'



```python
def get_keys(dict_varibal, value):
    return [k for k, v in dict_varibal.items() if v == value]
```

- get_keys 函数名
- （）中为参数； dict_varibal： 形参，调用的时候传递的值才是实参
- return 是返回值

    1、位置参数
    2、关键字参数, 可以不按照顺序去写


```python
get_keys(dict_varibal={'a': 40}, value=40)
```




    ['a']




```python
get_keys(value=40, dict_varibal={'a': 40})
```




    ['a']



### 函数通过参数获取我们传递的值，函数中改变了参数的值，那么我们传递进去的值会改变吗？


```python
def test(varibal):
    varibal = 100
    return varibal
```


```python
var = 1
test(var)
```




    100




```python
print(var)
```

    1



```python
def test(varibal):
    varibal.append(100)
    return varibal
```


```python
var = []
test(var)
```




    [100]




```python
var
```




    [100]



### 不建议对可变类型在函数内进行更改，建议用函数返回值进行重新赋值


```python
def test(varibal):
    temp = varibal.copy()
    temp.append(100)
    return temp
```


```python
var = []
var = test(var)
```


```python
var
```




    []



### 参数的收集


```python
def test(name, age, *args, **kwargs):
    print(name, age, *args, **kwargs)
```


```python
test('wong', 12)
```

    wong 12 ()



```python
test('wong', 12, 23, 'lkl', [23,34])
```

    wong 12 23 lkl [23, 34]



```python
dict_varibals = {
    'weight': 120,
    'height': 175
}
test('wong', 12, dict_varibals)
```

    wong 12 {'weight': 120, 'height': 175}


### 装饰器


```python
a = 10
b = [12,12]

def test():
    print('test')
    
c = test
```

### 可以把函数赋值给一个变量


```python
c.__name__
```




    'test'




```python
def test(func):
    return func

def func():
    print('func run')
    
f = test(func)
f.__name__
f()
```

    func run


### 函数可以当做函数的返回值进行返回


```python
# 返回一个从0到1的浮点值
def test():
    return round(random.random(), 1)
```


```python
# 函数返回的浮点值保留三个有效数字
```


```python
test()
```




    0.745



### python另一个语法糖，装饰器


```python
# 返回一个从0到1的浮点值
@decorator
def test():
    return random.random()

@decorator
def test_two():
    return random.random()*10
```


```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # do something 
        return round(func(*args, **kwargs), 2)
    return wrapper
```


```python
# f = decorator(test) 完全等价于装饰器@的写法
```


```python
test()
```




    0.92




```python
test_two()
```




    9.99



### 类


```python
class Person:
    
    def __init__(self, name, age):
        self._name = name
        self._age  = age
    
    def get_name(self):
        return self._name
    
    def rename(self, new_name):
        self._name = new_name
```

### 初始化函数中，self后面的是实例化对象的属性，加下划线的意思是，代表这个属性是私有的，不应该访问


```python
s = 'hello world'
s.center(12)
```




    'hello world '




```python
p = Person('wong', 12)
```


```python
p.get_name()
```




    'wong'




```python
p.rename('wong lei')
```


```python
p.get_name()
```




    'wong lei'




```python
p_2 = Person('li', 11)
p_2.get_name()
```




    'li'



#### pass代表着什么都不做，只是占个位而已


```python
class Student(Person):
    def set_score(self, score):
        self._score = score
        
    def get_score(self):
        return self._score
```


```python
s = Student('liu', 24)
s.get_name()
```




    'liu'




```python
s.set_score(100)
```


```python
s.get_score()
```




    100




```python
class Person:
    
    def __init__(self, name, age):
        self._name = name
        self._age  = age
    
    @property
    def name(self):
        return self._name
    
    def rename(self, new_name):
        self._name = new_name
```


```python
p = Person('liu', 24)
p.name
```




    'liu'



### 分享一下

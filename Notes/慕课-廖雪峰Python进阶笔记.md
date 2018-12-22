# 慕课-廖雪峰Python进阶笔记

### 函数式编程的特点

1、把计算视为函数而非指令

2、纯函数式编程：不需要用变量，没有副作用，测试简单

3、支持高阶函数，代码简洁

Python支持的函数式编程：

1、不是纯函数式编程：允许有变量  

2、支持高阶函数：函数也可以作为变量传入

3、支持闭包：有了闭包，就能返回函数

4、有限度的支持匿名函数

### 高阶函数
变量可以指向函数

函数名其实就是指向函数的变量

f = abs # f为指向函数abs的变量  
f(-20) # 结果为20  
高阶函数：能接收函数做参数的函数  

```import math
def add(x, y, f):
    return f(x) + f(y)
print add(25, 9, math.sqrt)
```


### python中filter()函数
请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
import math
def is_sqr(x):
    r = int(math.sqrt(x))
    return r*r==x
print filter(is_sqr, range(1, 101))

```

### python中返回函数
请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
```angular2html
def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod([1, 2, 3, 4])
print f()
```

### python中匿名函数
利用匿名函数简化以下代码：
```
def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
```

定义匿名函数时，没有return关键字，且表达式的值就是函数返回值。

参考代码:
```
print filter(lambda s: s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END'])
```

### python中装饰器
装饰器函数（参数是旧函数）返回一个新函数（参数是旧函数的参数），这个新函数增添了新的功能并且返回（调用）了旧函数

装饰器可以极大地简化代码，避免每个函数编写重复性代码

几种装饰器：

    打印日志：@log

    检测性能：@performance

    数据库事务：@transaction

    URL路由：@post（'/register'）
    

无参数decorator
计算函数调用的时间可以记录调用前后的当前时间戳，然后计算两个时间戳的差。  
```
import time
def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %fs' % (f.__name__, (t2 - t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
```

带参数decorator
请给 @performace 增加一个参数，允许传入's'或'ms'：

```
import time
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
```

### python中偏函数


### python中模块和包
引用其他模块：

import ——模块.函数名

包就是文件夹，可以有多级，模块就是py文件

包下面有个__init__.py，且每层都必须要有


### python中继承
1、用class 子类名（父类名）来继承父类

2、用super().__init__()来初始化父类已有的方法  
def __init__(self,args):
    super(SubClass,self).__init__(args)
    pass  
    
3、is关系：子类is父类【继承】

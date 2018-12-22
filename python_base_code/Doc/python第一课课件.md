
    人生苦短，我用python

# python课程

### 课表
    一、 python基础    -     变量与数据类型，及常见数据类型的用法
    二、 python基础    -     条件、循环、函数、类
    三、 python爬虫    -     python爬虫并用Mysql数据库存储
    四、 pandas通览    -     用pandas做数据处理与分析
    五、 实战          -     泰坦尼克幸存者预测

### 学完本课程之后，你会：
    1、 掌握基本的python语法，并编写简单的python程序
    2、 可以阅读别人写的python代码
    3、 编写简单的爬虫
    4、 进行基本的数据分析

### 机器学习需要：
    1、 数学理论知识  (统计、线性代数、微积分 。。。)
    2、 编程能力（python)

### python的特性
    1、python语法简单，容易理解，容易学习
    2、跨平台，可在windows/linux/mac os等系统上运行
    3、可以做网站、爬虫、大数据处理、机器学习
    4、拥有强大、丰富的第三方库  numpy、pandas ...

### 最简单的开始


```python
print('hello, "world')
```

    hello, "world



```python
print("hello, 'world")
```

    hello, 'world



```python
import this
```
python之禅  
                作者：Tim Peters

优美胜于丑陋                                                  Python 以编写优美的代码为目标
明了胜于晦涩                                                  优美的代码应当是明了的，命名规范，风格相似 
简洁胜于复杂                                                  优美的代码应当是简洁的，不要有复杂的内部实现 
复杂胜于凌乱                                                  如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁 
扁平胜于嵌套                                                  优美的代码应当是扁平的，不能有太多的嵌套
间隔胜于紧凑                                                  优美的代码有适当的间隔，不要奢望一行代码解决问题 
可读性很重要                                                  优美的代码是可读的 
即便假借特例的实用性之名，也不可违背这些规则                        这些规则至高无上 
不要包容所有错误，除非你确定需要这样做                             精准地捕获异常，不写 except:pass 风格的代码 
当存在多种可能，不要尝试去猜测 
而是尽量找一种，最好是唯一一种明显的解决方案                        如果不确定，就用穷举法
虽然这并不容易，因为你不是Python之父                             这里的 Dutch 是指 Guido 
做也许好过不做，但不假思索就动手还不如不做                          动手之前要细思量
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然             方案测评标准
命名空间是一种绝妙的理念，我们应当多加利用                          倡导与号召
### 从计算器开始


```python
5 + 100
```




    105




```python
100 / 10
```




    10.0




```python
100 * 10
```




    1000




```python
100 - 99
```




    1




```python
10 % 3
```




    1




```python
10 ** 3
```




    1000




```python
10 ** (1/3)
```




    2.154434690031884




```python
import math
```


```python
math.pi
```




    3.141592653589793




```python
math.sin(math.pi/2)
```




    1.0




```python
math.floor(9.23432)
```




    9




```python
math.ceil(9.234)
```




    10



### 应用题：
    1、小姐姐去买水果，苹果5元一斤，葡萄15元一斤，现在小姐姐买了2斤苹果，1.5斤葡萄，问，小姐姐买这两种水果分别花了多少钱？总共花了多少钱？


```python
# 苹果的花费
print(5*2)

# 葡萄的花费
print(15*1.5)

# 总花费
print((5*2) + (15*1.5))
```

    10
    22.5
    32.5


### 三个问题：
    1、如果脱离了题干和注释，我们无法理解 5 * 2 是什么意思
    2、当计算总价的时候，重复计算了苹果和葡萄的花费
    3、输出是一个数字，表达不清晰


```python
apple_price = 5
apple_weight = 2
apple_cost = apple_price * apple_weight

grape_price = 15
grape_weight = 1.5
grape_cost = grape_price * grape_weight

total_cost = apple_cost + grape_cost

print(apple_cost, total_cost)
```

    10 32.5


### 增强的格式化字符串函数 format


```python
"苹果的花费为：{}；葡萄的花费为：{}；总花费为：{}".format(apple_cost, grape_cost, total_cost)
```




    '苹果的花费为：10；葡萄的花费为：22.5；总花费为：32.5'



### 变量： 代表某个值得名称


```python
number + 2
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-34-e96a55dd7add> in <module>()
    ----> 1 number + 2
    

    NameError: name 'number' is not defined


### 语法糖


```python
a = 10 
b = 20

a, b = b, a
```


```python
print("a is {}, b is {}".format(a, b))
```

    a is 20, b is 10


### 命名规范

    1、标识符的第一个字符必须是字母表中的字母(大写或小写)或者一个下划线
    2、标识符名称的其他部分可以由字母(大写或小写)、下划线(‘_’)或数字(0-9)组成。
    3、标识符名称是对大小写敏感的。


```python
n = 10
N = 10
```


```python
# 错误： 首字符为数字
3thidnf = 10 
```


      File "<ipython-input-45-d2231249f0f8>", line 2
        3thidnf = 10
              ^
    SyntaxError: invalid syntax




```python
# 字母中间有空格，为非法字符
my name = 100
```


      File "<ipython-input-49-61ab1aa1327b>", line 2
        my name = 100
              ^
    SyntaxError: invalid syntax




```python
# -是变量命名中的非法字符
my-name = 10
```


      File "<ipython-input-48-69fd2ff4a721>", line 2
        my-name = 10
                    ^
    SyntaxError: can't assign to operator




```python
round(100/3, 3)
```




    33.333



### 代码规范建议

- 1、不要使用单字符
- 2、变量名能清晰表达变量的意思
- 3、合理使用字母中间下划线

### 变量类型

    1、字符串 str
    2、数字 int float complex ..
    3、列表 list
    4、元组 tuple
    5、字典 dict

### 数值类型


```python
number = 10
number = number + 10
number += 10
```


```python
number -= 10
number *= 10
number /= 10
```


```python
import math
```


```python
# 乘方、开放
math.pow(3, 10)
```




    59049.0




```python
# 推荐是用
3 ** 10
```




    59049




```python
math.floor(2.23242)
```




    2




```python
math.ceil(2.234234)
```




    3




```python
# 度的转换
math.radians(180)
```




    3.141592653589793




```python
math.sin(math.pi/2)
```




    1.0




```python
min(10, 12, 234, 100, 1)
```




    1




```python
max(10, 12, 234, 100, 1)
```




    234




```python
sum([10, 12, 234, 100, 1])
```




    357




```python
divmod(10, 3)
```




    (3, 1)



### bool型


```python
True, False
```




    (True, False)




```python
True == 1
```




    True




```python
False == 0
```




    True




```python
# 不建议这样写，没有意义， 有一个特例，后面会讲到
True + 10
```




    11




```python
100 > 10
```




    True



### bool类型，运算： 与运算、或运算、非运算


```python
# 与运算，同为真则为真
True and False
```




    False




```python
# 或运算, 只要一个为真则为真
True or False
```




    True




```python
# 非运算，取反
not False
```




    True



| 操作符 | 解释 |
| ---  | --- |
| <  | 小于 |
| <=  | 小于等于 |
| >  | 大于 |
| >=  | 大于等于 |
| ==  | 等于 |
| !=  | 不等于 |
| is  | 是相同对象 |

### 字符串


```python
# 字符串可以用双引号，也可以用单引号。通过单、双引号的恰当使用，可以避免不必要的字符转义（escape）,也就是说，可以避免使用 \ (转义字符)

line = "hello world"
line = "hello world\""
line = 'hello \'world'
```


```python
# 字符串的加法操作
line_1 = "ni hao, "
line_2 = 'xiaojiejie'
line_1 + line_2
```




    'ni hao, xiaojiejie'




```python
# 字符串的乘法操作
line = 'nihao '
line * 10
```




    'nihao nihao nihao nihao nihao nihao nihao nihao nihao nihao '




```python
# 字符串是不可变类型的变量
line
```




    'nihao '




```python
line = 'buhao '
line
```




    'buhao '




```python
# 返回字符串的长度
len(line)
```




    6




```python
line = 'nihao '
line_copy = line
# id函数，返回一个身份识别符，可以理解为一个变量的内存地址
id(line), id(line_copy)
```




    (4417536944, 4417536944)




```python
line = 'buhao '
id(line), id(line_copy)
```




    (4417537336, 4417536944)




```python
23 + 10
```




    33



### markdown中表格的写法

| 序号 | 名称 | 年龄 |
| --- | :---: | --- |
| 1 | wong | 18 |
| 2 | sun xing zhe | 500 |

### 切片


```python
line = 'huan ying da jia lai wan men shang ke'
```

### 取前十个字符


```python
line[0:10]
```




    'huan ying '




```python
line[0:20:3]
```




    'Akjd'



### 取后十个字符


```python
line[-10:]
```




    'n shang ke'



### 翻转字符


```python
line[::-1]
```




    'ek gnahs nem naw ial aij ad gniy nauh'



### 单字符

### 单字符是不可以进行赋值的


```python
line[-1] = 'E'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-134-6dbfc2cde6c6> in <module>()
    ----> 1 line[-1] = 'E'
    

    TypeError: 'str' object does not support item assignment



```python
line.capitalize()
```




    'Huan ying da jia lai wan men shang ke'




```python
line = "ASDFASDFEWFSDF"
line.capitalize()
```




    'Asdfasdfewfsdf'




```python
# 居中
line.center(20)
```




    '   ASDFASDFEWFSDF   '




```python
# 计数
line.count('Z')
```




    0



### 字符串首尾判断


```python
line.endswith('FEWFSDD')
```




    False




```python
line.startswith('ASDFA')
```




    True




```python
line
```




    'ASDFASDFEWFSDF'




```python
line.find('A', 2)
```




    4




```python
# 当字符不存在时，报错
line.index('Z')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-167-a63f130686f3> in <module>()
          1 # 当字符不存在时，报错
    ----> 2 line.index('Z')
    

    ValueError: substring not found



```python
line = 'Aslkdfjsldkf'
```


```python
line.upper()
```




    'ACDASDLDSD'




```python
line.lower()
```




    'acdasdldsd'




```python
line.istitle()
```




    True




```python
line.isupper()
```




    False




```python
line.islower()
```




    False




```python
line = '   lskdas k  \n\t   '
```


```python
line.strip()
```




    'lskd \n as k'




```python
line.rstrip()
```




    '   lskd \n as k'




```python
line.lstrip()
```




    'lskd \n as k  \n\t   '




```python
line = 'Aslkdfjsldkf'
```


```python
line.swapcase()
```




    'aSLKDFJSLDKF'



### 【重点】上面我们用到的所有字符串函数，都是为我们生成了一个新的字符串，原有的字符串是不变的


```python
line = "ni hao"
id(line)
```




    4417602368




```python
new_line = line.upper()
id(line), id(new_line)
```




    (4417602368, 4417601976)



### 列表


```python
# 空列表
varibals = []
varibals = list()
```

#### 可以容纳任意类型的对象，任意数量的对象 【重点】列表是可变类型的


```python
varibals = [1, 2, 3, 'ni hao', 'hello, python', [], [100, 100]]
```


```python
varibals = []
varibals.append(1)
varibals.append(2)
varibals.append('ni hao')
varibals
```




    [1, 2, 'ni hao']




```python
varibals[0] = 10
varibals
```




    [10, 2, 'ni hao']



### python是一种动态类型的语言，一个变量是什么类型，要看程序在运行过程中变量所代表的值是什么


```python
var = 10
type(var)
var = 'str'
type(var)
```




    str



### 切片


```python
varibals[-2:]
```




    [2, 'ni hao']




```python
varibals + [1,23]
```




    [10, 2, 'ni hao', 1, 23]




```python
varibals * 4
```




    [10, 2, 'ni hao', 10, 2, 'ni hao', 10, 2, 'ni hao', 10, 2, 'ni hao']



### 序列 列表是一种容器型的序列；字符串是一种扁平型的序列


```python
len(varibals)
```




    3




```python
# 没有返回值，而是修改了我们列表对象本身
varibals.append(1)
varibals
```




    [10, 2, 'ni hao', 1, 1, 1]




```python
# 清空
varibals.clear()
```


```python
varibals = [1,12,23,4234, [1,2]]
```


```python
new_varibals = varibals.copy()
```


```python
new_varibals[-1][0] = 99999
new_varibals
```




    [1, 12, 23, 4234, [99999, 2]]




```python
varibals
```




    [1, 12, 23, 4234, [99999, 2]]




```python
id(new_varibals[-1]), id(varibals[-1])
```




    (4414081800, 4414081800)




```python
a = [1,2]
b = [3,4]
a + b
```




    [1, 2, 3, 4]




```python
a.extend(b)
a
```




    [1, 2, 3, 4, 3, 4]




```python
a
```




    [1, 2, 3, 4, 3, 4]




```python
a.insert(0, 100)
```


```python
a
```




    [100, 1, 2, 3, 4, 3]




```python
a.pop(0)
```




    100




```python
a
```




    [1, 2, 3, 4, 3]




```python
a.remove('z')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-271-c7b29c338c05> in <module>()
    ----> 1 a.remove('z')
    

    ValueError: list.remove(x): x not in list



```python
a
```




    [1, 3, 4, 3]




```python
a.remove?
```


```python
a
```




    [1, 4, 3]




```python
a.sort(reverse=True)
```


```python
a
```




    [4, 3, 1]




```python
5 in a
```




    False



### tuple


```python
var = tuple()
var = ()
type(var)
```




    tuple




```python
var = (1,2, 1, 3,4,5, [23,34,43])
```


```python
var.count(1)
```




    2




```python
var.index(5)
```




    5




```python
a, b = 10, 20
```


```python
a = 10, 20
```


```python
a
```




    (10, 20)



| 元组变量 | 字符串变量 | 列表变量 | 
| --- | --- | -- |
| t_1 = [1,2,3,4,5] | s_1 = 'ni hao' | l_1 = [1,2,3,4,5] |
| t_2 = [5,6,7,8,9] | s_2 = 'how are you' | l_2 = [6,7,8,9,10] |

| 函数 | 元组 | 实例 | 字符串 | 实例 | 列表 | 实例 |
| :--- | :---: | :--- | :---: | :--- | :---: | :-- | :--- |
| + | ✅ | t_1 + t_2 | ✅ | s_1 + s_2 | ✅ | l_1 + l_2 |
| * | ✅ | t_1 * 2 | ✅ | s_1 * 2 | ✅ | l_1 * 2 |
| > < | ✅ | t_1 > t_2 | ✅ | s_1 > s_2 | ✅ | l_1 > l2 |
| [index] | ✅ | t_1[0] | ✅ | s_1[0] | ✅ | l_1[0] | 列表可以索引赋值，字符串、元组不可以 |
| [::] | ✅ | t_1[::] | ✅ | s_1[0:10:1] | ✅ | l_1[0:10:2] | 列表可以切片赋值，字符串、元组不可以 |
| len | ✅ | len(t_1) |✅ | len(s_1) | ✅ | len(l_1) |
| bool | ✅ | bool(t_1) |✅ | bool(s_1) | ✅ | bool(l_1) | 空字符串、空列表、空元组转换为布尔型为False |
| count | ✅ | t_1.count(1) | ✅ | s_1.count('n') | ✅ | l_1.count(1) |
| index | ✅ | t_1.index(3) | ✅ | s_1.index('n') | ✅ | l_1.index(1) | 
| replace | | | ✅ | s_1.replace('n', 'N') | | | 字符串replace函数返回一个新字符串，原来的变量不变 |
| sort | | | | | ✅ | l_1.sort() |
| reverse | | |  |  | ✅ | l_1.reverse() | 字符串不可更改，只能通过生成一个新的字符串来翻转 | 
| append | | |  | | ✅ | l_1.append(100) |
| extend | | | | | ✅ | l_1.extend(l_2) |
| remove | | | | | ✅ | l_1.remove(1) |
| pop | | | | | ✅ | l_1.pop() |

### 字典类型


```python
var = {}
var = dict()
type(var)
```




    dict




```python
var = {
    '中': 100,
    '左': 200
}
```


```python
var['中']
```




    100




```python
words = ['中', '左']
location = [100, 200]

location[words.index('中')]
```




    100



### 拉锁函数


```python
new_var = list(zip(words, location))
```


```python
new_var
```




    [('中', 100), ('左', 200)]




```python
dict(new_var)
```




    {'中': 100, '左': 200}




```python
list(zip([1,2], [3,4, 5], [4,5,5]))
```




    [(1, 3, 4), (2, 4, 5)]




```python
students = ['wong', 'li', 'sun', 'zhao', 'qian']
```


```python
money = dict.fromkeys(students, 10)
```

### 访问字典中的值


```python
money['wong']
```




    10




```python
a = money.get('ww', '100')
```


```python
print(a)
```

    100



```python
money.keys()
```




    dict_keys(['wong', 'sun', 'qian', 'li', 'zhao'])




```python
money.values()
```




    dict_values([10, 10, 10, 10, 10])




```python
money.items()
```




    dict_items([('wong', 10), ('sun', 10), ('qian', 10), ('li', 10), ('zhao', 10)])




```python
# 删除操作
money.pop('wong')
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-331-288dcedd1b7e> in <module>()
          1 # 删除操作
    ----> 2 money.pop('wong')
    

    KeyError: 'wong'



```python
money
```




    {'li': 10, 'qian': 10, 'sun': 10, 'zhao': 10}




```python
money['nihao'] = 100
```


```python
money
```




    {'guli': 100,
     'li': 10,
     'nihao': 100,
     'qian': 10,
     'sun': 10,
     'wong': 100,
     'zhao': 10}




```python
money.setdefault('haha', 1000)
```




    1000




```python
money
```




    {'guli': 100,
     'haha': 1000,
     'li': 10,
     'nihao': 100,
     'qian': 10,
     'sun': 10,
     'wong': 100,
     'zhao': 10}




```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```

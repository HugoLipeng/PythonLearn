[莫烦Python](https://github.com/MorvanZhou/easy-scraping-tutorial)

[莫烦机器学习 step by step](https://morvanzhou.github.io/learning-steps/)

[基础知识全套代码](https://github.com/MorvanZhou/tutorials/tree/master/basic)  

[多线程 threading 教程](https://morvanzhou.github.io/tutorials/python-basic/threading/)  

在多线程 (Threading) 里提到过, 它是有劣势的, GIL 让它没能更有效率的处理一些分摊的任务. 而现在的电脑大部分配备了多核处理器, 多进程 Multiprocessing 能让电脑更有效率的分配任务给每一个处理器, 这种做法解决了多线程的弊端. 也能很好的提升效率.  

[多进程 multiprocessing 教程](https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/)  



Notes  
* python当中^符号，区别于Matlab，在python中，^用两个**表示，如3的平方为3**2 , **3表示立方，**4表示4次方，依次类推

* 很遗憾的是 python 中并没有类似 condition ? value1 : value2 三目操作符;    
 python 可以通过 if-else 的行内表达式完成类似的功能。   
 var = var1 if condition else var2
 
### 函数默认参数
3.1 自调用

如果想要在执行脚本的时候执行一些代码，比如单元测试，可以在脚本最后加上单元测试 代码，但是该脚本作为一个模块对外提供功能的时候单元测试代码也会执行，这些往往我们不想要的，我们可以把这些代码放入脚本最后：
```
if __name__ == '__main__':
    #code_here
```

    
如果执行该脚本的时候，该 if 判断语句将会是 True,那么内部的代码将会执行。 如果外部调用该脚本，if 判断语句则为 False,内部代码将不会执行。

3.2 可变参数

顾名思义，函数的可变参数是传入的参数可以变化的，1个，2个到任意个。当然可以将这些 参数封装成一个 list 或者 tuple 传入，但不够 pythonic。使用可变参数可以很好解决该问题，注意可变参数在函数定义不能出现在特定参数和默认参数前面，因为可变参数会吞噬掉这些参数。


    ```
    def report(name, *grades):
    total_grade = 0
    for grade in grades:
        total_grade += grade
    print(name, 'total grade is ', total_grade)
    ```
定义了一个函数，传入一个参数为 name, 后面的参数 *grades 使用了 * 修饰，表明该参数是一个可变参数，这是一个可迭代的对象。该函数输入姓名和各科的成绩，输出姓名和总共成绩。所以可以这样调用函数 report('Mike', 8, 9)，输出的结果为 Mike total grade is 17, 也可以这样调用 report('Mike', 8, 9, 10)，输出的结果为 Mike total grade is 27

3.3 关键字参数

关键字参数可以传入0个或者任意个含参数名的参数，这些参数名在函数定义中并没有出现，这些参数在函数内部自动封装成一个字典(dict).


```
 def portrait(name, **kw):
    print('name is', name)
    for k,v in kw.items():
    print(k, v)
        
```
定义了一个函数，传入一个参数 name, 和关键字参数 kw，使用了 ** 修饰。表明该参数是关键字参数，通常来讲关键字参数是放在函数参数列表的最后。如果调用参数 portrait('Mike', age=24, country='China', education='bachelor') 输出:

name is Mike
age 24
country China
education bachelor
通过可变参数和关键字参数，任何函数都可以用 universal_func(*args, **kw) 表达。



### 错误处理  
错误处理 

输出错误：try:, except ... as ...: 看如下代码
```
try:
    file=open('eeee.txt','r')  #会报错的代码
except Exception as e:  # 将报错存储在 e 中
    print(e)

```

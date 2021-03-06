# 极客时间python 

### Python学习思维导图
![思维导图](asserts/python_knowledge_map.jpg)

### Python PEP8 编码规范
https: // www.python.org / dev / peps / pep - 0008/  


pycharm 安装PEP8  
cmd窗口输入：pip install autopep8  
Tools→Extends Tools→点击加号  

Name：Autopep8（可以随便取）  
- Tools settings:
    - Programs：`autopep8` （前提是你已经安装了哦）  
    - Parameters: `--in-place - -aggressive - -aggressive $FilePath$`  
    - Working directory: `$ProjectFileDir$`  
- 点击Output Filters→添加，在对话框中的：Regular expression to match output中输入：`$FILE_PATH$\: $LINE$\: $COLUMN$\: .*`  

### Python 日常应用比较广泛的模块
1. 文字处理的 re
2. 日期类型的time、datetime
3. 数字和数学类型的math、random
4. 文件和目录访问的pathlib、os.path
5. 数据压缩和归档的tarfile
6. 通用操作系统的os、logging、argparse
7. 多线程的 threading、queue
8. Internet数据处理的 base64 、json、urllib
9. 结构化标记处理工具的 html、xml
10. 开发工具的unitest
11. 调试工具的 timeit
12. 软件包发布的venv
13. 运行服务的__main__

### python 正则表达式  
```python
## 总结
## ^ 匹配字符串的开始。
## $ 匹配字符串的结尾。
## \b 匹配一个单词的边界。
## \d 匹配任意数字。
## \D 匹配任意非数字字符。
## x? 匹配一个可选的 x 字符 (换言之，它匹配 1 次或者 0 次 x 字符)。
## x* 匹配0次或者多次 x 字符。
## x+ 匹配1次或者多次 x 字符。
## x{n,m} 匹配 x 字符，至少 n 次，至多 m 次。
## (a|b|c) 要么匹配 a，要么匹配 b，要么匹配 c。
## (x) 一般情况下表示一个记忆组 (remembered group)。你可以利用 re.search 函数返回对象的 groups() 函数获取它的值。
## 正则表达式中的点号通常意味着 “匹配任意单字符”

```



### Python 机器学习
pip3 install numpy  
which python3  
把结果路径/usr/local/bin/python3导入   
File - Default Settings- Project InterPreter 和 Run - Edit Configurations- Project InterPreter  
pip3 install pandas   
pip3 install matplotlib  

**Tensorflow的安装**  
pip3 install tensorflow  

### Python 网络库
// TODO  


python3 setup.py install  


### 按章节分类的课上演示代码 

### 课程目录
![contents](asserts/lingjichuxuePython.jpeg)


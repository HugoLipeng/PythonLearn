
    人生苦短，我用python
# python第三课

### 推荐一个python数据结构可视化工具：http://www.pythontutor.com/

### 课表

    - Mysql数据库的基本操作
    - 用python操作数据库
    - 编写python爬虫并保存到数据库

### 数据库

    我们平时说到的数据库，指的是 数据库管理系统

### mysql数据库

    MariaDB： MariaDB的目的是完全兼容MySQL，包括API和命令行，使之能轻松成为MySQL的代替品

### 关系型数据库

    另外一种类型的数据库是：非关系型数据库。 比较流行的是：Mongodb, redis


```python
import json

data_1 = "{'a': 1, 'b': 2, 'c': 3}"
data_2 = '{"a": 1, "b": 2, "c": 3}'

j_data = json.loads(data_2)
type(j_data)

with open('/Users/wangyujie/Desktop/data.json', 'r') as f:
    j_data = json.load(f)
    print(j_data)
```

    {'a': 100, 'b': 200}


    json格式

### mysql数据库基本操作

### 命令行操作


```python
# 链接数据库? 
mysql -u root -p 
# u 是用户名 p: 需要用密码登录数据库

# 查看数据库
show databases;

# 选择数据库
use database_name;

# 查看数据库中的table表
show tables;

# 查看表格的结构
desc tables;

# 查看表中的数据
select * from table_name;

# 查看数据并限制数量
select * from table_name limit 10;
```


      File "<ipython-input-20-947601b7eca7>", line 2
        mysql -u root -p
                    ^
    SyntaxError: invalid syntax



### 数据库管理工具

sequelpro  链接：http://www.sequelpro.com/

### mysql与Excel的不同

| 姓名 | 性别 | 年龄 | 班级 | 考试 | 语文 | 数学 | 英语 | 物理 | 化学 | 生物 | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 高海 | 男 | 18 | 高三一班 | 第一次模拟 | 90 | 126 | 119 | 75 | 59 | 89 |
| 高海 | 男 | 18 | 高三一班 | 第二次模拟 | 80 | 120 | 123 | 85 | 78 | 87 |
| 秦佳艺 | 女 | 18 | 高三二班 | 第一次模拟 | 78 | 118 | 140 | 89 | 80 | 78 |
| 秦佳艺 | 女 | 18 | 高三二班 | 第二次模拟 | 79 | 120 | 140 | 83 | 78 | 82 |

### 命令行操作数据库

### 创建数据库
    create database Examination_copy;
### 删除数据库
    drop database Examination_coopy;
### 指定字符集和校对集，创建数据库
    create database Examination_copy default charset utf8mb4 collate utf8mb4_general_ci;
    
### 创建表格
CREATE TABLE `class` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
);

### 小数转二进制


```python
3 转换为二进制 11 整数部分

0.4 转换为二进制 0.5*0 + 0.25*1 + 0.125*1 
                    0 1 1 1 1 0 1
```

### mysql数据类型    http://www.runoob.com/mysql/mysql-data-types.html

### 插入数据


```python
insert into `class`(`id`, `name`) 
values(1, '高一三班');
```

### 修改数据


```python
update `class` set `name` = '高一五班'
where `name` = '高一三班';
```

### 删除操作


```python
delete from `class`
where `id` = 6;
```

## 使用python去操作数据库

### python 安装第三方库
    1、 pip ; 举例： pip install pymysql
    2、 conda; 举例： conda install pymysql


```python
import MySQLdb
```


```python
DATABASE = {
    'host': '127.0.0.1', # 如果是远程数据库，此处为远程服务器的ip地址
    'database': 'Examination',
    'user': 'root',
    'password': 'wangwei',
    'charset': 'utf8mb4'
}

db = MySQLdb.connect(host='localhost', user='root', password='wangwei', db='Examination')
# 等价于
db = MySQLdb.connect('localhost', 'root', 'wangwei', 'Examination')
# 等价于
db = MySQLdb.connect(**DATABASE)

# db就代表是我们的数据库
```

### 游标


```python
cursor = db.cursor()
```

### 查询


```python
sql = "select * from student where id <= 20 limit 4"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row)
```

    (1, 0, '男', '凌榭辉')
    (2, 0, '男', '高海')
    (3, 0, '男', '潘锦乐')
    (4, 0, '男', '邹新宇')


### 插入操作


```python
sql = "insert into `class`(`name`) values('高一五班');"
cursor = db.cursor()
cursor.execute(sql)
cursor.execute(sql)
db.commit()
```

### 删除操作


```python
sql = "delete from `class` where `name`='高一五班'"
cursor = db.cursor()
cursor.execute(sql)
db.commit()
```

### 更新操作


```python
sql = "update `class` set `name`='高一十四班' where `id`=4;"
cursor = db.cursor()
cursor.execute(sql)
db.commit()
```

### 捕捉异常


```python
a = 10
b = a + 'hello'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-73-ce8b6729d737> in <module>()
          1 a = 10
    ----> 2 b = a + 'hello'
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'



```python
try:
    a = 10
    b = a + 'hello'
except TypeError as e:
    print(e)
```

    unsupported operand type(s) for +: 'int' and 'str'


### 遗留问题： 数据库回滚操作失败


```python
try:
    sql = "insert into `class`(`name`) values('高一十六班')"
    cursor = db.cursor()
    cursor.execute(sql)
    error = 10 + 'sdfsdf'
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
  
```

    unsupported operand type(s) for +: 'int' and 'str'


# 爬虫

### python库

    1、requests 用来获取页面内容
    2、BeautifulSoup

### 安装
    pip install reqeusts
    pip install bs4


```python
import time
import MySQLdb
import requests

from bs4 import BeautifulSoup
```


```python
# 此处为数据库配置文件，每个人的配置不同，因此需要同学们自己配置

DATABASE = {
    'host': '127.0.0.1', # 如果是远程数据库，此处为远程服务器的ip地址
    'database': '',
    'user': '',
    'password': '',
    'charset': 'utf8mb4'
}
```


```python
# 获取url下的页面内容，返回soup对象
def get_page(url):
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    return soup

# 封装成函数，作用是获取列表页下面的所有租房页面的链接，返回一个链接列表
def get_links(link_url):
    soup = get_page(link_url)
    links_div = soup.find_all('div', class_="pic-panel")
    links = [div.a.get('href') for div in links_div]
    return links

def get_house_info(house_url):
    soup = get_page(house_url)
    price = soup.find('span', class_='total').text
    unit = soup.find('span', class_='unit').text.strip()
    house_info = soup.find_all('p')
    area = house_info[0].text[3:]
    layout = house_info[1].text[5:]
    floor = house_info[2].text[3:]
    direction = house_info[3].text[5:]
    subway = house_info[4].text[3:]
    community = house_info[5].text[3:]
    location = house_info[6].text[3:]
    create_time = house_info[7].text[3:]
    agent = soup.find('a', class_='name LOGCLICK')
    agent_name = agent.text
    agent_id = agent.get('data-el')
    evaluate = soup.find('div', class_='evaluate')
    score, number = evaluate.find('span', class_='rate').text.split('/')
    times = evaluate.find('span', class_='time').text[5:-1]
    info = {
            '价格': price,
            '单位': unit,
            '面积': area,
            '户型': layout,
            '楼层': floor,
            '朝向': direction,
            '发布时间': create_time,
            '地铁': subway,
            '小区': community,
            '位置': location,
            '经纪人名字': agent_name,
            '经纪人id': agent_id
    }
    return info

def get_db(setting):
    return MySQLdb.connect(**setting)

def insert(db, house):
    values = "'{}',"* 10 + "'{}'"
    sql_values = values.format(house['价格'],house['单位'],house['面积'],house['户型'],
                              house['楼层'],house['朝向'],house['地铁'],house['小区'],
                              house['位置'],house['经纪人名字'],house['经纪人id'])
    sql = """
        insert into `house`(`price`, `unit`, `area`, `layout`, `floor`, `direction`,
        `subway`, `community`, `location`, `agent_name`, `agent_id`)
        values({})
    """.format(sql_values)
    print(sql)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
```


```python
db = get_db(DATABASE)
links = get_links('https://bj.lianjia.com/zufang/')
for link in links:
    time.sleep(2)
    print('获取一个房子信息成功')
    house = get_house_info(link)
    insert(db, house)
```

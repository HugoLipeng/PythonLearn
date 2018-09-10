
    人生苦短，我用python
# python第四课


```python
# 新的数据格式，csv
```

- 纯文本，使用某个字符集，比如ASCII、Unicode、EBCDIC或GB2312（简体中文环境）等；
- 由记录组成（典型的是每行一条记录）；
- 每条记录被分隔符（英语：Delimiter）分隔为字段（英语：Field (computer science)）（典型分隔符有逗号、分号或制表符；有时分隔符可以包括可选的空格）；
- 每条记录都有同样的字段序列。


```python
import pandas as pd
import numpy as np
```


```python
abs_path = '/Users/wangyujie/Desktop/成绩表.csv'
df = pd.read_csv(abs_path)
```


```python
df.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>凌榭辉</td>
      <td>男</td>
      <td>85</td>
      <td>60</td>
      <td>80</td>
      <td>62</td>
      <td>73</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>高海</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>67</td>
      <td>74</td>
      <td>86</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>潘锦乐</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>66</td>
      <td>87</td>
      <td>79</td>
      <td>72</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>邹新宇</td>
      <td>男</td>
      <td>90</td>
      <td>75</td>
      <td>64</td>
      <td>72</td>
      <td>72</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>吴一中</td>
      <td>男</td>
      <td>80</td>
      <td>76</td>
      <td>69</td>
      <td>64</td>
      <td>72</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(df)
```




    pandas.core.frame.DataFrame



### DataFrame


```python
# 列名
print(df.columns)
# 索引
print(df.index)
```

    Index(['序号', '姓名', '性别', '语文', '数学', '英语', '物理', '化学', '生物'], dtype='object')
    RangeIndex(start=0, stop=37, step=1)



```python
df.loc[0]
```




    序号      1
    姓名    凌榭辉
    性别      男
    语文     85
    数学     60
    英语     80
    物理     62
    化学     73
    生物     80
    Name: 0, dtype: object




```python
a = np.array(range(10))
a > 3
```




    array([False, False, False, False,  True,  True,  True,  True,  True,  True], dtype=bool)




```python
# 筛选数学成绩大于80
df[df.数学 > 80]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>秦佳艺</td>
      <td>女</td>
      <td>98</td>
      <td>90</td>
      <td>96</td>
      <td>93</td>
      <td>96</td>
      <td>80</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>黄金虎</td>
      <td>男</td>
      <td>90</td>
      <td>90</td>
      <td>84</td>
      <td>91</td>
      <td>98</td>
      <td>80</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>李佳</td>
      <td>男</td>
      <td>90</td>
      <td>90</td>
      <td>78</td>
      <td>93</td>
      <td>92</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df.数学<70]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>凌榭辉</td>
      <td>男</td>
      <td>85</td>
      <td>60</td>
      <td>80</td>
      <td>62</td>
      <td>73</td>
      <td>80</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>杨烨</td>
      <td>男</td>
      <td>90</td>
      <td>60</td>
      <td>85</td>
      <td>34</td>
      <td>78</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 复杂筛选
df[(df.语文>80) & (df.数学>80) & (df.英语>80)]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>秦佳艺</td>
      <td>女</td>
      <td>98</td>
      <td>90</td>
      <td>96</td>
      <td>93</td>
      <td>96</td>
      <td>80</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>黄金虎</td>
      <td>男</td>
      <td>90</td>
      <td>90</td>
      <td>84</td>
      <td>91</td>
      <td>98</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>



### 排序


```python
df.sort_values(['数学', '语文', '英语']).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>凌榭辉</td>
      <td>男</td>
      <td>85</td>
      <td>60</td>
      <td>80</td>
      <td>62</td>
      <td>73</td>
      <td>80</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>杨烨</td>
      <td>男</td>
      <td>90</td>
      <td>60</td>
      <td>85</td>
      <td>34</td>
      <td>78</td>
      <td>80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>邹新宇</td>
      <td>男</td>
      <td>90</td>
      <td>75</td>
      <td>64</td>
      <td>72</td>
      <td>72</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>吴一中</td>
      <td>男</td>
      <td>80</td>
      <td>76</td>
      <td>69</td>
      <td>64</td>
      <td>72</td>
      <td>80</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>李杜伟</td>
      <td>男</td>
      <td>85</td>
      <td>78</td>
      <td>80</td>
      <td>60</td>
      <td>89</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>凌榭辉</td>
      <td>男</td>
      <td>85</td>
      <td>60</td>
      <td>80</td>
      <td>62</td>
      <td>73</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>高海</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>67</td>
      <td>74</td>
      <td>86</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>潘锦乐</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>66</td>
      <td>87</td>
      <td>79</td>
      <td>72</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>邹新宇</td>
      <td>男</td>
      <td>90</td>
      <td>75</td>
      <td>64</td>
      <td>72</td>
      <td>72</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>吴一中</td>
      <td>男</td>
      <td>80</td>
      <td>76</td>
      <td>69</td>
      <td>64</td>
      <td>72</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>



### 访问


```python
# 按照索引去定位
df.loc[3]
```




    序号      4
    姓名    邹新宇
    性别      男
    语文     90
    数学     75
    英语     64
    物理     72
    化学     72
    生物     80
    Name: 3, dtype: object



###  索引


```python
scores = {
    '英语': [90, 78, 89],
    '数学': [64, 78, 45],
    '姓名': ['wong', 'li', 'sun']
}
df = pd.DataFrame(scores, index=['one', 'two', 'three'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>姓名</th>
      <th>数学</th>
      <th>英语</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>wong</td>
      <td>64</td>
      <td>90</td>
    </tr>
    <tr>
      <th>two</th>
      <td>li</td>
      <td>78</td>
      <td>78</td>
    </tr>
    <tr>
      <th>three</th>
      <td>sun</td>
      <td>45</td>
      <td>89</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.index
```




    Index(['one', 'two', 'three'], dtype='object')




```python
# 因为此时不存在数字索引，所以不能通过数字索引去访问
# df.loc[1]
df.loc['one']
```




    姓名    wong
    数学      64
    英语      90
    Name: one, dtype: object




```python
# 实实在在的所谓的第几行
df.iloc[0]
```




    姓名    wong
    数学      64
    英语      90
    Name: one, dtype: object




```python
# 合并了loc和iloc的功能
df.ix[0]
```




    序号      1
    姓名    凌榭辉
    性别      男
    语文     85
    数学     60
    英语     80
    物理     62
    化学     73
    生物     80
    Name: 0, dtype: object




```python
df.loc[:2]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>凌榭辉</td>
      <td>男</td>
      <td>85</td>
      <td>60</td>
      <td>80</td>
      <td>62</td>
      <td>73</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>高海</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>67</td>
      <td>74</td>
      <td>86</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>潘锦乐</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>66</td>
      <td>87</td>
      <td>79</td>
      <td>72</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 当索引为数字索引的时候，ix和loc是等价的
df.ix[:2]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>凌榭辉</td>
      <td>男</td>
      <td>85</td>
      <td>60</td>
      <td>80</td>
      <td>62</td>
      <td>73</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>高海</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>67</td>
      <td>74</td>
      <td>86</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>潘锦乐</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>66</td>
      <td>87</td>
      <td>79</td>
      <td>72</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 访问某一行,是错误的
# df[0]

#访问多行数据是可以使用切片的
df[:2]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>凌榭辉</td>
      <td>男</td>
      <td>85</td>
      <td>60</td>
      <td>80</td>
      <td>62</td>
      <td>73</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>高海</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>67</td>
      <td>74</td>
      <td>86</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
# dataframe中的数组
df.数学.values
```




    array([60, 80, 80, 75, 76, 60, 78, 90, 80, 80, 80, 80, 80, 78, 80, 80, 80,
           80, 80, 80, 90, 80, 80, 80, 80, 78, 80, 78, 80, 80, 90, 80, 80, 80,
           80, 80, 80])




```python
# 简单的统计
df.数学.value_counts()
```




    80    26
    78     4
    90     3
    60     2
    76     1
    75     1
    Name: 数学, dtype: int64




```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>凌榭辉</td>
      <td>男</td>
      <td>85</td>
      <td>60</td>
      <td>80</td>
      <td>62</td>
      <td>73</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>高海</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>67</td>
      <td>74</td>
      <td>86</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>潘锦乐</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>66</td>
      <td>87</td>
      <td>79</td>
      <td>72</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>邹新宇</td>
      <td>男</td>
      <td>90</td>
      <td>75</td>
      <td>64</td>
      <td>72</td>
      <td>72</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>吴一中</td>
      <td>男</td>
      <td>80</td>
      <td>76</td>
      <td>69</td>
      <td>64</td>
      <td>72</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 提取多列
new = df[['数学', '语文']].head()
new
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>数学</th>
      <th>语文</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60</td>
      <td>85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>80</td>
      <td>85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>80</td>
      <td>85</td>
    </tr>
    <tr>
      <th>3</th>
      <td>75</td>
      <td>90</td>
    </tr>
    <tr>
      <th>4</th>
      <td>76</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
new * 2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>数学</th>
      <th>语文</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>120</td>
      <td>170</td>
    </tr>
    <tr>
      <th>1</th>
      <td>160</td>
      <td>170</td>
    </tr>
    <tr>
      <th>2</th>
      <td>160</td>
      <td>170</td>
    </tr>
    <tr>
      <th>3</th>
      <td>150</td>
      <td>180</td>
    </tr>
    <tr>
      <th>4</th>
      <td>152</td>
      <td>160</td>
    </tr>
  </tbody>
</table>
</div>



### 重点


```python
def func(score):
    if score>=80:
        return "优秀"
    elif score>=70:
        return "良"
    elif score>=60:
        return "及格"
    else:
        return "不及格"

df['数学分类'] = df.数学.map(func)
```


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
      <th>数学分类</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>凌榭辉</td>
      <td>男</td>
      <td>85</td>
      <td>60</td>
      <td>80</td>
      <td>62</td>
      <td>73</td>
      <td>80</td>
      <td>及格</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>高海</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>67</td>
      <td>74</td>
      <td>86</td>
      <td>80</td>
      <td>优秀</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>潘锦乐</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>66</td>
      <td>87</td>
      <td>79</td>
      <td>72</td>
      <td>优秀</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>邹新宇</td>
      <td>男</td>
      <td>90</td>
      <td>75</td>
      <td>64</td>
      <td>72</td>
      <td>72</td>
      <td>80</td>
      <td>良</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>吴一中</td>
      <td>男</td>
      <td>80</td>
      <td>76</td>
      <td>69</td>
      <td>64</td>
      <td>72</td>
      <td>80</td>
      <td>良</td>
    </tr>
  </tbody>
</table>
</div>




```python
# applymap 对dataframe中所有的数据进行操作的一个函数，非常重要
def func(number):
    return number+10
# 等价
func = lambda number: number+10

df.applymap(lambda x: str(x) + ' -').head(2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
      <th>数学分类</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1 -</td>
      <td>凌榭辉 -</td>
      <td>男 -</td>
      <td>85 -</td>
      <td>60 -</td>
      <td>80 -</td>
      <td>62 -</td>
      <td>73 -</td>
      <td>80 -</td>
      <td>及格 -</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2 -</td>
      <td>高海 -</td>
      <td>男 -</td>
      <td>85 -</td>
      <td>80 -</td>
      <td>67 -</td>
      <td>74 -</td>
      <td>86 -</td>
      <td>80 -</td>
      <td>优秀 -</td>
    </tr>
  </tbody>
</table>
</div>



### 匿名函数


```python
[i+ 100 for i in range(10)]
```




    [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]




```python
def func(x):
    return x + 100
```


```python
list(map(lambda x: x+100, range(10)))
```




    [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]




```python
# 根据多列生成新的一个列的操作，用apply
df['new_score'] = df.apply(lambda x: x.数学 + x.语文, axis=1)
```


```python
# 前几行
df.head(2)
# 最后几行
df.tail(2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
      <th>数学分类</th>
      <th>new_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>顾振楠</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>93</td>
      <td>88</td>
      <td>93</td>
      <td>78</td>
      <td>优秀</td>
      <td>165</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>沈嘉辉</td>
      <td>男</td>
      <td>90</td>
      <td>80</td>
      <td>80</td>
      <td>67</td>
      <td>94</td>
      <td>80</td>
      <td>优秀</td>
      <td>170</td>
    </tr>
  </tbody>
</table>
</div>



### pandas中的dataframe的操作，很大一部分跟 numpy中的二维数组的操作是近似的

# matplotlib绘图


```python
df = df.drop(['new_score'], axis=1)
```


```python
df.head(2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>序号</th>
      <th>姓名</th>
      <th>性别</th>
      <th>语文</th>
      <th>数学</th>
      <th>英语</th>
      <th>物理</th>
      <th>化学</th>
      <th>生物</th>
      <th>数学分类</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>凌榭辉</td>
      <td>男</td>
      <td>85</td>
      <td>60</td>
      <td>80</td>
      <td>62</td>
      <td>73</td>
      <td>80</td>
      <td>及格</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>高海</td>
      <td>男</td>
      <td>85</td>
      <td>80</td>
      <td>67</td>
      <td>74</td>
      <td>86</td>
      <td>80</td>
      <td>优秀</td>
    </tr>
  </tbody>
</table>
</div>



### 绘图


```python
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
# 上一行是必不可少的
```


```python
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.plot(x, np.cos(x))
```




    [<matplotlib.lines.Line2D at 0x11cb12a58>]




![png](output_49_1.png)



```python
plt.plot(x, y, '--')
```




    [<matplotlib.lines.Line2D at 0x11ce24160>]




![png](output_50_1.png)



```python
fig = plt.figure()
plt.plot(x, y, '--')
```




    [<matplotlib.lines.Line2D at 0x11cf342b0>]




![png](output_51_1.png)



```python
fig.savefig('/Users/wangyujie/Desktop/first_figure.png')
```


```python
# 虚线样式
plt.subplot(2,1,2)
plt.plot(x, np.sin(x), '--')

plt.subplot(2,1,1)
plt.plot(x, np.cos(x))
```




    [<matplotlib.lines.Line2D at 0x11d9a3ac8>]




![png](output_53_1.png)



```python
# 点状样式
x = np.linspace(0,10,20)
plt.plot(x, np.sin(x), 'o')
```




    [<matplotlib.lines.Line2D at 0x11d7d5c50>]




![png](output_54_1.png)



```python
# color控制颜色
x = np.linspace(0,10,20)
plt.plot(x, np.sin(x), 'o', color='red')
```




    [<matplotlib.lines.Line2D at 0x11dca9080>]




![png](output_55_1.png)



```python
# 加label
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, '--', label='sin(x)')
plt.plot(x, np.cos(x), 'o', label='cos(x)')
# legen控制label的显示效果， loc是控制label的位置的显示
plt.legend(loc='upper right')

```




    <matplotlib.legend.Legend at 0x11e0b72b0>




![png](output_56_1.png)



```python
plt.legend?
# 当遇到一个不熟悉的函数的时候，多使用？号，查看函数的文档
```


```python
# plot函数，可定制的参数非常多
x = np.linspace(0, 10, 20)
y = np.sin(x)
plt.plot(x, y, '-d', color='orange', markersize=16, linewidth=2, markeredgecolor='gray', markeredgewidth=1)
```


![png](output_58_0.png)



```python
# 具体参数可查看文档
plt.plot?
```


```python
# ylim xlim 限定范围
plt.plot(x, y, '-d', color='orange', markersize=16, linewidth=2, markeredgecolor='gray', markeredgewidth=1)
plt.ylim(-0.5, 1.2);
plt.xlim(2,8)
```




    (2, 8)




![png](output_60_1.png)



```python
# 散点图
plt.scatter(x, y, s=100, c='gray')
```




    <matplotlib.collections.PathCollection at 0x1201ffe10>




![png](output_61_1.png)



```python

plt.style.use('seaborn-whitegrid')

x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.4)
plt.colorbar();
```


![png](output_62_0.png)


### pandas本身自带绘图

### 线性图


```python
df = pd.DataFrame(np.random.rand(100,4).cumsum(0), columns=['A', 'B', 'C', 'D'])
df.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x120dd4780>




![png](output_65_1.png)



```python
df.A.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x120d79d68>




![png](output_66_1.png)


### 柱状图


```python
df = pd.DataFrame(np.random.randint(10,50,(3,4)),columns=['A','B','C','D'], index=['one','two','three'])
df.plot.bar()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1205d8978>




![png](output_68_1.png)



```python
# df.B.plot.bar()
```


```python
# 等价于上面的绘制
df.plot(kind='bar')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x12197a400>




![png](output_70_1.png)



```python
df.plot(kind='bar', stacked=True)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x121b0df60>




![png](output_71_1.png)


### 直方图


```python
df = pd.DataFrame(np.random.randn(100,4),columns=['A','B','C','D'])
df.hist(column='A',figsize=(5,4))
```




    array([[<matplotlib.axes._subplots.AxesSubplot object at 0x116256eb8>]], dtype=object)




![png](output_73_1.png)


### 密度图


```python
df.plot.kde() # df.plot(kind='kde')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x121f3bfd0>




![png](output_75_1.png)



```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
```


![png](output_76_0.png)


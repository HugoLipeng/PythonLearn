
    人生苦短，我用python
# python第四课

### 课程安排

    1、numpy
    2、pandas
    3、matplotlib

### numpy

    数组跟列表，列表可以存储任意类型的数据，而数组只能存储一种类型数据


```python
import array
```


```python
a = array.array('i', range(10))
```


```python
# 数据类型必须统一
a[1] = 's'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-d69281a18e4a> in <module>()
          1 # 数据类型必须统一
    ----> 2 a[1] = 's'
    

    TypeError: an integer is required (got type str)



```python
a
```




    array('i', [0, 10, 2, 3, 4, 5, 6, 7, 8, 9])




```python
import numpy as np
```

#### 从原有列表转换为数组


```python
a_list = list(range(10))
b = np.array(a_list)
type(b)
```




    numpy.ndarray



生成数组


```python
a = np.zeros(10, dtype=int)
print(type(a))
# 查看数组类型
a.dtype
```

    <class 'numpy.ndarray'>





    dtype('int64')




```python
a = np.zeros((4,4), dtype=int)
print(type(a))
# 查看数组类型
print(a.dtype)
a
```

    <class 'numpy.ndarray'>
    int64





    array([[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]])




```python
np.ones((4,4), dtype=float)
```




    array([[ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.]])




```python
np.full((3,3), 3.14)
```




    array([[ 3.14,  3.14,  3.14],
           [ 3.14,  3.14,  3.14],
           [ 3.14,  3.14,  3.14]])




```python
a
```




    array([[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]])




```python
np.zeros_like(a)
```




    array([[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]])




```python
np.ones_like(a)
```




    array([[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]])




```python
np.full_like(a, 4.12, dtype=float)
```




    array([[ 4.12,  4.12,  4.12,  4.12],
           [ 4.12,  4.12,  4.12,  4.12],
           [ 4.12,  4.12,  4.12,  4.12],
           [ 4.12,  4.12,  4.12,  4.12]])



### random


```python
print(random.randint(5,10))
print(random.random())
```

    10
    0.9339596085150149



```python
np.random.random((3,3))
```




    array([[ 0.5971154 ,  0.72772485,  0.70280899],
           [ 0.75344822,  0.55560113,  0.56678812],
           [ 0.28363847,  0.00863229,  0.89259802]])




```python
# 经常会用到
np.random.randint(0,10, (5,5))
```




    array([[7, 4, 3, 5, 9],
           [1, 2, 2, 8, 7],
           [5, 1, 4, 5, 1],
           [5, 4, 2, 9, 3],
           [4, 4, 2, 1, 0]])



### 范围取值


```python
list(range(0,10,2))
```




    [0, 2, 4, 6, 8]




```python
np.arange(0,3,2)
```




    array([0, 2])




```python
# 经常用到
np.linspace(0, 3, 10)
```




    array([ 0.        ,  0.33333333,  0.66666667,  1.        ,  1.33333333,
            1.66666667,  2.        ,  2.33333333,  2.66666667,  3.        ])




```python
# n维的单位矩阵
np.eye(5)
```




    array([[ 1.,  0.,  0.,  0.,  0.],
           [ 0.,  1.,  0.,  0.,  0.],
           [ 0.,  0.,  1.,  0.,  0.],
           [ 0.,  0.,  0.,  1.,  0.],
           [ 0.,  0.,  0.,  0.,  1.]])



| Data type	    | Description |
|:---------------|:-------------|
| ``bool_``     | Boolean (True or False) stored as a byte |
| ``int_``      | Default integer type (same as C ``long``; normally either ``int64`` or ``int32``)| 
| ``intc``      | Identical to C ``int`` (normally ``int32`` or ``int64``)| 
| ``intp``      | Integer used for indexing (same as C ``ssize_t``; normally either ``int32`` or ``int64``)| 
| ``int8``      | Byte (-128 to 127)| 
| ``int16``     | Integer (-32768 to 32767)|
| ``int32``     | Integer (-2147483648 to 2147483647)|
| ``int64``     | Integer (-9223372036854775808 to 9223372036854775807)| 
| ``uint8``     | Unsigned integer (0 to 255)| 
| ``uint16``    | Unsigned integer (0 to 65535)| 
| ``uint32``    | Unsigned integer (0 to 4294967295)| 
| ``uint64``    | Unsigned integer (0 to 18446744073709551615)| 
| ``float_``    | Shorthand for ``float64``.| 
| ``float16``   | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa| 
| ``float32``   | Single precision float: sign bit, 8 bits exponent, 23 bits mantissa| 
| ``float64``   | Double precision float: sign bit, 11 bits exponent, 52 bits mantissa| 
| ``complex_``  | Shorthand for ``complex128``.| 
| ``complex64`` | Complex number, represented by two 32-bit floats| 
| ``complex128``| Complex number, represented by two 64-bit floats|

### 访问数组中元素


```python
# 嵌套列表的元素访问
var = [[1,2,3], [3,4,5], [5,6,7]]
var[0][0]
```




    1




```python
# 数组中元素的访问
a = np.array(var)
a[-1][0]
```




    5




```python
a
```




    array([[1, 2, 3],
           [3, 4, 5],
           [5, 6, 7]])




```python
# 这两种访问方式是等价的
a[2, 0], a[2][0]
```




    (5, 5)




```python
# 数组切片
a[:2, :2]
```




    array([[1, 2],
           [3, 4]])




```python
# 同上边的方式是不等价的
a[:2][:2]
```




    array([[1, 2, 3],
           [3, 4, 5]])



### 数组属性


```python
a
```




    array([[1, 2, 3],
           [3, 4, 5],
           [5, 6, 7]])




```python
# 维度
print(a.ndim)
# shape
print(a.shape)
# size
print(a.size)
# dtype
print(a.dtype)
# a.itemsize
print(a.itemsize)
# nbytes
print(a.nbytes)
```

    2
    (3, 3)
    9
    int64
    8
    72


### 运算


```python
a = np.array(list(range(10)))
a
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
print(a + 10)
print(a - 10)
print(a * 100)
```

    [10 11 12 13 14 15 16 17 18 19]
    [-10  -9  -8  -7  -6  -5  -4  -3  -2  -1]
    [  0 100 200 300 400 500 600 700 800 900]



```python
a = np.full((3,3), 1.0, dtype=float)
a + 10 # 等价于 np.add(a, 10)
```




    array([[ 11.,  11.,  11.],
           [ 11.,  11.,  11.],
           [ 11.,  11.,  11.]])




| Operator	    | Equivalent ufunc    | Description                           |
|---------------|---------------------|---------------------------------------|
|``+``          |``np.add``           |Addition (e.g., ``1 + 1 = 2``)         |
|``-``          |``np.subtract``      |Subtraction (e.g., ``3 - 2 = 1``)      |
|``-``          |``np.negative``      |Unary negation (e.g., ``-2``)          |
|``*``          |``np.multiply``      |Multiplication (e.g., ``2 * 3 = 6``)   |
|``/``          |``np.divide``        |Division (e.g., ``3 / 2 = 1.5``)       |
|``//``         |``np.floor_divide``  |Floor division (e.g., ``3 // 2 = 1``)  |
|``**``         |``np.power``         |Exponentiation (e.g., ``2 ** 3 = 8``)  |
|``%``          |``np.mod``           |Modulus/remainder (e.g., ``9 % 4 = 1``)|



```python
a = np.linspace(0, np.pi, 5)
b = np.sin(a)
print(a)
print(b)
```

    [ 0.          0.78539816  1.57079633  2.35619449  3.14159265]
    [  0.00000000e+00   7.07106781e-01   1.00000000e+00   7.07106781e-01
       1.22464680e-16]


### 统计类型


```python
# 求和
print(sum([1,2,3,4,5,6]))
# 数组一维求和
a = np.full(10, 2.3)
print(sum(a))
# 数组多维求和
a = np.array([[1,2],[3,4]])
print(sum(a))

# np.sum 求和
np.sum(a)
np.sum(a, axis=1)
np.max(a, axis=1)
```

    21
    23.0
    [4 6]





    array([2, 4])




```python
n = np.random.rand(10000)
```

### notebook使用小技巧

%timeit 代码 ; 此方法来判断程序的执行效率


```python
%timeit sum(n)
```

    1000 loops, best of 3: 1.54 ms per loop



```python
%timeit np.sum(n)
```

    The slowest run took 14.71 times longer than the fastest. This could mean that an intermediate result is being cached.
    100000 loops, best of 3: 11 µs per loop


### 由上代码可已看出np.sum的执行效率高，推荐使用

### 比较


```python
a = np.array(range(10))
a
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
a > 3
```




    array([False, False, False, False,  True,  True,  True,  True,  True,  True], dtype=bool)




```python
a != 3
```




    array([ True,  True,  True, False,  True,  True,  True,  True,  True,  True], dtype=bool)




```python
a == a
```




    array([ True,  True,  True,  True,  True,  True,  True,  True,  True,  True], dtype=bool)



| Operator	    | Equivalent ufunc    || Operator	   | Equivalent ufunc    |
|---------------|---------------------||---------------|---------------------|
|``==``         |``np.equal``         ||``!=``         |``np.not_equal``     |
|``<``          |``np.less``          ||``<=``         |``np.less_equal``    |
|``>``          |``np.greater``       ||``>=``         |``np.greater_equal`` |


```python
np.all(a>-1)
```




    True




```python
np.any(a>-1)
```




    True



### 变形


```python
a = np.full((2,10), 1, dtype=float)
a
```




    array([[ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]])




```python
a.reshape(4, 5)
```




    array([[ 1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.]])



### 排序


```python
l = [
    [1,2,3],
    [34,12,4],
    [32,2,33]
]
a = np.array(l)
a
```




    array([[ 1,  2,  3],
           [34, 12,  4],
           [32,  2, 33]])




```python
np.sort(a)
a.sort(axis=0)
a
```




    array([[ 1,  2,  3],
           [ 2, 12, 33],
           [ 4, 32, 34]])



### 拼接


```python
a = np.array([1, 2, 3])
b = np.array([[0, 2, 4], [1, 3, 5]])
```


```python
# 按行去连接
np.concatenate([b,b,b], axis=0)
```




    array([[0, 2, 4],
           [1, 3, 5],
           [0, 2, 4],
           [1, 3, 5],
           [0, 2, 4],
           [1, 3, 5]])




```python
# 按列去连接
np.concatenate([b,b,b], axis=1)
```




    array([[0, 2, 4, 0, 2, 4, 0, 2, 4],
           [1, 3, 5, 1, 3, 5, 1, 3, 5]])




```python

```

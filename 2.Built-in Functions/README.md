# [Built-in Functions](https://docs.python.org/3.6/library/functions.html#built-in-functions)

Python解释器有一些总是可用的内建函数和类型。它们按字母顺序列在这儿。

|  |  Built-in|  | Functions |  |
| :---: | :---: | :---: | :---: | :---: |
| [abs()](#abs) | dict() | help() | min() | setattr() |
| [all()](#all) | dir() | hex() | next() | slice() |
| [any()](#any) | divmod() | id() | object() | sorted() |
| [ascii()](#ascii) | enumerate() | input() | oct() | staticmethod() |
| [bin()](#bin) | eval() | int() | open() | str() |
| [bool()](#bool) | exec() | isinstance() | ord() | sum() |
| bytearray() | filter() | issubclass() | pow() | super() |
| bytes() | float() | iter() | print() | tuple() |
| callable() | format() | len() | property() | type() |
| chr() | frozenset() | list() | range() | vars() |
| classmethod() | getattr() | locals() | repr() | zip() |
| compile() | globals() | map() | reversed() | __import__() |
| complex() | hasattr() | max() | round() |   |
| delattr() | hash() | memoryview() | set() |   |

# abs
abs(x): 返回一个数字的绝对值。参数可以是一个整数或浮点数。假如参数是一个复数，返回它的量级（magnitude）。
```ipnbpython
In[2]: a = 2+3j
In[3]: abs(a)
Out[3]: 3.605551275463989
In[4]: abs(-2)
Out[4]: 2
In[5]: abs(-1.500)
Out[5]: 1.5
```

# all
all(iterable): 返回True，假如可迭代对象的所有元素都为True（或可迭代对象为空）。相当于：
```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

# any
any(iterable): 返回True，假如可迭代对象中任意元素为True。假如可迭代对象为空，返回False。相当于：
```python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

# ascii
ascii(object): 如同repr()，返回一个包含对象的可打印表示的字符串，但是转义(escape)由repr()返回的字符串中的非ASCII字符，repr()使用\x、\u或\U转义。
这会产生一个类似于Python 2中的repr()返回的字符串。
```ipnbpython
In[2]: ascii('aa')
Out[2]: "'aa'"
In[3]: ascii('中国')
Out[3]: "'\\u4e2d\\u56fd'"
In[4]: ascii(max)
Out[4]: '<built-in function max>'
In[5]: ascii('中国1-1')
Out[5]: "'\\u4e2d\\u56fd1-1'"
```
# bin
bin(x): 转换一个整数为一个二进制字符串，前缀为“0b”。这个结果是一个有效的Python表达式。假如x不是一个Python的int对象，它必须定义一个__index__()方法，
它返回一个一个整数，一些例子：
```ipnbpython
In[2]: bin(3)
Out[2]: '0b11'
In[3]: bin(-10)
Out[3]: '-0b1010'
```
如果需要前缀“0b”或不需要，您可以使用以下两种方法。
```ipnbpython
In[2]: (format(14, '#b'), format(14, 'b'))
Out[2]: ('0b1110', '1110')
In[3]: (f'{14:#b}', f'{14:b}')
Out[4]: ('0b1110', '1110')
```
另请参阅[format()](#format)，以获取更多的信息。

# bool
class bool([x]): 返回一个Boolean值，即True或False。x是使用标准的真实测试程序([truth testing procedure](https://docs.python.org/3.6/library/stdtypes.html#truth))进行转换的。
假如x是false或被省去，这会返回False；否则它返回True。bool类是int的子类（查看[Numeric Types — int, float, complex](https://docs.python.org/3.6/library/stdtypes.html#typesnumeric)）。
它永远不可以被继承。它的唯一实例是False和True（查看[Boolean Values](https://docs.python.org/3.6/library/stdtypes.html#bltin-boolean-values)）。
```ipnbpython
In[2]: bool() == bool(0) == False
Out[2]: True
```

# bytearray
class bytearray([source[, encoding[, errors]]]): 返回一个新字节数组。bytearray类是一个整数的可变序列，整数范围为 0 <= x < 256。
它有可变序列的大多数可用方法，描述于[Mutable Sequence Types](https://docs.python.org/3.6/library/stdtypes.html#typesseq-mutable)，
也和types类型拥有的大多数方法一样。查阅[Bytes and Bytearray Operations](https://docs.python.org/3.6/library/stdtypes.html#bytes-methods)。  

**可选的原始参数被用来以几种不同的方式初始化数组：**
1. 假如它是一个字符串，你还必须给定编码 (以及可选的错误)参数；[bytearray()](https://docs.python.org/3.6/library/stdtypes.html#bytearray)此外使用[str.encode()](https://docs.python.org/3.6/library/stdtypes.html#str.encode)转换字符串为字节
    ```ipnbpython
    In[2]: bytearray('中国', encoding='utf8')
    bytearray(b'\xe4\xb8\xad\xe5\x9b\xbd')
    In[3]: list(bytearray('中国', encoding='utf8'))
    [228, 184, 173, 229, 155, 189]
    In[4]: str.encode('中国')
    b'\xe4\xb8\xad\xe5\x9b\xbd'
    ```
2. 假如它是一个整数，数组会有这么大的尺寸，并将被用null bytes初始化。
    ```ipnbpython
    In[2]: bytearray(4)
    Out[2]: bytearray(b'\x00\x00\x00\x00')
    ```
3. 假如它是一个符合缓冲区接口的对象，一个只读的缓冲区对象将被用来初始化字节数组。
4. 假如它是一个可迭代对象，它必须是一个整数的可迭代器，整数在 0 <= x < 256 的范围中，它被用作数组的初始内容。
    ```ipnbpython
    In[2]: bytearray([1,2,3,4])
    Out[2]: bytearray(b'\x01\x02\x03\x04')
    ```

在没有参数的情况下，创建了大小为0的数组。
另请查阅[Binary Sequence Types — bytes, bytearray, memoryview](https://docs.python.org/3.6/library/stdtypes.html#binaryseq)和[Bytearray Objects](https://docs.python.org/3.6/library/stdtypes.html#typebytearray)

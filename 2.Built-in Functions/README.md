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
```Python Console
>>> a = 2+3j
>>> abs(a)
3.605551275463989
>>> abs(-2)
2
>>> abs(-1.500)
1.5
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
```Python Console
>>> ascii('aa')
"'aa'"
>>> ascii('中国')
"'\\u4e2d\\u56fd'"
>>> ascii(max)
'<built-in function max>'
>>> ascii('中国1-1')
"'\\u4e2d\\u56fd1-1'"
```
# bin
bin(x): 转换一个整数为一个二进制字符串，前缀为“0b”。这个结果是一个有效的Python表达式。假如x不是一个Python的int对象，它必须定义一个__index__()方法，
它返回一个一个整数，一些例子：
```Python Console
>>> bin(3)
'0b11'
>>> bin(-10)
'-0b1010'
```
如果需要前缀“0b”或不需要，您可以使用以下两种方法。
```Python Console
>>> format(14, '#b'), format(14, 'b')
('0b1110', '1110')
>>> f'{14:#b}', f'{14:b}'
('0b1110', '1110')
```
另请参阅[format()](#format)，以获取更多的信息。

# bool
class bool([x]): 返回一个Boolean值，即True或False。x是使用标准的真实测试程序([truth testing procedure](https://docs.python.org/3.6/library/stdtypes.html#truth))进行转换的。
假如x是false或被省去，这会返回False；否则它返回True。bool类是int的子类（查看[Numeric Types — int, float, complex](https://docs.python.org/3.6/library/stdtypes.html#typesnumeric)）。
它永远不可以被继承。它的唯一实例是False和True（查看[Boolean Values](https://docs.python.org/3.6/library/stdtypes.html#bltin-boolean-values)）。

# [Built-in Functions](https://docs.python.org/3.6/library/functions.html#built-in-functions)

Python解释器有一些总是可用的内建函数和类型。它们按字母顺序列在这儿。

|  |  Built-in|  | Functions |  |
| :---: | :---: | :---: | :---: | :---: |
| [abs()](#abs(x)) | dict() | help() | min() | setattr() |
| all() | dir() | hex() | next() | slice() |
| any() | divmod() | id() | object() | sorted() |
| ascii() | enumerate() | input() | oct() | staticmethod() |
| bin() | eval() | int() | open() | str() |
| bool() | exec() | isinstance() | ord() | sum() |
| bytearray() | filter() | issubclass() | pow() | super() |
| bytes() | float() | iter() | print() | tuple() |
| callable() | format() | len() | property() | type() |
| chr() | frozenset() | list() | range() | vars() |
| classmethod() | getattr() | locals() | repr() | zip() |
| compile() | globals() | map() | reversed() | __import__() |
| complex() | hasattr() | max() | round() |   |
| delattr() | hash() | memoryview() | set() |   |

# abs(x)
返回一个数字的绝对值。参数可以是一个整数或浮点数。假如参数是一个复数，返回它的量级（magnitude）。
```
>>> a = 2+3j
>>> abs(a)
3.605551275463989
>>> abs(-2)
2
>>> abs(-1.500)
1.5
```

# all(iterable)



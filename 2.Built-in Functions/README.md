# [Built-in Functions](https://docs.python.org/3.6/library/functions.html#built-in-functions)

Python解释器有一些总是可用的内建函数和类型。它们按字母顺序列在这儿。

|  |  Built-in|  | Functions |  |
| :---: | :---: | :---: | :---: | :---: |
| [abs()](#abs) | [dict()](#dict) | help() | min() | setattr() |
| [all()](#all) | [dir()](#dir) | hex() | next() | slice() |
| [any()](#any) | [divmod()](#divmod) | id() | object() | sorted() |
| [ascii()](#ascii) | enumerate() | input() | oct() | staticmethod() |
| [bin()](#bin) | eval() | int() | open() | str() |
| [bool()](#bool) | exec() | isinstance() | ord() | sum() |
| [bytearray()](#bytearray) | filter() | issubclass() | pow() | super() |
| [bytes()](#bytes) | float() | iter() | print() | tuple() |
| [callable()](#callable) | format() | len() | property() | type() |
| [chr()](#chr) | frozenset() | list() | range() | vars() |
| [classmethod()](#classmethod) | getattr() | locals() | repr() | zip() |
| [compile()](#compile) | globals() | map() | reversed() | __import__() |
| [complex()](#complex) | hasattr() | max() | round() |   |
| [delattr()](#delattr) | hash() | memoryview() | set() |   |

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

# bytes
class bytes([source[, encoding[, errors]]]): 返回一个新的“bytes”对象，它是一个不变的整数序列，整数范围为0<=x<256。bytes是一个不可变版本的bytearray —— 它有相同的非可变的方法和相同的索引和切片行为。

因此，构造器参数被解释bytearray()。

字节对象也可以用字母创建，查看[String and Bytes literals](https://docs.python.org/3.6/reference/lexical_analysis.html#strings)

另请查阅[Binary Sequence Types — bytes, bytearray, memoryview](https://docs.python.org/3.6/library/stdtypes.html#binaryseq)和[Bytearray Objects](https://docs.python.org/3.6/library/stdtypes.html#typebytearray)

# callable
callable(object): 返回True假如对象参数看起来可被调用，假如不行则False。假如这返回true，它仍然可能是调用失败，但是假如它是false，调用object将从不会成功。
注意，类是可调用的（调用一个类返回一个新实例）；假如它们的类有一个__call__()方法，实例是可调用的。

New in version 3.2: This function was first removed in Python 3.0 and then brought back in Python 3.2.

# chr
chr(i): 返回代表一个字符的字符串，它的Unicode编码点是整数i。例如，chr(97)返回字符串'a', 然而chr(8364)返回字符串'€'。这与ord()是相反的。

参数的有效范围是从0到1,114,111(基于16进制的0x10FFFF)。

# @classmethod
@classmethod: 将一个方法转换为类方法。

一个类方法接收这个类作为隐式的第一个参数，就好像一个实例方法接收这个实例。为了声明一个类方法，使用这个习语(idiom)：
```python
class C:  
    @classmethod  
    def f(cls, arg1, arg2, ...): ...
```
@classmethod的形式是一个函数装饰器 —— 查阅在[Function definitions](https://docs.python.org/3.6/reference/compound_stmts.html#function)中函数定义描述的细节。

它也可以在类上（如C.f()）或一个实例上（如C().f()）被调用。除了它的类之外，该实例被忽略。假如为一个派生类调用类方法，派生类对象作为隐含的第一个参数传递。

类方法不同于C++或Java的静态方法。如果您想要这些，请参阅本节中的staticmethod（）。

有关类方法的更多信息，在[The standard type hierarchy](https://docs.python.org/3.6/reference/datamodel.html#types)参考标准类型层次结构的文档

# compile
compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

将source编译成一个code或AST对象。通过exec()或eval()，code对象可以被执行。source可以是一个普通的字符串，一个字节字符串，或一个AST对象。参考[ast模块](https://docs.python.org/3.6/library/ast.html#module-ast)文档中关于如何使用AST对象的信息。

filename 参数应该提供读取代码的文件；传递一些可识别的值，如果它不是从文件中读取的（“<string>”通常被使用）。

mode 参数指定必须编译什么类型的代码；它可能是‘exec’，假如source由一系列的语句构成的话，可以是‘eval’，假如它由一个单一的表达式构成的话，
或是‘single’，假如它由一个单一的交互式语句构成的话（在后一种情况下，对其他东西进行评估的表达式语句除了None将被打印出来）。

可选参数 flags和dont_inherit 控制[future statements](https://docs.python.org/3.6/reference/simple_stmts.html#future)影响source的编译。假如两者不存在（或都为0），代码由这些未来语句编译，它们在调用complie()的代码中生效。
假如给定了flag参数和dont_inherit不是（或是0），然后由flags参数指定的未来语句被使用，出这些之外，被用在任何地方。假如dont_inherit是一个非0整数，那么flag参数就是它——被调用编译生效的未来语句被忽略。

未来的语句由bits指定，bits可以对多个语句进行逐位分析。指定一个给定特性所需的位字段可以在将来模块的特性实例上找到编译器标志属性。

optimize参数指定编译器的优化级别；默认值-1选择由-O选项给出的解释器的优化级别。显式级别为0（没有优化;__debug__ 是true），1（断言被删除，__debug__ 为false）或2（docstring也被删除）。 

如果编译源是无效的，这个函数抛出[SyntaxError](https://docs.python.org/3.6/library/exceptions.html#SyntaxError)，如果source包含null字节，则是[ValueError](https://docs.python.org/3.6/library/exceptions.html#ValueError)。

如果您想要将Python代码解析成它的AST表示，请参阅[ast.parse()](https://docs.python.org/3.6/library/ast.html#ast.parse)。

**注意**：当在‘single’和‘eval’模式编译多行代码时，输入必须被至少一个换行符终止。：这是为了便于在代码模块中检测不完整和完整的语句。

**警告**：在Python的AST编译器中，由于堆栈深度限制而编译成AST对象时，有可能用一个足够大的/复杂的字符串来破坏Python解释器。

Changed in version 3.2: Allowed use of Windows and Mac newlines. Also input in 'exec' mode does not have to end in a newline anymore. Added the optimize parameter.

Changed in version 3.5: Previously, TypeError was raised when null bytes were encountered in source.


# complex
class complex([real[, imag]]): 返回一个值为 real+imag*1j 的复数，或将字符串或数字转换为复数。

假如第一个参数是字符串，它将被解释为复数，函数必须被调用时没有第二个参数。第二个参数从不可能是一个字符串。每个参数可能是数字类型（包括complex）。
假如imag被省略，它默认是0，构造函数是一个数字转换，如[int](#int)和[float](#float)。假如两个参数都被省略，返回`0j`。

**注意**：当从一个字符串转换时，字符串必须在中间`+`或`-`操作符周围不包含空格。例如，`complex('1+2 j')`是好的，但是`complex('1 + 2j')`抛出ValueError。

复数类型在[Numeric Types — int, float, complex](https://docs.python.org/3.6/library/stdtypes.html#typesnumeric)中被描述。

Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.

#  delattr
delattr(object, name): 这与[setattr](#setattr)相关。参数是一个对象和一个字符串。字符串必须是对象中一个属性的名字。函数删除命名的属性，如果对象允许的话。

例如，`delattr(x, 'foobar')` 等同于 `del x.foobar`.

# dict
创建一个新的字典。dict对象是字典类。查看[dict](https://docs.python.org/3.6/library/stdtypes.html#dict)和[Mapping Types — dict](https://docs.python.org/3.6/library/stdtypes.html#typesmapping)关于这个类的文档。
+ class dict(**kwarg)
+ class dict(mapping, **kwarg)
+ class dict(iterable, **kwarg) 

对于其他容器，查看内建[list](https://docs.python.org/3.6/library/stdtypes.html#list), [set](https://docs.python.org/3.6/library/stdtypes.html#set)和[tuple](https://docs.python.org/3.6/library/stdtypes.html#tuple)类,以及[collections](https://docs.python.org/3.6/library/collections.html#module-collections)模块。

# dir
dir([object]): 没有参数时，返回当前本地作用域内的名字列表。有一个参数时，尝试返回该对象的有效属性列表。

假如对象有一个名为[__dir__()](https://docs.python.org/3.6/reference/datamodel.html#object.__dir__)的方法，这个方法将被调用，并且必须返回属性列表。这允许实现定制[__getattr__()](https://docs.python.org/3.6/reference/datamodel.html#object.__getattr__)或[__getattribute__()](https://docs.python.org/3.6/reference/datamodel.html#object.__getattribute__)函数的对象去自定义dir()报告它们属性的方式。

假如对象没有提供__dir__()方法，函数尽量从对象的[__dict__](https://docs.python.org/3.6/library/stdtypes.html#object.__dict__)属性中收集信息，假如定义了，则从它的类型对象。结果列表没必要是完全的，并可能是错误的，当对象有一个定制的__getattr__()时。

默认的dir()原理在不同的类型的对象中表现不同，因为它试图产生最相关的，而不是完全的信息。
+ 假如对象是一个模块对象，列表包含模块属性的名字。 
+ 假如对象是一个类或类对象，列表包含它属性的名字，和对他基础属性进行递归。
+ 另外，列表包含对象的属性名字，它类属性的名字，和它类的基础类进行递归。

最终列表是按字母顺序排列的。例如：
```
>>> import struct
>>> import math
>>> len(dir())
4
>>> dir()
['__builtins__', 'math', 'struct', 'sys']
>>> print(*[','.join(list(map(lambda x: x.ljust(12), dir(struct)[5*i:5*(i+1)]))) for i in range(math.ceil(len(dir(struct))/5))], sep='\n')
Struct      ,__all__     ,__builtins__,__cached__  ,__doc__     
__file__    ,__loader__  ,__name__    ,__package__ ,__spec__    
_clearcache ,calcsize    ,error       ,iter_unpack ,pack        
pack_into   ,unpack      ,unpack_from 

>>> class Shape:
...     def __dir__(self):
...         return 'area', 'perimeter', 'location'
... 
>>> s = Shape()
>>> dir(s)
['area', 'location', 'perimeter']
```

**注意**:因为`dir()`首先被提供在交互式提示中作为一种便利使用的，它试图提供一个有趣的名字集合，而不是尝试提供一个严格的或一致定义的名称集合，并且其详细行为可能会在不同版本中发生变化，当参数是一个类时，元类属性不在结果列表中。


# divmod
divmod(a, b): 以2个数字（非复数）作为参数，当使用整数除法时，返回一对数字，它们由商(quotient)和余数(remainder)构成。用混合的运算对象类型，二进制算法运算符的规则被应用。
对于整数，结果等同于 `(a//b, a%b)`。对于浮点型数字，结果是`(q, a%b)`，q通常是`math.floor(a/b)`，但是可能比它少1。在任何示例中，`q*b+a%b`是非常接近a的，假如`a%b`是非0，它与b有相同的符号，并且`0 <= abs(a % b) < abs(b).`。   


# enumerate
enumerate(iterable, start=0): 

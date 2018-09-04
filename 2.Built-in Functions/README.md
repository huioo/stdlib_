# [Built-in Functions](https://docs.python.org/3.6/library/functions.html#built-in-functions)

Python解释器有一些总是可用的内建函数和类型。它们按字母顺序列在这儿。

|  |  Built-in|  | Functions |  |
| :---: | :---: | :---: | :---: | :---: |
| [abs()](#abs) | [dict()](#dict) | [help()](#help) | min() | setattr() |
| [all()](#all) | [dir()](#dir) | [hex()](#hex) | next() | slice() |
| [any()](#any) | [divmod()](#divmod) | [id()](#id) | object() | sorted() |
| [ascii()](#ascii) | [enumerate()](#enumerate) | [input()](#input) | oct() | staticmethod() |
| [bin()](#bin) | [eval()](#eval) | [int()](#int) | open() | str() |
| [bool()](#bool) | [exec()](#exec) | [isinstance()](#isinstance) | ord() | sum() |
| [bytearray()](#bytearray) | [filter()](#filter) | [issubclass()](#issubclass) | pow() | super() |
| [bytes()](#bytes) | [float()](#float) | [iter()](#iter) | print() | tuple() |
| [callable()](#callable) | [format()](#format) | [len()](#len) | property() | type() |
| [chr()](#chr) | [frozenset()](#forzenset) | [list()](#list) | range() | vars() |
| [classmethod()](#classmethod) | [getattr()](#getattr) | [locals()](#locals) | repr() | zip() |
| [compile()](#compile) | [globals()](#globals) | map() | reversed() | __import__() |
| [complex()](#complex) | [hasattr()](#hasattr) | max() | round() |   |
| [delattr()](#delattr) | [hash()](#hash) | memoryview() | set() |   |

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
enumerate(iterable, start=0): 返回一个enumerate对象。iterable必须是一个序列，一个[iterator](https://docs.python.org/3.6/glossary.html#term-iterator)或一些其他支持迭代的对象。

由enumerate()返回的迭代对象的__next__方法返回一个元组，它包含一个计数（默认0开始）和从迭代迭代器获得的值。
```
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```
等同于：
```python
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
```

#  eval
eval(expression, globals=None, locals=None): 参数是一个字符串和可选的全局和本地变量。假如提供，globals必须是一个字典。假如提供，locals可以是任何mapping对象。

表达式参数被解析和评估为Python表达式（从技术上讲，一个条件列表）进行评估，它使用globals和locals字典作为全局和本地命名空间。假如globals参数存在，且不包含键`__builtins__`的值，在表达式被解析之前，对内置模块[builtins](https://docs.python.org/3.6/library/builtins.html#module-builtins)的引用被插入到那个键下。
这意味着表达式通常可以完全访问到标准builtins模块，且受限的环境中传播。假如locals字典被省略，它默认是globals字典。假如两个字典都被省略，表达式在调用eval()的环境中被执行。返回值时评估的表达式的结果。语法错误被报告为异常，例如：
```
>>> x = 1
>>> eval('x+1')
2
```
这个函数还可以被用来执行任意的code对象（例如由compile()创建的）。在这个例子中，传递一个code对象代替字符串。假如code对象已经用‘exec’最为mode参数进行编译，eval()的返回值将为None。

**提示**: 动态执行的语句由exec()函数支持。[globals()](#globals)和[locals()](#locals)函数分别返回当前全局和本地字典，这可能对于分发给exec()和eval()使用是有用的。

对于一个可以安全地用只包含文字的表达式来评估字符串的函数，查看[ast.literal_eval()](https://docs.python.org/3.6/library/ast.html#ast.literal_eval)。


# exec
exec(object[, globals[, locals]]): 这函数支持Python代码的动态执行。object必须是字符串或code对象。

如果它是字符串，字符串被解析为一个合适的Python语句，它然后被执行（除非发生语法错误）。如果是一个code对象，它被简单执行。在所有情况下，执行的代码都将作为文件输入有效。请注意，即使在传递给exec()函数的代码的上下文中，return和yield语句也不能在函数定义之外使用。返回值是None。

在所有情况下，假如可选部分被省略，代码在当前域中执行。假如只给定globals，它必须是一个字典，它将被用于全局变量和局部变量。假如globals和locals被给出，它们分别用于全局变量和局部变量。如果提供，locals可以是任意的mapping对象。记住，在模块层面，globals和locals是相同的字典。
假如exec得到2个单独的对象作为globals和locals，代码将被执行，就好像它被嵌入到一个类定义中一样。

假如globals字典不包含键__builtins__的值，对内置模块builtins的引用被插入到那个键下。通过这种方式，在你可以通过插入你自己的`__builtins__`字典到globals中来控制builtins对执行代码的可用性，之后传递它给exec()。

**Note** The built-in functions globals() and locals() return the current global and local dictionary, respectively, which may be useful to pass around for use as the second and third argument to exec().

**Note** The default locals act as described for function locals() below: modifications to the default locals dictionary should not be attempted. Pass an explicit locals dictionary if you need to see effects of the code on locals after function exec() returns. 

# filter
filter(function, iterable): 从iterable中对于那个函数返回True的元素中构造一个迭代器。iterable或许是一个序列、一个支持迭代的容器，或一个迭代器。如果function是None，标识函数是假定的，也就是说，所有可迭代的元素都被删除了。

**注意** filter(function, iterable)等同于，如果function不是None，生成器表达式是`(item for item in iterable if function(item))`，如果function是None，生成器表达式是`(item for item in iterable if item)`。

查看[itertools.filterfalse()](https://docs.python.org/3.6/library/itertools.html#itertools.filterfalse) 对于互补函数，它返回iterable中函数返回flase的元素

# float
class float([x]): 返回一个由数字或字符串构成的浮点数。

如果参数是字符串，它应该包含一个十进制数，可选的前面有一个符号，并且可以选择性地嵌入空格。可选的符号可能是‘+’或‘-’，‘+’符号在产生的值前没有影响。参数也可能是一个表示NaN(Not-a-Number)的字符串，或正或负无穷。更准确来说，在前导和尾随空格字符被删除之后，输入必须符合下面的语法。
```
sign           ::=  "+" | "-"
infinity       ::=  "Infinity" | "inf"
nan            ::=  "nan"
numeric_value  ::=  floatnumber | infinity | nan
numeric_string ::=  [sign] numeric_value
```     
在这里，`floatnumber `是Python浮点文字的形式，描述于[Floating point literals](https://docs.python.org/3.6/reference/lexical_analysis.html#floating)。 对于正无穷来说，“inf”, “Inf”, “INFINITY” 和 “iNfINity”都是可接受的拼写。

否则，如果参数是整数或浮点数，返回一个具有相同的值（在Python的浮点精度中）的浮点数。如果参数超过Python的float的范围，一个[OverflowError](https://docs.python.org/3.6/library/exceptions.html#OverflowError)将被抛出。

对于一个一般的Python对象x，`float(x)`代表了`x.__float__()`。如果没有给定参数。返回`0.0`。
```
>>> float('+1.23')
1.23
>>> float('   -12345\n')
-12345.0
>>> float('1e-003')
0.001
>>> float('+1E6')
1000000.0
>>> float('-Infinity')
-inf
```
float类型被描述于[Numeric Types — int, float, complex](https://docs.python.org/3.6/library/stdtypes.html#typesnumeric)。  

Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.

# format
format(value[, format_spec]): 将一个值转换为一个“格式化”的表示，由format_spec控制。

format_spec的解释取决于值参数的类型。无论如何，有一个标准的格式化语法，它被大多数内置类型使用：[Format Specification Mini-Language](https://docs.python.org/3.6/library/string.html#formatspec)。

默认format_spec是一个空字符串，这通常会产生与调用str(value)相同的效果。

`format(value, format_spec)`的调用被解释为`type(value).__format__(value, format_spec)`，当搜索值的[__format__()](https://docs.python.org/3.6/reference/datamodel.html#object.__format__)方法时，它会绕过实例字典。
如果方法查找到object，且format_spec非空，TypeError异常被抛出，或如果format_spec或返回值不是空字符串时。
```
>>> class A:
...     def __format__(self, format_spec):
...         return 'aaaa'
...
>>> format(A(), 'bb')
'aaaa'

>>> class A:
...     def __format__(self, format_spec):
...         return 111
... 
>>> format(A(), '')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: __format__ must return a str, not int

>>> format(object())
'<object object at 0x000002081A7FBBD0>'
>>> format(object(), 'bb')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unsupported format string passed to object.__format__
```
Changed in version 3.4: object().__format__(format_spec) raises TypeError if format_spec is not an empty string.

# frozenset
class frozenset([iterable]): 返回一个新的frozenset对象，可选地使用可迭代的元素。frozenset是一个内置类。

See [frozenset](https://docs.python.org/3.6/library/stdtypes.html#frozenset) and [Set Types — set, frozenset](https://docs.python.org/3.6/library/stdtypes.html#types-set) for documentation about this class.

# getattr
getattr(object, name[, default]): 返回对象命名属性的值。name必须是字符串。如果字符串是对象的一个属性的名称，那么结果就是该属性的值。

例如，`getattr(x, 'foobar')` 等同于 `x.foobar`。如果指定的属性不存在，如果提供了默认值，则返回默认值，否则，AttributeError被抛出。

# globals
globals(): 返回代表当前全局符号表的字典。这总是当前模块的字典（在函数或方法中，这是定义它的模块，而不是它被调用的模块）。

# hasattr
hasattr(object, name): 参数是一个对象和一个字符串。如果字符串是对象属性的名称，结果是True，如果不是则是False。（这是通过调用getattr(object，name)来实现的，并观察它是否会引起AttributeError或不。）

# hash
hash(object): 返回对象的散列(hash)值（如果它有一个）。hash值是整数。它们用于在字典查找期间快速比较字典键。比较相等的数字值具有相同的散列值（即使它们是不同类型的，1和1的情况也是如此）。
```
>>> hash(1)
1
>>> hash(1.0)
1
>>> 1 == 1.0
True
```
**注意**: 对于带有定制__hash__()方法的对象，注意hash()根据主机的位宽来截短返回值。

# help
help([object]): 调用内置的帮助系统。（此功能用于交互使用。）如果没有给出任何参数，交互式帮助系统将从解释器控制台开始。如果参数是一个字符串，那么字符串就会被看作是模块、函数、类、方法、关键字或文档主题的名称，并且在控制台上打印一个帮助页面。如果参数是任何其他类型的对象，则会产生一个关于对象的帮助页面。

这个函数被[site](https://docs.python.org/3.6/library/site.html#module-site)模块添加到内置的名称空间中。

Changed in version 3.4: Changes to pydoc and inspect mean that the reported signatures for callables are now more comprehensive and consistent.

# hex
hex(x): 将一个整数编号转换为用“0x”前缀的小写十六进制字符串。如果x不是Python int对象,它必须定义返回整数的__index__()方法。一些例子:
```
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'

```
如果你想把一个整数的数字转换成大写或更低的十六进制字符串,你可以使用以下两种方式：
```
>>> '%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
>>> format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
>>> f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')
```
See also format() for more information.

See also int() for converting a hexadecimal string to an integer using a base of 16.

# id
id(object): 返回一个对象的“身份”。这是一个整数，它保证在它的生命周期中是唯一的和不变的。两个具有非重叠生存期的对象可能具有相同的id（）值。  
CPython实现细节：这是内存中对象的地址。

# input
input([prompt]): 如果提示参数存在，则将其写入标准输出，而不使用拖尾换行符。然后这个函数从输入中读取一行，把它转换成字符串（剥离一个尾随换行符）并返回。当EOF被读到时，EOFError被提出。例子:
```
>>> s = input('--> ')  
--> Monty Python's Flying Circus
>>> s  
"Monty Python's Flying Circus"
```
如果[readline](https://docs.python.org/3.6/library/readline.html#module-readline)模块被加载，那么input（）将使用它来提供精细的线编辑和历史特性。

# int
返回一个由数字或字符串`x`组成的整数对象，如果没有参数，则返回`0`。如果x定义了[__int__()](https://docs.python.org/3.6/reference/datamodel.html#object.__int__)，`int(x)`返回`x.__int__()`。如果x定义[__trunc__()](https://docs.python.org/3.6/reference/datamodel.html#object.__trunc__)，它返回`x.__trunc__()`。对于浮点数，这向零截断。
+ class int(x=0)
+ class int(x=0, base=10)

如果x不是一个数字或者如果给定base，那么x必须是一个字符串，bytes或bytearray实例，它在基数（radix）基础上表示整数文字。可选地，文字可以在前面加上+或-（两者之间没有空隙）并被空格包围。一个n进制的文字由数字 0 到 n-1 和 值为10~35的a~z（或A~Z）组成。
```
>>> int(0x12)   # 16进制字节表示
18
>>> int(0x12, 16)  # 16进制字节
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: int() can't convert non-string with explicit base

>>> int(0o12)   # 8进制字节表示
10
>>> int(0b1001) # 2进制字节表示
9

>>> int('- 12', base=4)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: invalid literal for int() with base 4: '- 12'
>>> int(' -12 ', base=4)
-6
>>> int(' -12 ', base=-4)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: int() base must be >= 2 and <= 36, or 0
```

默认的base是10。允许的值是0和2~36。base-2、base-8和base-16文字可以随意使用`0b/0B`、`0o/0O`或`0x/0X`，就像代码中的整数字面量一样。base-0的意思是完全解释为代码文字，所以实际的（actual）底数是2 8 10或16，所以int（'010'，0）是不合法的，而int（'010'）是合法的，和int（'010'，8）一样。
```
>>> int('010')
10
>>> int('010', 0)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: invalid literal for int() with base 0: '010'

>>> int('12', 0)
12
>>> int('010', 8)
8
```

整数类型描述于[Numeric Types — int, float, complex](https://docs.python.org/3.6/library/stdtypes.html#typesnumeric)
```python
print("-12的10进制整数   int('-12')", int('-12'))       # -12   
print("      包含空格   int('  -12  ')", int('  -12  '))      # -12
print("-12的4进制整数    int('-12', base=4)", int('-12', base=4))   # -6
print("-12的8进制整数    int('-12', base=8)", int('-12', base=8))   # -10
print("-12的16进制整数    int('-12', base=16)", int('-12', base=16))   # -18
print("-12的base为0的整数 int(' -12 ', base=0)", int(' -12 ', base=0))   # -12
```

Changed in version 3.4: If base is not an instance of int and the base object has a base.__index__ method, that method is called to obtain an integer for the base. Previous versions used base.__int__ instead of base.__index__.

Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.
```
>>> int('12_10', 0)
1210
```

# isinstance
isinstance(object, classinfo):  
如果object参数是classinfo参数的实例，或是一个（直接的，间接的或虚拟([virtual](https://docs.python.org/3.6/glossary.html#term-abstract-base-class))的）子类，则返回true。如果object不是给定类型的对象，这方法总返回false。  
如果classinfo是一个类型对象（或递归的其他元组）元组，如果object是任意一个类型的实例，返回True。如果classinfo不是类型或类型的元组和元组，一个TypeError异常将被抛出。

#  issubclass
issubclass(class, classinfo):   
如果class是classinfo的子类（直接，间接或虚拟([virtual](https://docs.python.org/3.6/glossary.html#term-abstract-base-class))的），则返回True。class被认为是它自身的子类。classinfo可以是class的元组，在这种情况下，classinfo中的每一个条目都会被检查。在任何其他情况下，都会抛出TypeError异常。
```
>>> class A:
...     pass
... class B(A):
...     pass
... 
>>> issubclass(A, B)
False
>>> issubclass(B, A)
True
>>> issubclass(B, B)
True

```

# iter
iter(object[, sentinel]): 返回一个[iterator](https://docs.python.org/3.6/glossary.html#term-iterator)对象。

第一个参数的解释非常不同，这取决于第二个参数的存在。如果没有第二个参数，object必须是一个collection对象，它支持迭代协议（ __iter__()方法），或者它必须支持序列协议（__getitem__()方法，用从0开始的整数参数）。如果它不支持任何一种协议，产生TypeError。  
如果给出第二个参数sentinel，object必须是一个可调用对象。在这种情况下创建的迭代器将无参调用object，每次调用它的__next__()方法；如果返回的值等于sentinel，[StopIteration](https://docs.python.org/3.6/library/exceptions.html#StopIteration)将被抛出，否则返回的值将被返回。

See also [Iterator Types](https://docs.python.org/3.6/library/stdtypes.html#typeiter).

一个关于第二种形式的iter()的有用的应用是去读取一个文件的行，直到到达某一行。下面的例子读一个文件，直到方法[readline()](https://docs.python.org/3.6/library/io.html#io.TextIOBase.readline)返回一个空字符串：
```python
with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)
```

# len
len(s): 返回一个对象（items数）的长度。参数必须是一个序列（如字符串，bytes，元组，列表，或range）或一个集合（如字典，set或frozenset）。

# list
class list([iterable]): 事实上[list](https://docs.python.org/3.6/library/stdtypes.html#list)是一个可变的序列类型，而不是一个方法，记录在[Lists](https://docs.python.org/3.6/library/stdtypes.html#typesseq-list) 和 [Sequence Types — list, tuple, range](https://docs.python.org/3.6/library/stdtypes.html#typesseq)。

# locals
locals(): 更新和返回一个字典，其表示当前本地符号表。当在函数块中调用locals()时，由locals()返回自由变量，而不是在类块中。

**注意** 这个字典的内容不应该被修改，更改可能不会影响解释器使用的本地和自由变量的值。

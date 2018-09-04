# [Built-in Functions](https://docs.python.org/3.6/library/functions.html#built-in-functions)

Python解释器有一些总是可用的内建函数和类型。它们按字母顺序列在这儿。

|  |  Built-in|  | Functions |  |
| :---: | :---: | :---: | :---: | :---: |
| [abs()](#abs) | [dict()](#dict) | [help()](#help) | [min()](#min) | setattr() |
| [all()](#all) | [dir()](#dir) | [hex()](#hex) | [next()](#next) | slice() |
| [any()](#any) | [divmod()](#divmod) | [id()](#id) | [object()](#object) | sorted() |
| [ascii()](#ascii) | [enumerate()](#enumerate) | [input()](#input) | [oct()](#oct) | staticmethod() |
| [bin()](#bin) | [eval()](#eval) | [int()](#int) | [open()](#open) | str() |
| [bool()](#bool) | [exec()](#exec) | [isinstance()](#isinstance) | ord() | sum() |
| [bytearray()](#bytearray) | [filter()](#filter) | [issubclass()](#issubclass) | pow() | super() |
| [bytes()](#bytes) | [float()](#float) | [iter()](#iter) | print() | tuple() |
| [callable()](#callable) | [format()](#format) | [len()](#len) | property() | type() |
| [chr()](#chr) | [frozenset()](#forzenset) | [list()](#list) | range() | vars() |
| [classmethod()](#classmethod) | [getattr()](#getattr) | [locals()](#locals) | repr() | zip() |
| [compile()](#compile) | [globals()](#globals) | [map()](#map) | reversed() | \_\_import__() |
| [complex()](#complex) | [hasattr()](#hasattr) | [max()](#max) | round() |   |
| [delattr()](#delattr) | [hash()](#hash) | [memoryview()](#memoryview) | set() |   |

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

假如对象有一个名为[\_\_dir__()](https://docs.python.org/3.6/reference/datamodel.html#object.__dir__)的方法，这个方法将被调用，并且必须返回属性列表。这允许实现定制[\_\_getattr__()](https://docs.python.org/3.6/reference/datamodel.html#object.__getattr__)或[\_\_getattribute__()](https://docs.python.org/3.6/reference/datamodel.html#object.__getattribute__)函数的对象去自定义dir()报告它们属性的方式。

假如对象没有提供__dir__()方法，函数尽量从对象的[\_\_dict__](https://docs.python.org/3.6/library/stdtypes.html#object.__dict__)属性中收集信息，假如定义了，则从它的类型对象。结果列表没必要是完全的，并可能是错误的，当对象有一个定制的__getattr__()时。

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

# eval
eval(expression, globals=None, locals=None): 参数是一个字符串和可选的全局和本地变量。假如提供，globals必须是一个字典。假如提供，locals可以是任何mapping对象。

expression参数被解析和评估为Python表达式（从技术上讲，一个条件列表）进行评估，它使用globals和locals字典作为全局和本地命名空间。假如globals参数存在，且不包含键`__builtins__`的值，在表达式被解析之前，对内置模块[builtins](https://docs.python.org/3.6/library/builtins.html#module-builtins)的引用被插入到那个键下。
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
```python
>>> class C:
...     pass
... 
>>> eval('C()')
<C object at 0x0000025449A86CF8>
>>> exec('a=C()')
>>> a
<C object at 0x0000025449A867B8>
```

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

`format(value, format_spec)`的调用被解释为`type(value).__format__(value, format_spec)`，当搜索值的[\_\_format__()](https://docs.python.org/3.6/reference/datamodel.html#object.__format__)方法时，它会绕过实例字典。
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
Changed in version 3.4: object().\_\_format__(format_spec) raises TypeError if format_spec is not an empty string.

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
返回一个由数字或字符串`x`组成的整数对象，如果没有参数，则返回`0`。如果x定义了[\_\_int__()](https://docs.python.org/3.6/reference/datamodel.html#object.__int__)，`int(x)`返回`x.__int__()`。如果x定义[\_\_trunc__()](https://docs.python.org/3.6/reference/datamodel.html#object.__trunc__)，它返回`x.__trunc__()`。对于浮点数，这向零截断。
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

# map
map(function, iterable, ...): 返回一个迭代器，该迭代器将function应用于iterable的每一项，yielding结果。

假如额外的iterable参数被传递，function必须取多个参数，并且并行地被应用于所有迭代器的items。
有了多个迭代器，迭代器会在最短的迭代器被耗尽时停止。对于函数输入已经被安排成参数元组的情况，查看 [itertools.starmap()](https://docs.python.org/3.6/library/itertools.html#itertools.starmap)。
```
>>> list(map(lambda x: 2*x,[1,2,3]))
[2, 4, 6]
>>> list(map(lambda x,y: x+y,[1,2,3], [4,5]))
[5, 7]
>>> list(map(lambda x,y: x+y,[1,2,3], [4,5,6]))
[5, 7, 9]

>>> list(map(lambda x: 2*x,[1,2,3],[4,5]))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: <lambda>() takes 1 positional argument but 2 were given
```

# max
返回一个可迭代器里最大的item，或者2个或更多的参数最大的。
+ max(iterable, *[, key, default])
+ max(arg1, arg2, *args[, key])

如果提供了一个位置的参数，它应该是一个[iterable](https://docs.python.org/3.6/glossary.html#term-iterable)。iterable中最大的一项被返回。假如2个或更多的位置参数(positional arguments)被提供，返回最大的位置参数。

有2个可选的关键字参数。key参数指定一个参数的排序方法，就像list.sort()的使用。default参数指定要返回的对象，如果提供的iterable为空的话。假如iterbale为空且没有提供default，ValueError将被抛出。
```
>>> max(1,2,3,4,key=lambda x: x%4)
3
>>> max([1,2],[0,3],key=lambda x: x[1])
[0, 3]
>>> max([1,2],[0,3])
[1, 2]
```
如果多个items是最大值，函数范围第一个遇到的。这与其他稳定排序的保存工具是一致的，如`sorted(iterable, key=keyfunc, reverse=True)[0]` 和 `heapq.nlargest(1, iterable, key=keyfunc)`。

New in version 3.4: The default keyword-only argument.

# memoryview
memoryview(obj): 返回一个“内存试图”对象，它由给定的参数创建。有关更多信息，请参见[Memory Views](https://docs.python.org/3.6/library/stdtypes.html#typememoryview)。 

# min
返回一个iterable中最小的项或最小的两个或更多的参数中最小的。

+ min(iterable, *[, key, default])
+ min(arg1, arg2, *args[, key])

如果提供了一个位置的参数，它应该是一个[iterable](https://docs.python.org/3.6/glossary.html#term-iterable)。iterable中最小的一项被返回。假如2个或更多的位置参数(positional arguments)被提供，返回最小的位置参数。

有2个可选的关键字参数。key参数指定一个参数的排序方法，就像list.sort()的使用。default参数指定要返回的对象，如果提供的iterable为空的话。假如iterbale为空且没有提供default，ValueError将被抛出。

如果多个items是最小值，函数范围第一个遇到的。这与其他稳定排序的保存工具是一致的，如`sorted(iterable, key=keyfunc)[0]` 和 `heapq.nsmallest(1, iterable, key=keyfunc)`。

New in version 3.4: The default keyword-only argument.

# next
next(iterator[, default]): 从iterator调用它的__next__()方法，获取下一个item。如果给定default，如果iterator耗尽了，它将被返回，否则，StopIteration被抛出。

# object
class object: 返回一个没有特征的对象。[object](https://docs.python.org/3.6/library/functions.html#object)是所有class的基础。它有对所有Python类实例都通用的方法。这个函数不接受任何参数。

**注意** object没有一个__dict__，所以你不能给object类的实例分配任意属性。

# oct
oct(x): 将一个整数转换成前缀为“0o”的8进制字符。结果是一个有效的Python表达式。假如x不是一个Python int对象，它必须定义一个__index__()方法，它返回一个整数。例如：
```
>>> oct(8)
'0o10'
>>> oct(-56)
'-0o70'
```
假如你想将一个整数转换成8进制字符，要么前缀是“0o”要么不是，你可以使用下面方式的一种：
```
>>> '%#o' % 10, '%o' % 10
('0o12', '12')
>>> format(10, '#o'), format(10, 'o')
('0o12', '12')
>>> f'{10:#o}', f'{10:o}'
('0o12', '12')
```
See also format() for more information.

# open
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

打开文件并返回一个相应的file object。若果文件不能被打开，OSError被抛出。

file：file是一个[path-like object](https://docs.python.org/3.6/glossary.html#term-path-like-object)，它给定被打开的文件的pathname（绝对或相对当前工作目录），或者被包装的文件的整型文件描述符。（如果给定一个文件描述符 ，当返回的I/O对象被关闭时，它将被关闭，除非closefd被设置为false。）

mode：mode是一个可选字符，它指定文件以哪个模式打开。它默认是‘r’，这意味着以文本模式打开阅读。其他常见的值是‘w’写（如果文件已经存在，则截断该文件），‘x’为专有创造，‘a’为附加（在一些Unix系统中，这意味着*all writes*添加到文件末尾，而不管当前的查找位置是什么）。在text模式，如果没有指定encoding，使用的encoding依赖于平台（platform）：`locale.getpreferredencoding(False)`被调用来获取当前本地的encoding。（对于读写原始字节（raw butes），使用binary模式，且允许不指定编码）。可用的模式是：  

| Character | Meaning |
| :--- | :--- |
| 'r' | open for reading (default) |  
| 'w' | open for writing, truncating the file first |  
| 'x' | open for exclusive creation, failing if the file already exists |  
| 'a' | open for writing, appending to the end of the file if it exists |  
| 'b' | binary mode |  
| 't' | text mode (default) |  
| '+' | open a disk file for updating (reading and writing) |  
| 'U' | universal newlines mode (deprecated) | 

默认的模式是‘r’（打开阅读text，‘rt’的同义词）。对于二进制读写访问，‘w+b’模式打开和把文件截成0字节（truncates the file to 0 bytes）。‘r+b’不截断（truncation）打开文件。

正如在[overview](https://docs.python.org/3.6/library/io.html#io-overview)中提到的，Python区分二进制和文本输入/输出（I/O）。以二进制模式打开的文件（mode参数中包括“b”）返回内容为不进行任何解码的字节对象。在文本模式（默认情况下，或者mode参数中包含“t”），返回的文件内容为[str](https://docs.python.org/3.6/library/stdtypes.html#str)，这些字节已先被解码，通过使用平台相关的编码，或者在给定的情况下使用指定的编码。

**注意** Python并不依赖于底层操作系统的文本文件概念；有的处理都是由Python本身完成的，因此是独立于平台的。

buffering：buffering是一个可选的整数，它被用来设置缓冲策略。传0来选择关闭缓冲（只在二进制模式中允许），传1来选择行缓冲（只在文本模式有用），和传大于1的整数来表示一个固定缓冲区的字节大小。当没有给定buffering参数，默认的缓冲策略如下：
- 二进制文件以固定大小的块进行缓冲；缓冲区的大小是使用启发式方法来确定底层设备的“块大小”，然后返回到[ io.DEFAULT_BUFFER_SIZE](https://docs.python.org/3.6/library/io.html#io.DEFAULT_BUFFER_SIZE)。在许多系统中，缓冲区通常为4096或8192字节长。
- “互动”的文本文件（[isatty()](https://docs.python.org/3.6/library/io.html#io.IOBase.isatty)返回`True`的文件）使用行缓冲。其他的文本文件使用上面描述的二进制文件的策略。

encoding：encoding是用来解码或编码文件的编码的名称。这只应该在文本模式中使用。默认的编码是平台相关的（无论locale.getpreferredencoding()返回什么），但是Python支持的任何文本编码都可以使用。对于支持的编码列表，查看[codecs](https://docs.python.org/3.6/library/codecs.html#module-codecs)模块

error：error是可选字符，它指定如何解决编码和解码错误——这可能用在二进制模式。有各种标准错误处理程序可用(被列在[Error Handlers](https://docs.python.org/3.6/library/codecs.html#error-handlers))，尽管在 [codecs.register_error()](https://docs.python.org/3.6/library/codecs.html#codecs.register_error) 中注册的任何错误处理名称都是有效的。标准名称包括：
- 如果有一个编码错误，`strict`用于产生一个ValueError异常。默认值None有相同的作用。
- `ignore`忽略错误。注意，忽略编码错误可能导致数据丢失。
- `replace`会引起一个替换标记（如“？”）被插入在有错误数据的地方。
- `surrogateescape`将任何不正确的字节表示为代码点，使用范围是从`U+DC80`到`U+DCFF`的Unicode私有使用区域（Unicode Private Use Area）。当`surrogateescape`错误处理器被用在写入数据时，这些私有代码点将被转换成相同的字节。
- `surrogateescape`只支持在写入文件时。编码不支持的字符被替换为适当的XML字符，参考`&#nnn`。
- `backslashreplace`用Python的反斜杠转义序列替换错误的数据。
- `namereplace`（也只在写入时支持）用`\N{...}`转义序列代替不支持的字符。

newline: newline控制 [universal newlines](https://docs.python.org/3.6/glossary.html#term-universal-newlines)模式是如何工作的（它只应用在文本模式）。它可以为`None`、`''`、`'\n'`、`'\r'` 和 `'\r\n'`。它工作如下：
- 当从流（stream）中读取输入时，如果newline是`None`，普通换行模式生效。输入中的行可以以`'\n'`、`'\r'` 和 `'\r\n'`作为结尾，并在返回给访问者之前，它们被翻译为`'\n'`。如果它是`''`，普通换行模式生效，但是返回给访问者的行结束符没有被翻译。如果它是其它的合法值，输入行只被给定的字符串中断，并且返回给访问者的行结束符没有被翻译。
- 当把输出写到流（stream）中时，如果newline是`None`，任何被写的`\n`字符被翻译为系统默认的行分隔符，[os.linesep](https://docs.python.org/3.6/library/os.html#os.linesep)。如果newline是`''`或`\n`，没有翻译发生。如果newline是其它任何合法的值，任何写入的`'\n'`字符被转化成给定的字符串。

closefd：如果closefd是`False`，且给定一个文件描述符而不是文件名，当文件被关闭，底层文件描述符将保持打开状态。如果给定文件名，closefd必须是`True`（默认）否则一个错误将产生。

opener：一个定制的opener可通过传一个callable作为opener来使用。文件对象的底层文件描述符可通过调用opener（with (file, flags)）获得。opener必须返回一个打开的文件描述符（传[os.open](https://docs.python.org/3.6/library/os.html#os.open)作为opener的结果在功能上类似于传None）。 

The newly created file is [non-inheritable](https://docs.python.org/3.6/library/os.html#fd-inheritance).

下面的例子使用os.open()函数的[dir_fd](https://docs.python.org/3.6/library/os.html#dir-fd)参数来打开相对于给定目录的文件：
```python
>>> import os
>>> dir_fd = os.open('somedir', os.O_RDONLY)
>>> def opener(path, flags):
...     return os.open(path, flags, dir_fd=dir_fd)
...
>>> with open('spamspam.txt', 'w', opener=opener) as f:
...     print('This will be written to somedir/spamspam.txt', file=f)
...
>>> os.close(dir_fd)  # don't leak a file descriptor
```

由open()函数返回file object类型取决于模式。当open()被用来以文本模式('w', 'r', 'wt', 'rt'等)打开文件时，它返回一个[io.TextIOBase](https://docs.python.org/3.6/library/io.html#io.TextIOBase)的子类（特别的io.TextIOBase）。当被用来在二进制模式下用buffering打开文件时，它返回一个[io.BufferedReader](https://docs.python.org/3.6/library/io.html#io.BufferedReader)；在写入和追加二进制模式中，它返回一个[io.BufferedWriter](https://docs.python.org/3.6/library/io.html#io.BufferedWriter)，且在读写模式下，它返回[io.BufferedRandom](https://docs.python.org/3.6/library/io.html#io.BufferedRandom)。当buffering生效，原始流，[io.RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase)的子类，返回[io.FileIO](https://docs.python.org/3.6/library/io.html#io.FileIO)。

也可查看文件处理模块，如[fileinput](https://docs.python.org/3.6/library/fileinput.html#module-fileinput)，[io](https://docs.python.org/3.6/library/io.html#module-io)（open()声明的地方），[os](https://docs.python.org/3.6/library/os.html#module-os)，[os.path](https://docs.python.org/3.6/library/os.path.html#module-os.path)，[tempfile](https://docs.python.org/3.6/library/tempfile.html#module-tempfile) 和 [shutil](https://docs.python.org/3.6/library/shutil.html#module-shutil)。

    Changed in version 3.3:

        The opener parameter was added.
        The 'x' mode was added.
        IOError used to be raised, it is now an alias of OSError.
        FileExistsError is now raised if the file opened in exclusive creation mode ('x') already exists.

    Changed in version 3.4:

        The file is now non-inheritable.

Deprecated since version 3.4, will be removed in version 4.0: The 'U' mode.

    Changed in version 3.5:

        If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an InterruptedError exception (see PEP 475 for the rationale).
        The 'namereplace' error handler was added.

    Changed in version 3.6:

        Support added to accept objects implementing os.PathLike.
        On Windows, opening a console buffer may return a subclass of io.RawIOBase other than io.FileIO.


# ord
ord(c): 给定一个表示Unicode字符的字符串，返回一个表示该字符的Unicode编码点的整数。例如，`ord('a')`返回整数`97`和 `ord('€')`（欧元符号）返回`8364`。这与chr()相反。

# pow
pow(x, y[, z]): 返回x的y幂次方；如果z存在，返回x的y幂次方，除z取模（比计算`pow(x, y) % z`更有效）。`pow(x, y)`2个参数等同于使用幂次方操作符：x**y。

参数必须是数学类型。混合操作数类型，对二进制算术运算符的强制规则适用。对于int操作对象，结果与操作数相同（在强制之后），除非第二个参数为负;在这种情况下，所有的参数都被转换为浮点数，并交付浮动结果。例如，`10**2`返回100，但是`10**-2`返回0.01。如果第二个参数为负，则必须省略第三个参数。如果z是存在的，那么x和y必须是整数类型，而y必须是非负的。

# print
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

将objects打印到文本流file中，由sep分离，然后是end。如果存在sep、end、file和flush，则必须以关键字参数的形式给出。

所有非关键字形式参数都被转换成字符串，像str()所做的那样，并写入到流中，由sep分隔和最后跟着end。sep和end两者都必须是字符串；它们也可以是None，这意味着使用默认值。如果没有给定objects，print()将只会写入`end`。

file参数必须是一个有`write(string)`方法对象；如果它不存在或为None，[sys.stdout](https://docs.python.org/3.6/library/sys.html#sys.stdout)将被使用。由于打印的参数被转换成文本字符串，所以print()不能与二进制模式文件对象一起使用。对于这些，使用`file.write(...)`代替。

输出是否被缓冲通常由file决定，但是如果flush关键字参数是true，the stream is forcibly(强制) flushed_。

Changed in version 3.3: Added the flush keyword argument.

# property
class property(fget=None, fset=None, fdel=None, doc=None): 返回一个property属性。

fget是一个用来获取一个属性值的函数。fset是一个用来设置一个属性值的函数。fdef是一个用来删除属性值的方法。且doc创建一个属性的docstring。

一个典型的用法是来定义一个被管理的属性x：
```python
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    """ 
    >>> type(C.x)
    <class 'property'>
    """
    x = property(getx, setx, delx, "I'm the 'x' property.")
```
如果c是C的实例，`c.x`将调用获取方法（getter），`c.x=value`将调用设置方法（setter），且`del c.x`将调用删除方法（deleter）。

如果给定了，doc将是这个性质属性的docstring。否则，property将复制`fget`的docstring（如果它存在的话）。这使得可以很容易地创建只读属性，通过使用`property()`作为一个装饰器（[decorator](https://docs.python.org/3.6/glossary.html#term-decorator)）。
```python
class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage.
        
        >>> type(Parrot.voltage)
        <class 'property'>
        """
        return self._voltage
```
`@property`装饰器将`voltage()`方法变成一个`具有相同名字`的只读属性的“getter”，并且它设置voltage的docstring为“Get the current voltage.”。

一个property对象拥可使用装饰器的 `getter`, `setter` 和 `deleter` 方法，装饰器创建property的副本，并将相应的存取器函数设置到被装饰的函数，最好用一个例子来解释：
```python
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```
这段代码恰好等同于第一个例子。一定要赋予额外的函数与原始属性相同的名称（在本例中为x）

返回的property对象也有属性`fget`, `fset` 和 `fdel`，对应于构造函数参数。

Changed in version 3.5: The docstrings of property objects are now writeable.

# range

range事实上是一个不可变的序列类型，而不是一个函数，记录在[Ranges](https://docs.python.org/3.6/library/stdtypes.html#typesseq-range)和[Sequence Types — list, tuple, range](https://docs.python.org/3.6/library/stdtypes.html#typesseq)。
+ class range(stop)
+ class range(start, stop[, step])

# repr
repr(object): 返回一个字符串，它含有一个可打印表现的对象。

对许多的类型来说，这个方法试图返回一个字符串，当他被传给eval()时，这将会产生一个具有相同值的对象，否则的话，表示是一个用尖括号括起来的字符串，它包含对象类型的名称和附加的信息，通常包括对象的名称和地址。通过定义一个[\_\_repr__()](https://docs.python.org/3.6/reference/datamodel.html#object.__repr__)方法，一个类可以控制这个函数返回对于其实例的内容。

# reversed
reversed(seq): 返回一个相反的序列。seq必须是一个对象，它有[\_\_reversed__()](https://docs.python.org/3.6/reference/datamodel.html#object.__reversed__)方法或支持序列协议(有从0开始的整数参数的__len__()方法和__getitrm__()方法)。

# round
round(number[, ndigits]): 返回小数点后ndigits精度的四舍五入的数字。假如ndigits被省略或为None，它返回它输入的最近的整数（`it returns the nearest integer to its input.`）。

对于支持round()的内置类型，值被四舍五入到最接近10的ndigits负幂次方的倍数（multiple）；如果两边的倍数距离都相等，四舍五入偏向于选择偶数（例如，`round(0.5)` 和 `round(-0.5)` 两者都是 0，且`round(1.5)`是2）。
> For the built-in types supporting round(), values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done toward the even choice (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2).
```python
>>> round(0.5), round(-0.5), round(1.5)   # 当出现.5的时候，两边的距离都一样，取最近的偶数
(0, 0, 2)
>>> round(1023, -2)
1000
>>> round(1023.1234, 2)
1023.12

```
任何整数值对于ndigits是有效的（整数，0或负数）。如果ndigits被省略或为None，返回值是一个整数。否则返回值和number类型相同。

对于一般的Python对象`number`，`round`代表`number.__round__`。

**注意** 对于浮点数的`round()`的行为是令人惊奇的。例如，`round(2.675, 2)`得到`2.67`代替了期望的`2.68`，这不是一个bug。这是由于大多数小数部分不能完全表示为浮点数。为了更多信息，查看[Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3.6/tutorial/floatingpoint.html#tut-fp-issues)。

# set
class set([iterable]): 返回一个新的set对象，可选的元素从iterable中获取。set是内置类，为了更多关于这个类的信息，查看[set](https://docs.python.org/3.6/library/stdtypes.html#set)和[Set Types — set, frozenset](https://docs.python.org/3.6/library/stdtypes.html#types-set)。

For other containers see the built-in frozenset, list, tuple, and dict classes, as well as the collections module.

# setattr
setattr(object, name, value): 这是getattr()的相似物。参数是一个对象、一个字符串和一个任意的值。字符串可能会命名一个已有的属性或一个新属性。函数将值赋给属性，只要对象允许。例如，`setattr(x, 'foobar', 123)`等同于`x.foobar = 123`。

# slice
返回一个slice对象，它表示由`range(start, stop, step)`指定的索引集合。start和step默认为None。slice对象有只读的数据属性`start`、`stop`和`step`，这仅仅返回参数的值（或它们的默认值）。它们没有其他特定的功能；但是它们是由Numerical Python和其他第三方扩展所使用的。当使用扩展的索引语法时，也会生成切片对象。例如：`a[start:stop:step]`或`a[start:stop, i]`。请参阅[itertools.islice()](https://docs.python.org/3.6/library/itertools.html#itertools.islice)，以获得一个返回迭代器的备用版本。
- class slice(stop)
- class slice(start, stop[, step])

# sorted
sorted(iterable, *, key=None, reverse=False): 从iterable的项目中返回一个新的排序列表。

有两个可选的参数，必须指定为关键字参数。

key 指定一个参数的函数，它被用来从每个列表元素中提取一个比较键：`key=str.lower`。默认值是None（直接比较元素）。

reverse 是一个布尔值。如果它设为`True`，然后，列表元素被排序，就好像每个比较都被颠倒了一样。

使用[functools.cmp_to_key()](https://docs.python.org/3.6/library/functools.html#functools.cmp_to_key)将旧式的cmp函数转换为一个key函数。

内置的sorted()函数保证是稳定的。如果它保证不改变比较相等的元素的相对顺序，排序是稳定的 —— 这有助于在多个传递中进行排序（例如，按部门排序，然后按工资等级排序）。

对于排序示例和一个简短的排序教程，查看[ Sorting HOW TO ](https://docs.python.org/3.6/howto/sorting.html#sortinghowto)。

# staticmethod
@staticmethod: 将一个方法转变为静态方法。

静态方法不接受隐式的第一个参数。要声明一个静态方法，请使用这个习语：
```python
class C:
    @staticmethod
    def f(arg1, arg2, ...): ...
```

`@staticmethod`的形式是一个函数装饰器 —— 查看在[Function definitions](https://docs.python.org/3.6/reference/compound_stmts.html#function)中的函数定义描述的细节。

它可以在类上调用（例如 `C.f()`），也可以在实例上调用（ 例如`C().f()`）。除了它的类之外，该实例被忽略。

Python中的静态方法与在Java或C++中发现的方法类似。也请参阅[classmethod()](https://docs.python.org/3.6/library/functions.html#classmethod)，以获得对创建备用类构造函数有用的变体。

像所有的decorator一样，也可以将staticmethod称为常规函数，且用它的结果做点什么。这在某些情况下你需要来自类主体中函数的引用，这是需要的。你想要避免自动转换到实例方法。对于这些案例，使用这个习语：
```python
class C:
    builtin_open = staticmethod(open)
```
要了解更多关于静态方法的信息，请参考[The standard type hierarchy](https://docs.python.org/3.6/reference/datamodel.html#types)中的标准类型层次结构的文档。

# str
返回object的str版本。对于细节，查看[str()](https://docs.python.org/3.6/library/stdtypes.html#str)。
- class str(object='')
- class str(object=b'', encoding='utf-8', errors='strict')

str is the built-in string class. For general information about strings, see Text Sequence Type — str.

# sum
sum(iterable[, start]): 计算start和iterable从左到右的项的总合，并返回总数。

start默认是0。iterable的项通常是数字，start值不允许是字符串。

对于某些用例来说，sum()有很好的替代方法。连接字符串序列的首选、快速方法是通过调用`''.join(sequence)`。为了增加浮点值的精度，查看[math.fsum()](https://docs.python.org/3.6/library/math.html#math.fsum)。要连接一系列的iterables，可以考虑使用[itertools.chain()](https://docs.python.org/3.6/library/itertools.html#itertools.chain)。

# super
super([type[, object-or-type]]): 

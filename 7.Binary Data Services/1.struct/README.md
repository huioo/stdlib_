# struct

[struct](https://docs.python.org/3.6/library/struct.html#module-struct) — Interpret bytes as packed binary data

这个模块执行Python值和用Python字节对象表示的C结构体之间的转换。这可以用于处理存储在文件中或来自网络连接的二进制数据，以及其他来源。它使用[格式字符串](https://docs.python.org/3.6/library/struct.html#struct-format-strings)作为C结构体布局的紧凑描述，以及与Python值的预期转换。

> Note: 默认情况下，包装（packing）给定C结构体的结果包括pad bytes，以便为涉及的C类型保持适当的对齐；类似地，开箱（unpacking）时也要考虑对齐。选择此行为是为了使打包结构的字节与相应C结构在内存中的布局完全对应。若要处理与平台无关的数据格式或省略隐式pad bytes，使用`standrad` size 和 alignment 代替`native` size 和 alignment：详细信息查看[Byte Order, Size, and Alignment](https://docs.python.org/3.6/library/struct.html#struct-alignment)。

一些struct函数(和 Struct 的方法)使用一个*buffer*参数。这是指实现缓冲区协议（[Buffer Protocol](https://docs.python.org/3.6/c-api/buffer.html#bufferobjects)）并提供可读或可写缓冲区的对象。最常用的类型是bytes和bytearray，但是许多其他类型的字节可以被看作是一个实现缓冲协议的字节数组，这样它们就可以被读取/填充，而无需从bytes对象中进行额外的复制。

## 1. Functions and Exceptions

该模块定义了以下异常和函数：

***exception***  

- struct.error: 在各种场合抛出的异常，参数是一个描述错误的字符串。
  
  Exception raised on various occasions; argument is a string describing what is wrong.

***funcrtions***

- struct.pack(fmt, v1, v2, ...)  
  返回一个字节对象，其中包含按格式字符串*fmt*打包的值*v1*, *v2*，...。参数必须与格式所需的值完全匹配。

- struct.pack_into(fmt, buffer, offset, v1, v2, ...)  
  按格式字符串*fmt*打包值*v1*, *v2*，...。从位置偏移量 *offset* 开始将打包的字节写入可写缓冲区 *buffer*。注意，*offset*是必需的参数。

- struct.unpack(fmt, buffer)  
  根据格式字符串*fmt*从缓冲区*buffer*（可能有`pack(fmt, ...)`打包）中解包。结果是一个元组，即使它只包含一个项。缓冲区的字节大小必须匹配格式所需的大小，如`calcsize()`所示。

- struct.unpack_from(fmt, buffer, offset=0)  
  根据格式字符串 *fmt*，从位置偏移量 *offset* 处开始从缓冲区解压。结果是一个元组，即使它只包含一个项。缓冲区的字节大小(减去偏移量offset**)必须至少是格式所需的大小，如`calcsize()`所反映的那样。

- struct.iter_unpack(fmt, buffer)  
  根据格式字符串 *fmt* 迭代地从缓冲区 *buffer* 解包。这个函数返回一个迭代器，它将从缓冲区读取大小相同的块，直到所有内容都被使用。缓冲区的字节大小必须是格式所需大小的倍数，如`calcsize()`所示。

  每次迭代生成一个由格式字符串指定的元组。

  New in version 3.4.

- struct.calcsize(fmt)  
  返回与格式字符串 *fmt* 对应的结构体(以及由`pack(fmt，...)`生成的bytes对象）的大小。

## 2. Format Strings

格式化字符串是在打包和解包数据时用来指定预期布局的机制。它们是由格式字符（[Format Characters](https://docs.python.org/3.6/library/struct.html#format-characters)）构建的，格式字符指定打包/解压的数据类型。此外，还有用于控制字节顺序、大小和对齐（[Byte Order, Size, and Alignment](https://docs.python.org/3.6/library/struct.html#struct-alignment)）的特殊字符。

### 2.1. Byte Order, Size, and Alignment

默认情况下，C类型以机器的native（本机）格式和字节顺序表示，并在必要时通过跳过pad字节(根据C编译器使用的规则)进行适当对齐。

或者，格式字符串的第一个字符可以用来指示打包数据的字节顺序、大小和对齐方式，如下表所示：

Character | Byte order | Size | Alignment
--- | --- | --- | ---
@ | native | native | native
= | native | standard | none
< | little-endian | standard | none
> | big-endian | standard | none
! | network (= big-endian) | standard | none

如果第一个字符不是这些字符中的一个，则假定为“`@`”。

native字节顺序为大端（big-endian）或小端（little-endian），取决于主机系统。例如，Intel x86和AMD64 (x86-64)是little-endian；Motorola 68000和PowerPC G5是 big-endian；ARM和Intel Itanium的特点是可切换的字节顺序（endianness）(bi-endian)。使用`sys.byteorder`检查系统的字节顺序。

native大小和对齐是使用C编译器的表达式`sizeof`确定的。这总是与native字节顺序相结合。

标准尺寸只取决于格式字符；参见格式字符部分中的表格。

注意“`@`”和“`=`”之间的区别:两者都使用native字节顺序，但后者的大小和对齐方式是标准化的。

形式“`!`”适用于那些声称不记得网络字节顺序是大端字节还是小端字节的可怜人。

无法指示非native字节顺序(强制字节交换);使用适当的“<”或“>”选项。

Notes:

1. 填充仅在连续结构成员之间自动添加。在编码结构的开头或结尾不添加任何填充。
2. 使用非native大小和对齐时不添加填充，例如，用“<”、“>”、“=”和“!”。
3. 若要将结构的结尾与特定类型的对齐要求对齐，请在格式的结尾使用该类型的代码，重复计数为0。See [Examples](https://docs.python.org/3.6/library/struct.html#struct-examples)。

### 2.2. Format Characters

格式字符有以下含义；鉴于C和Python值的类型，它们之间的转换应该是显而易见的。“Standard size”列是指使用标准尺寸时所包装的值的字节大小；也就是说，当格式字符串以“`<`”、“`>`”和“`!`”或“`=`”。在使用native size时，打包值的大小依赖于平台。

Format | C Type | Python type | Standard size | Notes
--- | --- | --- | --- | ---
x | pad byte | no value |   |  
c | char | bytes of length 1 | 1 |  
b | signed char | integer | 1 | (1),(3)
B | unsigned char | integer | 1 | (3)
? | _Bool | bool | 1 | (1)
h | short | integer | 2 | (3)
H | unsigned short | integer | 2 | (3)
i | int | integer | 4 | (3)
I | unsigned int | integer | 4 | (3)
l | long | integer | 4 | (3)
L | unsigned long | integer | 4 | (3)
q | long long | integer | 8 | (2), (3)
Q | unsigned long long | integer | 8 | (2), (3)
n | ssize_t | integer |   | (4)
N | size_t | integer |   | (4)
e | (7) | float | 2 | (5)
f | float | float | 4 | (5)
d | double | float | 8 | (5)
s | char[] | bytes |   |  
p | char[] | bytes |   |  
P | void * | integer |   | (6)

Changed in version 3.3: Added support for the 'n' and 'N' formats.

Changed in version 3.6: Added support for the 'e' format.

Notes:

1. 转换代码“`?`”对应由C99定义的`_Bool`类型。如果该类型不可用，则使用`char`进行模拟。在标准模式中，它总是由一个字节表示。
2. 只有当平台C编译器支持C `long long`，或者在Windows上支持`__int64`时，“`q`”和“`Q`”转换代码才在native模式下可用。它们总是在标准模式下可用。
3. 当尝试使用任何整数转换代码打包非整数时，如果非整数有`__index__()`方法，则在打包之前调用该方法将参数转换为整数。

   Changed in version 3.2: Use of the __index__() method for non-integers is new in 3.2.
4. “`n`”和“`N`”转换码仅适用于native大小(选择为默认值或使用“`@`”字节顺序字符)。对于标准大小，您可以使用适合您的应用程序的任何其他整数格式的转换码。
5. 对于“`f`”、“`d`”和“`e`”转换码，无论平台使用何种浮点格式，打包表示（the packed representation）都使用IEEE 754 binary32、binary64或binary16格式(分别用于“`f`”、“`d`”或“`e`”)。
6. “`P`”格式字符仅适用于native字节顺序(选择为默认值或使用“@”字节顺序字符)。字节顺序字符“`=`选择使用基于主机系统的小端或大端排序。struct模块不将其解释为本机排序，因此“P”格式不可用。
7. IEEE 754 binary16 “半精度”类型是在2008年修订的[IEEE 754标准](https://en.wikipedia.org/wiki/IEEE_floating_point#IEEE_754-2008)中引入的。它有一个符号位、一个5位指数（exponent）和11位精度（precision）（显式存储10位），并且可以在全精度下表示大约`6.1e-05`到`6.5e+04`之间的数字。C编译器不广泛支持这种类型：在标准的（typical）机器上，无符号短整型可以用于存储，但不能用于数学操作。See the Wikipedia page on the half-precision floating-point format for more information.

格式字符的前面可以有一个整数重复计数。例如，格式字符串“`4h`”的含义与“`hhhh`”完全相同。

格式之间的空格字符被忽略；但是，计数及其格式不能包含空格。

对于“`s`”格式字符，计数被解释为字节的长度，而不是像其他格式字符那样的重复计数；举个例子，"`'10s'`"指一个10字节字符串，然而“`'10c`”指10个字符。假如没有给定计数，默认是1。对于打包，字符串将被截断（truncate）或使用空字节进行填充（pad），适当地使其相符。对于解包，生成的bytes对象始终具有指定的字节数。在特殊情况下，“`0s`”表示一个空字符串(而“`0c`”表示0个字符)。

当使用整数格式(`'b'`， `'b'`， `'h'`， `'h'`， `'i'`， `'i'`， `'l'`， `'l'`， `'q'`， `'q'`)包装一个值`x`时，如果`x`在该格式的有效范围之外，那么会抛出`struct.error`。

Changed in version 3.1: In 3.0, some of the integer formats wrapped out-of-range values and raised [DeprecationWarning](https://docs.python.org/3.6/library/exceptions.html#DeprecationWarning) instead of struct.error.

“`p`”格式字符编码一个“Pascal string”，意思是一个短的可变长度的字符串，存储在一个固定的字节数中，由计数器给出。存储的第一个字节是字符串的长度，或255，以较小的长度为准。字符串的字节如下。如果传递给`pack()`的字符串太长(长于`count-1`)，则只存储字符串的前`count-1`字节。如果字符串小于`count-1`，则用空字节填充字符串，这样就可以准确地计算所有字符串的字节数。注意，对于`unpack()`，“`p`”格式字符使用`count`字节，但是返回的字符串不能包含超过255字节。

对于“`?`”格式化字符，返回值为`True`或`False`。包装时，使用实参对象的真实值。在本机或标准bool表示中，0或1将被打包，并且在解包时，任何非零值都将为True。

### 2.3. Examples

Note: All examples assume a native byte order, size, and alignment with a *big-endian* machine.

packing/unpacking 三个整数的基本示例:

```python
>>> from struct import *
>>> pack('hhl', 1, 2, 3)
b'\x00\x01\x00\x02\x00\x00\x00\x03'
>>> unpack('hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03')
(1, 2, 3)
>>> calcsize('hhl')
8
```

可以通过将未打包的字段分配给变量或将结果包装在命名的元组中来命名它们：

```python
>>> record = b'raymond   \x32\x12\x08\x01\x08'
>>> name, serialnum, school, gradelevel = unpack('<10sHHb', record)

>>> from collections import namedtuple
>>> Student = namedtuple('Student', 'name serialnum school gradelevel')
>>> Student._make(unpack('<10sHHb', record))
Student(name=b'raymond   ', serialnum=4658, school=264, gradelevel=8)
```

格式字符的顺序可能会影响大小，因为满足对齐要求所需的填充是不同的：

```python
>>> pack('ci', b'*', 0x12131415)
b'*\x00\x00\x00\x12\x13\x14\x15'
>>> pack('ic', 0x12131415, b'*')
b'\x12\x13\x14\x15*'
>>> calcsize('ci')
8
>>> calcsize('ic')
5
```

下面的格式`'llh0l'`指定两个填充字节在最后，假设长整型是以4字节的边界对齐：

```python
>>> pack('llh0l', 1, 2, 3)
b'\x00\x00\x00\x01\x00\x00\x00\x02\x00\x03\x00\x00'
```

只有当native大小和对齐方式生效时，此操作才有效；标准尺寸和对齐不强制任何对齐。

See also

**Module** [array](https://docs.python.org/3.6/library/array.html#module-array)

Packed binary storage of homogeneous data.

**Module** [xdrlib](https://docs.python.org/3.6/library/xdrlib.html#module-xdrlib)

Packing and unpacking of XDR data.

## 3. [Classes](https://docs.python.org/3.6/library/struct.html#classes)

The struct module also defines the following type:

*class* struct.**Struct**(*format*)

Return a new Struct object which writes and reads binary data according to the format string format. Creating a Struct object once and calling its methods is more efficient than calling the struct functions with the same format since the format string only needs to be compiled once.

Compiled Struct objects support the following methods and attributes:

- pack(v1, v2, ...)

Identical to the pack() function, using the compiled format. (len(result) will equal size.)

- pack_into(buffer, offset, v1, v2, ...)

Identical to the pack_into() function, using the compiled format.

- unpack(buffer)

Identical to the unpack() function, using the compiled format. The buffer’s size in bytes must equal size.

- unpack_from(buffer, offset=0)

Identical to the unpack_from() function, using the compiled format. The buffer’s size in bytes, minus offset, must be at least size.

- iter_unpack(buffer)

Identical to the iter_unpack() function, using the compiled format. The buffer’s size in bytes must be a multiple of size.

New in version 3.4.

- format

The format string used to construct this Struct object.

- size

The calculated size of the struct (and hence of the bytes object produced by the pack() method) corresponding to format.
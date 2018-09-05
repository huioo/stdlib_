# [Built-in Constants](https://docs.python.org/3.6/library/constants.html#built-in-constants)

少量的常量存在于内置的名称空间中。它们是：

# Flase
bool类型的错误值。分配给False是非法的，并增加一个语法错误（SyntaxError）。
```python
>>> False = 1
  File "<input>", line 1
SyntaxError: can't assign to keyword
```

# True
bool类型的真正值。分配给True是非法的，并增加了一个语法错误（SyntaxError）。
```python
>>> True = 1
  File "<input>", line 1
SyntaxError: can't assign to keyword
```

# None
类型`NoneType`的唯一值。`None`被频繁地用来表示一个值没有价值，当默认参数没有传递给函数时。分配给`None`是非法的，并增加了一个语法错误（SyntaxError）。

# NotImplemented
特殊值应该由二进制特殊方法返回（举例来说，\_\_eq__(), \_\_lt__(), \_\_add__(), \_\_rsub__() 等），以表明该操作不是针对另一种类型实现的。可以用就地的（in-place）二进制特殊方法（如__imul__()、\_\_iand__()等）返回，以达到相同的目的。它的真值是true。

**注意** 当二进制（或就地——in-place）方法返回`NotImplemented`时，解释器会在另一种类型上尝试反射操作（或者其他的回退，取决于操作人员）。如果所有的尝试都返回`NotImplemented`，解释器会提出一个适当的异常。错误地返回`NotImplemented`将导致令人误解的错误消息或返回到Python代码的`NotImplemented`值。请参阅[Implementing the arithmetic operations](https://docs.python.org/3.6/library/numbers.html#implementing-the-arithmetic-operations)的示例。

**注意** `NotImplementedError` 和 `NotImplemented`不是可交换的，即使他们有相似的名字和目的。有关何时使用它的详细信息，请参见 [NotImplementedError](https://docs.python.org/3.6/library/exceptions.html#NotImplementedError)。

# Ellipsis
与`...`相同的特别值主要用于与用户定义的容器数据类型的扩展切片语法相结合。

# \_\_debug__
如果Python不是以-O选项开始的，那么这个常量就是True。见[assert](https://docs.python.org/3.6/reference/simple_stmts.html#assert)语句。

**注意** None、False、True和__debug__不能被重新分配（分配给它们，即使作为一个属性名，也会提高SyntaxError），因此它们可以被认为是“真正的”常量。

# Constants added by the [site](https://docs.python.org/3.6/library/site.html#module-site) module
> site模块（在启动时自动导入，除非给出了-S命令行选项）为内置的命名空间添加了几个常量。它们对于交互式解释器shell很有用，不应该在程序中使用。

## quit
quit(code=None)

## exit
exit(code=None)

对象被打印时，打印一个信息，像“Use quit() or Ctrl-D (i.e. EOF) to exit”，当被调用时，用特别的退出代码产生[SystemExit](https://docs.python.org/3.6/library/exceptions.html#SystemExit)。

## copyright

## credits
对象呗打印或调用时，分别打印copyright和credits的文本。

## license
对象被打印时，打印“Type license() to see the full license text”信息，当被调用时，以类似于pager的方式显示完整的许可文本（一次一个屏幕）

```python
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
>>> print(exit)
Use exit() or Ctrl-Z plus Return to exit
>>> print(quit)
Use quit() or Ctrl-Z plus Return to exit
>>> print(license)
Type license() to see the full license text
>>> print(credits)
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
>>> print(copyright)
Copyright (c) 2001-2018 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

... ...
>>> print(quit)
Use quit() or Ctrl-Z plus Return to exit
```

```python
>>> license()
A. HISTORY OF THE SOFTWARE
==========================

Python was created in the early 1990s by Guido van Rossum at Stichting
Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
as a successor of a language called ABC.  Guido remains Python's
principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for
National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)

... ...

Hit Return for more, or q (and Return) to quit: >? q
>>> credits
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
>>> credits()
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
>>> copyright()
Copyright (c) 2001-2018 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

... ...
>>> quit()

Process finished with exit code 0

```

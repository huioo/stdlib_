# 3. collections —— Container datatypes

## 3.7. UserDict objects

[UserDict](https://docs.python.org/3.6/library/collections.html#collections.UserDict)类充当了一个围绕字典对象的包装（wrapper）。对该类的需求已经部分由直接继承dict的子类的能力所代替；然而，这个类可以更简单地使用，因为底层字典可作为一个属性来访问。

class collections.UserDict([initialdata])

该类模仿一个字典。实例的上下文被保存在一个有规则的（regular）字典内，这可以通过`UserDict`实例的`data`属性来访问。  
如果提供initialdata，`data`用它的内容来初始化。注意，initialdata的引用并不会被保存，允许它用于其它的目的。

除了支持`mappings`的方法和操作之外，UserDict实例提供了下面的属性：

- data:
  一个用来存储UserDict类的内容的真实字典

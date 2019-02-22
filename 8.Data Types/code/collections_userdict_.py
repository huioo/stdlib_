from collections import UserDict


# 直接使用
print(UserDict({'a': 1}))              # {'a': 1}
print(UserDict({'a': 1}, ab=1))        # {'a': 1, 'ab': 1}
print(UserDict(ab=1))                  # {'ab': 1}
print(UserDict(ab=1, dict={'a': 1, 'b': 2}))  # {'a': 1, 'b': 2, 'ab': 1}
print(UserDict({'a': 1}, ab=1, dict={'a': 2, 'b': 2}))  # {'a': 1, 'ab': 1, 'dict': {'a': 2, 'b': 2}}
print('- '*30)


# 作为基类继承
def ljust(s, length=28):
    return s.ljust(length)


class A(UserDict):
    def __init__(self, name, *args, **kwargs):
        """
        https://www.programcreek.com/python/example/100014/collections.UserDict.__init__
        """
        UserDict.__init__(self, *args, **kwargs)
        self['self_name'] = name
        print(ljust('UserDict __ini__: args'), args)
        print(ljust('UserDict __ini__: kwargs'), kwargs)
        print(ljust('UserDict __ini__: self'), self)
        print(ljust('UserDict __ini__: self.data'), self.data)
        print(ljust('[self == self.data]'), self == self.data)
        print(ljust('[self is self.data]'), self is self.data)
        
        self.name = name
        print(ljust('UserDict __ini__: self'), self)
        print(ljust('[self == self.data]'), self == self.data)  # def __repr__(self): return repr(self.data)
        print(ljust('[self is self.data]'), self is self.data)


a = A('abc', {'a': 1}, a1=1, a2=2)
print(a.data)

"""
UserDict __ini__: args       ({'a': 1},)
UserDict __ini__: kwargs     {'a1': 1, 'a2': 2}
UserDict __ini__: self       {'a': 1, 'a1': 1, 'a2': 2, 'self_name': 'abc'}
UserDict __ini__: self.data  {'a': 1, 'a1': 1, 'a2': 2, 'self_name': 'abc'}
[self == self.data]          True
[self is self.data]          False
UserDict __ini__: self       {'a': 1, 'a1': 1, 'a2': 2, 'self_name': 'abc'}
[self == self.data]          True
[self is self.data]          False
{'a': 1, 'a1': 1, 'a2': 2, 'self_name': 'abc'}

"""


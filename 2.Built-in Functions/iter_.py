# iter(object[, sentinel])
"""

sentinel: 迭代返回的值等于sentinel时，结束循环且不进行操作
"""

"""
fp.readline:
    <built-in method readline of _io.TextIOWrapper object at 0x00000171E9E67B40>
fp.readlines:
    <built-in method readlines of _io.TextIOWrapper object at 0x000002E16D0F7B40>
fp.readlines():
    ['a b c d e\n', 'a  d e\n', 'a b c e\n', 'a b c d e end\n', 'end\n', 'a\n']
"""
with open('iter_.txt') as fp:
    for line in iter(fp.readline, 'end\n'):
        print(line)



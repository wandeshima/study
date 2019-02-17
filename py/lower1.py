#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
练习
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
AttributeError: 'int' object has no attribute 'lower'
使用内建的isinstance函数可以判断一个变量是不是字符串：

>>> x = 'abc'
>>> y = 123
>>> isinstance(x, str)
True
>>> isinstance(y, str)
False
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
'''
L = ['Hello', 'World', 18, 'Apple', None]
print ([s.lower() if isinstance(s,str) else s for s in L])
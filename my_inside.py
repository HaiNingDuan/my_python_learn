#!/usr/bin/env python
# -*- coding: utf-8 -*-
#namedtuple

#namedtuple('名称', [属性list])
from collections import namedtuple
Point = namedtuple('Point', ['x','y']) #声明Point名称的tuple

p = Point(1,2)
print p.x
print p.y
#end namedtuple

#deque双向链表
from collections import deque
list = deque(['a','b','c','d'])
list.append('e')
list.appendleft('0')
print list
list.pop()
list.popleft()
print list
#end deque

#defaultdict(lambda:‘出错返回的默认值’)
from collections import defaultdict
dict = defaultdict(lambda:'N/A')
dict['key1'] = 'abc'
print dict['key1']  #返回key对应的'abc'
print dict['key2']  #无对应的key返回设定的默认值N/A
#end defaultdict

#OrderedDict 有序的字典
#from collections import OrderedDict
#dict_nor = dict[('a', 1), ('b', 2), ('c', 3)]
#print dict_nor #字典是无序的
#end OrderedDict




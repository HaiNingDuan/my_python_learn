#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

s = r'abc\012'  #自然转译
s1 = 'abc\012'  #不需转译
print s1

s = r'^\d{2}\w{2}-\d{1}\w{2}$'
match = re.match(s, '01dd-3ab')

print s
if match:
    print 'Match'
else :
    print 'No Match'

#split
s = 'a b  c  d, e, f;g  h ;i'
print s.split(' ')
print re.split(r'[\s\,\;]+', s)

#v1
s = raw_input('please input your email:')
re_s1 = r'^[a-zA-Z\.]+\@[a-z0-9A-Z]+\.[a-zA-Z]+$'
re_s2 = r'^\<[a-zA-Z0-9]+\>[0-9a-zA-Z]+\@[a-zA-Z0-9]+\.[a-zA-Z]+$'
match = re.match(re_s2, s)
if match:
    print 'Match'
else :
    print 'Not Match %s' % s
#v2

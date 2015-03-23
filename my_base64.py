#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
b64_string = base64.b64encode('binary\x00string')     #进行base64编码
binary_string = base64.b64decode(b64_string) #将base64编码转换成二进制编码

print b64_string
print binary_string

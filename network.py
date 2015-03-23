#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #创建套接字

s.connect(('www.sina.com.cn', 80))                      #链接服务器 

s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n') #发送请求

buffer = []

while True:
    d = s.recv(1024) #最多接收1k数据/每次
    if d:
        buffer.append(d)
    else:
        break
data = '.'.join(buffer)

s.close()    #关闭链接

header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)


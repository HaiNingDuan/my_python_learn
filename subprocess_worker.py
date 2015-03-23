#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, sys, Queue
from multiprocessing.managers import BaseManager

#创建队列管理
class QueueManager(BaseManager):
    pass

#由于这个QueueManager只从网络中获取Queue，所以只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#链接服务器
server = '127.0.0.1'
print ('Connect to Server %s' %server)

#设置链接属性
m = QueueManager(address=(server, 5050), authkey='abc')
#链接
m.connect()

#获取task对象
task = m.get_task_queue()
result = m.get_result_queue()

#从task队列取出任务,并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print ('run task %d * %d' %(n,n))
        r = '%d * %d = %d' %(n, n, n*n)
        time.sleep(1)
        task.put(r)
    except:
        print 'task_queue is empty'

print 'Worker out!'

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sub process --- manageer

import random, time, Queue
from multiprocessing.managers import BaseManager

#发送任务队列
task_queue = Queue.Queue()

#接收结果队列
result_queue = Queue.Queue()

#从BaseManager中继承出的QueueManager
class QueueManager(BaseManager):
    pass

#将两个Queue注册到网络上,callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda:task_queue)
QueueManager.register('get_result_queue', callable=lambda:task_queue)

#绑定端口5050，验证码abc
manager = QueueManager(address=('', 5050), authkey = 'abc')

#启动queue
manager.start()

#等待客户端启动

task = manager.get_task_queue()
result = manager.get_result_queue()

#放任务进入queue
for i in range(10):
    n = random.randint(0, 1000)
    print ('Put task %d...' % n)
    task.put(n)

time.sleep(1)
#从result中读取结果
print ('Try get results')
for i in range(10):
    r = result.get(timeout=10)
    print 'Result: %s' % r

#关闭
manager.shutdown()    


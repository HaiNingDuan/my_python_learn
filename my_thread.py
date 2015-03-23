#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, threading

# 新线程执行的代码:
#def loop():
#    print 'thread %s is running...' % threading.current_thread().name
#    n = 0
#    while n < 5:
#        n = n + 1
#        print 'thread %s >>> %s' % (threading.current_thread().name, n)
#        time.sleep(1)
#    print 'thread %s ended.' % threading.current_thread().name
#
#print 'thread %s is running...' % threading.current_thread().name
#t = threading.Thread(target=loop, name='LoopThread')
#t.start()
#t.join()
#print 'thread %s ended.' % threading.current_thread().name

local_school = threading.local()

def process_std():
    print 'hello %s(in %s)' %(local_school.std_name, threading.current_thread().name)

def process_thread(name):
    local_school.std_name = name  
    process_std()

t1 = threading.Thread(target=process_thread, args=('Tim', ), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Tom', ), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

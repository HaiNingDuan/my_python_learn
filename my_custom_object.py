#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):  #defining str method as my own so i can format the output string as i wish
        return 'Student Object (name: %s)' % self.name
print Student('jack', 18)

#定制类:斐波那契数列类
class Fib:
    def __init__(self): 
        self.a = 0
        self.b = 1
    def __iter__(self): 
        return self
    def next(self):
        self.a, self.b = self.b, self.a + self.b 
        if(self.a > 1000):
            raise StopIteration();
        return self.a
    def __getitem__(self, n):
        if(isinstance(n, int)):
            a,b = 1,1
            for x in range(n):
                a,b = b, a+b
            return a
        elif(isinstance(n, slice)):
            start = n.start
            stop = n.stop
            a,b = 1,1
            L = []
            for x in stop:
                if(x >= start):
                    L.append(a)
                a,b = b, a+b
            return L
f = Fib()
print f[10]

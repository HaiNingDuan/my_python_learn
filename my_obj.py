#!/usr/bin/env python 

#class Student(object):
#    def __init__(self, name, sorce):
#        self.name = name
#        self.sorce = sorce
#        self.__pri_name = u'hahaha'
#        self.__pri_sorce = 90
#
#    def print_self(self):
#        print 'name:',self.name,',','sorce:',self.sorce
#        
#    def get_pri_name(self):
#        return self._pri_name
#    def get_pri_sorce(self): 
#        return self._pri_sorce
#
#jack = Student('jack', 50)
#adm = Student('adm', 70)

#jack.print_self()
#print jack.get_pri_name()
#print jack.get_pri_sorce()
#adm.print_self()
#end object Student

#sub object
#class Animal(object):
#    def run(self):
#        print 'Animal run....'
#
#
#class Dog(Animal):
#    def run_self(self):
#        print 'Dog run...'
#    def eat_self(self):
#        print 'Dog eat bone'
#class Cat(Animal):
#    pass
#dog = Dog()
#dog.run()
#dog.run_self()
#dog.eat_self()
#
#cat = Cat()
#cat.run()
#
#print dir(dog)
#print dog.__str__()

#end sub object




#method
#class Myobject:
#    __slot__('name', 'age', 'sorce')
#def set_age(self, age):
#    self.age = age
#
#def set_sorce(self, sorce):
#    self.sorce = sorce
#
#myobject = Myobject()
#myobject.name = 'jack'
#
#from types import MethodType
#myobject.set_age = MethodType(set_age, myobject, Myobject)  #for instance
#Myobject.set_sorce = MethodType(set_sorce, None, Myobject)  #for class
#
#myobject.set_age(10)
#myobject.set_sorce(100)

#print myobject.name    ///< output
#print myobject.age     ///< output 
#print myobject.sorce   ///< output
#end method

#property
class Myobject:
    @property   #
    def score(self):
        return self._sorce
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value > 100 or value < 10:
            raise ValueError('score must between 10~100')
        self._score = value
            
m = Myobject()
m.score = 0
print m.score
        


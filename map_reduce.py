#!/usr/bin/env python
#map demo
input = ['adm', 'JacK', 'Jim']
def Convert_str(str):
    print str.capitalize()
#end func
map(Convert_str, input);

#reduce demo
def multi(x,y):
    return x*y 
#end func
print reduce(multi, [1,2,3,4,5,6]);

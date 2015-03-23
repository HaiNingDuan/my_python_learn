#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
#print os.name
#print os.uname()
#for x in os.listdir('.'):
#    if os.path.isdir(x):
#        print 'this is dir! %s' %(x)
#    else:
#        print 'this is file ! %s' %(x)
def search(s):
    for x in os.listdir('.'):   
        if os.path.isdir(x):
            pass
        else:
            if 0 <= x.find(s):
                print 'find! file name is %s' %(x)
    return
search('my')

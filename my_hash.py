#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

m = hashlib.md5()
print m.hexdigest()

m.update('this is test')
m.update('just kidding')
print m.hexdigest()

m2 = hashlib.md5()
m2.update('this is test just kidding')
print m2.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(usr, passwd):
    if not isinstance(usr, str):    #判断输入类型
        raise TypeError('usr arg should be string type')
    if not isinstance(passwd, str): #判断输入类型
        raise TypeError('passwd arg should be string type')
    if usr in db:   #循环遍历db成员
        #md5 = hashlib.md5()
        #md5.update(passwd)
        #m = md5.hexdigest()
        if passwd == db[usr]:
            print 'Matched! usr:%s, passwd md5:%s' %(usr, db[usr])
            return True
        else:
            print 'Not Matched!'
            return False
    else:
        print 'Not Matched!'
        return False

login('Michael', 'e10adc3949ba59abbe56e057f20f883e')

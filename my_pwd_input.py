#!/usr/bin/env python
# -*- coding: utf-8 -*-

#msvcrt is for windows system
import sys,os,tty,termios

def linux_getch(): 
    fd = sys.stdin.fileno()
    old_setting = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_setting)
    return unicode(ch, 'utf-8')


def pwd_input():
        pwd = []
        while True:
            newChar = linux_getch()
            if newChar in '\r\n':   #如果为换行
                break;
            elif newChar == '\b' or ord(newChar) == 127:   #为退格符
                if newChar:
                    sys.stdout.write('\b \b')
                    pwd = pwd[:-1]
            else:
                sys.stdout.write('*')
                pwd.append(newChar)
        return (''.join(pwd))            
##################################################
###测试代码
##################################################
if __name__ == "__main__" :
    print "Enter PassWord:",
    passwd = pwd_input()
    print passwd

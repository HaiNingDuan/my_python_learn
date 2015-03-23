#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email              import encoders
from email.mime.text    import MIMEText
from email.header       import Header
from email.utils        import parseaddr, formataddr
from my_pwd_input       import *

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((\
            Header(name, 'utf-8').encode(),\
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))


##################################################
### 输入模块
##################################################
smtp_server = raw_input('Please enter mail server addr:')

from_addr = raw_input('Please enter email addr:')

print "Please enter passwd:",
passwd = pwd_input()

to_addr = raw_input('Please enter guest addr:')

msg = MIMEText('hello this mail is from python', 'plain', 'utf-8') #构造邮件头

msg['From']     = _format_addr(u'爱潜水的老段<%s>' %from_addr)
msg['To']       = _format_addr(u'同样爱潜水的老段<%s>' %to_addr)
msg['Subject']  = Header(u'来自潜水星的问候', 'utf-8').encode()
import smtplib

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, passwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()




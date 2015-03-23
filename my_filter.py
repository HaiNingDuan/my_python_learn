#!/usr/bin/env python
#filert demo
def prime_nu_chk(n):
    if 1 == n:
        return
    if 2 == n:
        return
    for i in range(3,100):
        if 0 == n%i:
            return
    print n
    return n

#end func  prime_nu_chk
print filter(prime_nu_chk, range(1,100))

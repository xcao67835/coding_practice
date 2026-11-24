# -*- coding: utf-8 -*-
from functools import cache

@cache
def egg(n):
    if n==1:
        return 1
    return n-1+egg(n-1)


while 1:
    try:
        n=int(input())
        i=0
        while 1:
            i+=1
            if egg(i)>n:
                print(i-1)
                break
    except EOFError:
        break
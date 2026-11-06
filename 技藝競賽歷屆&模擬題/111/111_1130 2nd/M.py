# -*- coding: utf-8 -*-

from functools import lru_cache

@lru_cache(None)
def f(x):
    if x==1:
        return ['0','1']
    
    p=f(x-1)
    r=[]
    for i in p:
        r.append('0'+i)
    for i in reversed(p):
        r.append("1"+i)
    return r
n=int(input())
for i in f(n):
    print(i)
# -*- coding: utf-8 -*-

def f(p,i):
    if len(p)==0:
        return []
    if len(p)==1:
        return [*p]
    r=p.pop(0)
    idx=i.index(r)
    return *f(p[:idx], i[:idx]),*f(p[idx:], i[idx+1:]),r
    
while 1:
    try:
        p,i=input().split()
        p=list(p)
        i=list(i)
        print(*f(p,i),sep="")
    except EOFError:
        break
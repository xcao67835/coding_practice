# -*- coding: utf-8 -*-

def tree(p,i):
    if len(p)<=1:
        return p
    root=p[0]
    idx=i.index(root)

    return *tree(p[1:idx+1],i[:idx]),*tree(p[idx+1:],i[idx+1:]),root
while 1:
    try:
        a,b=map(list,input().split())
        print(*tree(a,b),sep="")
    except EOFError:
        break
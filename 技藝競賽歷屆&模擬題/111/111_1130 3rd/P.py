# -*- coding: utf-8 -*-

def post(po,io):
    if len(po)<=1:
        return po
    idx=io.index(po[0])
    return *post(po[1:1+idx], io[:idx]), *post(po[1+idx:], io[idx+1:]), po[0]
while 1:
    try:
        a,b=map(list, input().split())
        print(*post(a,b),sep="")
    except EOFError:
        break
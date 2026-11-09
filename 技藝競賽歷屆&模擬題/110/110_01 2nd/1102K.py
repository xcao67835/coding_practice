# -*- coding: utf-8 -*-
bk=0
while 1:
    a=int(input())
    b=int(input())
    c=int(input())
    print(pow(a,b,c))
    try:
        _=input()
    except:
        break
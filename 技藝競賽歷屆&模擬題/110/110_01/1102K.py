# -*- coding: utf-8 -*-

while 1:
    try:
        x=int(input())
        y=int(input())
        m=int(input())
        print(pow(x,y,m))
        _=input()
        
    except EOFError:
        break
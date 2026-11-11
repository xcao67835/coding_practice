# -*- coding: utf-8 -*-

while 1:
    try:
        n=input()
        a=int(n[0])
        for i in range(1,len(n)):
            a+=int(n[i])* ((i)%2*2-1)
        print(a)
    except EOFError:
        break
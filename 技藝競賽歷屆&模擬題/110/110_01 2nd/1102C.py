# -*- coding: utf-8 -*-

while 1:
    try:
        n=input()
        
        a=int(n[0])
        for i in range(1,len(n)):
            a+=int(n[i]) * (-1 if i%2==0 else 1)
        print(a)
    except EOFError:
        break
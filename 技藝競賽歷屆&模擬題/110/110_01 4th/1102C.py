# -*- coding: utf-8 -*-

while 1:
    try:
        n=input()
        a = int(n[0])
        for i in range(1,len(n)):
            if i%2==1:
                a+=int(n[i])
            else:
                a-=int(n[i])
        print(a)
        
        
    except EOFError:
        break
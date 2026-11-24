# -*- coding: utf-8 -*-
while 1:
    try:
        s=set()
        a,b=input().split()
        b=int(b)
        a=list(map(int,a.split(",")))
        
        for i in range(len(a)):
            t=b-a[i]
            if t in s:
                print(a.index(t),i,sep=",")
                break
            else:
                s.add(a[i])
                
    except EOFError:
        break

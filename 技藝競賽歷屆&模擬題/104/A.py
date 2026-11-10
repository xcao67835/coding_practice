# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split(",")))
    a=0
    for i in range(n-1):
        d=l[i+1]-l[i]
        if d>0:
            a+=20*d
        else:
            a+=-10*d
            
    print(a)
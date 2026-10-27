# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a,b=map(int,input().split())
    c=a//b
    if c<0 and a%b!=0:
        c+=1
        
    print(c)
# -*- coding: utf-8 -*-

a,b=map(int,input().split())
l=input().split()
for i in range(b):
    tl=[]
    for i in range(a//2):
        tl+=[l[i],l[i+a//2]]
    l=tl
print(*l)
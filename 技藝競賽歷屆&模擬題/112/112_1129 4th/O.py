# -*- coding: utf-8 -*-

a,b=map(int,input().split())
c=list(map(int,input().split()))
for i in range(b):
    t=[c[:a//2],c[a//2:]]
    c=[]
    for i in zip(*t):
        c.extend(i)
        
print(*c)
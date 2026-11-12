# -*- coding: utf-8 -*-

a,b=map(int,input().split())
m=[]
for i in range(a):
    m.append(list(map(int,input().split())))
    
for i in zip(*m):
    print(*i)
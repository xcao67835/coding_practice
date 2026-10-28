# -*- coding: utf-8 -*-

l=[]
for i in range(int(input())):
    l.append(tuple(map(int,input().split())))
    
l=sorted(l)
for i in l:
    print(*i)
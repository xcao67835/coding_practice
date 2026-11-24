# -*- coding: utf-8 -*-
l=[]
for _ in range(int(input())):
    l.append(tuple(map(int,input().split())))
    
l.sort()
for i in l:
    print(*i)
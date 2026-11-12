# -*- coding: utf-8 -*-

n=int(input())
l=[]
for _ in range(n):
    l.append(tuple(map(int,input().split())))
l.sort()
for i in l:
    print(*i)
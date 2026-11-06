# -*- coding: utf-8 -*-

n=int(input())
l=list(set(map(int,input().split())))
l.sort()
print(len(l))
print(*l)
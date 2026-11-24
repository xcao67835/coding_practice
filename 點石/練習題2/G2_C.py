# -*- coding: utf-8 -*-

n=int(input())
l=[0]
for i in list(map(int,input().split())):
    l.append(l[-1]+i)
print(*l[1:])
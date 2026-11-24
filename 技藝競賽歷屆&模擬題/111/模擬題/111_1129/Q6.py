# -*- coding: utf-8 -*-

l=list(map(int,input().split(",")))
a,b=[],[]
for i in l:
    if i==0:
        b.append(i)
    else:a.append(i)

print(*a+b,sep=",")
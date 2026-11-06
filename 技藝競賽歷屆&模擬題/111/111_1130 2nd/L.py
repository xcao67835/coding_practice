# -*- coding: utf-8 -*-

n=int(input())
r=0
for i in range(1,n+1):
    a=bin(i)
    r+=a.count("1")
print(r)
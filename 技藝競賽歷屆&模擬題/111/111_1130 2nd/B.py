# -*- coding: utf-8 -*-

a,b=map(int,input().split())
n=0
while (a+n)%200!=b:
    n+=1
print(n)
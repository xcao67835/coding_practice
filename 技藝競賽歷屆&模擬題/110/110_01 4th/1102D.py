# -*- coding: utf-8 -*-

n=int(input())
l=list(map(int,input().split()))
mi=min([i for i in l if i%2==1])
s = sum(l)
if s%2==1:
    s-=mi
print(s)
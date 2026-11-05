# -*- coding: utf-8 -*-

n = int(input())
l = list(map(int,input().split()))
s=sum(l)
if s%2!=0:
    l.sort()
    l = [i for i in l if i%2==1]
    s-=l[0]
print(s)
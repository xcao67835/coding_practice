# -*- coding: utf-8 -*-
from bisect import bisect_left
l=[]
for _ in range(int(input())):
    n=int(input())
    idx=bisect_left(l, n)
    if idx==len(l):
        l.append(n)
    else:
        l.insert(idx,n)
        
        
    if len(l)%2==1:
        print(l[len(l)//2])
    else:
        print((l[len(l)//2]+l[len(l)//2-1])//2)
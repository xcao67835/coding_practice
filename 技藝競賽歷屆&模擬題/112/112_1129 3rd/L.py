# -*- coding: utf-8 -*-
from bisect import bisect_left
l=[]
for _ in range(int(input())):   
    n=int(input())
    l.insert(bisect_left(l,n), n)
    
    ll=len(l)
    if ll%2==0:
        print((l[ll//2]+l[ll//2-1])//2)
    else:
        print(l[ll//2])
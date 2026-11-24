# -*- coding: utf-8 -*-

from math import isqrt

for _ in range(int(input())):
    l=[]
    a,b=map(int,input().split())
    l.append(isqrt(a))
    while l[-1]**2<b:
        l.append(l[-1]+1)
        
    ans=len(l)
    if l[0]**2<a:
        ans-=1
    if l[-1]**2>b:
        ans-=1
    print(ans)
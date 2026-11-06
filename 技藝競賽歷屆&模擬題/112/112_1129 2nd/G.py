# -*- coding: utf-8 -*-
from math import isqrt
n=int(input())
r=set()
for i in range(1,isqrt(n)+1):
    if n%i==0:
        r.add(i)
        r.add(n//i)
        
r=sum(r)
print(r)
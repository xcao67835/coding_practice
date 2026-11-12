# -*- coding: utf-8 -*-
from math import isqrt
r=[]
n=int(input())
while n!=1:
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            r.append(i)
            n//=i
            break
    else:
        if n!=1:
            r.append(n)
            break
        
print(*r)
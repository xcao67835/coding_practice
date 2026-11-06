# -*- coding: utf-8 -*-
from math import isqrt
n=int(input())
r=[]
while n!=1:
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            r.append(i)
            n//=i
            break
    else:
        r.append(n)
        break
    
print(*r)
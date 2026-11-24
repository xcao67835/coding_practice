# -*- coding: utf-8 -*-
from math import isqrt
for i in range(int(input())):
    n=int(input())
    aaa=1
    for a in range(isqrt(n)+1):
        for b in range(a,isqrt(n)+1):
            c2=n-(a**2+b**2)
            if c2<0:
                continue
            
            c=isqrt(c2)
            if c**2+b**2+a**2==n:
                print(a,b,c)
                aaa=0
                break
        if not aaa:
            break
            
    else:
        print(-1)
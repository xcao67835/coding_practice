# -*- coding: utf-8 -*-
from math import isqrt
for _ in range(int(input())):
    n=int(input())
    d=0
    for a in range(255):
        for b in range(a,255):
            c=n-(a**2+b**2)
            if c>0:
                c=isqrt(c)
                if n==a**2+b**2+c**2:
                    print(a,b,c)
                    d=1
                    break
            
           
        if d:
            break
                
    else:
        print(-1)
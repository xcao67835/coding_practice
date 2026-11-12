# -*- coding: utf-8 -*-
from math import isqrt
for _ in range(int(input())):
    n=int(input())
    st=0
    for a in range(isqrt(n)+1):
        for b in range(a,isqrt(n)+1):
            c = n-a**2-b**2
            if c>=0 and c-isqrt(c)**2==0:
                c=isqrt(c)
                print(a,b,c)
                st=1
                break
        if st:
            break
        
    else:
        print(-1)
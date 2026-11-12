# -*- coding: utf-8 -*-
from math import isqrt
while 1:
    n=int(input())
    nn=n
    if n==0:
        break
    r=set()
    while n!=1:
        for i in range(2,isqrt(n)+1):
            if n%i==0:
                r.add(i)
                n//=i
                break
        else:
            if n!=0:
                r.add(n)
                break
            
    print(f"{nn} : {len(r)}")
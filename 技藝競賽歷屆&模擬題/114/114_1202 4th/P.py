# -*- coding: utf-8 -*-
from math import isqrt
for _ in range(int(input())):
    n=int(input())
    s=[]
    while n!=1:
        for i in range(2,isqrt(n)+1):
            if n%i==0:
                n//=i
                s.append(i)
                break
        else:
            if n!=1:
                s.append(n)
                n=1
                
    print(sum(s))
            
        
# -*- coding: utf-8 -*-
from math import isqrt
while 1:
    n=int(input())
    
    if n==0:
        break
    
    r=set()
    print(f"{n} : ",end="")
    
    while n>1:
        for i in range(2,isqrt(n)+1):
            if n%i==0:
                r.add(i)
                n//=i
                break
        
        else:
            if n!=1:
                r.add(n)
            n=1
                
    print(len(r))
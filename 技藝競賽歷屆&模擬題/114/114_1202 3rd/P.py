# -*- coding: utf-8 -*-
from math import isqrt
for _ in range(int(input())):
    n=int(input())
    if n ==1:
        print(0)
        continue
    ans=0
    while n!=1:
        for i in range(2,isqrt(n)+1):
            if n%i==0:
                ans+=i
                n//=i
                break
        else:
            if n!=1:
                ans+=n
                break
    
    print(ans)
    
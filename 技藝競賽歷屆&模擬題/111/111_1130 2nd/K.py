# -*- coding: utf-8 -*-
from math import isqrt
while 1:
    n=int(input())
    if n==0:
        break
    r=set()
    for i in range(1,isqrt(n)+1):
        if n%i==0:
            r.add(i)
            r.add(n//i)
            
    count=0
    for i in r:
        if i<2:
            continue
        for j in range(2,isqrt(i)+1):
            if i%j==0:
                break
        else:
            count+=1
            
    print(f"{n} : {count}")
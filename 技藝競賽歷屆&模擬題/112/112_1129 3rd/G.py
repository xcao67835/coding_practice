# -*- coding: utf-8 -*-
from math import isqrt
s=set()
n=int(input())
for i in range(1,isqrt(n)+1):
    if n%i==0:
        s.add(i)
        s.add(n//i)
print(sum(s))
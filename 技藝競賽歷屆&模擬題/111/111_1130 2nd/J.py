# -*- coding: utf-8 -*-
from math import isqrt
for _ in range(int(input())):
    a,b=map(int,input().split())
    for n in range(max(2,a),b+1):
        for i in range(2,isqrt(n)+1):
            if n%i==0:
                break
        else:
            print(n)
    print()
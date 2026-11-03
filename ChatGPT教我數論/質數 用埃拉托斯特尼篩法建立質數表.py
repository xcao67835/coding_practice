# -*- coding: utf-8 -*-
from math import isqrt


limit = 1000000
chartlen=isqrt(limit)+1
chart=bytearray([1])*chartlen
chart[0],chart[1] = 0,0

for i in range(2,chartlen):
    if chart[i]==1:
        for j in range(i**2, chartlen, i):
            chart[j]=0




for _ in range(int(input())):
    n = int(input())
    if n<2:
        print(False)
        continue

    for i in range(2,isqrt(n)+1):
        if chart[i]==1 and n%i==0:
            print(False)
            break
    else:
        print(True)
            
    
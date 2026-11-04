# -*- coding: utf-8 -*-

from math import gcd
for _ in range(int(input())):
    d=list(map(int,input().split(",")))
    md=1
    for i in range(len(d)):
        for j in range(i+1,len(d)):
            md = max(md, gcd(d[i], d[j]))
    print(md)
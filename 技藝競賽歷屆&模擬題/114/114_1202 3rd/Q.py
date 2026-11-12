# -*- coding: utf-8 -*-
from bisect import bisect_left, bisect_right
from math import isqrt
for _ in range(int(input())):
    a,b=map(int,input().split())
    c = list(range(isqrt(a), isqrt(b)+1))
    c= [i**2 for i in c]
    l,r=bisect_left(c, a),bisect_right(c, b)
    print(r-l)
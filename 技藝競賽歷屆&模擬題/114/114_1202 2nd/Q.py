# -*- coding: utf-8 -*-
from bisect import bisect_left, bisect_right
from math import isqrt
for _ in range(int(input())):
    a,b=map(int,input().split())
    c = [i**2 for i in range(isqrt(a), isqrt(b)+2)]
    ans = bisect_right(c, b)  - bisect_left(c, a)
    print(ans)
# -*- coding: utf-8 -*-

from bisect import bisect_left
a,b=input().split()
b=int(b)
a=list(map(int,a.split(",")))

print(bisect_left(a, b))
# -*- coding: utf-8 -*-
c=[1,2]
def fib(n):
    while n>c[-1]:
        c.append(c[-1]+c[-2])
from bisect import bisect_left, bisect_right
for _ in range(int(input())):
    a,b=map(int,input().split())
    fib(b)
    print(bisect_right(c, b) - bisect_left(c, a))
    
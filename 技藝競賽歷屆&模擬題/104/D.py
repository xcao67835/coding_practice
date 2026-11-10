# -*- coding: utf-8 -*-

from math import gcd
for _ in range(int(input())):
    ns=list(map(int,input().split(",")))
    a=gcd(*ns)
    print(a)
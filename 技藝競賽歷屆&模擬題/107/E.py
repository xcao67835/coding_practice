# -*- coding: utf-8 -*-

from math import log10
for _ in range(int(input())):
    a,b=map(int,input().split(","))
    print(1+int(log10(a)*b))
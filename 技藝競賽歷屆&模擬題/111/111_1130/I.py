# -*- coding: utf-8 -*-

from collections import Counter
l = list(input())
co = list(Counter(l).items())

co=list(map(lambda x:[ord(x[0]), x[1]], co))
co.sort(key=lambda x:(x[1], -x[0]))
for i in co:
    print(*i)
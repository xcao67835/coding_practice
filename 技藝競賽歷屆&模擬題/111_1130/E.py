# -*- coding: utf-8 -*-

from collections import Counter
a = input()
l = list(map(int,input().split()))
co = Counter(l).items()

co=sorted(co,key=lambda x:x[0])
for i in co:
    print(*i)
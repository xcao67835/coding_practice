# -*- coding: utf-8 -*-

from collections import Counter
a=input()
l=list(map(int,input().split()))
cl=list(Counter(l).items())
cl.sort()
for i in cl:
    print(*i)
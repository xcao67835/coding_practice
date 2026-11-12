# -*- coding: utf-8 -*-

from itertools import combinations
l=list(map(int,input().split(",")))
cl=combinations(l, 3)
cl=set(map(lambda x:sum(x), cl))
print(len(cl))
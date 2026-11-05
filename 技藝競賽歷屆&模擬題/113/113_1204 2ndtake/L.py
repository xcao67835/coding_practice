# -*- coding: utf-8 -*-

from itertools import permutations
n=int(input())
pn=sorted(list(permutations(range(1,1+n))), reverse=1)
for i in pn:
    print(*i,sep="")

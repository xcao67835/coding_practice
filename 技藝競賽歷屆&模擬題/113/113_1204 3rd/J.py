# -*- coding: utf-8 -*-

from itertools import permutations
n=int(input())
p = list(permutations(range(1,1+n)))
p.sort(reverse=1)
for i in p:
    print(*i,sep="")
    
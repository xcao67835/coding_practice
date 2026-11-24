# -*- coding: utf-8 -*-

from itertools import permutations
n=int(input())
p=permutations(range(1,n+1))

for i in sorted(p,reverse=1):
    print(*i,sep="")
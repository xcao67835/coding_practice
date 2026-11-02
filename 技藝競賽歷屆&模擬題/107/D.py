# -*- coding: utf-8 -*-
from itertools import permutations
for _ in range(int(input())):
    n,*l,k=list(map(int,input().split(",")))
    
    
    pl=sorted(list(permutations(l)))
    print(*pl[k-1],sep="")
# -*- coding: utf-8 -*-
from itertools import permutations
n=int(input())
np=list(permutations(range(1,1+n)))
np.sort(reverse=1)
for i in np:
    print(*i,sep="")
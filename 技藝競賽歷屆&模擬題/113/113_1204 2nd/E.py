# -*- coding: utf-8 -*-

from collections import Counter
n=int(input())
ds=list(map(int,input().split()))
cds=Counter(ds)
mcds=sorted(list(cds.items()), key=lambda x:(-x[1], x[0]))
for i in mcds:
    if i[1]==mcds[0][1]:
        print(*i)
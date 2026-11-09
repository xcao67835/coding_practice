# -*- coding: utf-8 -*-
n=int(input())
from bisect import bisect_right
l=list(map(int,input().split()))
bs=[]

ans=0
for i in l:
    idx=bisect_right(bs, i)
    ans+=len(bs)-idx
    bs.insert(idx, i)
print(ans)
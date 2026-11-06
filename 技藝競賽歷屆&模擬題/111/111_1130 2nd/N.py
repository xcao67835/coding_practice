# -*- coding: utf-8 -*-
from bisect import bisect_left
n=int(input())
best=[]
l=list(map(int,input().split()))
for i in l:
    idx=bisect_left(best, i)
    if idx==len(best):
        best.append(i)
    else:
        best[idx]=i
print(len(best))
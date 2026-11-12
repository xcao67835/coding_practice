# -*- coding: utf-8 -*-
from bisect import bisect_left
bst=[]

n=int(input())
l=list(map(int,input().split()))
for i in l:
    idx=bisect_left(bst, i)
    if idx>=len(bst):
        bst.append(i)
    else:
        bst[idx]=i
        
print(len(bst))
# -*- coding: utf-8 -*-

n=int(input())
from collections import Counter
l=list(map(int,input().split()))
cl=Counter(l)
mxl=max(cl.values())
ancl=[i[0] for i in cl.items() if i[1]==mxl]
print(*sorted(ancl))
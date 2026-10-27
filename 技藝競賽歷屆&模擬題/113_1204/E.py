# -*- coding: utf-8 -*-
from collections import Counter
n=int(input())
l=sorted(Counter(input().split()).items(),key=lambda x:(-x[1], x[0]))
m=l[0][1]
for i in l:
    if i[1]==m:
        print(*i)
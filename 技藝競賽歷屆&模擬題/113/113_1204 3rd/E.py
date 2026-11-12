# -*- coding: utf-8 -*-

from collections import Counter

n=int(input())
c=list(Counter(map(int,input().split())).items())
c.sort(key=lambda x:(-x[1], x[0]))

m=c[0][1]
for i in c:
    if i[1]==m:
        print(*i)
    else:
        break
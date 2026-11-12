# -*- coding: utf-8 -*-

from collections import Counter
n=int(input())
c = sorted(list(Counter(map(int,input().split())).items()), key=lambda x:(x[0]))

for i in c:
    print(*i)
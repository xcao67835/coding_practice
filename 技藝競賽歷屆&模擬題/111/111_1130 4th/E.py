# -*- coding: utf-8 -*-

from collections import Counter

n=int(input())
c=Counter(map(int,input().split()))

for  i in sorted(c.items()):
    print(*i)
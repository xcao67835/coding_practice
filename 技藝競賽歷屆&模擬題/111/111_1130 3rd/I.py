# -*- coding: utf-8 -*-

from collections import Counter

c = sorted(list(Counter(input()).items()), key=lambda x:(x[1], -ord(x[0])))


for a,b in c:
    print(ord(a), b)
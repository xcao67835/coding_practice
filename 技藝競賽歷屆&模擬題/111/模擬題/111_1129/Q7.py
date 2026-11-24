# -*- coding: utf-8 -*-
from collections import Counter
l=input().lower().split()

c=list(Counter(l).items())
c.sort(key=lambda x:-x[1])

if c[0][1]!=c[1][1]:
    print(*c[0])
else:
    print("No")
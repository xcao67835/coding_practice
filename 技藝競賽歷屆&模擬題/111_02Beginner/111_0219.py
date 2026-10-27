# -*- coding: utf-8 -*-
from collections import Counter
s=input()

cs=Counter(s)

c0=cs["C"]-cs["#"]-(cs["+"]//2)
c1=cs["#"]
c2=cs["+"]//2

print(c0,c2,c1,sep=",")
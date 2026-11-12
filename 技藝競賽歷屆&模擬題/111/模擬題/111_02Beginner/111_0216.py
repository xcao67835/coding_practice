# -*- coding: utf-8 -*-

from collections import Counter
ds=input().split()

cds=Counter(ds)
scds=sorted(cds.items(), key=lambda x:x[1])
print(scds[-1][0])
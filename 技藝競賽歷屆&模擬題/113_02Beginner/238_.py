# -*- coding: utf-8 -*-

from collections import Counter

s=input()
sc=Counter(s)
print(sc.most_common(1)[0][0])


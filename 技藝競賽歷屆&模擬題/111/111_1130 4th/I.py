# -*- coding: utf-8 -*-

from collections import Counter

s=input()
c=Counter(s)

s=list(c.items())
s=[[ord(i[0]), i[1]] for i in s]
s.sort(key=lambda x:(x[1],-x[0]))

for i in s:
    print(*i)
# -*- coding: utf-8 -*-

from collections import Counter
s=input()
sc=list(Counter(s).items())
sc=[(ord(i[0]), i[1]) for i in sc]
sc.sort(key=lambda x:(x[1],-x[0]))
for i in sc:
    print(*i)
# -*- coding: utf-8 -*-

from collections import Counter


inl=[]
for i in range(int(input())):
    inl.append(input().split()[0])
cinl=Counter(inl)

scinl=sorted(cinl.items(), key=lambda x:x[0])


for i in scinl:
    print(*i)

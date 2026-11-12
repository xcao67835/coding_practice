# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:30:07 2026

@author: user
"""
import itertools
s = range(1,1+int(input()))
l = list(itertools.permutations(s))[::-1]
for i in l:
    i = map(str,i)
    print("".join(i))
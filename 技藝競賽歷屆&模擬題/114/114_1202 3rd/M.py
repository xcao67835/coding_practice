# -*- coding: utf-8 -*-
from bisect import bisect_left, bisect_right
c=[1,2]
def find(x):
    while x>c[-1]:
        c.append(c[-1]+c[-2])
        
for _ in range(int(input())):
    a,b = map(int,input().split())
    find(b)
    l,r = bisect_left(c, a), bisect_right(c, b)
    print(r-l)    
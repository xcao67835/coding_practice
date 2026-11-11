# -*- coding: utf-8 -*-
from bisect import bisect_left, bisect_right
c=[1,2]
def f(x):
    while x>c[-1]:
        c.append(c[-1]+c[-2])
        
for _ in range(int(input())):
    a,b=map(int,input().split())
    f(b)
    ans = bisect_right(c, b) - bisect_left(c, a)
    
    print(ans)
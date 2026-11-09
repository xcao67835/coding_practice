# -*- coding: utf-8 -*-
from math import isqrt
from bisect import bisect_left,bisect_right
chart=[1]
for i in range(2,1001):
    for j in range(2,isqrt(i)+1):
        if i%j==0:
            break
    else:
        chart.append(i)
        
while 1:
    try:
        n,c=map(int,input().split())
        p=chart[:bisect_right(chart, n)]
        k=len(p)
        print(f"{n} {c}: ",end="")
        if k%2==0:
            if 2*c>=k:
                print(*p)
            else:
                print(*p[k//2-c: k//2+c])
        else:
            if 2*c-1>=k:
                print(*p)
            else:
                print(*p[k//2-c+1: k//2+c])
            
    except EOFError:
        break
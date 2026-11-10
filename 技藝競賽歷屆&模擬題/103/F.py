# -*- coding: utf-8 -*-
from bisect import bisect_right
chart=[0,1,1]

def f(x):
    while x>=len(chart):
        chart.append(chart[-1]+chart[-2])
    return chart[x]

f(10000)

     
def find(x):
    idx=bisect_right(chart, x)-1
    x-=chart[idx]
    if x==0:
        return [idx]
    else:
        return [idx]+find(x)
    
for i in range(int(input())):
    n=int(input())
    print(f"{n}=",end="")
    r=find(n)
    m=max(r)
    r=set(r)
    for i in range(m,1,-1):
        if i in r:
            print(1,end="")
        else:
            print(0,end="")
    print()
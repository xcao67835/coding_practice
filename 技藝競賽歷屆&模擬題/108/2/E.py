# -*- coding: utf-8 -*-
from collections import Counter
for _ in range(int(input())):
    a,b=map(int,input().split())
    l=[]
    for i in range(a):
        l.append(input())
    
    for i in zip(*l):
        a=min(Counter(i).items(),key=lambda x:(-x[1],x[0]))
        print(a[0],end="")
    print()
        
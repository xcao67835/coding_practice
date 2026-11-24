# -*- coding: utf-8 -*-

from collections import Counter
n=int(input())
c=sorted(Counter(map(int,input().split())).items(),key=lambda x:(-x[1],x[0]))
m=0
for a,b in c:
    if b>=m:
        m=b
        print(a,b)
        
    else:
        break
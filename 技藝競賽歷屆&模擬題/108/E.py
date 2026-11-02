# -*- coding: utf-8 -*-

from collections import Counter

for _ in range(int(input())):
    n,m=map(int,input().split())
    dna=[]
    for i in range(n):
        dna.append(input())
        
    for i in range(m):
        comp=[]
        for j in range(n):
            comp.append(dna[j][i])
        ccomp=Counter(comp)
        ans=min(ccomp.items(), key=lambda x:(-x[1], x[0]))
        print(ans[0],end="")
    print()
# -*- coding: utf-8 -*-
from math import isqrt
from collections import defaultdict
n,q=map(int,input().split())
l=input().split()


qs=[]
for i in range(q):
    qs.append(list(map(int,input().split()))+[i])


bl=isqrt(n)
qs.sort(key = lambda x:(x[0]//bl, x[1]))

rc=[0]*q

cts=defaultdict(int)
ct=1
left=0
right=0
cts[l[0]]=1
for a,b,idx in qs:
    while left!=a-1 or right!=b-1:
        if right<b-1:
            right+=1
            if cts[l[right]]==0:
                ct+=1
            cts[l[right]]+=1
            
        elif right>b-1:
            if cts[l[right]]==1:
                ct-=1
            cts[l[right]]-=1
            right-=1
            
        elif left<a-1:
            if cts[l[left]]==1:
                ct-=1
            cts[l[left]]-=1
            left+=1
            
        elif left>a-1:
            left-=1
            if cts[l[left]]==0:
                ct+=1
            cts[l[left]]+=1
            
    rc[idx]=ct
    
print(*rc,sep="\n")
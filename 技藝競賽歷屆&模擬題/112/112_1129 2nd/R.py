# -*- coding: utf-8 -*-
from collections import defaultdict
V=int(input())
tree=defaultdict(set)
for i in range(V-1):
    a,b=map(int,input().split())
    tree[a].add(b)
    tree[b].add(a)
    
stack=[1]
visi={1}
dr=[None]+[0]*V
md=0
mn=-1
while stack:
    node=stack.pop()
    for nx in tree[node]:
        if nx not in visi:
            visi.add(nx)
            stack.append(nx)
            dr[nx]=dr[node]+1
            if dr[nx]>md:
                md=dr[nx]
                mn=nx

stack=[mn]
visi={mn}
dr=[None]+[0]*V
md=0
while stack:
    node=stack.pop()
    for nx in tree[node]:
        if nx not in visi:
            visi.add(nx)
            stack.append(nx)
            dr[nx]=dr[node]+1
            if dr[nx]>md:
                md=dr[nx]
                
print(md)
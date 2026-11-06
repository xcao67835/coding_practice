# -*- coding: utf-8 -*-
from collections import defaultdict
V,E=map(int,input().split())
graph=defaultdict(set)

for i in range(E):
    a,b=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
    
visi=set()
r=0
for i in range(1,V+1):
    if i in visi:
        continue
    sub={i}
    stack=[i]
    while stack:
        node=stack.pop()
        for nx in graph[node]:
            if nx not in visi:
                visi.add(nx)
                sub.add(nx)
                stack.append(nx)
                
    for j in sub:
        if len(graph[j])!=2:
            break
    else:
        r+=1


print(r)
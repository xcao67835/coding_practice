# -*- coding: utf-8 -*-
from collections import defaultdict
n,m=map(int,input().split())
graph=defaultdict(list)

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    
s,g = map(int,input().split())

stack=[s]
vis=set()
while stack:
    n = stack.pop()
    if n==g:
        print("Yes")
        break
    for nx in graph[n]:
        if nx not in vis:
            vis.add(nx)
            stack.append(nx)
    
    
else:
    print("No")
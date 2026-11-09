# -*- coding: utf-8 -*-

from collections import defaultdict
V,E=map(int,input().split())
graph=defaultdict(list)
for i in range(E):
    a,b=input().split()
    graph[a].append(b)
    
    
start,goal=input().split()
visi=set()
stack=[start]
while stack:
    ct=stack.pop()
    if ct==goal:
        print("Yes")
        break
    
    for nx in graph[ct]:
        if nx not in visi:
            visi.add(nx)
            stack.append(nx)
            
else:
    print("No")
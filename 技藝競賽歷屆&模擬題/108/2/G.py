# -*- coding: utf-8 -*-
from collections import defaultdict
for _ in range(int(input())):
    V=int(input())
    E=int(input())
    color=[None]*V 
    color[0]=0
    graph=defaultdict(list)
    
    t=1
    for i in range(E):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    stack=[0]
    while stack:
        node=stack.pop()
        for nx in graph[node]:
            if color[nx] is None:
                color[nx]=1-color[node]
                stack.append(nx)
                
            elif color[nx]==color[node]:
                t=0
                break
        if not t:
            break
        
    print("T" if t else "F")
                
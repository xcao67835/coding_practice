# -*- coding: utf-8 -*-
from collections import defaultdict
n=int(input())
graph=defaultdict(list)

for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    

md=(0,0)

stack=[(1,0)]
visited={1}

while stack:
    node,d=stack.pop()
    if d>md[1]:
        md=(node,d)
        
    for nx in graph[node]:
        if nx not in visited:
            visited.add(nx)
            stack.append((nx,d+1))
            



stack=[(md[0],0)]
visited={md[0]}
md2=0
while stack:
    node,d=stack.pop()
    if d>md2:
        md2=d
        
    for nx in graph[node]:
        if nx not in visited:
            visited.add(nx)
            stack.append((nx,d+1))
            

print(md2)
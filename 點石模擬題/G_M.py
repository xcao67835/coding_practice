# -*- coding: utf-8 -*-
from collections import defaultdict
n=int(input())
graph=defaultdict(list)
for _ in range(n):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
stack=[]
for i in graph.items():
    node,link=i
    
    if len(link)==1:
        stack.append(node)
        
while stack:
    node=stack.pop()    
    links=graph[node]
    for link in links:
        graph[link].remove(node)
        
        if len(graph[link])==1:
            stack.append(link)
    
    del graph[node]
    
print(len(graph))
print(*sorted(graph.keys()))
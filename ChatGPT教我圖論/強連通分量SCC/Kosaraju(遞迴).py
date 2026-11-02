# -*- coding: utf-8 -*-

from collections import defaultdict

V,E=8,10
sides=[
(1, 2),
(2, 3),
(3, 1),
(3, 4),
(4, 5),
(5, 6),
(6, 4),
(6, 7),
(7, 8),
(8, 7)]

graph = defaultdict(lambda:{"in":[], "out":[]})
for i in sides:
    a,b=i
    graph[a]["out"].append(b)
    graph[b]["in"].append(a)
    
    
    
    
visited=set()
order = []
def dfs(node,mode):
    visited.add(node)
    
    for nxt in graph[node][mode]:
        if nxt not in visited:
            dfs(nxt,mode)
    
    order.append(node)
    
for i in range(1,V+1):
    if i not in visited:
        dfs(i,"out")
        
visited=set()
o=order.copy()
ore = []
for _ in range(V):
    i=o.pop()
    order=[]
    if i not in visited:
        dfs(i,"in")
        ore.append(order.copy())
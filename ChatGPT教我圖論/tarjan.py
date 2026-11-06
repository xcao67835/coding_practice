# -*- coding: utf-8 -*-

V,E=7,7
sides=[
(7, 7),
(0, 1),
(1, 2),
(2, 0),
(1, 3),
(3, 4),
(4, 5),
(5, 3)]

graph=[None]+[set()]*V
for a,b in sides:
    graph[a].add(b)
    graph[b].add(a)
    
low=[-1][0]*V
d=[-1][0]*V
ts=0
visited={}
def dfs(node):
    if node not in visited:
        visited.add(node)
        global ts
        d[node]=ts
        ts+=1
        for nx in graph[node]:
            d[nx]
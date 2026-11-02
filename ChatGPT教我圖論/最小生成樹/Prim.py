# -*- coding: utf-8 -*-

#import
import heapq
from collections import defaultdict
#input
"""sides = [
(0, 1, 2),
(0, 2, 6),
(0, 3, 5),
(1, 3, 3),
(2, 3, 1)
]
V,E=4,5
"""
sides = [
    (4, 0, 1),  # A-B
    (2, 0, 2),  # A-C
    (1, 1, 2),  # B-C
    (5, 1, 3),  # B-D
    (8, 2, 3),  # C-D
    (10, 2, 4), # C-E
    (2, 3, 4),  # D-E
    (6, 1, 4)   # B-E
]
V,E=5,8


#初始化
graph=defaultdict(list)
for w,a,b in sides:
    graph[a].append((w,b,a))
    graph[b].append((w,a,b))
     
root=list(graph.keys())[0]
visited={root}
heap=graph[root].copy()
heapq.heapify(heap)
cost=0
mst=[]

while heap:
    weight, node, parent = heapq.heappop(heap)
    if node not in visited:
        visited.add(node)
        cost+=weight
        mst.append((weight, parent, node))
        if len(mst)==V-1:
            break
        for i in graph[node]:
            w,n,p = i
            if n not in visited:
                
                heapq.heappush(heap, (w,n,p))

comp = True if len(mst)==V-1 else False
print(cost, len(mst), comp)
print(mst)
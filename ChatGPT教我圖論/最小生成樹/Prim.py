# -*- coding: utf-8 -*-

#import
import heapq
from collections import defaultdict
#input
sides = [
(0, 1, 2),
(0, 2, 6),
(0, 3, 5),
(1, 3, 3),
(2, 3, 1)
]
V,E=4,5


#初始化
graph=defaultdict(list)
for a,b,w in sides:
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
        mst.append((weight, node, parent))
        if len(mst)==V-1:
            break
        for i in graph[node]:
            w,n,p = i
            if n not in visited:
                
                heapq.heappush(heap, (w,n,p))

comp = True if len(mst)==V-1 else False
print(cost, len(mst), comp)
print(mst)
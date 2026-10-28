# -*- coding: utf-8 -*-
from collections import defaultdict
import heapq

for _ in range(int(input())):
    graph=defaultdict(list)
    m,n=map(int,input().split())
    sides=[]
    oridist=0
    for i in range(n):
        side=list(map(int,input().split()))
        sides.append(side)
        
        a,b,c=side
        oridist+=c
        graph[a].append((b,c))
        graph[b].append((a,c))
                        #node,cost
        
        #print(graph)
        
        
        
    mst=set([0])
    mstcost=0
    heap=[]
    for i in graph[0]:
        heapq.heappush(heap, (i[1],i[0]))
    
    while heap:
        cost,nxtnode=heapq.heappop(heap)
        if nxtnode in mst:
            continue
        mst.add(nxtnode)
        mstcost+=cost
        
        
        for i in graph[nxtnode]:
            heapq.heappush(heap, (i[1],i[0]))
    
            

            
    print(oridist-mstcost)
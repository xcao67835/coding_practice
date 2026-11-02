# -*- coding: utf-8 -*-
import heapq
dir=((0,1),(0,-1),(1,0),(-1,0))
for _ in range(int(input())):
    r=int(input())
    c=int(input())
    maze=[]
    for i in range(r):
        maze.append(list(map(int,input().split())))
    dist=[[float("inf")]*c for i in range(r)]
    dist[0][0]=maze[0][0]
    #cost, r, c
    heap=[(maze[0][0], 0, 0)]
    while heap:
        cost, rm, cm=heapq.heappop(heap)
        for aa,bb in dir:
            rn,cn=rm+aa,cm+bb
            if 0<=rn<=r-1 and 0<=cn<=c-1:
                n=dist[rm][cm]+maze[rn][cn]
                if dist[rn][cn]>n:
                    dist[rn][cn]=n
                    heapq.heappush(heap, (n, rn, cn))
                    
    print(dist[-1][-1])
            
            
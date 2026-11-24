# -*- coding: utf-8 -*-
import heapq
for _ in range(int(input())):
    grid=[]
    m=int(input())
    n=int(input())
    for i in range(m):
        grid.append(list(map(int,input().split())))
        
    dist=[[float("inf")]*n for i in range(m)]
    dist[0][0]=grid[0][0]
    
    heap=[(dist[0][0],0,0)]
    while heap:
        d,y,x=heapq.heappop(heap)
        for xx,yy in ((0,-1),(0,1),(-1,0),(1,0)):
            ny,nx=y+yy,x+xx
            if 0<=ny<m and 0<=nx<n:
                if d+grid[ny][nx]<dist[ny][nx]:
                    heapq.heappush(heap,(d+grid[ny][nx],ny,nx))
                    dist[ny][nx]=d+grid[ny][nx]
    print(dist[-1][-1])
# -*- coding: utf-8 -*-
'''
2
4
5
03129
73499
17553
23425
1
6
012345
'''
import heapq

available=((0,1),(0,-1),(1,0),(-1,0))

for _ in range(int(input())):
    heap=[]
    n=int(input())
    m=int(input())
    grid=[]
    for _ in range(n):
        grid.append(list(map(int,input().split())))
        
    heapq.heappush(heap,(grid[0][0], 0, 0))
        
    dist=[[float("inf")]*m for _ in range(n)]
    dist[0][0]=grid[0][0]
        
    available=((0,1),(0,-1),(1,0),(-1,0))
    #右 左 下 上
    while heap:
        cost,y,x=heapq.heappop(heap)
        if cost>dist[y][x]:
            continue
        for ya,xa in available:
            
            if 0<=(y+ya)<=n-1 and 0<=(x+xa)<=m-1:
                
                
                
                if cost + grid[y+ya][x+xa] < dist[y+ya][x+xa]: 
                    dist[y+ya][x+xa] = cost + grid[y+ya][x+xa]
                    heapq.heappush(heap, (cost + grid[y+ya][x+xa], y+ya, x+xa))
                    
    print(dist[-1][-1])
                    
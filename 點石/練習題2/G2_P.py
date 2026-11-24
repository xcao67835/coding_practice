# -*- coding: utf-8 -*-

from collections import deque
for _ in range(int(input())):
    n,m,a1,a2,b1,b2=map(int,input().split())
    a1-=1
    a2-=1
    b1-=1
    b2-=1
    grid=[]
    for i in range(n):
        grid.append(list(input()))
    if grid[a1][a2]=="1":
        print(0)
    
    else:
        grid[a1][a2]="1"
        
        dist=[[0]*m for i in range(n)]
        dist[a1][a2]=1
        q=deque([(a1,a2,1)])
        while q:
            i,j,d=q.popleft()
            for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
                x,y=j+dx,i+dy
                if 0<=y<n and 0<=x<m:
                    if grid[y][x]=="0":
                        q.append((y,x,d+1))
                        dist[y][x]=d+1
                        grid[y][x]="1"
                        
        print(dist[b1][b2])
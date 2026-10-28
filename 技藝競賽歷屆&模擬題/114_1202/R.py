''# -*- coding: utf-8 -*-
"""
Sample Input 1
3 4
0 7 8 9
1 5 1 1
2 4 10 0

Sample Output 1
8
"""
import heapq



maze=[]
n,m=map(int,input().split())
for _ in range(n):
    maze.append(list(map(int,input().split())))
    
dist=[[float("inf")]*m for i in range(n)]
dist[0][0]=maze[0][0]
q=[(dist[0][0],0,0)]
search=((0,1),(1,0))
while q:
    cost,y,x=heapq.heappop(q)
    for yd,xd in search:
        if 0<=x+xd<=m-1 and 0<=y+yd<=n-1:
            if dist[y+yd][x+xd]>cost+maze[y+yd][x+xd]:
                dist[y+yd][x+xd]=cost+maze[y+yd][x+xd]
                heapq.heappush(q, (cost+maze[y+yd][x+xd], y+yd, x+xd))
                
print(dist[-1][-1])
    
''
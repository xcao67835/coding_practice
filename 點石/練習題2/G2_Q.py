from collections import deque

n,m=map(int,input().split())
grid=[]
for i in range(n):
    grid.append(list(input()))
if grid[0][0]=="#":
    print(-1)
else:
    
    dist=[[-1]*m for i in range(n)]
    dist[0][0]=0
    q=deque([(0,0,0)])
    while q:
        i,j,d=q.popleft()
        for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
            x,y=j+dx,i+dy
            if 0<=y<n and 0<=x<m:
                if grid[y][x]==".":
                    q.append((y,x,d+1))
                    dist[y][x]=d+1
                    grid[y][x]="#"
                    
    print(dist[-1][-1])
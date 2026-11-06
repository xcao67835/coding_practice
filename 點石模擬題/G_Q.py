# -*- coding: utf-8 -*-

n,m=map(int,input().split())
graph=[None]+[set() for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

    
low,times,iscut=[None]+[float("inf")]*n, [None]+[-1]*n, [0]+[0]*n
t=0
visi=set()
def dfs(node, parent=False):
    visi.add(node)
    global t
    times[node]=t
    t+=1
    
    count=0
    for nx in graph[node]:
        if nx == parent:
            continue
        if nx not in visi:
            visi.add(nx)
            count+=1
            dfs(nx, node)
            if low[nx]>=times[node] and parent:
                iscut[node]=1
            low[node]=min(low[node], low[nx])
        else:
            low[node]=min(low[node], times[nx])
    
    if parent==False and count>1:
        iscut[node]=1

for i in range(1,1+n):
    if i not in visi:
        dfs(i)
        
print(sum(iscut))
for i in range(1,1+n):
    if iscut[i]:
        print(i,end=" ")
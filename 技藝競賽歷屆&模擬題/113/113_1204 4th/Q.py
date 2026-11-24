# -*- coding: utf-8 -*-

n=int(input())
tree=[None]+[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
stack=[(1,0)]
dr1=[None]+[0]*n
visited={1}

while stack:
    node,d=stack.pop()
    dr1[node]=d
    
    for nx in tree[node]:
        if nx not in visited:
            visited.add(nx)
            stack.append((nx,d+1))
            
            
mxd=max(dr1[1:])
d1=dr1.index(mxd)
stack=[(d1,0)]
dr2=[None]+[0]*n
visited={d1}

while stack:
    node,d=stack.pop()
    dr2[node]=d
    
    for nx in tree[node]:
        if nx not in visited:
            visited.add(nx)
            stack.append((nx,d+1))
            
            
mxd=max(dr2[1:])
d2=dr2.index(mxd)
stack=[(d2,0)]
dr3=[None]+[0]*n
visited={d2}

while stack:
    node,d=stack.pop()
    dr3[node]=d
    
    for nx in tree[node]:
        if nx not in visited:
            visited.add(nx)
            stack.append((nx,d+1))
            
for i in range(1,n+1):
    print(max(dr2[i],dr3[i]),end=" ")
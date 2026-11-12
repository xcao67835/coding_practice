# -*- coding: utf-8 -*-
from collections import defaultdict
n=int(input())
tree=defaultdict(list)
for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
    
stack=[(1, 0)]
dist=[]
for i in range(3):
    dist.append({})
    visi=set()
    visi.add(stack[-1][0])
    while stack:
        node,d=stack.pop()
        dist[i][node]=d
        
        for nx in tree[node]:
            if nx not in visi:
                visi.add(nx)
                stack.append((nx,d+1))
                
                
    if i<=1:
        td = list(dist[i].items())
        stack = [(max(td, key = lambda x:x[1])[0],0)]

for i in range(1,1+n):
    print(max(dist[1][i], dist[2][i]), end=" ")
# -*- coding: utf-8 -*-
from collections import defaultdict
n=int(input())
tree=defaultdict(list)
for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
dr=[[0]*(n+1) for i in range(2)]
stack=[(1,0)]
for i in (0,1):
    visi=set()
    visi.add(stack[-1][0])
   
    while stack:
        node,dis=stack.pop()
        dr[i][node]=dis
        
        for nx in tree[node]:
            if nx not in visi:
                visi.add(nx)
                stack.append((nx,dis+1))
                
    stack.append((dr[0].index(max(dr[0])), 0))
                

print(max(dr[1]))
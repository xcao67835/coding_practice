# -*- coding: utf-8 -*-
from collections import defaultdict
V,E=map(int,input().split())
edges=[]
deg=defaultdict(int)
parent={}
for i in range(E):
    a,b=map(int,input().split())
    edges.append((a,b))
    deg[a]+=1
    deg[b]+=1
    parent[a]=a
    parent[b]=b
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    
    a,b=find(x),find(y)
    if a!=b:
        parent[a]=b
        
for a,b in edges:
    union(a,b)
for key in parent.keys():
    find(key)
    
found=defaultdict(lambda:True)

ans=0
for k,v in list(parent.items()):
    if v not in found:
        found[v]=True
    if deg[k]!=2:
        found[v]=False
        
for i in found.values():
    if i:
        ans+=1
        
print(ans)
        
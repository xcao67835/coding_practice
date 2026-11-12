# -*- coding: utf-8 -*-
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    a,b=find(x),find(y)
    if a!=b:
        parent[a]=b


for _ in range(int(input())):
    V,E=map(int,input().split())
    sides=[]
    for i in range(E):
        sides.append(tuple(map(int,input().split())))
    sides.sort(key=lambda x:x[-1])
    
    ans=0
    parent=[i for i in range(V)]
    
    for a,b,c in sides:
        if find(a)==find(b):
            ans+=c
        else:
            union(a,b)
            
    print(ans)
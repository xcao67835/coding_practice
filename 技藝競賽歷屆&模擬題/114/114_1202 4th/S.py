# -*- coding: utf-8 -*-
parent=[]
def find(x):
    if parent[x]!=x:
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
        parent=[i for i in range(V)]
        a,b,c=map(int,input().split())
        sides.append((c,a,b))
        
    save=0
    sides.sort()
    for c,a,b in sides:
        if find(a)!=find(b):
            union(a,b)
        else:
            save+=c
            
    print(save)
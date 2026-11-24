# -*- coding: utf-8 -*-
parent=[]
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    a,b=find(x),find(y)
    if a!=b:
        parent[b]=a
for ii in range(int(input())):
    n=int(input())
    parent=[i for i in range(n)]
    edges=[]
    for i in range(n):
        l=list(map(int,input().split(",")))
        for j in range(i+1,n):
            if l[j]!=0:
                edges.append((l[j],i,j))
    edges.sort()
    r=[]
    for c,b,a in edges:
        if find(b)!=find(a):
            union(a,b)
            if a>b:
                a,b=b,a
            r.append((a,b,c))
            
    r.sort(key=lambda x:(x[2],x[0],x[1]))
    
    print(f"Case {ii+1}:")
    for a,b,c in r:
        print(f"{chr(65+a)}-{chr(65+b)} {c}")
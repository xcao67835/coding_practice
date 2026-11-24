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
        
n,m=map(int,input().split())
e=[]
for i in range(m):
    e.append(tuple(map(int,input().split())))
parent=[i for i in range(n)]
e.sort(key=lambda x:x[2])
ans=0
for a,b,c in e:
    if find(a)!=find(b):
        union(a,b)
        ans+=c
print(ans)
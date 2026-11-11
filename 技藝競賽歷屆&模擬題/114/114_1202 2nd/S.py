# -*- coding: utf-8 -*-


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    a,b = find(x), find(y)
    if a!=b:
        parent[a]=b
        
        
for _ in range(int(input())):
    m,n=map(int,input().split())
    parent=[i for i in range(m)]
    sides=[]
    
    for i in range(n):
        a,b,w=map(int,input().split())
        sides.append((a,b,w))
                
    sides.sort(key=lambda x:x[-1])
    
    ans=0
    for a,b,w in sides:
        if find(a)==find(b):
            ans+=w
        else:
            union(a,b)
            
    print(ans)
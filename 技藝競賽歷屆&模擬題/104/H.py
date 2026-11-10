#from collections import defaultdict
parent=None
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    a,b=find(x), find(y)
    if a!=b:
        parent[a]=b




for _ in range(int(input())):
    parent=dict()
    l=input().split()
    sides=[]
    for i in l:
        a,b,w = i.split(",")
        parent[a]=a
        parent[b]=b
        sides.append((w,a,b))
    
    sides.sort(key=lambda x:int(x[0]))
    
    cost=0
    for w,a,b in sides:
        if find(a)!=find(b):
            cost+=int(w)
            union(a,b)
            
    print(cost)
    
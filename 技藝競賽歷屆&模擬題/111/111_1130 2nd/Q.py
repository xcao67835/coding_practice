# -*- coding: utf-8 -*-
n=int(input())
tree=[set() for i in range(n)]
dg=[0]*n
pr=[-1]*n
de=[0]*n
hi=[0]*n
for i in range(n):
    r,a,b=map(int,input().split())
    if a!=-1:
        tree[r].add(a)
        pr[a]=r
        dg[r]+=1
    if b!=-1:
        tree[r].add(b)
        dg[r]+=1
        pr[b]=r
for i in range(n):
    if pr[i]==-1:
        root=i
visi={root}
def fde(root, d):
    de[root]=d
    for i in tree[root]:
        if i not in visi:
            visi.add(i)
            fde(i,d+1)
            
fde(root,0)
        
visi={root}
def fhi(v):
    if len(tree[v])==0:
        hi[v]=0
        return 0
    h=0
    for i in tree[v]:
        if i not in visi:
            visi.add(i)
            h=max(h,fhi(i)+1)
    
    hi[v]=h
    return h
fhi(root)

for i in range(n):
    print(f"node {i}: parent = {pr[i]}, degree = {dg[i]}, depth = {de[i]}, height = {hi[i]},")
# -*- coding: utf-8 -*-

n=int(input())
tree=[]
parent = [-1]*n
degree = [999]*n
depth = [999]*n
height = [999]*n
for i in range(n):
    a,b,c=map(int,input().split())
    tree.append((b,c))
    d=0
    if b!=-1:
        parent[b]=a
        d+=1
    if c!=-1:
        parent[c]=a
        d+=1
    degree[a]=d
        
def fh(root=0):
    h=-1
    if tree[root][0]!=-1:
        h=max(h,fh(tree[root][0]))
    if tree[root][1]!=-1:
        h=max(h,fh(tree[root][1]))
    height[root]=h+1
    return h+1
fh()

def fd(root=0,d=0):
    depth[root]=d
    if tree[root][0]!=-1:
        fd(tree[root][0],d+1)
    if tree[root][1]!=-1:
        fd(tree[root][1],d+1)
fd()


for i in range(n):
    print(f"node {i}: parent = {parent[i]}, degree = {degree[i]}, depth = {depth[i]}, height = {height[i]},")
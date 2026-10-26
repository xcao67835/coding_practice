# -*- coding: utf-8 -*-
from collections import defaultdict
n = int(input())
tree=defaultdict(lambda:defaultdict(lambda:-1))
for i in range(n):
    a,b,c=map(int,input().split())
    tree[a]["child"]=[b,c]
    if b!=-1:
        tree[b]["parent"]=a
    if c!=-1:
        tree[c]["parent"]=a
    
def height_calc(node):
    now = tree[node]
    if node==-1:
        return
    #try:
    if tree[now["child"][0]]==-1 and tree[now["child"][1]]==-1:
        return 0
    #except:
    #    print(node)
    #    print(now["child"])
    #    print(now["child"][0])
    else:
        height_l=tree[now["child"][0]]["height"]
        
        if height_l==-1:
            tree[now["child"][0]]["height"] = height_calc(now["child"][0])
            height_l=tree[now["child"][0]]["height"]
        if height_l==None:
            height_l=-1
        height_r=tree[now["child"][1]]["height"]
        
        if height_r==-1:
            tree[now["child"][1]]["height"] = height_calc(now["child"][1])
            height_r=tree[now["child"][1]]["height"]
        if height_r==None:
            height_r=-1
        
        return max(height_l,height_r)+1
    
def depth_calc(node):

    now = tree[node]
    if now["parent"]==-1:
        return 0
    else:
        parent = tree[now["parent"]]
        if parent["depth"]==-1:
            parent["depth"] = depth_calc(now["parent"])
        return parent["depth"]+1

    
for i in range(n):
    tree[i]["degree"]=2-(tree[i]["child"].count(-1))
    if tree[i]["height"]==-1:
        tree[i]["height"]=height_calc(i)
    if tree[i]["depth"]==-1:
        tree[i]["depth"]=depth_calc(i)
    print(f"node {i}: ", end="")
    print(f"parent = {tree[i]['parent']}, ", end="")
    print(f"degree = {tree[i]['degree']}, ", end="")
    print(f"depth = {tree[i]['depth']}, ", end="")
    print(f"height = {tree[i]['height']},")

"""
6
0 3 -1
3 4 -1
4 1 2
2 -1 -1
1 5 -1
5 -1 -1
"""

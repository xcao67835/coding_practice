# -*- coding: utf-8 -*-
from collections import defaultdict
t=defaultdict(dict)
t[0]={"p":-1}
n=int(input())

for i in range(n):
    a,b,c=map(int,input().split())
    t[b]["p"]=a
    t[c]["p"]=a
    t[a]["c"]=(b,c)
    
de=[0]*n
he=[0]*n
def fd(n,d=0):
    de[n]=d
    for nx in t[n]["c"]:
        if nx !=-1:
            fd(nx, d+1)
        
def fh(n):
    if t[n]["c"]==(-1,-1):
        he[n]=0
        return 0
    
    mh=0
    for nx in t[n]["c"]:
        if nx!=-1:
            mh=max(mh, fh(nx))
    he[n]=mh+1
    return mh+1


fd(0)
fh(0)
for i in range(n):
    print(f'node {i}: parent = {t[i]["p"]}, degree = {len(t[i]["c"])-t[i]["c"].count(-1)}, depth = {de[i]}, height = {he[i]},')
# -*- coding: utf-8 -*-
from collections import deque
def par(i):
    if i==0:
        return  -1
    else:
        return (i-1)//2
def chi(i):
    return (i*2+1, i*2+2)    
    
for _ in range(int(input())):
    tree=input()[1:-1].split(",")
    
    q=deque([(0, 0)])
    visited=set()
    visited.add(0)
    dr=[float("-inf")]*len(tree)
    dr[0]=0
    while q:
        tind,dis=q.popleft()
        conn=[par(tind)]+list(chi(tind))
        
        for i in conn:
            if i<len(tree):
                if tree[i].isdigit():
                    if i not in visited:
                        visited.add(i)
                        

                        dr[i]=dis+1
                        q.append((i, dis+1))
    #print(dr)
    ml=max(dr)
    mlind=dr.index(ml)
    
    
    q=deque([(mlind, 0)])
    visited=set()
    visited.add(mlind)
    dr=[float("-inf")]*len(tree)
    dr[mlind]=0
    while q:
        tind,dis=q.popleft()
        conn=[par(tind)]+list(chi(tind))
        
        for i in conn:
            if i<len(tree):
                if tree[i].isdigit():
                    if i not in visited and i!=-1:
                        visited.add(i)
                        

                        dr[i]=dis+1
                        q.append((i, dis+1))
                        
    print(max(dr))
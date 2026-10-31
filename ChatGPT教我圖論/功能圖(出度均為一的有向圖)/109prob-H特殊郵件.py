# -*- coding: utf-8 -*-
from collections import deque
#input
for _ in range(int(input())):
    V=int(input())
    nodes=set([i for i in range(1,1+V)])
    nxt=[None]+[None]*V
    for i in range(V):
        a,b=map(int,input().split())
        nxt[a]=b
        
    inde=[None]+[0]*V
    for i in nxt[1:]:
        inde[i]+=1
     
    #indegree peeling
    q=deque()
    for i in range(1,V+1):
        if inde[i]==0:
            q.append(i)
    rem=[]
    while q:
        n=q.popleft()
        rem.append(n)
        nx=nxt[n]
        inde[nx]-=1
        if inde[nx]==0:
            q.append(nx)
            
    #搜尋loop +計算最多數量
    inloop=nodes-set(rem)
    
    countrec=[None]+[0]*V
    while inloop:
        now=next(iter(inloop))
        loop=set()
        while 1:
            if now not in loop:
                loop.add(now)
                nx=nxt[now]
                now=nx
            else:
                break
            
        inloop=inloop-loop
        for i in loop:
            countrec[i]=len(loop)
            
    while rem:
        node=rem.pop()
        countrec[node] = countrec[nxt[node]]+1
        
        
        
    mx=max(countrec[1:])
    print(countrec.index(mx))
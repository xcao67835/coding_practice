# -*- coding: utf-8 -*-
from collections import defaultdict
v,e=map(int,input().split())
graph=defaultdict(list)
dg=defaultdict(int)
for i in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    dg[a]+=1
    dg[b]+=1
    
visi=set()
ans=0
for k in graph:
    if k not in visi:
        visi.add(k)
        stack=[k]
        small={k}
        while stack:
            node=stack.pop()
            for nx in graph[node]:
                if nx not in visi:
                    visi.add(nx)
                    small.add(nx)
                    stack.append(nx)
                    

        for n in small:
            if dg[n]!=2:
                break
        else:
            ans+=1
    


print(ans)
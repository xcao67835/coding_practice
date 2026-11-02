# -*- coding: utf-8 -*-
from collections import defaultdict
for _ in range(int(input())):
    can=True
    v=int(input())
    e=int(input())
    vs=[-1 for i in range(v)]
    vs[0]=False
    graph=defaultdict(list)
    
    for i in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    stack=[0]
    while stack:
        if not can:
            break
        nod=stack.pop()
        for con in graph[nod]:
            #print(vs[nod], vs[con])
            if vs[con]!=-1:
                if vs[nod]==vs[con]:
                    can=False
                    break
                
            else:
                vs[con]=False if vs[nod] else True
                stack.append(con)
    print("T" if can else "F")
                    
# -*- coding: utf-8 -*-
"""
6 6  #n,m

1 3
2 3
3 4
1 5
5 4
4 6
"""
n,m=map(int,input().split())
graph=dict()
for i in range(1,1+n):
    graph[i]={"child":[],"requirement":0,"latest":1}
for _ in range(m):
    a,b=map(int,input().split())
    
    graph[a]["child"].append(b)
    graph[b]["requirement"]+=1
    
    
#[(proj, seme)*n]
stack=[]
for i in range(1,1+n):
    if graph[i]["requirement"]==0:
        stack.append((i,1))
        
visited=set()
while stack:
    proj, seme=stack.pop()
    
    if proj not in visited:
        visited.add(proj)
        
        for  nxt in graph[proj]["child"]:
            
            graph[nxt]["requirement"]-=1
            graph[nxt]["latest"]=max(graph[nxt]["latest"], seme+1)
            if graph[nxt]["requirement"]==0:
                stack.append((nxt,graph[nxt]["latest"]))
                

mreq=max([i["requirement"] for i in graph.values()])
if mreq!=0:
    print(-1)
else:
    mlate=max([i["latest"] for i in graph.values()])
    print(mlate)
# -*- coding: utf-8 -*-
V,E=5,5
graph = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4, 5],
    4: [1, 3],
    5: [3]
}

for i in graph.items():
    if len(i[1])%2==1:
        start=i[0]
        break
else:
    start=list(graph.keys())[0]
    
stack=[start]
path=[]
while stack:
    node = stack[-1]
    
    
    if len(graph[node])==0:
        path.append(stack.pop())
        continue
    
    nxt = graph[node][-1]
    graph[node].remove(nxt)
    graph[nxt].remove(node)
    stack.append(nxt)

    
    
    
    
    
    
    
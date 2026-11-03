'''# -*- coding: utf-8 -*-
from collections import defaultdict
for _ in range(int(input())):
    inp=input().split()
    E=len(inp)
    inp = [i.split(",") for i in inp]
    graph = defaultdict(list)
    
    for a,b in inp:
        graph[a].append(b)
        graph[b].append(a)
    
    V = len(graph)
    stack=[inp[0][0]]
    visi={stack[-1]}
    while stack:
        node = stack.pop()
        for i in graph[node]:
            if i not in visi:
                visi.add(i)
                stack.append(i)
    
    stack=[]
    for i in graph.items():
        if len(i[-1])<=1:
            stack.append(i[0])
            
    while stack:
        node = stack.pop()
        if graph[node]:
            nxt=graph[node][0]
            graph[nxt].remove(node)
            if len(graph[nxt])<=1:
                stack.append(nxt)
            
        del graph[node]
        
       
            
    ans=sorted(list(graph.keys()))
    
    
    if ans:
        print(*ans,sep=", ")
    elif len(visi)!=V:
        print("F")
    elif V-E==1:
        print("T")
    else:
        print("F")
        '''
                    
                    
# -*- coding: utf-8 -*-
from collections import defaultdict
for _ in range(int(input())):
    inp=input().split()
    E=len(inp)
    inp = [i.split(",") for i in inp]
    graph = defaultdict(list)
    
    for a,b in inp:
        graph[a].append(b)
        graph[b].append(a)
    
    V = len(graph)
    stack=[inp[0][0]]
    visi={stack[-1]}
    while stack:
        node = stack.pop()
        for i in graph[node]:
            if i not in visi:
                visi.add(i)
                stack.append(i)
        
    
            
    ans=sorted(list(graph.keys()))
    
    
    if len(visi)!=V:
        print("F")
    elif V==E:
        stack=[]
        for i in graph.items():
            if len(i[-1])<=1:
                stack.append(i[0])
                
        while stack:
            node = stack.pop()
            if graph[node]:
                nxt=graph[node][0]
                graph[nxt].remove(node)
                if len(graph[nxt])<=1:
                    stack.append(nxt)
                
            del graph[node]
            
           
                
        ans=sorted(map(int,list(graph.keys())))
        print(*ans,sep=", ")
    
    elif V==E+1:
        print("T")
    else:
        print("F")
        
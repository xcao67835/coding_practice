# -*- coding: utf-8 -*-

from collections import defaultdict

V,E=8,10
sides=[
(1, 2),
(2, 3),
(3, 1),
(3, 4),
(4, 5),
(5, 6),
(6, 4),
(6, 7),
(7, 8),
(8, 7)]

graph = defaultdict(lambda:{"in":[], "out":[]})
for i in sides:
    a,b=i
    graph[a]["out"].append(b)
    graph[b]["in"].append(a)
    
    
    
    
visited=set()
discovered=set()
order=[]

for i in range(1,V+1):
    if i not in visited:
        stack=[(i, 0)]
        discovered.add(i)
        while stack:
            node, status = stack.pop()
           
            
            if status==1:
                order.append(node)
                continue
            
            if node in visited:
                continue
            visited.add(node)
            stack.append((node, 1))
            
            for j in graph[node]["out"]:
                if j not in discovered:
                    stack.append((j, 0))
                    discovered.add(j)
                    
allSCC=[]
visited=set()
stack=[]
for i in order[::-1]:
    if i not in visited:
        visited.add(i)
        SCC=set()
        SCC.add(i)
        
        stack.append(i)
        
        while stack:
            
            node = stack.pop()
            print(node)
            for j in graph[node]["in"]:
                if j not in visited:
                    visited.add(j)
                    SCC.add(j)
                    stack.append(j)
                    
        allSCC.append(SCC)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: 我去，是吳奇隆 -*-
        
n1 ,n2 = 5,5
cando=[
(3, 1, 2, 3),
(2, 1, 2),
(2, 2, 3),
(2, 3, 4),
(2, 4, 5)
]
graph=[]
for i in cando:
    graph.append(i[1:])
    
    
match = [-1]*n2
ans=0

def dfs(man):
    for work in graph[man]:
        if work-1 in visited:
            continue
        
        visited.add(work-1)
        
        if match[work-1]==-1:
            match[work-1] = man
            return True
        
        if dfs(match[work-1]):
            match[work-1] = man
            return True

    return False


for i in range(n1):
    visited=set()
    if dfs(i):
        ans+=1
        
print(ans)
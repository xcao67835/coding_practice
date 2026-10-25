# -*- coding: utf-8 -*-

from collections import defaultdict
d = defaultdict(list)

m,n=map(int,input().split())
for _ in range(n):
    a,b = map(int,input().split())
    if b not in d[a]:
        d[a].append(b)
    if a not in d[b]:
        d[b].append(a)
#print(d)
    
ans=0

visited = set()
for i in range(1,1+m):
    if i not in visited:
        nodes=[]
        stack=[i]
        while stack:
            nodes.append(stack.pop())
            nownode = d[nodes[-1]]
            visited.add(nodes[-1])
            for j in nownode:
                if j not in visited:
                    stack.append(j)
        
        for k in nodes:
            if len(d[k])!=2:
                break
        else:
            ans+=1
            
print(ans)
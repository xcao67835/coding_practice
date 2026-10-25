# -*- coding: utf-8 -*-
from collections import defaultdict,deque

n = int(input())
tree = defaultdict(list)
while 1:
    try:
        tmp=input()
        if not tmp:
            break
        a,b = map(int,tmp.split())
        tree[a].append(b)
        tree[b].append(a)
    except EOFError:
        break
farest=None
for j in [1,0]:
    visited=set()
    dis={0:-1}
    if j:
        #parentdis,node
        stack=deque([[-1,1]])
    else:
        stack=deque([[-1,farest]])
    while stack:
        parentdis,node = stack.popleft()
        if node in visited:
            continue
        else:
            visited.add(node)
            dis[node]=parentdis+1
            nextnodes=tree[node]
            for i in nextnodes:
                stack.append([dis[node],i])
    

    farest=max(dis.items(),key=lambda x:x[1])[0]
print(dis[farest])
        
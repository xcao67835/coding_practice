# -*- coding: utf-8 -*-
from collections import defaultdict,deque




n=int(input())
tree=defaultdict(list)
for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def finddist(tree, node):
    visited = set()
    q = deque([(node, 0)])
    distrec=dict()
    while q:
        now,nowdist=q.popleft()
        visited.add(now)
        distrec[now]=nowdist
        nxt=tree[now]
        for g in nxt:
            if g not in visited:
                q.append((g, nowdist+1))
                
    return distrec    
dists_root = finddist(tree, 1)

node2r_1=max(dists_root.items(),key=lambda x:x[1])[0]
dist_node2r_1 = finddist(tree, node2r_1)

node2r_2=max(dist_node2r_1.items(),key=lambda x:x[1])[0]
dist_node2r_2 = finddist(tree, node2r_2)

for i in range(1,1+n):
    print(max(dist_node2r_1[i],dist_node2r_2[i]), end=" ")
    
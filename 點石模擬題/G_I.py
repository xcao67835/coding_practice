# -*- coding: utf-8 -*-
from collections import defaultdict
for _ in range(int(input())):
    tree=defaultdict(list)
    n,k=map(int,input().split())
    hiverec=list(map(int,input().split()))
    for i in range(n-1):
        t1,t2=map(int,input().split())
        tree[t1].append(t2)
        tree[t2].append(t1)
        
        
    fruits=0
    stack=[(1,0)]
    visited=set()
    visited.add(1)
    if n==1:
        stack=0
    while stack:
        node,endur=stack.pop()
        benchcount=0

        for i in tree[node]:
            if i not in visited:
                visited.add(i)
                benchcount+=1
                if hiverec[i-1]==0:
                    stack.append((i,0))
                    
                else:
                    if endur+1<=k:
                        stack.append((i,endur+1))

        if not benchcount:

            fruits+=1

                
            
    print(fruits)
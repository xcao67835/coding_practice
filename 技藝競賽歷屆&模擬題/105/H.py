# -*- coding: utf-8 -*-
import heapq
for _ in range(int(input())):
    ori=input().split(",")
    ch=list(map(lambda x:[int(x), 1, [int(x)]],ori))
    heapq.heapify(ch)
    
    while len(ch)!=1:
        a=heapq.heappop(ch)
        b=heapq.heappop(ch)
        
        heapq.heappush(ch, [a[0]+b[0], 2, [a[2], b[2]]])
        
    d = {}
    stack = [[ch[0][2], 0]]
    while stack:
        
        a=stack.pop()
        if len(a[0])==1:
            d[a[0][0]]=a[1]
        else:
            for i in a[0]:
                stack.append([i, a[1]+1])
                
    ans=[]
    for i in ori:
        ans.append(d[int(i)])
    print(*ans, sep=",")
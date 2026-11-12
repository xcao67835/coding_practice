# -*- coding: utf-8 -*-

import heapq

while 1:

    n=int(input())
    
    if n==0:
        break
    l=list(map(int,input().split()))
    heapq.heapify(l)
    ans=0
    while len(l)!=1:
        a,b=heapq.heappop(l),heapq.heappop(l)
        ans+=a+b
        heapq.heappush(l, a+b)
        
    print(ans)

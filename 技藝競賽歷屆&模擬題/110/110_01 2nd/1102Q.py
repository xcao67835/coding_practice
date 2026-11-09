# -*- coding: utf-8 -*-
import heapq
ans=0
n=int(input())
l=list(map(int,input().split()))
heapq.heapify(l)
while len(l)!=1:
    a,b=heapq.heappop(l),heapq.heappop(l)
    heapq.heappush(l, a+b)
    ans+=a+b
    
print(ans)
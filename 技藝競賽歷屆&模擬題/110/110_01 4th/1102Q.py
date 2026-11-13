# -*- coding: utf-8 -*-
import heapq
n=int(input())
l=list(map(int,input().split()))
heapq.heapify(l)

r=0
while len(l)!=1:
    a,b=heapq.heappop(l),heapq.heappop(l)
    r+=a+b
    heapq.heappush(l,a+b)
    
print(r)
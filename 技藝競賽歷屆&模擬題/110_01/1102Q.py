# -*- coding: utf-8 -*-
import heapq
n = int(input())
l = list(map(int,input().split()))
heapq.heapify(l)
an=0
while len(l)!=1:

    a,b=heapq.heappop(l),heapq.heappop(l)
    heapq.heappush(l, a+b)
    an+=a+b
    
print(an)
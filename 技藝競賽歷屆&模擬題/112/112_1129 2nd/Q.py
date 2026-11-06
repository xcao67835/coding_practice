# -*- coding: utf-8 -*-
import heapq
while 1:
    n=int(input())
    if not n:
        break
    
    l=list(map(int,input().split()))
    heapq.heapify(l)
    c=0
    while len(l)!=1:
        a,b=heapq.heappop(l),heapq.heappop(l)
        c+=a+b
        heapq.heappush(l, a+b)
        
    print(c)
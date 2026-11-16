# -*- coding: utf-8 -*
import heapq

while 1:
    n=int(input())
    if n==0:
        break
    
    l=list(map(int,input().split()))
    heapq.heapify(l)
    a=0
    while len(l)>1:
        b,c=heapq.heappop(l),heapq.heappop(l)
        a+=b+c
        heapq.heappush(l, b+c)
        
    print(a)
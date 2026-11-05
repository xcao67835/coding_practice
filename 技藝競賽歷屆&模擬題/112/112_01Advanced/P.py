# -*- coding: utf-8 -*-
import heapq
n=int(input())
inp=list(map(int,input().split()))
merge=[(i,1) for i in inp]
heapq.heapify(merge)


ans=0

while len(merge)!=1:
    a=heapq.heappop(merge)
    b=heapq.heappop(merge)
    
    incre=a[1]+b[1]
    ans+=incre
    
    heapq.heappush(merge, (a[0]+b[0], incre))
    
print(ans)
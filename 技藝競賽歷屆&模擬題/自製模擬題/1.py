# -*- coding: utf-8 -*-
import heapq
#n,k=map(int,input().split())
n,k=3,3
#l=list(map(int,input().split()))
l=[2,-1,3]
pfx=[0]

for i in l:
    pfx.append(pfx[-1]+i)
    
minheap=[0]
maxheap=[]
ans=0
for i in range(n+1):
    while minheap and pfx[i]<minheap[0]:
        heapq.heappush(maxheap, -heapq.heappop(minheap))
    while maxheap and pfx[i]>=-maxheap[0]:
        heapq.heappush(minheap, -heapq.heappop(maxheap))
    ans+=len(maxheap)
    heapq.heappush(minheap,k-pfx[i])
print(ans)
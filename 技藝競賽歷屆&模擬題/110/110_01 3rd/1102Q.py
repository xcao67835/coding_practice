import heapq

n=input()
l=list(map(int,input().split()))
tc=0
heapq.heapify(l)
while len(l)!=1:
    a,b=heapq.heappop(l),heapq.heappop(l)
    tc+=a+b
    heapq.heappush(l, a+b)
    
print(tc)
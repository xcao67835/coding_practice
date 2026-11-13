# -*- coding: utf-8 -*-

n=int(input())
l=list(map(int,input().split()))

dp=[1]+[0]*sum(l)
for c in l:
    for i in range(len(dp)-1,0,-1):
        if i-c>=0:
            if dp[i-c]==1:
                dp[i]=1
                
r=[i for i in range(1,len(dp)) if dp[i]==1]
print(len(r))
print(*r)
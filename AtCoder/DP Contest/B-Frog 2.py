# -*- coding: utf-8 -*-

n,k=map(int,input().split())
dp=[0]*n
stones=list(map(int,input().split()))
for i in range(1,n):
    ops=[]
    for j in range(1,k+1):
        if i>j-1:
            ops.append(abs(stones[i] - stones[i-j])+dp[i-j])

    dp[i]=min(ops)
    
print(dp[-1])
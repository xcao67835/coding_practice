# -*- coding: utf-8 -*-

n=int(input())
dp=[0]*n
stones=list(map(int,input().split()))
for i in range(1,n):
    op1=abs(stones[i] - stones[i-1])+dp[i-1]
    if i>1:
        op2=abs(stones[i] - stones[i-2])+dp[i-2]
    else:
        op2=float("inf")
    dp[i]=min(op1,op2)
    
print(dp[-1])
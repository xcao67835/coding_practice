# -*- coding: utf-8 -*-

n,x=map(int,input().split())
coins=list(map(int,input().split()))
dp=[1]+[0]*x
for c in coins:
    for i in range(1,len(dp)):
        inc=dp[i-c] if i-c>=0 else 0
        
        dp[i]+=inc
        
print(dp[-1]%(10**9+7))
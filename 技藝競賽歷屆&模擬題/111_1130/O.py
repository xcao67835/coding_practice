# -*- coding: utf-8 -*-

n,x=map(int,input().split())
ts = list(map(int,input().split()))
dp=[0]*(x+1)
for i in range(n):
    dp.append([0]*(x+1))
    can=[dp[i]]
    for j in range(1,x+1):
        
        if ts[i]-j>=0:
            dp[i+1][j]

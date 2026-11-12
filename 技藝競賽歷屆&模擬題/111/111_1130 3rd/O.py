# -*- coding: utf-8 -*-

n,x=map(int,input().split())
coins = list(map(int,input().split()))
dp=[1]+[0]*x

for coin in coins:
    for j in range(1,len(dp)):
        if j-coin>=0:
            can=dp[j-coin]
        else:
            can=0
            
        dp[j]+=can
        
print(dp[-1])
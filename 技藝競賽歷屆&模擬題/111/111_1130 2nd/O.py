# -*- coding: utf-8 -*-

n,tar=map(int,input().split())
dp=[1]+[0]*tar
coins=list(map(int,input().split()))
for coin in coins:
    for i in range(1,tar+1):
        if i-coin>=0:
            dp[i]+=dp[i-coin]
print(dp[-1])
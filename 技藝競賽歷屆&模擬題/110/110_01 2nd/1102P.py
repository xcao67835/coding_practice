# -*- coding: utf-8 -*-

n=int(input())
coins=list(map(int,input().split()))
dp=[1]+[0]*sum(coins)

for coin in coins:
    for i in range(len(dp)-1,0,-1):
        if i-coin>=0 : 
            dp[i] = 1 if (dp[i] or dp[i-coin]) else 0
            
print(sum(dp)-1)
for i in range(1,len(dp)):
    if dp[i]==1:
        print(i,end=" ")
print()
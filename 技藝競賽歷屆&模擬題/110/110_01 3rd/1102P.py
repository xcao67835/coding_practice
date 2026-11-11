# -*- coding: utf-8 -*-

n=int(input())
coins=list(map(int,input().split()))

dp=[0]*(sum(coins)+1)

dp[0]=1
for coin in coins:
    for i in range(len(dp)-1, -1, -1):
        
        if dp[i]==1:
            if i+coin<len(dp):
                dp[i+coin]=1
                
r=[]
for i in range(1,len(dp)):
    if dp[i]==1:
        r.append(i)
        
print(sum(dp)-1)
print(*r)
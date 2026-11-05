# -*- coding: utf-8 -*-

n,x=map(int,input().split())
ts = list(map(int,input().split()))
dp=[[1]+[0]*(x)]
for i in range(1,1+n):
    dp.append([1]+[0]*(x))

    for j in range(1,x+1):
        a = 0
        if j-ts[i-1]>=0:
            a = dp[i][j-ts[i-1]]
        b = dp[i-1][j]
        dp[i][j]=a+b
print(dp[-1][-1])

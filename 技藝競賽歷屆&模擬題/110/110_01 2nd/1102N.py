# -*- coding: utf-8 -*-

a=input()
b=input()
dp=[[j+i for j in range(len(a)+1)] for i in range(len(b)+1)]

for i in range(1,1+len(b)):
    for j in range(1,1+len(a)):
        if b[i-1]==a[j-1]:
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
            
print(dp[-1][-1])
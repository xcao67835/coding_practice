# -*- coding: utf-8 -*-

a=input()
b=input()

dp=[[j+i for j in range(len(a)+1)] for i in range(len(b)+1)]

#print(dp)

for bi in range(1,1+len(b)):
    for ai in range(1,1+len(a)):
        if a[ai-1]==b[bi-1]:
            dp[bi][ai]=dp[bi-1][ai-1]
        else:
            dp[bi][ai]=min(dp[bi-1][ai], dp[bi][ai-1], dp[bi-1][ai-1])+1
            
print(dp[-1][-1])
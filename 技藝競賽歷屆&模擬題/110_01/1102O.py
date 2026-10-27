# -*- coding: utf-8 -*-

a=input()
b=input()
c=input()

dp=[[[0]*(len(a)+1) for i in range(len(b)+1)] for i in range(len(c)+1)]

for ci in range(1,1+len(c)):
    for bi in range(1,1+len(b)):
        for ai in range(1,1+len(a)):
            if a[ai-1]==b[bi-1]==c[ci-1]:
                dp[ci][bi][ai]=dp[ci-1][bi-1][ai-1]+1
            else:
                dp[ci][bi][ai]=max(dp[ci-1][bi][ai],dp[ci][bi-1][ai],dp[ci][bi][ai-1])
                
print(dp[-1][-1][-1])
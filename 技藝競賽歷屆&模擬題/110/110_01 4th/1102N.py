# -*- coding: utf-8 -*-

a,b=input(),input()
dp=[[i+j for i in range(len(a)+1)] for j in range(len(b)+1)]

for bb in range(1,len(b)+1):
    for aa in range(1,len(a)+1):
        if a[aa-1]==b[bb-1]:
            dp[bb][aa]=dp[bb-1][aa-1]
        else:
            dp[bb][aa]=min(dp[bb][aa-1],dp[bb-1][aa],dp[bb-1][aa-1])+1
            
print(dp[-1][-1])
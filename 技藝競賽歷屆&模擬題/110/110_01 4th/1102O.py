# -*- coding: utf-8 -*-

a,b,c=input(),input(),input()

dp=[[[0]*(len(a)+1) for i in range(len(b)+1)] for i in range(len(c)+1)]

for cc in range(1,len(c)+1):
    for bb in range(1,len(b)+1):
        for aa in range(1,len(a)+1):
            if a[aa-1]==b[bb-1]==c[cc-1]:
                dp[cc][bb][aa]=dp[cc-1][bb-1][aa-1]+1
            else:
                dp[cc][bb][aa]=max(dp[cc-1][bb][aa],dp[cc][bb-1][aa],dp[cc][bb][aa-1])
                
print(dp[-1][-1][-1])
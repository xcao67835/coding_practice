# -*- coding: utf-8 -*-

a=input()
b=input()
c=input()

dp = [[[0]*(len(c)+1) for i in range(len(b)+1)] for i in range(len(a)+1)]
for aa in range(1,1+len(a)):
    for bb in range(1,1+len(b)):
        for cc in range(1,1+len(c)):
            if a[aa-1]==b[bb-1]==c[cc-1]:
                dp[aa][bb][cc]=dp[aa-1][bb-1][cc-1]+1
            else:
                dp[aa][bb][cc]=max(dp[aa-1][bb][cc], dp[aa][bb-1][cc], dp[aa][bb][cc-1])
                
                
print(dp[-1][-1][-1])
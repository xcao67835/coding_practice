# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    dp=[0]+[float("inf")]*a
    for i in range(len(dp)-b):
        if dp[i] is not float("inf"):
            dp[i+b]=min(dp[i+b],dp[i]+1)
    for i in range(len(dp)-c):
        if dp[i] is not float("inf"):
            dp[i+c]=min(dp[i+c],dp[i]+1)
    
    print(dp[-1] if type(dp[-1]) is int else -1)
            
# -*- coding: utf-8 -*-

while 1:
    try:
        items=[]
        n=int(input())
        for i in range(n):
            items.append(tuple(map(int,input().split())))
        dp=[0]*101
        for w,v in items:
            for i in range(100,w-1,-1):
                dp[i] = max(dp[i],dp[i-w]+v)
                
        print(dp[-1])
    except EOFError:
        break
# -*- coding: utf-8 -*-

a,b=map(int,input().split())
m=[]
for i in range(a):
    m.append(list(map(int,input().split())))
dp = [[0]*b for i in range(a)]

for i in range(a):
    for j in range(b):
        if i==j==0:
            continue
        c1=c2=float("inf")
        if i-1>=0:
            c1=dp[i-1][j]
        if j-1>=0:
            c2=dp[i][j-1]
            
        dp[i][j]=min(c1,c2)+m[i][j]
        
        
print(dp[-1][-1])
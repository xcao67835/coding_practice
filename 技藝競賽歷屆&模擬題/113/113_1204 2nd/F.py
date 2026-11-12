# -*- coding: utf-8 -*-

m,n,_,p=map(int,input().split())
r1=[]
r2=[]
for i in range(m):
    r1.append(list(map(int,input().split())))
for i in range(n):
    r2.append(list(map(int,input().split())))
    
ans=[[0]*p for i in range(m)]
for i in range(m):
    for j in range(p):
        for k in range(n):
            ans[i][j]+=r1[i][k]*r2[k][j]
            
for i in ans:
    print(*i)
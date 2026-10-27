# -*- coding: utf-8 -*-

m,n,_,p=map(int,input().split())

a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
b=[]
for i in range(n):
    b.append(list(map(int,input().split())))
    
    
ans = [[0]*p for i in range(m)]
for i in range(m):
    for j in range(p):
        for k in range(n):
            ans[i][j]+=a[i][k]*b[k][j]
            
for i in ans:
    print(*i)
# -*- coding: utf-8 -*-

m,n=map(int,input().split())
r=[]
for i in range(m):
    r.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(m):
        print(r[j][i],end=" ")
    print()
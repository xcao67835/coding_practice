# -*- coding: utf-8 -*-

m,n,n,p=map(int,input().split())
m1,m2=[],[]
for i in range(m):
    m1.append(list(map(int,input().split())))
for i in range(n):
    m2.append(list(map(int,input().split())))
    

for a in range(m):
    for b in range(p):
        tmp=0
        for c in range(n):
            tmp+=m1[a][c]*m2[c][b]
        print(tmp,end=" ")
    print()
            
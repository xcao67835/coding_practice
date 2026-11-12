# -*- coding: utf-8 -*-

a,b,c,d=map(int,input().split())
m1=[]
m2=[]
for i in range(a):
    m1.append(list(map(int,input().split())))
for i in range(c):
    m2.append(list(map(int,input().split())))
    
    
for i in range(a):
    for j in range(d):
        tmp=0
        for k in range(b):
            tmp+=m1[i][k]*m2[k][j]
        print(tmp,end=" ")
    print()
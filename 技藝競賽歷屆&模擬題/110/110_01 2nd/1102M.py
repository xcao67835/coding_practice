# -*- coding: utf-8 -*-

a,b,c,d=map(int,input().split())
m1=[]
for i in range(a):
    m1.append(list(map(int,input().split())))
m2=[]
for i in range(c):
    m2.append(list(map(int,input().split())))


for k in range(a):
    for kk in range(c):
        for i in range(b):
            for j in range(d):
                print(m1[k][i]*m2[kk][j],end=" ")
        print()
# -*- coding: utf-8 -*-

a,b,c,d=map(int,input().split())
m1,m2=[],[]
for i in range(a):
    m1.append(list(map(int,input().split())))
for i in range(c):
    m2.append(list(map(int,input().split())))
    
for aa in range(a):
    for cc in range(c):
        for bb in range(b):
            for dd in range(d):
                print(m1[aa][bb]*m2[cc][dd],end=" ")
        print()
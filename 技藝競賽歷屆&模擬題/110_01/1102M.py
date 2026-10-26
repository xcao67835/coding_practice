# -*- coding: utf-8 -*-

a,b,c,d=map(int,input().split())

l1,l2=[],[]
for i in range(a):
    l1.append(list(map(int,input().split())))
for ii in range(c):
    l2.append(list(map(int,input().split())))


for l1li in range(a):
    for l2li in range(c):
        for l1r in range(b):
            for l2r in range(d):
                print(l1[l1li][l1r] * l2[l2li][l2r],end=" ")
                
        print()
# -*- coding: utf-8 -*-

m=[]
t=0
for i in range(3):
    l=list(map(int,input().split()))
    t+=sum(l)
    m.append(l)
    
t//=2

for i in m:
    a=t-sum(i)
    for j in i:
        if j==0:
            print(a,end=" ")
        else:
            print(j,end=" ")
    print()
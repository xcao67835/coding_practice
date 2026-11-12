# -*- coding: utf-8 -*-

m=[]
s=0
for _ in range(3):
    tl=list(map(int,input().split()))
    s+=sum(tl)
    m.append(tl)
    
ta=s//2

for i in range(3):
    l=m[i]
    s=sum(l)
    for j in l:
        if j==0:
            j=ta-s
        print(j,end=" ")
    print()
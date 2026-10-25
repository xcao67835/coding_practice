# -*- coding: utf-8 -*-

n = int(input())
l = list(map(int,input().split()))
dp=[[l.pop(0),1]]
for i in l:
    comp=[]
    for j in dp:
        if j[0]<i:
            comp.append(j[1])
    if comp:
        dpa=max(comp)
    else:
        dpa=0
    dp.append([i,dpa+1])
ansl=[i[1] for i in dp]
print(max(ansl))
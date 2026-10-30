# -*- coding: utf-8 -*-
rec=[[],[]]
r1,c1=map(int,input().split())
for i in range(r1):
    rec[0].append(list(map(int,input().split())))
r2,c2=map(int,input().split())
for i in range(r2):
    rec[1].append(list(map(int,input().split())))

ar=[[0]*c2 for i in range(r1)]

for r in range(r1):
    for c in range(c2):
        for x in range(c1):
            ar[r][c]+=rec[0][r][x]*rec[1][x][c]
            
"""
print("[",end="")
for i in range(len(ar)):
    print("[",end="")
    for j in range(len(ar[i])):
        print(ar[i][j],end="")
        if j!=len(ar[i])-1:
            print(",",end="")
    print("]",end="")
    if i!=len(ar)-1:
        print(",",end="")
print("]")
"""

print(str(ar).replace(" ", "")) 
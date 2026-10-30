"""
9,2,6,8,7,1,3,4,5
4,7,5,2,3,6,8,9,1
8,3,1,5,4,9,7,2,6
5,6,8,4,2,7,9,1,3
3,4,2,9,1,5,6,8,7
1,9,7,?,8,3,2,5,4
2,1,9,7,6,4,5,3,8
7,5,4,3,9,8,1,6,2
6,8,3,1,5,2,4,7,1
"""
# -*- coding: utf-8 -*-
c = list("123456789")
inl=[]
ill=0

missing=[-1,-1,-1]
for i in range(9):
    a=list(input().split(","))
    inl.append(a)
    

for i in range(9):
    if sorted(inl[i])!=c:
        if missing[0]==0:
            missing[0]=i
        else:
            ill=1
            break
        
for i in range(9):
    if sorted([j[i] for j in inl])!=c:
        if missing[1]==0:
            missing[1]=i
        else:
            ill=1
            break
                
for i in range(9):
    d=(i//3,i%3)
    tl= inl[d[0]*3][d[1]*3:d[1]*3+3] + inl[d[0]*3+1][d[1]*3:d[1]*3+3] + inl[d[0]*3+2][d[1]*3:d[1]*3+3]
    if sorted(tl)!=c:
        if missing[2]==0:
            missing[2]=i
        else:
            ill=1
            break
        
if ill:
    print(-1)
else:
    for i in inl[missing[0]]:
        if i in c:
            c.remove(i)
    print(*c)
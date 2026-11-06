# -*- coding: utf-8 -*-
n,m=map(int,input().split())
c=input().split()
for i in range(m):
    nc=[]
    for j in range(n//2):
        nc+=[c[j], c[j+n//2]]
    c=nc
print(*c)
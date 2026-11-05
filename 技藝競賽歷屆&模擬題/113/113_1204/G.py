# -*- coding: utf-8 -*-

m,n=map(int,input().split())
ma=[]
for i in range(m):
    ma.append(input().split())
    
for i in range(n):
    for j in range(m):
        print(ma[j][i],end=" ")
        
    print()
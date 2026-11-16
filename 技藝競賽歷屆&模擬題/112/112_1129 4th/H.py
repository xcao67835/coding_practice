# -*- coding: utf-8 -*-

n,x=map(int,input().split())
for i in range(x):
    if n%10==0:
        n//=10
    else:
        n-=1
        
print(n)
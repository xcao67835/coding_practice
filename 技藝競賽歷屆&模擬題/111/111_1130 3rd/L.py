# -*- coding: utf-8 -*-

n=int(input())
r=0
for i in range(n+1):
    r+=bin(i).count("1")
    
print(r)
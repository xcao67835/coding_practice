# -*- coding: utf-8 -*-

n=int(input())
if n%2==0:
    n//=2
else:
    n = -(n//2)-1
    
print(n)
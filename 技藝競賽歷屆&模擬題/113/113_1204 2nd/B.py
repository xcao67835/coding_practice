# -*- coding: utf-8 -*-

a=0
b,c=map(int,input().split())
if c<b:
    b,c=c,b
for i in range(b,c+1):
    if i%2==0:
        a+=i
print(a)
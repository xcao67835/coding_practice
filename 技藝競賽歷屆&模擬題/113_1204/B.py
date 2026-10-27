# -*- coding: utf-8 -*-

s=0
a,b=map(int,input().split())
if a>b:
    a,b=b,a

if a%2!=0:
    a+=1

for i in range(a,b+1,2):
    s+=i
print(s)
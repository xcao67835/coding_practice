# -*- coding: utf-8 -*-

a=int(input())
b=int(input())


if a>b:
    a,b=b,a
    
for i in range(a+1,b):
    if i%5 in (2,3):
        print(i)
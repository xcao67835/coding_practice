# -*- coding: utf-8 -*-
from math import isqrt
def f(x):
    if x<2:
        return False
    for i in range(2,isqrt(x)+1):
        if x%i==0:
            return False
            break
    else:
        return True
for _ in range(int(input())):
    a,b=map(int,input().split(","))
    
    if abs(a-b)!=2:
        print("N")
        continue
    if f(a) and f(b):
        print("Y")
    else:
        print("N")
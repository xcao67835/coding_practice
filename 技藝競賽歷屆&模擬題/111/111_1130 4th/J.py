# -*- coding: utf-8 -*-
from math import isqrt
def isp(n):
    if n<=1:
        return False
    
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

for _ in range(int(input())):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        if isp(i):
            print(i)
            
    print()
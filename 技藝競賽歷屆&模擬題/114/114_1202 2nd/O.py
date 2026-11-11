# -*- coding: utf-8 -*-
from functools import cache
from math import isqrt
@cache
def isp(x):
    if x<=1:
        return False
    
    for i in range(2,isqrt(x)+1):
        if x%i==0:
            return False
            break
    else:
        return True
    
    

for _ in range(int(input())):
    n=input()
    if isp(int(n)):
        if n!=n[::-1] and isp(int(n[::-1])):
            print(f"{n} is an emirp number.")
        else:
            print(f"{n} is a prime number.")
            
    else:
        print(f"{n} is not a prime number.")
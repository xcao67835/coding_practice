# -*- coding: utf-8 -*-

from functools import cache
from math import isqrt
@cache
def prime(n):
    if n<=1:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True
    


for _ in range(int(input())):
    n=int(input())
    
    if prime(n):
        if n!=int(str(n)[::-1]) and prime(int(str(n)[::-1])):
            print(f"{n} is an emirp number.")
        else:
            print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
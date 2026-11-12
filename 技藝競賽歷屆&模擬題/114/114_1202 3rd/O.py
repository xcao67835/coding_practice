# -*- coding: utf-8 -*-
from math import isqrt
def isp(n):
    if n<=0:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True



for _ in range(int(input())):
    n=int(input())
    if isp(n):
        if str(n)!=str(n)[::-1] and isp(int(str(n)[::-1])):
            print(f"{n} is an emirp number.")
        else:
            print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
# -*- coding: utf-8 -*-
from math import isqrt
n=int(input())
l=list(map(int,input().split()))

for n in l:
    while n!=1:
        for i in (2,3,5):
            if n%i==0:
                n//=i
                break
        else:
            print(False)
            break
    else:
        print(True)
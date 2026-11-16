# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    if n%2==1:
        t=1
        n-=3
    else:
        t=0
        
    print("7"*t+"1"*(n//2))
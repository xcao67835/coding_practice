# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    if n%2==1:
        n-=3
        seven=1
    else:
        seven=0
        
    if seven:
        print(7,end="")
    print("1"*(n//2))
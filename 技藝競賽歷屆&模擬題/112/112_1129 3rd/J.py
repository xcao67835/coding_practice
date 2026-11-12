# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    if n%2==1:
        s=1
        n-=3
    else:
        s=0
        
    if s==0:
        a=""
    else:
        a="7"
    a+="1"*(n//2)
    
    print(a)
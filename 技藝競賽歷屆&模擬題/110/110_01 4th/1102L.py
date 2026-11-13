# -*- coding: utf-8 -*-
from math import isqrt
def isp(n):
    if n<1:
        return False
    
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
        
    return True

while 1:
    try:
        a,b=map(int,input().split())
        print(f"{a} {b}: ",end="")
        p=[]
        for i in range(1,a+1):
            if isp(i):
                p.append(i)
                
                
        k=len(p)
        if k%2==0:
            if 2*b>=k:
                print(*p)
            else:
                print(*p[k//2-b:k//2+b])
        else:
            if 2*b-1>=k:
                print(*p)
            else:
                print(*p[k//2-b+1:k//2+b])
        print()
    except EOFError:
        break
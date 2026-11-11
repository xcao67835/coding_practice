# -*- coding: utf-8 -*-
from math import isqrt
def p(n):
    if n<1:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
            break
    return True

while 1:
    try:
        a,b=map(int,input().split())
        print(f"{a} {b}: ",end="")
        ps=[]
        for i in range(1,a+1):
            if p(i):
                ps.append(i)
                
        k=len(ps)
        
        if k%2==0:
            if 2*b>=k:
                print(*ps)
            else:
                print(*ps[k//2-b:k//2+b])
        else:
            if 2*b-1>=k:
                print(*ps)
            else:

                print(*ps[k//2-b+1:k//2+b])
            
    except EOFError:
        break
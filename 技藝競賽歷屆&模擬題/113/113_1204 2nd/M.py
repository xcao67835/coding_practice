# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    d=0
    for a in range(255):
        for b in range(a,255):
            for c in range(b,255):
                if n==a**2+b**2+c**2:
                    print(a,b,c)
                    d=1
                    break
            if d:
                break
           
        if d:
            break
                
    else:
        print(-1)
                
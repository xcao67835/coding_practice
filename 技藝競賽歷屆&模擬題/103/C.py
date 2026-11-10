# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a=set(input())
    b=set(input())
    c=a&b
    
    if c:
        print(*sorted(c),sep="")
    else:
        print("N")
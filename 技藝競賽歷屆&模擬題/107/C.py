# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    visited=set()

    while 1:
        if n in visited:
            print("F")
            break
        elif n == 1:
            print("T")
            break
        
        visited.add(n)
        n=list(map(int,list(str(n))))
        n=sum(list(map(lambda x:x**2, n)))
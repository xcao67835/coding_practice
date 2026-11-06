# -*- coding: utf-8 -*-

for _ in range(int(input())):
    l=list(input())
    while len(l)!=0:
        a=l.pop(0)
        n=""
        while l and l[0].isdigit():
            n+=l.pop(0)
        n=int(n)
        print(a*n,end="")
    print()
    
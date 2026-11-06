# -*- coding: utf-8 -*-

while 1:
    a=input()
    if a=="0":
        break
    n,s=a.split()
    n=int(n)
    m=len(s)//n
    s=list(s)
    for i in range(n):
        t=[]
        for j in range(m):
            t.append(s.pop(0))
        print(*t[::-1],sep="",end="")
    print()
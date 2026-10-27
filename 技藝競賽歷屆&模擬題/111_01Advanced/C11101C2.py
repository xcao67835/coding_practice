# -*- coding: utf-8 -*-
for _ in range(int(input())):
    ar=[0]*10
    a=int(input())
    for i in range(1,1+a):
        aaa=str(i)
        for g in aaa:
            g=int(g)
            ar[g]+=1
    print(*ar)


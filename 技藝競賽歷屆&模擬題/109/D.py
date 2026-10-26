# -*- coding: utf-8 -*-

n=int(input())
for _ in range(n):
    d=int(input())
    if d==1:
        print(1)
        continue
    ds=[]
    while d!=1:
        for i in range(9,1,-1):
            if d%i==0:
                d//=i
                ds.append(i)
                break
        else:
            if d!=1:
                print(-1)
                break
    else:
         print(*sorted(ds),sep="")           
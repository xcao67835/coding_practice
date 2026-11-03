# -*- coding: utf-8 -*-

for _ in range(int(input())):
    l=list(map(int,input().split(",")))
    ll=l.copy()
    l.sort()
    ans=[]
    for i in range(len(l)):
        ans.append(l.index(ll[i])+1)
    print(*ans,sep=", ")
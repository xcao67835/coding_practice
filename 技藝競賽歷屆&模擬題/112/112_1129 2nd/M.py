# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n,x=map(int,input().split())
    m=sorted(list(map(int,input().split())),reverse=1)
    
    mans=0
    r=0
    for i in m:
        mans+=1
        if mans*i>=x:
                r+=1
                mans=0
    print(r)
    
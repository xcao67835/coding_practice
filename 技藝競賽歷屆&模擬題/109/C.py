# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a=list(map(int,input().split("/")))
    b=list(map(int,input().split("/")))
    
    y = a[-1]-b[-1]
    if a[1]<b[1] or (a[1]==b[1] and a[0]<b[0]):
        y-=1
    print(y)
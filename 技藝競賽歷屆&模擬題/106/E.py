# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a,b=input().split("/")
    a = list(map(int,a.split(".")))
    b = list(map(int,b.split(".")))
    c=[0,0,0,0]
    for i in range(4):
        c[i] = a[i] | (~b[i]&255)
    print(*c,sep=".")
        
    
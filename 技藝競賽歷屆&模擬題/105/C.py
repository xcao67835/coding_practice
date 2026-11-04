# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a,b = input().split("/")
    a = list(map(int,a.split(".")))
    b = list(map(int,b.split(".")))
    c = [a[i]&b[i] for i in range(4)]
    print(*c,sep=".")
    
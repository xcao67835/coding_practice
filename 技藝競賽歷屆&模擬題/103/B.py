# -*- coding: utf-8 -*-
for _ in range(int(input())):
    n,a,b,tot=map(int,input().split(","))
    y=(tot-n*a)//(b-a)
    x=(tot-n*b)//(a-b)
    print(x,y,sep=",")
# -*- coding: utf-8 -*-
chart=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday",]
mchart=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(int(input())):
    m,d=map(int,input().split())
    while m!=1:
        d+=mchart[m-2]
        m-=1
    print(chart[d%7])
# -*- coding: utf-8 -*-

while 1:
    a,b,c,d=map(int,input().split())
    if a==b==c==d==0:
        break
    mina=a*60+b
    minb=c*60+d
    t=(minb-mina) + (1440 if (minb-mina)<0 else 0)
    print(t)
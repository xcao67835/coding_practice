# -*- coding: utf-8 -*-

a=int(input())
d,s=0,0
while a:
    if a%2==0:
        a//=2
        d+=1
    else:
        a-=1
        s+=1
print(d*2+s)
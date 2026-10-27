# -*- coding: utf-8 -*-

s=int(input())
steps=0
while s:
    if s%2==0:
        s//=2
    else:
        s-=1
    
    steps+=1
    
print(steps)
    
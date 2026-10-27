# -*- coding: utf-8 -*-

x,y=0,0

s=input()
for i in s:
    if i=="U":
        y+=1
    if i=="D":
        y-=1
    if i=="L":
        x-=1
    if i=="R":
        x+=1
        
if (x,y)==(0,0):
    print("Y")
else:
    print("N")
# -*- coding: utf-8 -*-

a=input()
m=0
tm=0
for i in a:
    if i=="(":
        tm+=1
        m=max(m,tm)
    if i==")":
        tm-=1
        
print(m)
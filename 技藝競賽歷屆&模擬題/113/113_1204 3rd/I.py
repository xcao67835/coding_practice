# -*- coding: utf-8 -*-

s=input()
sc=0
if len(s)>=8:
    sc+=1
    
for i in s:
    if i.isupper():
        sc+=1
        break
    
for i in s:
    if i.islower():
        sc+=1
        break
    
for i in s:
    if i.isdigit():
        sc+=1
        break
    
for i in s:
    if i in '[!@#$^&*(),.?":{}|<>]':
        sc+=1
        break
    
print(sc)
# -*- coding: utf-8 -*-

l=input()
b,m,s=0,0,0

normal=1
for i in l:
    if i == "(":
        s+=1
    elif i == ")":
        s-=1
    elif i == "[":
        m+=1
    elif i == "]":
        m-=1
    elif i == "{":
        b+=1
    elif i == "}":
        b-=1
        
    if b<0 or s<0 or m<0:
        normal=0
        break
    
if not b==m==s==0:
    normal=0
    
if normal:
    print(1)
else:
    print(0)
    
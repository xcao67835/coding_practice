# -*- coding: utf-8 -*-

s=int(input())
o=input()
for i in o:
    if i=="-":
        s-=1
        s=str(s)
        s=s[1:]+s[0]
        s=int(s)
    elif i=="+":
        s+=1
        s=str(s)
        s=s[-1]+s[:-1]
        s=int(s)
print(s)
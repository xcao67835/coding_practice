# -*- coding: utf-8 -*-

a,b=input().split(",")
a=int(a,3)
b=int(b,6)
c=a+b
r=[]
while c>=5:
    r.append(c%5)
    c//=5
else:
    if c!=0:
        r.append(c)
for i in r[::-1]:
    print(i,end="")
# -*- coding: utf-8 -*-

dig=[]
alp=[]
s=input()
for i in s:
    if i.isalpha():
        alp.append(ord(i)-64)
    else:
        dig.append(int(i))
a,b=0,0
i=0
while dig:
    a+=dig.pop()*10**i
    i+=1
    

i=0
while alp:
    b+=alp.pop()*26**i
    i+=1
print(a*b)
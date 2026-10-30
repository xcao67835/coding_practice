# -*- coding: utf-8 -*-

pw=input()

lastlower=0
firstupper=-1
u=False
l=False
s=False
for i in range(len(pw)):
    if pw[i].isupper():
        u=True
        if firstupper==-1:
            firstupper=i
    elif pw[i].islower():
        l=True
        lastlower=i
    elif pw[i].isdigit():
        s=True

li = True if lastlower<firstupper else False
print(1 if (li and u and l and s)else 0)
        
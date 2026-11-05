# -*- coding: utf-8 -*-

ina=input()
inb=input()
a,b=0,0
nono=False
if not inb.isdigit():
    nono=True
elif len(inb)!=4:
    nono=True
elif len(set(inb))<4:
    nono=True
    
if nono:
    print("0A0B")
else:
    a,b=0,0
    for i in range(4):
        if ina[i]==inb[i]:
            a+=1
        elif inb[i] in ina:
            b+=1
            
    print(f"{a}A{b}B")
    
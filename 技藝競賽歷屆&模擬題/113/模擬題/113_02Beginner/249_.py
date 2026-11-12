# -*- coding: utf-8 -*-
from collections import Counter
a,b=input().split(",")

ac=Counter(a)
bc=Counter(b)

s=sum(ac.values()) + sum(bc.values())

c=0
c+=ac["A"]*800
c+=ac["E"]*500
c+=ac["C"]*200
c+=bc["A"]*800
c+=bc["E"]*400
c+=bc["C"]*100

if s>=20:
    c*=0.9
    
print(int(c))
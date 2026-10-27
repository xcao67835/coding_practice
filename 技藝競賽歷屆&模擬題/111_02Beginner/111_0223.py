# -*- coding: utf-8 -*-

from collections import Counter
s=input()
cs=Counter(s)

survive=0

for i in range(ord("A"),ord("H")+1):
    team=chr(i)
    if 2-cs[team]>=1:
        survive=1
        print(team,end="")
        

for i in range(ord("I"),ord("Z")+1):
    team=chr(i)
    if 3-cs[team]>=1:
        survive=1
        print(team,end="")
        
if not survive:
    print("*")
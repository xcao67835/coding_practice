# -*- coding: utf-8 -*-

for _ in range(int(input())):
    s=input()
    if len(s)==5:
        print(3)
        continue
    
    one=0
    for i in range(3):
        if s[i]=="one"[i]:
            one+=1
    if one>=2:
        print(1)
    else:
        print(2)
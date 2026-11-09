# -*- coding: utf-8 -*-

for i in range(int(input())):
    s=input()
    if len(s)==5:
        print(3)
        continue
    one=two=0
    for i in range(3):
        if s[i]=="one"[i]:
            one+=1
        if s[i]=="two"[i]:
            two+=1
            
    if one>=2:
        print(1)
    else:
        print(2)
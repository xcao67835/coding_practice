# -*- coding: utf-8 -*-

for _ in range(int(input())):
    a=  input()
    if len(a)==5:
        print(3)
        continue
    
    one=0
    for i in range(3):
        if a[i] == "one"[i]:
            one+=1
    
    if one>=2:
        print(1)
    else:
        print(2)
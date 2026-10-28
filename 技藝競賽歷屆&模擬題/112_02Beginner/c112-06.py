# -*- coding: utf-8 -*-

l=input().replace(","," ").replace("."," ").split()

ac=1

for i in l:
    now = i.isupper() or i.islower() or (i[0].isupper() and "".join(i[1:]).islower())
    if not now:
        ac=0
        
print(ac)
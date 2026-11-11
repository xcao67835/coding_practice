# -*- coding: utf-8 -*-

c=set("yaeiou")
s=input().lower()
for i in s:
    if i not in c:
        print(F".{i}",end="")
# -*- coding: utf-8 -*-

s=input()
for i in s:
    i=i.lower()
    if i not in "aoyeui":
        print(f'.{i}',end="")
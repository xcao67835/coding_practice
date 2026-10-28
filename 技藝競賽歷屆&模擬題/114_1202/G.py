# -*- coding: utf-8 -*-

s=input().lower().replace("a","").replace("o","").replace("y","").replace("e","").replace("u","").replace("i","")
for i in s:
    print(f".{i}",end="")
# -*- coding: utf-8 -*-

a = list(input())
while a[-1]=="0":
    a.pop()
c = a[::-1]
 
print("".join(c))
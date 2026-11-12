# -*- coding: utf-8 -*-

s=input()
s=s.lower()
l = "".join([i.upper() if i in "aeiou" else i for i in s])
print(l)
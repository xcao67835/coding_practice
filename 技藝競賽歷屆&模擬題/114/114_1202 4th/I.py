# -*- coding: utf-8 -*-

s=input()
for i in range(len(s)-1):
    print(abs(ord(s[i])-ord(s[i+1])),end="")
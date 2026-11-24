# -*- coding: utf-8 -*-

s=input().split()
for i in range(2,len(s)-2):
    s[i] = "*"*len(s[i])
print(*s)
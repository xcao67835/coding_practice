# -*- coding: utf-8 -*-

s=input()
c=0

for i in range(len(s)-3):
    for j in range(len(s)-i-3):
        if s[i]==s[j+i+3] and s[i].isupper():
            c+=1
print(c)
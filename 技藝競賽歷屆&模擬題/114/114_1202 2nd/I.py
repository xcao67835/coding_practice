# -*- coding: utf-8 -*-

s=input()
r=[]
for i in range(len(s)-1):
    r.append(abs(ord(s[i]) - ord(s[i+1])))
    
print(*r,sep="")
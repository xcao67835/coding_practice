# -*- coding: utf-8 -*-

s=input()

now=1
mx=1

for i in range(len(s)):
    now=1
    for j in range(1,1+min(i,len(s)-i-1)):
        if s[i-j]==s[i+j]:
            now+=2
            mx=max(mx,now)
        else:
            now=1
            break
            
for i in range(len(s)-1):
    now=0
    for j in range(min(i+1,len(s)-i-1)):
        if s[i-j]==s[i+j+1]:
            now+=2
            mx=max(mx,now)
        else:
            now=0
            break 
        
        
print(mx)
# -*- coding: utf-8 -*-

s=input()
ans=""
for i in s[::-1]:
    if i not in ans:
        ans = i+ans
        
print(ans)
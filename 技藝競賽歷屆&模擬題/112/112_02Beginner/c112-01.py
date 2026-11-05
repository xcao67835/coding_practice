# -*- coding: utf-8 -*-

s=input()
sec=[]
mx=0
for i in s:
    if i not in sec:
        sec.append(i)
        mx=max(mx,len(sec))
        
    else:
        while i in sec:
            sec.pop(0)
        sec.append(i)
        
print(mx)

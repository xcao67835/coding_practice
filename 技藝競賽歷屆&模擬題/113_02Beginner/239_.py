# -*- coding: utf-8 -*-

s=input()
ch=""
count=0
for i in s:
    if i==ch:
        count+=1
    else:
        if count>0:
            print(f"{ch}{count}",end="")
        ch=i
        count=1    
else:
    if count>0:
        print(f"{ch}{count}",end="")
        
            
        
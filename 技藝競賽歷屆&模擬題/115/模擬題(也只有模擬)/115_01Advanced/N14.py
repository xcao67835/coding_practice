# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:30:35 2026

@author: taiyu
"""

l = input().split()
stack=[]
sym = ("+","-","*","/","(",")")
p = {"+":1,"-":1,"*":2,"/":2}
pr=[]
for i in l:
    if i in sym:
        if i=="(":
            stack.append(i)
            
        elif i==")":
            while stack[-1]!="(":
                pr.append(stack.pop())
            stack.pop()
        else:
            while stack and not stack[-1]=="(" and p[stack[-1]]>=p[i]:
                pr.append(stack.pop()) 
            stack.append(i)
    else:
        pr.append(i)
while stack:
    pr.append(stack.pop())
print(" ".join(pr))
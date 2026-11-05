# -*- coding: utf-8 -*-

s=input().split()
stack=[]
for i in s:
    
    if i in "+-":
        while stack and stack[-1] in "+-*/":
            print(stack.pop(),end=" ")
        stack.append(i)
    elif i in "*/":
        while stack and stack[-1] in "*/":
            print(stack.pop(),end=" ")
        stack.append(i)
    elif i =="(":
        stack.append(i)
    elif i==")":
        while stack and stack[-1] !="(":
            print(stack.pop(),end=" ")
        stack.pop()
    else:
        print(i,end=" ")
print(*stack[::-1])
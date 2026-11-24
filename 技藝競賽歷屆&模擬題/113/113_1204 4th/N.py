# -*- coding: utf-8 -*-

l=list(input().split())
stack=[]
for i in l:
    if i not in "+-*/()":
        print(i,end=" ")
    elif i=="(":
        stack.append(i)
    elif i==")":
        while stack and stack[-1]!="(":
            print(stack.pop(),end=" ")
        if stack:
            stack.pop()
    elif i in "+-":
        while stack and stack[-1] in "+-*/":
            print(stack.pop(),end=" ")
        stack.append(i)
    elif i in "*/":
        while stack and stack[-1] in "*/":
            print(stack.pop(),end=" ")
        stack.append(i)
            
print(*reversed(stack))
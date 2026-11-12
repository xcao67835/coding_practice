# -*- coding: utf-8 -*-

l=input().split()

stack=[]
for a in l:
    if a not in "+-*/()":
        print(a,end=" ")
    elif a in "+-":
        while stack and stack[-1] in "+-*/":
            print(stack.pop(),end=" ")
        stack.append(a)
    elif a in "*/":
        while stack and stack[-1] in "*/":
            print(stack.pop(),end=" ")
        stack.append(a)
    elif a=="(":
        stack.append(a)
    elif a==")":
        while stack and stack[-1] != "(":
            print(stack.pop(),end=" ")
        stack.pop()
        
print(*stack[::-1])
        
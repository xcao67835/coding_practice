def op(a,c,b):
    if c=="/":
        return a//b
    return eval(str(a)+c+str(b))


# -*- coding: utf-8 -*-
from collections import deque
for _ in range(int(input())):
    stack=[]
    l=deque(input().split())
    for i in range(len(l)):
        c = l.popleft()
        if c.isdigit():
            stack.append(int(c))
        else:
            b=stack.pop()
            a=stack.pop()
            stack.append(op(a,c,b))
    
    print(int(stack[-1]))
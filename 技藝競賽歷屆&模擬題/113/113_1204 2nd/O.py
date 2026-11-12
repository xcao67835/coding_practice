# -*- coding: utf-8 -*-

l=list(input().split())
while len(l)!=1:
    for i in range(len(l)):
        if l[i] in "+-*/":
            break
    a,b,o=l.pop(i-2),l.pop(i-2),l.pop(i-2)
    l.insert(i-2, str(eval(f"{a}{o}{b}")))
    
print(l[-1])
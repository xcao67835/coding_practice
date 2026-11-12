# -*- coding: utf-8 -*-


l = input().split()
while len(l)!=1:
    for i in range(len(l)-1):
        if l[i].isdigit() and l[i+1].isdigit() and l[i+2] in "+-*/":
            t = str(eval(l[i]+l[i+2]+l[i+1]))
            l.pop(i+2)
            l.pop(i+1)
            l.pop(i)
            l.insert(i, t)
            break

print(*l)
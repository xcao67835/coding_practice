# -*- coding: utf-8 -*-

l=input().split()
while len(l)>1:
    for i in range(len(l)-2):
        if l[i].isdigit() and l[i+1].isdigit() and not l[i+2].isdigit():
            a,b,c=l.pop(i),l.pop(i),l.pop(i)
            l.insert(i,str(eval(f"{a}{c}{b}")))
print(*l)
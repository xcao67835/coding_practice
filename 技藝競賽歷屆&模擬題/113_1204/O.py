# -*- coding: utf-8 -*-

l=input().split()
l = [int(i) if i.isdigit() else i for i in l]

while len(l)!=1:
    for i in range(len(l)):
        if isinstance(l[i], str):
            tmp = eval(str(l[i-2])+l[i]+str(l[i-1]))
            l=l[:i-2]+[tmp]+l[i+1:]
            break
else:
    print(l[0])
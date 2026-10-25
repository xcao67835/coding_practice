# -*- coding: utf-8 -*-
l  =[]
for _ in range(3):
    l.append(list(map(int,input().split())))

av=(l[0][1]+l[0][2]+l[1][0]+l[1][2]+l[2][0]+l[2][1])//2

a=av-(l[0][1]+l[0][2])
print(a, l[0][1], l[0][2])
a=av-(l[1][0]+l[1][2])
print(l[1][0], a, l[1][2])
a=av-(l[2][0]+l[2][1])
print(l[2][0], l[2][1],a)
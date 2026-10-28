# -*- coding: utf-8 -*-

l=input()

w="123 456 789 147 268 369 159 357"
w=w.split()
win=3
for i in w:
    i=list(map(int,list(i)))
    if l[i[0]-1] == l[i[1]-1] == l[i[2]-1] == "X":
        win=2
    if l[i[0]-1] == l[i[1]-1] == l[i[2]-1] == "O":
        win=1
print(win)
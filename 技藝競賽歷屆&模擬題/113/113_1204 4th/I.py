# -*- coding: utf-8 -*-

s=input()
score=[0]*5

if len(s)>=8:
    score[0]=1
for i in s:
    if i.isdigit():
        score[1]=1
    elif i.isupper():
        score[2]=1
    elif i.islower():
        score[3]=1
    elif i in '[!@#$^&*(),.?":{}|<>]':
        score[4]=1
print(sum(score))
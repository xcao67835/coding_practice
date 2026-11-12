# -*- coding: utf-8 -*-

s=input()
st=set(input())
for i in s:
    if i not in st:
        print(i,end="")
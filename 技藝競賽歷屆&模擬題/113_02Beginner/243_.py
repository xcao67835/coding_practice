# -*- coding: utf-8 -*-

s,a=input().split("=")
for i in range(1,101):
    if eval(s.replace("X",str(i))) == int(a):
        print(i)
        break
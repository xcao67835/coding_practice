# -*- coding: utf-8 -*-

a=input().replace(" ","")
w={"YX", "XO", "OY"}
l={"XY", "OX", "YO"}

if a in w:
    print(1)
elif a in l:
    print(2)
else:
    print(0)

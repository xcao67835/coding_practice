# -*- coding: utf-8 -*-

win=["BT","TC","CW","WB"]

a,b=input().split()
if a+b in win:
    print(1)
elif b+a in win:
    print(2)
else:
    print(0)
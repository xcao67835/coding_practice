# -*- coding: utf-8 -*-

a,b = input().split()
if a==b:
    print(0)
elif (a,b)==("Y","O") or (a,b)==("O","X") or (a,b)==("X","Y") :
    print(2)
else:
    print(1)
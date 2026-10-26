# -*- coding: utf-8 -*-

d = dict()
while 1:
    a = input()
    if a=="":
        break
    a,b=a.split()
    d[b]=a
    
while 1:
    try:
        a = input()
        if a in d:
            print(d[a])
        else:
            print("eh")
    except EOFError:
        break
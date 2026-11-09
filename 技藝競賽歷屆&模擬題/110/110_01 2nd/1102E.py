# -*- coding: utf-8 -*-

d={}
while 1:
    s=input()
    if s=="":
        break
    a,b=s.split()
    d[b]=a
    
while 1:
    try:
        s=input()
    except EOFError:
        break
    
    if s in d:
        print(d[s])
    else:
        print("eh")
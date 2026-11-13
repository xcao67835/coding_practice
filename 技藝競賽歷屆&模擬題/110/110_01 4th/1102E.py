# -*- coding: utf-8 -*-
d={}
while 1:
    a=input()
    if a=="":
        break
    
    a,b=a.split()
    d[b]=a
    
    
while 1:
    try:
        i=input()
        if i in d:
            print(d[i])
        else:
            print("eh")
            
    except EOFError:
        break
# -*- coding: utf-8 -*-

while 1:
    a=input()
    if a=="0":
        break
    
    while len(a)!=1:
        a=list(a)
        a=list(map(int,a))
        a=sum(a)
        a=str(a)
        
    print(a)
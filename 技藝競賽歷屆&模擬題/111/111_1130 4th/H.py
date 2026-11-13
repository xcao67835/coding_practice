# -*- coding: utf-8 -*-
while 1:
    a=input()
    if a=="0":
        break
    
    a,b=a.split()
    a=int(a)
    p=""
    for i in range(len(b)):
        if i%(len(b)//a)==0:
            print(p[::-1],end="")
            p=""
        p+=b[i]
    print(p[::-1])
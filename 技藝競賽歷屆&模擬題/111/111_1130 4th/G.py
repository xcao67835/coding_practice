# -*- coding: utf-8 -*-
for _ in range(int(input())):
    s=input()
    
    
    c=""
    n=""
    
    for i in s:
        if i.isdigit():
            n+=i
        else:
            if c!="":
                print(c*int(n),end="")
            n=""
            c=i
    else:
        if c!="":
            print(c*int(n))
        n=""
        c=i
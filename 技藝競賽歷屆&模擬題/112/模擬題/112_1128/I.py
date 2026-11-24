# -*- coding: utf-8 -*-

while 1:
    try:
        s=input()
        d="0"
        r=0
        for i in s:
            if i.isdigit():
                d+=i
            elif i==",":
                r+=int(d)
                d="0"
        if d:
            r+=int(d)
                
        print(r)
    except EOFError:
        break
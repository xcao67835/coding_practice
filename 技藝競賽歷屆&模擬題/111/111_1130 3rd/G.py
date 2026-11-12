# -*- coding: utf-8 -*-

for _ in range(int(input())):
    s=input()
    c=""
    d=""
    for i in s:
        if i.isdigit():
            d+=i
        else:
            if d:
                print(c*int(d),end="")
                d=""
            c=i
    print(c*int(d))
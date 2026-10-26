# -*- coding: utf-8 -*-

for _ in range(int(input())):
    s=input()
    a,b="",""
    for i in s:
        if i=="4":
            a+="3"
            b+="1"
        else:
            a+=i
            b+="0"
    print(int(a),int(b))
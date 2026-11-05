# -*- coding: utf-8 -*-

while 1:
    a = input()
    if a=="0":
        break
    a,b=a.split()
    a = int(a)
    b = list(b)
    l = len(b)
    r = []
    for i in range(a):
        t = ""
        for j in range(l//a):
            t+=b.pop()
        r.append(t)
    print("".join(r[::-1]))
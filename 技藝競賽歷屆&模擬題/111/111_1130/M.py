# -*- coding: utf-8 -*-

l = [["0","1"]]
for i in range(int(input())-1):
    n = []
    for a in ["0","1"]:
        ite=l[i] if a=="0" else l[i][::-1]
        for b in ite:
            n.append(a+b)
    l.append(n)
print("\n".join(l[-1]))
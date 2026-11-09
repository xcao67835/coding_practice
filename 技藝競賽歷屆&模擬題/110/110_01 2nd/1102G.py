# -*- coding: utf-8 -*-

tar=input().split()
for i in range(int(input())):
    l=input().split()
    a=b=0
    t=tar.copy()
    for i in range(4):
        if l[i]==t[i]:
            a+=1
            l[i]=-1
            t[i]=-2
    for i in range(4):
        if l[i] in t:
            b+=1
            t[t.index(l[i])]=-2
            l[i]=-1
            
            
    print(f"{a}A{b}B")
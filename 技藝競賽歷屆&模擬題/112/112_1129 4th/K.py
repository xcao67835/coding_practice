# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    s=input()
    a=len(s)-1
    for i in range(len(s)-2):
        if s[i]==s[i+2]:
            a-=1
            
    print(a)
# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n=int(input())
    s=input()
    for i in range(n-2):
        if s[i]==s[i+2]:
                   n-=1
                   
    print(n-1)
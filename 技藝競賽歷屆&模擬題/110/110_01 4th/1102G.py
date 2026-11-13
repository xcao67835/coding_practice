# -*- coding: utf-8 -*-

tt=input().split()
n=int(input())


for _ in range(n):
    
    s=input().split()
    t=tt.copy()
    
    a=b=0
    for i in range(4):
        if t[i]==s[i]:
            a+=1
            s[i]=1234
            t[i]=5678
            
    for i in range(4):
        if s[i] in t:
            t[t.index(s[i])] = 1357
            s[i]=2468
            b+=1
    print(F"{a}A{b}B")
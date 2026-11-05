# -*- coding: utf-8 -*-

an = input().split()
n = int(input())

for _ in range(n):
    anc=an.copy()
    inp = input().split()
    a,b=0,0
    for j in range(4):
        if inp[j]==anc[j]:
            a+=1
            anc[j]=None
            inp[j]=1234564789
    for j in range(4):     
        if inp[j] in anc:
            b+=1
            anc[anc.index(inp[j])]=None
            
    print(f"{a}A{b}B")
# -*- coding: utf-8 -*-

n,m=map(int,input().split())
pai=input().split()
for i in range(m):
    pai1,pai2=pai[:n//2],pai[n//2:]
    pai=[]
    for ii in range(n//2):
        pai+=[pai1[ii],pai2[ii]]
print(" ".join(pai))
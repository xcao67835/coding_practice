# -*- coding: utf-8 -*-
n,q=map(int,input().split())
l=input().split()


for i in range(q):
    a,b = map(int,input().split())
    print(len(set(l[a-1:b])))
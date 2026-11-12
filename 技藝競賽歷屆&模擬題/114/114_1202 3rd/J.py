# -*- coding: utf-8 -*-

inp=list(map(int,input().split(".")))
for i in inp:
    i=bin(i)[2:].zfill(8)
    print(i,end="")
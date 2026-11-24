# -*- coding: utf-8 -*-

s=input().split(".")
for i in s:
    print(bin(int(i))[2:].zfill(8),end="")
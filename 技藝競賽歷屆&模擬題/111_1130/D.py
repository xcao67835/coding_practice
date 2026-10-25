# -*- coding: utf-8 -*-

a = input()
l = list(set(map(int,input().split())))
print(len(l))
print(*sorted(l))
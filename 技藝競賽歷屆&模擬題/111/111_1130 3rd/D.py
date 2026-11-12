# -*- coding: utf-8 -*-
n=int(input())
s = set(map(int,input().split()))
print(len(s))
print(*sorted(s))
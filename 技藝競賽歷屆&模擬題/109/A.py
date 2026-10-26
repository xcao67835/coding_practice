# -*- coding: utf-8 -*-

for _ in range(int(input())):
    l = list(map(int,input().split()))
    l.sort()
    print(l.pop(),l.pop())
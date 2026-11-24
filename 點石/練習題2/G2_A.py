# -*- coding: utf-8 -*-

s=set(range(1,int(input())+1))
print(*s-set(map(int,input().split())))
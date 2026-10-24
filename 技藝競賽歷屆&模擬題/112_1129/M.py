# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n,x=map(int,input().split())
    l = list(map(int,input().split()))
    l.sort(reverse=True)
    ans=0
    for 